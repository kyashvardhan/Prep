<?php
use PHPMailer\PHPMailer\PHPMailer;
require 'vendor/autoload.php';

$mail = new PHPMailer();
$mail->setFrom('your-email@example.com');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Email Verification';
$mail->Body = 'Click the link to verify your email: <a href="verify.php?code=xyz">Verify</a>';
$mail->send();

echo "Verification email sent!";
?>
