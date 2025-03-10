<?php
/**
 * Plugin Name: Advanced Settings Plugin
 * Description: Adds an admin settings page for custom plugin options.
 * Version: 1.0
 * Author: yash
 */

// Register the settings page
function asp_register_settings_page() {
    add_menu_page(
        'Advanced Settings', // Page title
        'Advanced Settings', // Menu title
        'manage_options',    // Capability
        'advanced-settings', // Menu slug
        'asp_render_settings_page', // Callback function
        'dashicons-admin-generic',
        90
    );
}
add_action('admin_menu', 'asp_register_settings_page');

// Register settings, sections, and fields
function asp_register_settings() {
    register_setting('asp_options_group', 'asp_options', 'asp_sanitize_options');

    add_settings_section(
        'asp_main_section',
        'Main Settings',
        'asp_main_section_callback',
        'advanced-settings'
    );

    add_settings_field(
        'asp_custom_text',
        'Custom Text',
        'asp_custom_text_callback',
        'advanced-settings',
        'asp_main_section'
    );
}
add_action('admin_init', 'asp_register_settings');

function asp_main_section_callback() {
    echo '<p>Main configuration for the Advanced Settings Plugin.</p>';
}

function asp_custom_text_callback() {
    $options = get_option('asp_options');
    $value = isset($options['asp_custom_text']) ? esc_attr($options['asp_custom_text']) : '';
    echo "<input type='text' name='asp_options[asp_custom_text]' value='$value' />";
}

function asp_sanitize_options($input) {
    $input['asp_custom_text'] = sanitize_text_field($input['asp_custom_text']);
    return $input;
}

// Render the settings page
function asp_render_settings_page() {
    ?>
    <div class="wrap">
        <h1>Advanced Settings Plugin</h1>
        <form method="post" action="options.php">
            <?php
                settings_fields('asp_options_group');
                do_settings_sections('advanced-settings');
                submit_button();
            ?>
        </form>
    </div>
    <?php
}
?>
