<?php
$data = [["Name", "Email"], ["John Doe", "john@example.com"]];
$fp = fopen('users.csv', 'w');
foreach ($data as $fields) {
    fputcsv($fp, $fields);
}
fclose($fp);
echo "CSV created.";
?>
