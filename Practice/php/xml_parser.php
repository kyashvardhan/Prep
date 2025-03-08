<?php
$xml = simplexml_load_file('data.xml');
foreach ($xml->record as $record) {
    echo $record->name . "\n";
}
?>
