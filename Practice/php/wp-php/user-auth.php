<?php
session_start();
$users = ["admin" => "password123", "user" => "pass456"];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    if (isset($users[$username]) && $users[$username] == $password) {
        $_SESSION["user"] = $username;
        header("Location: dashboard.php");
    } else {
        echo "Invalid credentials.";
    }
}
?>
