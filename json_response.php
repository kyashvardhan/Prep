<?php
$data = ["status" => "success", "message" => "API is working!"];
header('Content-Type: application/json');
echo json_encode($data);
?>
