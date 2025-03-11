<?php
$github_username = 'kyashvardhan';
$api_url = "https://api.github.com/users/{$github_username}/repos";

$repos = json_decode(file_get_contents($api_url), true);

$languages = [];
foreach ($repos as $repo) {
    $lang = $repo['language'];
    if ($lang) {
        $languages[$lang] = isset($languages[$lang]) ? $languages[$lang] + 1 : 1;
    }
}

arsort($languages);

$stats = "## My Language Statistics\n\n";
foreach ($languages as $lang => $count) {
    $percentage = round(($count / count($repos)) * 100, 2);
    $stats .= "- {$lang}: {$percentage}%\n";
}

file_put_contents('language_stats.md', $stats);
