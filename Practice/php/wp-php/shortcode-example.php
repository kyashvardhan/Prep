<?php
/**
 * Plugin Name: Custom Shortcode Plugin
 * Description: Adds a [greet_user] shortcode to display a greeting message.
 */

function greet_user_shortcode() {
    return "<h3>Hello, WordPress User! 🚀</h3>";
}

add_shortcode('greet_user', 'greet_user_shortcode');
?>
