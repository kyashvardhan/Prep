<?php
$xml = simplexml_load_file("data.xml");
foreach ($xml->user as $user) {
    echo $user->name . " - " . $user->email . "<br>";
}
?>
