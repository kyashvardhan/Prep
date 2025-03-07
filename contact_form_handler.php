<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "admin@example.com";
    $subject = "New Contact Form Submission";
    $message = "Name: " . $_POST['name'] . "\nMessage: " . $_POST['message'];
    $headers = "From: " . $_POST['email'];

    mail($to, $subject, $message, $headers);
    echo "Message Sent!";
}
?>
