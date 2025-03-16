class Slideshow {
    constructor(slides) {
        this.slides = slides;
        this.currentIndex = 0;
        this.showSlide(this.currentIndex);
    }

    showSlide(index) {
        document.getElementById("slide").innerHTML = this.slides[index];
    }

    nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.slides.length;
        this.showSlide(this.currentIndex);
    }

    prevSlide() {
        this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
        this.showSlide(this.currentIndex);
    }
}

// Example usage
const slides = ["Slide 1 Content", "Slide 2 Content", "Slide 3 Content"];
const mySlideshow = new Slideshow(slides);

document.getElementById("next").addEventListener("click", () => mySlideshow.nextSlide());
document.getElementById("prev").addEventListener("click", () => mySlideshow.prevSlide());
