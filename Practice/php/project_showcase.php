<?php
$projects = [
    ['name' => 'Project A', 'description' => 'A cool project', 'image' => 'project_a.png'],
    ['name' => 'Project B', 'description' => 'An awesome project', 'image' => 'project_b.png'],
    ['name' => 'Project C', 'description' => 'A fantastic project', 'image' => 'project_c.png'],
];

$showcase = "## Project Showcase\n\n";
foreach ($projects as $project) {
    $showcase .= "### {$project['name']}\n\n";
    $showcase .= "{$project['description']}\n\n";
    $showcase .= "![{$project['name']}]({$project['image']})\n\n";
}

file_put_contents('project_showcase.md', $showcase);
