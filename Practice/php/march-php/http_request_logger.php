<?php
$log = date('Y-m-d H:i:s') . " " . $_SERVER['REQUEST_METHOD'] . " " . $_SERVER['REQUEST_URI'] . "\n";
file_put_contents('requests.log', $log, FILE_APPEND);
?>
