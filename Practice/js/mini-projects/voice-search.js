const searchInput = document.getElementById("search");
const searchButton = document.getElementById("voice-search");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.onresult = (event) => {
    searchInput.value = event.results[0][0].transcript;
};

searchButton.addEventListener("click", () => {
    recognition.start();
});
