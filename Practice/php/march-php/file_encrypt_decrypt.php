<?php
$key = "encryption_key";
$data = file_get_contents("file.txt");

// Encrypt
$encrypted = openssl_encrypt($data, 'AES-128-ECB', $key);
file_put_contents("encrypted.txt", $encrypted);

// Decrypt
$decrypted = openssl_decrypt($encrypted, 'AES-128-ECB', $key);
file_put_contents("decrypted.txt", $decrypted);
?>
