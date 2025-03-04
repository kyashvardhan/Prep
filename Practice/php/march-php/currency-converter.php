<?php
$amount = 100;
$fromCurrency = "USD";
$toCurrency = "INR";
$apiKey = "your_api_key";

$url = "https://api.exchangerate-api.com/v4/latest/$fromCurrency";
$response = file_get_contents($url);
$data = json_decode($response, true);

$convertedAmount = $amount * $data['rates'][$toCurrency];
echo "$amount $fromCurrency = $convertedAmount $toCurrency";
?>
