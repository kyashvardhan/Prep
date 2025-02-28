<?php
$users = [
    "admin" => "password123",
    "user" => "welcome2025"
];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if (isset($users[$username]) && $users[$username] == $password) {
        echo "Login successful! Welcome, $username.";
    } else {
        echo "Invalid username or password.";
    }
}
?>
