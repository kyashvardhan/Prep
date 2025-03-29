import hashlib

def shorten_url(long_url):
    hash_object = hashlib.sha1(long_url.encode())
    short_hash = hash_object.hexdigest()[:6]
    return f"https://short.ly/{short_hash}"

# Example
print(shorten_url("https://www.example.com/some-long-url"))
