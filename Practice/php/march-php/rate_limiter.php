<?php
$ip = $_SERVER['REMOTE_ADDR'];
$file = "logs/$ip";
$requests = file_exists($file) ? (int)file_get_contents($file) : 0;

if ($requests > 100) {
    http_response_code(429);
    die("Too many requests");
} else {
    file_put_contents($file, $requests + 1);
    echo "Request allowed.";
}
?>
