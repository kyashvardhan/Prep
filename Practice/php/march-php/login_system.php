<?php
$users = [
    "admin" => "password123",
    "user" => "welcome"
];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    if (isset($users[$username]) && $users[$username] === $password) {
        echo "Welcome, $username!";
    } else {
        echo "Invalid credentials.";
    }
}
?>

<form method="post">
    Username: <input type="text" name="username">
    Password: <input type="password" name="password">
    <input type="submit" value="Login">
</form>
