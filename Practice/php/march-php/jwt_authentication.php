<?php
require 'vendor/autoload.php';
use Firebase\JWT\JWT;

$key = "secretkey";
$payload = [
    "user_id" => 123,
    "exp" => time() + 3600
];

$jwt = JWT::encode($payload, $key, 'HS256');
echo json_encode(["token" => $jwt]);
?>
