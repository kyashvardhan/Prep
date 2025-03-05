<?php
/**
 * Wrapper for external API calls using cURL.
 *
 * @param string $url The API endpoint URL.
 * @return mixed Decoded JSON data or false on error.
 */
function api_wrapper($url) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    if(curl_errno($ch)) {
        curl_close($ch);
        return false;
    }
    curl_close($ch);
    return json_decode($response, true);
}

// Example usage:
$data = api_wrapper("https://jsonplaceholder.typicode.com/todos/1");
print_r($data);
?>
