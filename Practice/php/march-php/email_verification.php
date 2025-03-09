<?php
session_start();
use PHPMailer\PHPMailer\PHPMailer;
require 'vendor/autoload.php';

$otp = rand(100000, 999999);
$_SESSION['otp'] = $otp;

$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';
$mail->setFrom('user@example.com', 'Admin');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Your OTP Code';
$mail->Body = 'Your OTP is: ' . $otp;
$mail->send();
?>
