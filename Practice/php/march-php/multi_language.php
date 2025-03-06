<?php
$lang = $_GET['lang'] ?? 'en';
$messages = [
    'en' => 'Hello',
    'es' => 'Hola',
    'fr' => 'Bonjour'
];
echo $messages[$lang];
?>
