function cache_data($key, $data, $expiration = 3600) {
    set_transient($key, $data, $expiration);
}

function get_cached_data($key) {
    return get_transient($key);
}
