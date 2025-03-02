function get_recent_posts_by_category($category_id, $limit = 5) {
    $args = [
        'category' => $category_id,
        'posts_per_page' => $limit,
        'post_status' => 'publish'
    ];
    return get_posts($args);
}

function add_custom_footer_message() {
    echo "<p>🚀 Powered by Custom WordPress Development</p>";
}
add_action('wp_footer', 'add_custom_footer_message');

function add_custom_footer_with_admin() {
    $admin_name = get_bloginfo('name');
    echo "<p>🚀 Managed by {$admin_name} | Powered by Custom WordPress Development</p>";
}
add_action('wp_footer', 'add_custom_footer_with_admin');

