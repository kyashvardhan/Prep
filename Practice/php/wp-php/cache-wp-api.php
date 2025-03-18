<?php
function get_cached_posts() {
    $cached_posts = get_transient('wp_api_posts');

    if (!$cached_posts) {
        $api_url = "https://wptavern.com/wp-json/wp/v2/posts?per_page=5";
        $response = wp_remote_get($api_url);
        if (is_wp_error($response)) return [];
        
        $cached_posts = wp_remote_retrieve_body($response);
        set_transient('wp_api_posts', $cached_posts, 12 * HOUR_IN_SECONDS);
    }

    return json_decode($cached_posts);
}

$posts = get_cached_posts();
foreach ($posts as $post) {
    echo "<h2>{$post->title->rendered}</h2>";
    echo "<a href='{$post->link}'>Read More</a><hr>";
}
?>
