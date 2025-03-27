import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import os

def download_file(url, directory="downloads"):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(directory, local_filename)

    os.makedirs(directory, exist_ok=True)
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(local_filepath, 'wb') as f, tqdm(
        total=total_size, unit='B', unit_scale=True, desc=local_filename
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            f.write(data)
            bar.update(len(data))

def download_files(urls, max_threads=5):
    with ThreadPoolExecutor(max_threads) as executor:
        executor.map(download_file, urls)

if __name__ == "__main__":
    urls = [
        "https://speed.hetzner.de/100MB.bin",
        "https://speed.hetzner.de/10MB.bin",
        "https://speed.hetzner.de/1MB.bin"
    ]
    download_files(urls)
