function convert_to_title_case($string) {
    return ucwords(strtolower($string));
}

function reverse_string($string) {
    $reversed = "";
    for ($i = strlen($string) - 1; $i >= 0; $i--) {
        $reversed .= $string[$i];
    }
    return $reversed;
}

function reverse_string_optimized($string) {
    return implode('', array_reverse(str_split($string)));
}
