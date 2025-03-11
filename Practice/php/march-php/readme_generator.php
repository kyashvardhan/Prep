<?php
$github_username = 'your_username';
$api_url = "https://api.github.com/users/{$github_username}/repos";

$repos = json_decode(file_get_contents($api_url), true);

$readme = "# Welcome to my GitHub Profile!\n\n";
$readme .= "## My Top Repositories\n\n";

foreach (array_slice($repos, 0, 5) as $repo) {
    $readme .= "- [{$repo['name']}]({$repo['html_url']}): {$repo['description']}\n";
}

file_put_contents('README.md', $readme);
