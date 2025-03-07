<?php
if ($_FILES['file']) {
    $uploadDir = "uploads/";
    $file = $uploadDir . basename($_FILES["file"]["name"]);
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $file)) {
        echo "File uploaded successfully!";
    } else {
        echo "Upload failed.";
    }
}
?>
