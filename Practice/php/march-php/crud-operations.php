<?php
$pdo = new PDO("mysql:host=localhost;dbname=testdb", "root", "");

// Create
$pdo->exec("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')");

// Read
$stmt = $pdo->query("SELECT * FROM users");
while ($row = $stmt->fetch()) {
    echo $row['name'] . " - " . $row['email'] . "<br>";
}

// Update
$pdo->exec("UPDATE users SET name='Jane Doe' WHERE email='john@example.com'");

// Delete
$pdo->exec("DELETE FROM users WHERE email='john@example.com'");
?>
