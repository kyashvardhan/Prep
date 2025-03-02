function sanitize_string($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}
