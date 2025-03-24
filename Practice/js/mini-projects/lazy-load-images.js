document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll("img[data-src]");

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.getAttribute("data-src");
        img.removeAttribute("data-src");
        obs.unobserve(img);
      }
    });
  });

  images.forEach(img => observer.observe(img));
});

// Example HTML:
// <img data-src="image1.jpg" alt="Lazy image" width="300" height="200">
