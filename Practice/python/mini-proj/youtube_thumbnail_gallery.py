#!/usr/bin/env python3
"""
youtube_thumbnail_gallery.py
"""

import os
import re
import argparse
import requests
from urllib.parse import urlparse, parse_qs

# Thumbnail resolutions to try in order
RESOLUTIONS = [
    "maxresdefault.jpg",
    "sddefault.jpg",
    "hqdefault.jpg",
    "mqdefault.jpg",
    "default.jpg"
]

OEMBED_URL = "https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={vid}"

def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.netloc in ("youtu.be", "www.youtu.be"):
        return parsed.path.lstrip('/')
    if 'youtube' in parsed.netloc:
        qs = parse_qs(parsed.query)
        if 'v' in qs:
            return qs['v'][0]
    raise ValueError(f"Cannot extract video ID from URL: {url}")

def find_best_thumbnail(video_id):
    for res in RESOLUTIONS:
        thumb_url = f"https://img.youtube.com/vi/{video_id}/{res}"
        r = requests.head(thumb_url)
        if r.status_code == 200 and r.headers.get('Content-Type','').startswith('image'):
            return thumb_url
    return None

def download_thumbnail(thumb_url, output_dir, video_id):
    r = requests.get(thumb_url, stream=True)
    r.raise_for_status()
    ext = os.path.splitext(thumb_url)[1]
    filename = f"{video_id}{ext}"
    path = os.path.join(output_dir, filename)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    return filename

def fetch_title(video_id):
    try:
        r = requests.get(OEMBED_URL.format(vid=video_id))
        r.raise_for_status()
        data = r.json()
        return data.get("title", video_id)
    except Exception:
        return video_id

def generate_html(entries, output_path):
    html_head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><title>YouTube Thumbnail Gallery</title>
  <style>
    body { font-family: sans-serif; margin: 2rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill,minmax(200px,1fr)); gap: 1rem; }
    .item { text-align: center; }
    .item img { max-width: 100%; border: 1px solid #ccc; }
    .item a { text-decoration: none; color: #333; display: block; margin-top: 0.5rem; }
  </style>
</head><body>
  <h1>YouTube Thumbnail Gallery</h1>
  <div class="grid">
"""
    html_tail = """  </div>
</body></html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_head)
        for vid, thumb_file, title in entries:
            f.write(f'    <div class="item">\n')
            f.write(f'      <a href="https://www.youtube.com/watch?v={vid}" target="_blank">\n')
            f.write(f'        <img src="{thumb_file}" alt="{title}">\n')
            f.write(f'        <div>{title}</div>\n')
            f.write(f'      </a>\n')
            f.write(f'    </div>\n')
        f.write(html_tail)

def main():
    parser = argparse.ArgumentParser(description="YouTube Thumbnail Gallery Generator")
    parser.add_argument('urls', nargs='+', help="YouTube video URLs")
    parser.add_argument('-o','--output', default='.', help="Directory to save thumbnails and HTML")
    parser.add_argument('--html', default='gallery.html', help="HTML filename to generate")
    args = parser.parse_args()

    out_dir = args.output
    os.makedirs(out_dir, exist_ok=True)
    entries = []

    for url in args.urls:
        try:
            vid = extract_video_id(url)
            thumb_url = find_best_thumbnail(vid)
            if not thumb_url:
                print(f"[!] No thumbnail found for {vid}")
                continue
            filename = download_thumbnail(thumb_url, out_dir, vid)
            title = fetch_title(vid)
            entries.append((vid, filename, title))
            print(f"[+] {vid}: downloaded {filename}, title: {title}")
        except Exception as e:
            print(f"[!] Error with {url}: {e}")

    html_path = os.path.join(out_dir, args.html)
    generate_html(entries, html_path)
    print(f"[+] Gallery generated at {html_path}")

if __name__ == "__main__":
    main()
