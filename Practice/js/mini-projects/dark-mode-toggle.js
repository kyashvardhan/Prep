const toggleButton = document.getElementById("dark-mode-toggle");

function setTheme(theme) {
    document.body.className = theme;
    localStorage.setItem("theme", theme);
}

toggleButton.addEventListener("click", () => {
    const currentTheme = localStorage.getItem("theme") === "dark" ? "light" : "dark";
    setTheme(currentTheme);
});

// Load saved theme
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    setTheme(savedTheme);
});
