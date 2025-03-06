<?php
$secretKey = "YOUR_SECRET_KEY";
$responseKey = $_POST['g-recaptcha-response'];
$verify = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=$secretKey&response=$responseKey");
$response = json_decode($verify);
if ($response->success) {
    echo "Verified.";
} else {
    echo "Failed.";
}
?>
