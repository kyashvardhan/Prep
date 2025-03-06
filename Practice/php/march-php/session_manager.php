<?php
session_start();

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

if ($username === 'admin' && $password === 'password') {
    $_SESSION['user'] = $username;
    echo "Welcome, $username!";
} else {
    echo isset($_SESSION['user']) ? "Logged in as {$_SESSION['user']}" : "Invalid login.";
}
?>
