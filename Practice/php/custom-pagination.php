<?php
/**
 * Generate custom pagination links.
 *
 * @param int $total_items Total number of items.
 * @param int $items_per_page Number of items per page.
 * @param int $current_page Current page number.
 * @return string HTML pagination links.
 */
function custom_pagination($total_items, $items_per_page, $current_page) {
    $total_pages = ceil($total_items / $items_per_page);
    $pagination = '<nav class="pagination">';
    for ($i = 1; $i <= $total_pages; $i++) {
        if ($i == $current_page) {
            $pagination .= "<span class='current'>{$i}</span> ";
        } else {
            $pagination .= "<a href='?page={$i}'>{$i}</a> ";
        }
    }
    $pagination .= '</nav>';
    return $pagination;
}

// Example usage:
echo custom_pagination(100, 10, 3);
?>
