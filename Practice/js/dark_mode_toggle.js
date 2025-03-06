const toggleDarkMode = () => {
  document.body.classList.toggle("dark-mode");
};
document.querySelector("#darkModeBtn").onclick = toggleDarkMode;
