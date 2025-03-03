<?php
header("Content-Type: application/json");

$data = [
    "message" => "Hello, this is a custom API response!",
    "status" => "success"
];

echo json_encode($data);
?>
