document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowRight") {
        document.getElementById("next").click();
    } else if (event.key === "ArrowLeft") {
        document.getElementById("prev").click();
    }
});
