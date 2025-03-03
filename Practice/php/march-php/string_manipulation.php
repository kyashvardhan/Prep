<?php
// Reverse a string
function reverseString($str) {
    return strrev($str);
}

// Convert a string to uppercase
function toUpperCase($str) {
    return strtoupper($str);
}

echo "Reversed: " . reverseString("hello") . "\n";  // Output: olleh
echo "Uppercase: " . toUpperCase("hello") . "\n";  // Output: HELLO
?>
