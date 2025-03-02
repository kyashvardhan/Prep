function cache_data($key, $data, $expiration = 3600) {
    set_transient($key, $data, $expiration);
}

function get_cached_data($key) {
    return get_transient($key);
}

function fetch_or_cache_data($key, $callback, $expiration = 3600) {
    $data = get_transient($key);
    if (!$data) {
        $data = $callback();
        set_transient($key, $data, $expiration);
    }
    return $data;
}
