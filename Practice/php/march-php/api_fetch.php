<?php
$url = "https://jsonplaceholder.typicode.com/posts/1";
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
echo "Post Title: " . $data["title"];
?>
