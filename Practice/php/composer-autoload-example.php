<?php
// Assuming you've run `composer init` and created a composer.json file.
// Create a simple class in src/Greeting.php:
require 'vendor/autoload.php'; // Composer's autoloader

use App\Greeting;

$greet = new Greeting("Yash");
echo $greet->sayHello();

// File: src/Greeting.php
// namespace App;
// class Greeting {
//     private $name;
//     public function __construct($name) {
//         $this->name = $name;
//     }
//     public function sayHello() {
//         return "Hello, " . $this->name . "!";
//     }
// }
?>
