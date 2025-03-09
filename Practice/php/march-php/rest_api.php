<?php
header("Content-Type: application/json");
$conn = new mysqli("localhost", "root", "", "api_db");

// Fetch all records
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $result = $conn->query("SELECT * FROM data");
    echo json_encode($result->fetch_all(MYSQLI_ASSOC));
}

// Insert record
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);
    $name = $data['name'];
    $conn->query("INSERT INTO data (name) VALUES ('$name')");
    echo json_encode(["message" => "Record Added"]);
}

// Update record
if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
    $data = json_decode(file_get_contents("php://input"), true);
    $id = $data['id'];
    $name = $data['name'];
    $conn->query("UPDATE data SET name='$name' WHERE id=$id");
    echo json_encode(["message" => "Record Updated"]);
}

// Delete record
if ($_SERVER['REQUEST_METHOD'] == 'DELETE') {
    $id = $_GET['id'];
    $conn->query("DELETE FROM data WHERE id=$id");
    echo json_encode(["message" => "Record Deleted"]);
}
?>
