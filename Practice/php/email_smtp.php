<?php
use PHPMailer\PHPMailer\PHPMailer;
require 'vendor/autoload.php';

$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';
$mail->setFrom('user@example.com', 'User');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email.';
$mail->send();
?>
