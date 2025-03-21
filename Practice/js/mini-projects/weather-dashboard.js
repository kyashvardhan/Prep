const apiKey = "YOUR_OPENWEATHER_API_KEY";
const city = "New York";

async function fetchWeather(city) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        console.log(`🌦️ Weather in ${city}:`);
        console.log(`🌡️ Temperature: ${data.main.temp}°C`);
        console.log(`💧 Humidity: ${data.main.humidity}%`);
        console.log(`🌤️ Condition: ${data.weather[0].description}`);
    } catch (error) {
        console.error("Error fetching weather data:", error);
    }
}

// Example usage
fetchWeather(city);
