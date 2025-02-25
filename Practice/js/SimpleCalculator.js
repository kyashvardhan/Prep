// Assume HTML has: <input id="calcDisplay" readonly> and buttons with data-value attributes
const buttons = document.querySelectorAll(".calc-btn");
const display = document.getElementById("calcDisplay");

buttons.forEach(button => {
  button.addEventListener("click", function() {
    const value = this.getAttribute("data-value");
    if (value === "=") {
      display.value = eval(display.value); // Warning: eval() used for simplicity
    } else if (value === "C") {
      display.value = "";
    } else {
      display.value += value;
    }
  });
});
