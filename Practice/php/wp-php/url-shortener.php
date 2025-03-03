<?php
$shortLinks = [
    "yt" => "https://youtube.com",
    "gh" => "https://github.com"
];

$key = $_GET["key"] ?? null;

if ($key && isset($shortLinks[$key])) {
    header("Location: " . $shortLinks[$key]);
} else {
    echo "Invalid short URL.";
}
?>
