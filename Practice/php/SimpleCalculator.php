<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $operation = $_POST['operation'];

    switch ($operation) {
        case "add":
            echo "Result: " . ($num1 + $num2);
            break;
        case "subtract":
            echo "Result: " . ($num1 - $num2);
            break;
        case "multiply":
            echo "Result: " . ($num1 * $num2);
            break;
        case "divide":
            echo ($num2 != 0) ? "Result: " . ($num1 / $num2) : "Cannot divide by zero!";
            break;
        default:
            echo "Invalid operation.";
    }
}
?>
