<?php
$url = "https://jsonplaceholder.typicode.com/posts/1";
$response = file_get_contents($url);
$data = json_decode($response, true);

echo "Title: " . $data["title"] . "<br>";
echo "Content: " . $data["body"];
?>
