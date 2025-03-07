<?php
session_start();
$user = "admin";
$pass = "1234";

if ($_POST['username'] === $user && $_POST['password'] === $pass) {
    $_SESSION['user'] = $user;
    echo "Login successful!";
} else {
    echo "Invalid credentials.";
}
?>
