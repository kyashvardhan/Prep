<?php
// Simple Task Manager REST API using OOP in PHP
header("Content-Type: application/json");

// Task Manager Class
class TaskManager {
    private $tasks = [];

    public function __construct() {
        // Load existing tasks from file if exists
        if (file_exists('tasks.json')) {
            $this->tasks = json_decode(file_get_contents('tasks.json'), true);
        }
    }

    public function addTask($title) {
        $id = uniqid();
        $this->tasks[$id] = [
            "id" => $id,
            "title" => $title,
            "completed" => false
        ];
        $this->saveTasks();
        return $this->tasks[$id];
    }

    public function getTasks() {
        return $this->tasks;
    }

    public function updateTask($id, $title, $completed) {
        if (isset($this->tasks[$id])) {
            $this->tasks[$id]["title"] = $title;
            $this->tasks[$id]["completed"] = $completed;
            $this->saveTasks();
            return $this->tasks[$id];
        }
        return null;
    }

    public function deleteTask($id) {
        if (isset($this->tasks[$id])) {
            unset($this->tasks[$id]);
            $this->saveTasks();
            return true;
        }
        return false;
    }

    private function saveTasks() {
        file_put_contents('tasks.json', json_encode($this->tasks, JSON_PRETTY_PRINT));
    }
}

// API Logic
$taskManager = new TaskManager();
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        echo json_encode(["tasks" => $taskManager->getTasks()]);
        break;

    case 'POST':
        $data = json_decode(file_get_contents('php://input'), true);
        if (isset($data['title'])) {
            $task = $taskManager->addTask($data['title']);
            echo json_encode(["message" => "Task added", "task" => $task]);
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Task title required"]);
        }
        break;

    case 'PUT':
        $data = json_decode(file_get_contents('php://input'), true);
        if (isset($data['id'], $data['title'], $data['completed'])) {
            $task = $taskManager->updateTask($data['id'], $data['title'], $data['completed']);
            if ($task) {
                echo json_encode(["message" => "Task updated", "task" => $task]);
            } else {
                http_response_code(404);
                echo json_encode(["error" => "Task not found"]);
            }
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Invalid data"]);
        }
        break;

    case 'DELETE':
        $data = json_decode(file_get_contents('php://input'), true);
        if (isset($data['id'])) {
            if ($taskManager->deleteTask($data['id'])) {
                echo json_encode(["message" => "Task deleted"]);
            } else {
                http_response_code(404);
                echo json_encode(["error" => "Task not found"]);
            }
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Task ID required"]);
        }
        break;

    default:
        http_response_code(405);
        echo json_encode(["error" => "Method not allowed"]);
        break;
}
?>
