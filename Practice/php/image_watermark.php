<?php
$image = imagecreatefromjpeg('input.jpg');
$color = imagecolorallocate($image, 255, 255, 255);
$font = __DIR__ . '/arial.ttf';
$text = "Watermarked";

imagettftext($image, 20, 0, 10, 30, $color, $font, $text);
imagejpeg($image, 'watermarked.jpg');
imagedestroy($image);
?>
