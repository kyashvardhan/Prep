<?php
$images = glob("images/gallery/*.{jpg,png,gif}", GLOB_BRACE);
$per_page = 4;
$total_images = count($images);
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$total_pages = ceil($total_images / $per_page);
$start = ($page - 1) * $per_page;
$gallery = array_slice($images, $start, $per_page);

echo "<div class='gallery'>";
foreach ($gallery as $img) {
    echo "<img src='$img' alt='Gallery Image' style='width:200px;margin:5px;'/>";
}
echo "</div>";

echo custom_pagination($total_images, $per_page, $page);
?>
