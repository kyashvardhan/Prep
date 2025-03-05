<?php
// Custom exception class
class MyCustomException extends Exception {}

function divide($numerator, $denominator) {
    if ($denominator == 0) {
        throw new MyCustomException("Division by zero error.");
    }
    return $numerator / $denominator;
}

try {
    echo divide(10, 0);
} catch (MyCustomException $e) {
    echo "Caught exception: " . $e->getMessage();
}
?>
