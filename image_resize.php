<?php
function resizeImage($filename, $width, $height) {
    list($w, $h) = getimagesize($filename);
    $src = imagecreatefromjpeg($filename);
    $dst = imagecreatetruecolor($width, $height);
    imagecopyresampled($dst, $src, 0, 0, 0, 0, $width, $height, $w, $h);
    imagejpeg($dst, 'resized_' . $filename);
}
resizeImage('image.jpg', 200, 150);
?>
