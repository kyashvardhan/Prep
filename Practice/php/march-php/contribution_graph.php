<?php
$github_username = 'kyashvardhan';
$api_url = "https://api.github.com/users/{$github_username}/events";

$events = json_decode(file_get_contents($api_url), true);

$contributions = array_fill(0, 7, 0);
foreach ($events as $event) {
    $day = date('w', strtotime($event['created_at']));
    $contributions[$day]++;
}

$graph = "## My Weekly Contribution Graph\n\n";
foreach ($contributions as $day => $count) {
    $graph .= str_repeat('█', $count) . " " . date('D', strtotime("Sunday +{$day} days")) . "\n";
}

file_put_contents('contribution_graph.md', $graph);
