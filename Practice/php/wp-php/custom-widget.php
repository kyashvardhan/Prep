<?php
class Custom_Widget extends WP_Widget {
    function __construct() {
        parent::__construct('custom_widget', __('Custom Widget', 'text_domain'));
    }

    public function widget($args, $instance) {
        echo $args['before_widget'];
        echo '<h4>Custom Widget Content</h4>';
        echo '<p>This is a simple custom widget.</p>';
        echo $args['after_widget'];
    }
}

function register_custom_widget() {
    register_widget('Custom_Widget');
}

add_action('widgets_init', 'register_custom_widget');
?>
