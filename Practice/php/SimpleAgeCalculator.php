<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $birth_year = $_POST['birth_year'];
    $current_year = date("Y");
    
    if ($birth_year > 1900 && $birth_year <= $current_year) {
        $age = $current_year - $birth_year;
        echo "You are $age years old.";
    } else {
        echo "Please enter a valid birth year.";
    }
}
?>

<form method="post">
    <input type="number" name="birth_year" min="1900" max="<?= date("Y") ?>" required>
    <button type="submit">Calculate Age</button>
</form>
