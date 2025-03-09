<?php
$conn = new mysqli("localhost", "root", "", "chat_db");
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $msg = $_POST['message'];
    $conn->query("INSERT INTO chat (message) VALUES ('$msg')");
}
$result = $conn->query("SELECT * FROM chat");
echo json_encode($result->fetch_all(MYSQLI_ASSOC));
?>
