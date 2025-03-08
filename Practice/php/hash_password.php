<?php
$password = "SecurePass123";
$hash = password_hash($password, PASSWORD_BCRYPT);
echo "Hashed Password: " . $hash;

// Verify password
if (password_verify("SecurePass123", $hash)) {
    echo "Password is valid!";
} else {
    echo "Invalid password!";
}
?>
