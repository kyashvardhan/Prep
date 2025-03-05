<?php
/**
 * Cache data to a file.
 *
 * @param string $key Cache key.
 * @param mixed $data Data to cache.
 * @param int $expiration Cache expiration in seconds.
 */
function cache_set($key, $data, $expiration = 3600) {
    $cacheFile = "cache_" . md5($key) . ".cache";
    $cacheData = [
        'expiration' => time() + $expiration,
        'data' => $data
    ];
    file_put_contents($cacheFile, serialize($cacheData));
}

/**
 * Retrieve cached data from a file.
 *
 * @param string $key Cache key.
 * @return mixed Cached data or false if expired/not found.
 */
function cache_get($key) {
    $cacheFile = "cache_" . md5($key) . ".cache";
    if (!file_exists($cacheFile)) {
        return false;
    }
    $cacheData = unserialize(file_get_contents($cacheFile));
    if (time() > $cacheData['expiration']) {
        unlink($cacheFile);
        return false;
    }
    return $cacheData['data'];
}

// Example usage:
cache_set("greeting", "Hello, World!", 60);
echo cache_get("greeting");
?>
