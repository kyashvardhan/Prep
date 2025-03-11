<?php
$github_username = 'kyashvardhan';
$api_url = "https://api.github.com/users/{$github_username}/events/public";

$events = json_decode(file_get_contents($api_url), true);

$activity = "## Recent Activity\n\n";
foreach (array_slice($events, 0, 5) as $event) {
    $repo = $event['repo']['name'];
    $type = str_replace('Event', '', $event['type']);
    $date = date('Y-m-d', strtotime($event['created_at']));
    $activity .= "- {$type} in {$repo} on {$date}\n";
}

file_put_contents('recent_activity.md', $activity);
