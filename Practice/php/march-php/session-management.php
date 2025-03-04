<?php
session_start();
$_SESSION["user"] = "JohnDoe";
echo "Session started for user: " . $_SESSION["user"];
?>
