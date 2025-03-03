<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    $uploadDir = "uploads/";
    $file = $_FILES["file"];
    $targetPath = $uploadDir . basename($file["name"]);

    if (move_uploaded_file($file["tmp_name"], $targetPath)) {
        echo "File uploaded successfully!";
    } else {
        echo "Failed to upload file.";
    }
}
?>
