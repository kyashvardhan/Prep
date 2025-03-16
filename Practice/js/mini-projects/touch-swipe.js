function addTouchSwipe(slideshow) {
    let touchStartX = 0;

    document.addEventListener("touchstart", function(event) {
        touchStartX = event.touches[0].clientX;
    });

    document.addEventListener("touchend", function(event) {
        let touchEndX = event.changedTouches[0].clientX;
        if (touchStartX - touchEndX > 50) {
            slideshow.nextSlide();
        } else if (touchEndX - touchStartX > 50) {
            slideshow.prevSlide();
        }
    });
}

// Usage Example
const mySlideshow = new Slideshow(["Slide 1", "Slide 2", "Slide 3"]);
addTouchSwipe(mySlideshow);
