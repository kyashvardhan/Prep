<?php
class DB {
    private static $instance = null;
    private $conn;
    private function __construct() {
        $this->conn = new PDO("mysql:host=localhost;dbname=test", "root", "");
    }
    public static function getInstance() {
        if (!self::$instance) self::$instance = new DB();
        return self::$instance->conn;
    }
}
$db = DB::getInstance();
?>
