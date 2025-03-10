<?php
// In a custom plugin or functions.php

function register_custom_api_endpoint() {
    register_rest_route('custom/v1', '/secure-data/', array(
        'methods' => 'GET',
        'callback' => 'custom_api_secure_data',
        'permission_callback' => 'custom_api_permission_check'
    ));
}
add_action('rest_api_init', 'register_custom_api_endpoint');

function custom_api_secure_data(WP_REST_Request $request) {
    $data = array(
        'message' => 'Hello, this is secured data!',
        'data' => array(1, 2, 3, 4)
    );
    return rest_ensure_response($data);
}

function custom_api_permission_check(WP_REST_Request $request) {
    // Simple token check in header
    $headers = $request->get_headers();
    if (isset($headers['x-custom-token']) && $headers['x-custom-token'] == 'secret123') {
        return true;
    }
    return new WP_Error('forbidden', 'Invalid token', array('status' => 403));
}
?>
