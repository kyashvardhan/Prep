function sanitize_string($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

function validate_email($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

function sanitize_input($input, $db_connection) {
    return mysqli_real_escape_string($db_connection, trim($input));
}

