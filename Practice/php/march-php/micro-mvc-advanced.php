<?php
// index.php - Entry point for our advanced micro MVC framework

// Simple Autoloader for controllers and models
spl_autoload_register(function($class) {
    if (file_exists("controllers/{$class}.php")) {
        require "controllers/{$class}.php";
    } elseif (file_exists("models/{$class}.php")) {
        require "models/{$class}.php";
    }
});

// Basic Router
$url = isset($_GET['url']) ? rtrim($_GET['url'], '/') : '';
$urlComponents = explode('/', $url);

// Default controller and method
$controllerName = !empty($urlComponents[0]) ? ucfirst($urlComponents[0]) . 'Controller' : 'HomeController';
$methodName = isset($urlComponents[1]) ? $urlComponents[1] : 'index';
$params = array_slice($urlComponents, 2);

// Load controller file
if (file_exists("controllers/{$controllerName}.php")) {
    $controller = new $controllerName();
    if (method_exists($controller, $methodName)) {
        call_user_func_array([$controller, $methodName], $params);
    } else {
        echo "Method {$methodName} not found in {$controllerName}";
    }
} else {
    echo "Controller {$controllerName} not found.";
}
?>
