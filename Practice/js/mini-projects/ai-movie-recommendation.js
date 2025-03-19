const apiKey = "YOUR_OPENAI_API_KEY";
const movieList = [
    { title: "Interstellar", genre: "Sci-Fi" },
    { title: "The Dark Knight", genre: "Action" },
    { title: "Inception", genre: "Thriller" },
    { title: "Titanic", genre: "Romance" },
    { title: "The Godfather", genre: "Crime" }
];

async function getMovieRecommendation(userInput) {
    const prompt = `User likes ${userInput}. Suggest a similar movie.`;

    const response = await fetch("https://api.openai.com/v1/completions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "text-davinci-003",
            prompt: prompt,
            max_tokens: 50
        })
    });

    const data = await response.json();
    return data.choices[0].text.trim();
}

// Handling User Input
document.getElementById("getRecommendation").addEventListener("click", async () => {
    const userPreference = document.getElementById("userInput").value;
    const recommendation = await getMovieRecommendation(userPreference);

    document.getElementById("output").innerText = `Recommended Movie: ${recommendation}`;
});
