<?php
// index.php - Entry point for our micro MVC framework

// Autoloader
spl_autoload_register(function($class) {
    include 'controllers/' . $class . '.php';
});

// Simple Router
$url = $_GET['url'] ?? '';
$url = rtrim($url, '/');
$url = explode('/', $url);

$controllerName = !empty($url[0]) ? ucfirst($url[0]) . 'Controller' : 'HomeController';
$method = $url[1] ?? 'index';
$params = array_slice($url, 2);

if (file_exists("controllers/{$controllerName}.php")) {
    $controller = new $controllerName();
    if (method_exists($controller, $method)) {
        call_user_func_array([$controller, $method], $params);
    } else {
        echo "Method not found.";
    }
} else {
    echo "Controller not found.";
}
?>
