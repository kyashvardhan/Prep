document.addEventListener("keydown", function(event) {
  if (event.ctrlKey && event.key === "s") {
    event.preventDefault();
    console.log("Ctrl + S was pressed – Saving the document!");
  }

  if (event.ctrlKey && event.key === "z") {
    event.preventDefault();
    console.log("Ctrl + Z was pressed – Undo action triggered!");
  }
});
