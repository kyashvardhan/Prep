<?php
$data = [
    ["Name", "Age"],
    ["Virat", 30],
    ["Rohit", 25]
];

$fp = fopen('output.csv', 'w');
foreach ($data as $line) {
    fputcsv($fp, $line);
}
fclose($fp);
echo "CSV generated.";
?>
