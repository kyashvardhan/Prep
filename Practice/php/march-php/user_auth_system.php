<?php
session_start();
$conn = new mysqli("localhost", "root", "", "auth_db");

// User Registration
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $conn->query("INSERT INTO users (username, password) VALUES ('$username', '$password')");
    echo "User Registered!";
}

// User Login
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $result = $conn->query("SELECT * FROM users WHERE username='$username'");
    $user = $result->fetch_assoc();

    if (password_verify($password, $user['password'])) {
        $_SESSION['user'] = $username;
        echo "Login Successful!";
    } else {
        echo "Invalid Credentials!";
    }
}

// Logout
if (isset($_GET['logout'])) {
    session_destroy();
    echo "Logged out!";
}
?>
