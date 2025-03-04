<?php
session_start();
if (!isset($_SESSION['last_request_time'])) {
    $_SESSION['last_request_time'] = time();
}

$timeDifference = time() - $_SESSION['last_request_time'];
if ($timeDifference < 5) {
    die("Too many requests. Try again later.");
}

$_SESSION['last_request_time'] = time();
echo "Request successful!";
?>
