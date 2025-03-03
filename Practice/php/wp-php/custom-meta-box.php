<?php
function custom_meta_box() {
    add_meta_box('book_details', 'Book Details', 'book_meta_box_callback', 'books', 'side', 'high');
}

function book_meta_box_callback($post) {
    $value = get_post_meta($post->ID, '_book_price', true);
    echo '<label for="book_price">Price: </label>';
    echo '<input type="text" id="book_price" name="book_price" value="' . esc_attr($value) . '">';
}

function save_book_meta_box($post_id) {
    if (array_key_exists('book_price', $_POST)) {
        update_post_meta($post_id, '_book_price', $_POST['book_price']);
    }
}

add_action('add_meta_boxes', 'custom_meta_box');
add_action('save_post', 'save_book_meta_box');
?>
