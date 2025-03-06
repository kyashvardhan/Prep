<?php
$page = $_GET['page'] ?? 1;
$limit = 10;
$offset = ($page - 1) * $limit;

$db = new PDO("mysql:host=localhost;dbname=test", "root", "");
$stmt = $db->query("SELECT * FROM posts LIMIT $limit OFFSET $offset");
echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
?>
