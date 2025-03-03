<?php
session_start();

function generateToken() {
    return bin2hex(random_bytes(32));
}

if (empty($_SESSION["csrf_token"])) {
    $_SESSION["csrf_token"] = generateToken();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if ($_POST["csrf_token"] !== $_SESSION["csrf_token"]) {
        die("Invalid CSRF token.");
    } else {
        echo "Form submitted successfully!";
    }
}
?>
