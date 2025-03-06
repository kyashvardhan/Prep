const countdown = (date) => {
  const end = new Date(date).getTime();
  const timer = setInterval(() => {
    const now = new Date().getTime();
    const distance = end - now;
    if (distance < 0) {
      clearInterval(timer);
      console.log("Time's up!");
    } else {
      console.log(
        Math.floor(distance / (1000 * 60 * 60 * 24)) + " days remaining"
      );
    }
  }, 1000);
};

countdown("2025-12-31");
