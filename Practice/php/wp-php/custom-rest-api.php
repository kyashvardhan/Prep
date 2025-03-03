<?php
function custom_api_endpoint() {
    register_rest_route('custom/v1', '/message/', array(
        'methods' => 'GET',
        'callback' => function() {
            return rest_ensure_response(array('message' => 'Hello from the custom API!'));
        }
    ));
}

add_action('rest_api_init', 'custom_api_endpoint');
?>
