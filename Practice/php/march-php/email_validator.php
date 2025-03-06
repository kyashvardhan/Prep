<?php
header("Content-Type: application/json");
$email = $_GET['email'];
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(["valid" => true]);
} else {
    echo json_encode(["valid" => false]);
}
?>
