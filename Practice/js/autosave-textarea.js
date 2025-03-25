const textarea = document.getElementById("editor");

textarea.value = localStorage.getItem("draft") || "";

textarea.addEventListener("input", () => {
  localStorage.setItem("draft", textarea.value);
});

window.addEventListener("beforeunload", () => {
  alert("Your draft is saved automatically!");
});
