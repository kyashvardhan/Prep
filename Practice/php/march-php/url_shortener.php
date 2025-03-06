<?php
function shorten($url) {
    return substr(md5($url), 0, 6);
}
echo "Short URL: https://short.ly/" . shorten("https://example.com");
?>
