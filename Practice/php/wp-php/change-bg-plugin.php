/*
Plugin Name: Change Post Background
Description: A simple plugin to add custom background color to posts
Version: 1.0
Author: Yash
*/

function add_custom_styles() {
    echo "<style> .post-content { background-color: #f4f4f4; padding: 20px; } </style>";
}
add_action('wp_head', 'add_custom_styles');
