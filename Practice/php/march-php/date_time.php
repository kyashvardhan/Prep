<?php
// Display current date and time
echo "Current date: " . date("Y-m-d") . "\n";
echo "Current time: " . date("H:i:s") . "\n";

// Get time difference
$now = time();
$futureDate = strtotime("+7 days");
$diff = $futureDate - $now;
echo "Days left: " . floor($diff / (60 * 60 * 24)) . "\n";
?>
