<?php
session_start();
if (!isset($_SESSION['number'])) {
    $_SESSION['number'] = rand(1, 10);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $guess = (int)$_POST['guess'];
    if ($guess == $_SESSION['number']) {
        echo "Congratulations! You guessed the correct number!";
        session_destroy();
    } elseif ($guess > $_SESSION['number']) {
        echo "Too high! Try again.";
    } else {
        echo "Too low! Try again.";
    }
}
?>

<form method="post">
    <input type="number" name="guess" min="1" max="10" required>
    <button type="submit">Guess</button>
</form>
