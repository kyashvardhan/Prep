function get_recent_posts_by_category($category_id, $limit = 5) {
    $args = [
        'category' => $category_id,
        'posts_per_page' => $limit,
        'post_status' => 'publish'
    ];
    return get_posts($args);
}
