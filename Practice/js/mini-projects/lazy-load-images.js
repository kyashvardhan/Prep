document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll("img[data-src]");

    const lazyLoad = function (entries, observer) {
        entries.for
