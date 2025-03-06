<?php
$cacheFile = "cache/page.html";
if (file_exists($cacheFile) && time() - filemtime($cacheFile) < 60) {
    readfile($cacheFile);
} else {
    ob_start();
    echo "Page generated at ".date('H:i:s');
    file_put_contents($cacheFile, ob_get_contents());
    ob_end_flush();
}
?>
