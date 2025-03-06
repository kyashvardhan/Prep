document.querySelectorAll(".accordion").forEach((btn) => {
  btn.onclick = () => {
    btn.classList.toggle("active");
    const panel = btn.nextElementSibling;
    panel.style.display =
      panel.style.display === "block" ? "none" : "block";
  };
});
