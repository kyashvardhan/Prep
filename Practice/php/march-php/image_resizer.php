<?php
$source = imagecreatefromjpeg($_FILES['image']['tmp_name']);
$resized = imagescale($source, 200, 200);
imagejpeg($resized, "resized/".uniqid().".jpg");
echo "Image resized successfully.";
?>
