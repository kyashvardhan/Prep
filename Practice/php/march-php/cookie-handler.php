<?php
setcookie("user", "JohnDoe", time() + (86400 * 30), "/");
if(isset($_COOKIE["user"])) {
    echo "User: " . $_COOKIE["user"];
} else {
    echo "No cookie set!";
}
?>
