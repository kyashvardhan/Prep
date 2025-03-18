<?php
$api_url = "https://wptavern.com/wp-json/wp/v2/posts?per_page=5";
$response = file_get_contents($api_url);
$posts = json_decode($response);

foreach ($posts as $post) {
    echo "<h2>{$post->title->rendered}</h2>";
    echo "<p>{$post->excerpt->rendered}</p>";
    echo "<a href='{$post->link}' target='_blank'>Read More</a><hr>";
}
?>
