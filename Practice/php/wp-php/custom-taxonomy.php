<?php
function create_book_genre_taxonomy() {
    register_taxonomy('genre', 'books', array(
        'label' => __('Genre'),
        'rewrite' => array('slug' => 'genre'),
        'hierarchical' => true,
    ));
}

add_action('init', 'create_book_genre_taxonomy');
?>
