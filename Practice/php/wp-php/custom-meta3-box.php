function add_custom_meta_box() {
    add_meta_box(
        'custom_meta',
        'Custom Post Info',
        'custom_meta_callback',
        'post',
        'side',
        'default'
    );
}

function custom_meta_callback($post) {
    $custom_data = get_post_meta($post->ID, '_custom_meta', true);
    echo '<input type="text" name="custom_meta" value="' . esc_attr($custom_data) . '">';
}

function save_custom_meta($post_id) {
    if (array_key_exists('custom_meta', $_POST)) {
        update_post_meta
