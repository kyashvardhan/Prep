<?php
$data = file_get_contents("https://jsonplaceholder.typicode.com/posts");
$posts = json_decode($data, true);

foreach ($posts as $post) {
    echo "<h3>" . $post['title'] . "</h3>";
    echo "<p>" . $post['body'] . "</p><hr>";
}
?>
