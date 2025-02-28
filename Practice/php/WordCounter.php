<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $text = $_POST['text'];
    $word_count = str_word_count($text);
    echo "Word count: $word_count";
}
?>

<form method="post">
    <textarea name="text" placeholder="Enter text here" required></textarea>
    <button type="submit">Count Words</button>
</form>
