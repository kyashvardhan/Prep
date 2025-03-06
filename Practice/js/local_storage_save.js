function saveData(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}

function loadData(key) {
  return JSON.parse(localStorage.getItem(key));
}

saveData("user", { name: "John", age: 30 });
console.log(loadData("user"));
