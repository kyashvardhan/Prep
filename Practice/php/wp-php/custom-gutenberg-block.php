function register_custom_block() {
    wp_register_script(
        'custom-block-js',
        get_template_directory_uri() . '/js/custom-block.js',
        array('wp-blocks', 'wp-editor'),
        filemtime(get_template_directory() . '/js/custom-block.js')
    );

    register_block_type('custom/block', array(
        'editor_script' => 'custom-block-js',
    ));
}
add_action('init', 'register_custom_block');
