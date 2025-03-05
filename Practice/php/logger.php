<?php
/**
 * Logs a message with timestamp and rotates logs if size exceeds threshold.
 *
 * @param string $message The log message.
 * @param string $file Log file path.
 */
function log_message($message, $file = "app.log") {
    $max_size = 1024 * 100; // 100KB
    if (file_exists($file) && filesize($file) > $max_size) {
        rename($file, $file . '.' . time());
    }
    $timestamp = date("Y-m-d H:i:s");
    file_put_contents($file, "[$timestamp] $message" . PHP_EOL, FILE_APPEND);
}

log_message("System initialized.");
log_message("User logged in.");
?>
