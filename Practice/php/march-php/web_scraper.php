<?php
$url = "https://example.com";
$html = file_get_contents($url);
preg_match("/<title>(.*?)<\/title>/", $html, $title);
preg_match_all("/<h2>(.*?)<\/h2>/", $html, $headings);
preg_match_all("/<a href=\"(.*?)\">/", $html, $links);

echo "Title: " . $title[1] . "\n";
print_r($headings[1]);
print_r($links[1]);
?>
