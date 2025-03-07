<?php
$page = $_GET['page'] ?? 1;
$limit = 10;
$offset = ($page - 1) * $limit;

$query = "SELECT * FROM posts LIMIT $limit OFFSET $offset";
?>
