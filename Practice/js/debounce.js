function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

// Example usage: (For window resize events)
window.addEventListener("resize", debounce(() => {
  console.log("Resized at:", new Date());
}, 500));
