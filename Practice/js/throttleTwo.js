function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Example usage: Attach to scroll event
window.addEventListener("scroll", throttle(() => {
  console.log("Scroll event triggered at:", new Date());
}, 1000));
