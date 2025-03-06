<?php
$password = 'MySecurePassword123';

// Hash the password
$hashedPassword = password_hash($password, PASSWORD_BCRYPT);
echo "Hashed Password: $hashedPassword\n";

// Verify the password
$inputPassword = 'MySecurePassword123';
if (password_verify($inputPassword, $hashedPassword)) {
    echo "Password is valid.";
} else {
    echo "Invalid password.";
}
?>
