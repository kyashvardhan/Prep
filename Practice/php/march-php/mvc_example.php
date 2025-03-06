<?php
// Model
class User {
    public function getUser() {
        return ['name' => 'John Doe', 'email' => 'john@example.com'];
    }
}

// Controller
class UserController {
    public function show() {
        $user = (new User())->getUser();
        include 'user_view.php';
    }
}

// View (user_view.php)
// <?php
// echo "Name: {$user['yash']}<br>Email: {$user['email']}";

// Run
(new UserController())->show();
?>
