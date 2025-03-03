<?php
function custom_login_style() {
    echo '<style>
        body.login { background-color: #1e1e1e; }
        .login h1 a { filter: brightness(0) invert(1); }
    </style>';
}

add_action('login_head', 'custom_login_style');
?>
