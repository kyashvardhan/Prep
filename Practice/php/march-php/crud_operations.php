<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data
$sql = "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')";
$conn->query($sql);

// Fetch data
$result = $conn->query("SELECT * FROM users");
while ($row = $result->fetch_assoc()) {
    echo "User: " . $row["name"] . " - Email: " . $row["email"] . "\n";
}

$conn->close();
?>
