<?php
$file = "test.txt";

// Write to file
file_put_contents($file, "Hello, PHP File Handling!");

// Read from file
$content = file_get_contents($file);
echo "File content: " . $content;
?>
