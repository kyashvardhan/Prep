<?php
$data = ['name' => 'John Doe', 'email' => 'john@example.com'];
$jsonData = json_encode($data);

file_put_contents("user.json", $jsonData);
echo "JSON file created!";
?>
