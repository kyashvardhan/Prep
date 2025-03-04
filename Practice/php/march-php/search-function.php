<?php
$pdo = new PDO("mysql:host=localhost;dbname=testdb", "root", "");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $query = $_POST["query"];
    $stmt = $pdo->prepare("SELECT * FROM users WHERE name LIKE :query");
    $stmt->execute(["query" => "%$query%"]);

    while ($row = $stmt->fetch()) {
        echo $row['name'] . " - " . $row['email'] . "<br>";
    }
}
?>
<form method="post">
    <input type="text" name="query" placeholder="Search users...">
    <button type="submit">Search</button>
</form>
