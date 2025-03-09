<?php
if ($_FILES) {
    $image = $_FILES['image']['tmp_name'];
    $destination = 'uploads/' . $_FILES['image']['name'];
    move_uploaded_file($image, $destination);

    // Resize Image
    $resized = imagecreatefromjpeg($destination);
    $thumb = imagescale($resized, 200, 200);
    imagejpeg($thumb, 'uploads/resized_' . $_FILES['image']['name']);
    echo "Image Uploaded & Resized!";
}
?>
