<?php
function create_books_post_type() {
    register_post_type('books',
        array(
            'labels' => array(
                'name' => __('Books'),
                'singular_name' => __('Book')
            ),
            'public' => true,
            'has_archive' => true,
            'menu_icon' => 'dashicons-book',
            'supports' => array('title', 'editor', 'thumbnail'),
        )
    );
}

add_action('init', 'create_books_post_type');
?>
