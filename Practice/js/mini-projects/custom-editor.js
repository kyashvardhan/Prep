document.addEventListener("DOMContentLoaded", () => {
    const editor = document.getElementById("editor");

    editor.addEventListener("input", () => {
        localStorage.setItem("editorContent", editor.innerHTML);
    });

    editor.innerHTML = localStorage.getItem("editorContent") || "<p>Edit this text...</p>";
});
