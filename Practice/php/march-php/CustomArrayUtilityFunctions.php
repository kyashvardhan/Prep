function find_max_value($array) {
    $max = $array[0];
    foreach ($array as $num) {
        if ($num > $max) {
            $max = $num;
        }
    }
    return $max;
}

function find_min_value($array) {
    $min = $array[0];
    foreach ($array as $num) {
        if ($num < $min) {
            $min = $num;
        }
    }
    return $min;
}
