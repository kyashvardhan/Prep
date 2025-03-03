<?php
function custom_theme_scripts() {
    wp_enqueue_style('custom-style', get_stylesheet_directory_uri() . '/custom.css');
    wp_enqueue_script('custom-script', get_template_directory_uri() . '/custom.js', array('jquery'), null, true);
}

add_action('wp_enqueue_scripts', 'custom_theme_scripts');
?>
