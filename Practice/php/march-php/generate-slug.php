<?php
function generateSlug($string) {
    return strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $string), '-'));
}

$title = "Learn PHP in 30 Days!";
echo generateSlug($title);
?>
