<?php
// Sorting an array
$numbers = [5, 3, 8, 1, 2];
sort($numbers);
print_r($numbers); // Output: [1, 2, 3, 5, 8]

// Filtering an array
$evenNumbers = array_filter($numbers, function($num) {
    return $num % 2 == 0;
});
print_r($evenNumbers); // Output: [2, 8]
?>
