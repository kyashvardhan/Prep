#!/usr/bin/env python3
"""
youtube_thumbnail_extractor.py
Download the best-available thumbnail for given YouTube video URLs.

Usage:
    python youtube_thumbnail_extractor.py -o thumbnails https://youtu.be/VIDEO_ID1 https://www.youtube.com/watch?v=VIDEO_ID2

It will attempt, in order, maxresdefault, sddefault, hqdefault, mqdefault, default.
"""

import os
import re
import argparse
import requests
from urllib.parse import urlparse, parse_qs

# Common YouTube thumbnail resolutions in descending order of quality
RESOLUTIONS = [
    "maxresdefault.jpg",
    "sddefault.jpg",
    "hqdefault.jpg",
    "mqdefault.jpg",
    "default.jpg"
]

def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    Supports youtu.be and youtube.com/watch?v= formats.
    """
    parsed = urlparse(url)
    if parsed.netloc in ("youtu.be", "www.youtu.be"):
        return parsed.path.lstrip('/')
    if 'youtube' in parsed.netloc:
        qs = parse_qs(parsed.query)
        if 'v' in qs:
            return qs['v'][0]
    raise ValueError(f"Could not extract video ID from URL: {url}")

def find_best_thumbnail(video_id):
    """
    Try each resolution URL via HEAD and return the first that exists.
    """
    for res in RESOLUTIONS:
        thumb_url = f"https://img.youtube.com/vi/{video_id}/{res}"
        resp = requests.head(thumb_url)
        if resp.status_code == 200 and resp.headers.get('Content-Type', '').startswith('image'):
            return thumb_url
    return None

def download_thumbnail(thumb_url, output_dir, video_id):
    """
    Download the thumbnail and save it as {video_id}.jpg in output_dir.
    """
    resp = requests.get(thumb_url, stream=True)
    resp.raise_for_status()
    ext = os.path.splitext(thumb_url)[1]
    filename = f"{video_id}{ext}"
    path = os.path.join(output_dir, filename)
    with open(path, 'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)
    return path

def main():
    parser = argparse.ArgumentParser(description="YouTube Thumbnail Extractor")
    parser.add_argument('urls', nargs='+', help="YouTube video URLs")
    parser.add_argument('-o', '--output', default='.', help="Directory to save thumbnails")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    for url in args.urls:
        try:
            vid = extract_video_id(url)
            print(f"[+] Processing video ID: {vid}")
            thumb = find_best_thumbnail(vid)
            if not thumb:
                print(f"    ✖ No thumbnail found for {vid}")
                continue
            saved = download_thumbnail(thumb, args.output, vid)
            print(f"    ✔ Downloaded thumbnail: {saved}")
        except Exception as e:
            print(f"    ✖ Error for URL '{url}': {e}")

if __name__ == "__main__":
    main()
