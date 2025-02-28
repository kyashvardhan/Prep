<?php
session_start();
if (!isset($_SESSION['tasks'])) {
    $_SESSION['tasks'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST['task'])) {
    $_SESSION['tasks'][] = htmlspecialchars($_POST['task']);
}

if (isset($_GET['clear'])) {
    session_destroy();
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}

echo "<h3>To-Do List:</h3><ul>";
foreach ($_SESSION['tasks'] as $task) {
    echo "<li>$task</li>";
}
echo "</ul>";
?>

<form method="post">
    <input type="text" name="task" placeholder="Enter a task" required>
    <button type="submit">Add Task</button>
</form>
<a href="?clear=true">Clear List</a>
