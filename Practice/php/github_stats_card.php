<?php
$github_username = 'kyashvardhan';
$api_url = "https://api.github.com/users/{$github_username}";

$user_data = json_decode(file_get_contents($api_url), true);

$stats_card = "## GitHub Stats\n\n";
$stats_card .= "| Metric | Value |\n";
$stats_card .= "|--------|-------|\n";
$stats_card .= "| Repositories | {$user_data['public_repos']} |\n";
$stats_card .= "| Followers | {$user_data['followers']} |\n";
$stats_card .= "| Following | {$user_data['following']} |\n";
$stats_card .= "| Gists | {$user_data['public_gists']} |\n";

file_put_contents('github_stats_card.md', $stats_card);
