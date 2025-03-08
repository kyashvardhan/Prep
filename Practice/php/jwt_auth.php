<?php
require 'vendor/autoload.php';
use Firebase\JWT\JWT;

$key = "secretkey";
$payload = [
    "user_id" => 123,
    "exp" => time() + 3600
];

$jwt = JWT::encode($payload, $key, 'HS256');
echo "JWT Token: " . $jwt;

// Decoding
$decoded = JWT::decode($jwt, new \Firebase\JWT\Key($key, 'HS256'));
print_r($decoded);
?>
