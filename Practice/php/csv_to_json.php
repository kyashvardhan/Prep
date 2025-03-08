<?php
$csv = array_map('str_getcsv', file('data.csv'));
$json = json_encode($csv);
file_put_contents('data.json', $json);
echo "CSV converted to JSON!";
?>
