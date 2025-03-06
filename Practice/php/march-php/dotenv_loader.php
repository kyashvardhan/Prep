<?php
foreach (file('.env') as $line) {
    putenv(trim($line));
}
echo getenv('DB_HOST');
?>
