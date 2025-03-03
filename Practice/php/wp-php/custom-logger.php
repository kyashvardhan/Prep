<?php
function logMessage($message, $file = "logs.txt") {
    $timestamp = date("Y-m-d H:i:s");
    file_put_contents($file, "[$timestamp] $message" . PHP_EOL, FILE_APPEND);
}

logMessage("This is a test log.");
echo "Log recorded.";
?>
