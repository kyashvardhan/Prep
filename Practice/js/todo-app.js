// HTML structure (for reference):
// <input id="todo-input" type="text" placeholder="Add a task">
// <button id="add-todo">Add Task</button>
// <ul id="todo-list"></ul>

document.getElementById("add-todo").addEventListener("click", function() {
  const input = document.getElementById("todo-input");
  const task = input.value.trim();
  if (task !== "") {
    addTodo(task);
    input.value = "";
  }
});

function addTodo(task) {
  const li = document.createElement("li");
  li.textContent = task;
  li.addEventListener("click", () => li.classList.toggle("completed"));
  document.getElementById("todo-list").appendChild(li);
}
