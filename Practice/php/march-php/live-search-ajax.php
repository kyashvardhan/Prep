<?php
// In functions.php or a custom plugin file

// Enqueue our custom JavaScript for AJAX
function enqueue_live_search_script() {
    wp_enqueue_script('live-search', plugin_dir_url(__FILE__) . 'live-search.js', array('jquery'), null, true);
    wp_localize_script('live-search', 'liveSearch', array(
        'ajax_url' => admin_url('admin-ajax.php')
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_live_search_script');

// AJAX handler for live search
function live_search_handler() {
    $search_query = sanitize_text_field($_POST['query']);
    $args = array(
        's' => $search_query,
        'post_status' => 'publish'
    );
    $query = new WP_Query($args);
    $results = array();
    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            $results[] = array(
                'title' => get_the_title(),
                'link'  => get_permalink()
            );
        }
    }
    wp_reset_postdata();
    wp_send_json($results);
}
add_action('wp_ajax_live_search', 'live_search_handler');
add_action('wp_ajax_nopriv_live_search', 'live_search_handler');
?>
