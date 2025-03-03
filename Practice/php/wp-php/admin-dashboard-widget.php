<?php
function custom_dashboard_widget() {
    wp_add_dashboard_widget('custom_widget', 'Custom Dashboard Widget', function() {
        echo '<p>Welcome to the custom WordPress dashboard widget!</p>';
    });
}

add_action('wp_dashboard_setup', 'custom_dashboard_widget');
?>
