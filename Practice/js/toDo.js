// HTML elements (assume these exist in your HTML)
// <input id="taskInput" type="text" placeholder="Add a task">
// <button id="addTaskBtn">Add Task</button>
// <ul id="taskList"></ul>

document.getElementById("addTaskBtn").addEventListener("click", function() {
  const taskInput = document.getElementById("taskInput");
  const task = taskInput.value.trim();
  if (task !== "") {
    addTask(task);
    taskInput.value = "";
  }
});

function addTask(task) {
  const taskList = document.getElementById("taskList");
  const li = document.createElement("li");
  li.textContent = task;
  li.addEventListener("click", function() {
    li.classList.toggle("completed");
    saveTasks();
  });
  taskList.appendChild(li);
  saveTasks();
}

function saveTasks() {
  const tasks = Array.from(document.querySelectorAll("#taskList li"))
    .map(li => ({ text: li.textContent, done: li.classList.contains("completed") }));
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  tasks.forEach(taskObj => addTask(taskObj.text));
}

loadTasks();
