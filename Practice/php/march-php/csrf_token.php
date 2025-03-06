<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
    echo $_SESSION['csrf'];
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $token = $_POST['csrf'] ?? '';
    if (hash_equals($_SESSION['csrf'], $token)) {
        echo "Valid request.";
    } else {
        echo "Invalid CSRF token.";
    }
}
?>
