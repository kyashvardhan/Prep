#!/usr/bin/php
<?php
// Simple CLI to greet users and perform basic math operations.
if (php_sapi_name() == "cli") {
    $options = getopt("n:a:b:");
    if (isset($options["n"])) {
        $name = $options["n"];
        echo "Hello, $name!\n";
    }
    if (isset($options["a"]) && isset($options["b"])) {
        $sum = $options["a"] + $options["b"];
        echo "The sum of {$options['a']} and {$options['b']} is $sum\n";
    }
} else {
    echo "This script is intended for command-line usage.\n";
}
?>
