<?php
/**
 * Plugin Name: Books CPT and Meta Boxes
 * Description: Registers a custom post type "Books" with meta boxes for price and a custom taxonomy for genres.
 * Version: 1.0
 * Author: Your Name
 */

// Register Custom Post Type "Books"
function register_books_cpt() {
    $labels = array(
        'name'                  => _x('Books', 'Post Type General Name', 'text_domain'),
        'singular_name'         => _x('Book', 'Post Type Singular Name', 'text_domain'),
        'menu_name'             => __('Books', 'text_domain'),
        'name_admin_bar'        => __('Book', 'text_domain'),
    );
    $args = array(
        'label'                 => __('Book', 'text_domain'),
        'labels'                => $labels,
        'supports'              => array('title', 'editor', 'thumbnail'),
        'public'                => true,
        'has_archive'           => true,
        'show_in_rest'          => true,
    );
    register_post_type('books', $args);
}
add_action('init', 'register_books_cpt');

// Register Custom Taxonomy "Genre"
function register_book_genre_taxonomy() {
    $labels = array(
        'name'              => _x('Genres', 'taxonomy general name', 'text_domain'),
        'singular_name'     => _x('Genre', 'taxonomy singular name', 'text_domain'),
    );
    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_in_rest'      => true,
    );
    register_taxonomy('genre', array('books'), $args);
}
add_action('init', 'register_book_genre_taxonomy');

// Add Meta Box for Book Price
function add_book_price_meta_box() {
    add_meta_box(
        'book_price',
        'Book Price',
        'render_book_price_meta_box',
        'books',
        'side',
        'default'
    );
}
add_action('add_meta_boxes', 'add_book_price_meta_box');

function render_book_price_meta_box($post) {
    $price = get_post_meta($post->ID, '_book_price', true);
    echo '<label for="book_price">Price ($): </label>';
    echo '<input type="number" id="book_price" name="book_price" value="' . esc_attr($price) . '" />';
}

function save_book_price_meta_box($post_id) {
    if (isset($_POST['book_price'])) {
        update_post_meta($post_id, '_book_price', sanitize_text_field($_POST['book_price']));
    }
}
add_action('save_post', 'save_book_price_meta_box');
?>
