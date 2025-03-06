<?php
$apiUrl = "https://jsonplaceholder.typicode.com/posts";
$response = file_get_contents($apiUrl);
$posts = json_decode($response, true);

foreach ($posts as $post) {
    echo "Title: {$post['title']}<br>";
    echo "Body: {$post['body']}<hr>";
}
?>
