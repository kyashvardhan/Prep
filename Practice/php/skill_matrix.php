<?php
$skills = [
    'PHP' => 90,
    'JavaScript' => 85,
    'Python' => 95,
    'SQL' => 80,
    'Git' => 95,
];

$matrix = "## Skill Matrix\n\n";
foreach ($skills as $skill => $level) {
    $bars = str_repeat('█', $level / 10);
    $spaces = str_repeat('░', 10 - ($level / 10));
    $matrix .= "{$skill}: [{$bars}{$spaces}] {$level}%\n";
}

file_put_contents('skill_matrix.md', $matrix);
