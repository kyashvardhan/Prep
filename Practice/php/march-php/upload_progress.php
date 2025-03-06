<?php
session_start();
$key = ini_get("session.upload_progress.prefix") . "123";
echo isset($_SESSION[$key]) ? json_encode($_SESSION[$key]) : "No upload in progress.";
?>
