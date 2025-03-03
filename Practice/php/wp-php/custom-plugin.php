<?php
/**
 * Plugin Name: Custom Greeting Plugin
 * Description: A simple WordPress plugin that adds a greeting to the footer.
 * Version: 1.0
 * Author: Yash Vardhan
 */

function add_custom_footer_text() {
    echo '<p style="text-align:center; color:blue;">Welcome to my WordPress site!</p>';
}

add_action('wp_footer', 'add_custom_footer_text');
?>
