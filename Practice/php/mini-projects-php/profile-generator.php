<?php

require 'vendor/autoload.php';

$token = getenv('GH_TOKEN');
$client = new \GuzzleHttp\Client([
    'base_uri' => 'https://api.github.com/',
    'headers' => [
        'Authorization' => 'token ' . $token,
        'Accept' => 'application/vnd.github.v3+json'
    ]
]);

// Get repository statistics
$repos = json_decode($client->get('users/{username}/repos?per_page=5&sort=pushed')->getBody());
$activity = json_decode($client->get('users/{username}/events/public?per_page=10')->getBody());

// Generate SVG metrics
$metrics = [
    'daily_commits' => array_sum(array_column($activity, 'size')),
    'active_repos' => count(array_unique(array_column($activity, 'repo'))),
    'prs' => count(array_filter($activity, fn($e) => $e->type === 'PullRequestEvent'))
];

$svgTemplate = <<<SVG
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="150">
  <style>
    .title { font: 14px sans-serif; fill: #2f80ed; }
    .metric { font: bold 20px sans-serif; fill: #333; }
  </style>
  <text x="20" y="30" class="title">Development Metrics</text>
  <text x="20" y="60" class="metric">📊 Daily Commits: {$metrics['daily_commits']}</text>
  <text x="20" y="90" class="metric">🚀 Active Repos: {$metrics['active_repos']}</text>
  <text x="20" y="120" class="metric">🤝 Open PRs: {$metrics['prs']}</text>
</svg>
SVG;

file_put_contents('public/metrics.svg', $svgTemplate);

// Update README
$readme = <<<MD
<!--PROFILE_START-->
## 🛠️ Recent Activity

{$renderActivity($activity)}

## 🏆 Top Projects

{$renderProjects($repos)}

![Metrics](public/metrics.svg)
<!--PROFILE_END-->
MD;

function renderActivity($events) {
    return implode("\n", array_map(function($e) {
        $date = date('M j H:i', strtotime($e->created_at));
        return "- ⚡ {$date}: {$e->type} in [{$e->repo->name}]({$e->repo->url})";
    }, $events));
}

function renderProjects($repos) {
    return implode("\n", array_map(function($r) {
        $lang = $r->language ?: 'Multi-language';
        return "### [{$r->name}]({$r->html_url})\n⭐ {$r->stargazers_count} | 🍴 {$r->forks} | 📚 $lang";
    }, $repos));
}
