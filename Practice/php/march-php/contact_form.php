<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    echo "Thank you, $name. We will contact you at $email.";
}
?>

<form method="post">
    Name: <input type="text" name="name">
    Email: <input type="email" name="email">
    <input type="submit" value="Submit">
</form>
