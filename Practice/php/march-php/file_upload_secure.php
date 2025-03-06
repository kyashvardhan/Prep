<?php
if ($_FILES['file']['error'] == UPLOAD_ERR_OK) {
    $allowed = ['jpg', 'png', 'pdf'];
    $ext = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
    if (in_array($ext, $allowed)) {
        move_uploaded_file($_FILES['file']['tmp_name'], "uploads/".uniqid().".$ext");
        echo "Upload successful.";
    } else {
        echo "Invalid file type.";
    }
}
?>
