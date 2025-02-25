async function fetchWeather(city) {
  // Simulated API URL (replace with a real endpoint if available)
  const url = `https://api.example.com/weather?city=${city}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    displayWeather(data);
  } catch (error) {
    console.error("Error fetching weather data:", error);
  }
}

function displayWeather(data) {
  // Assume an HTML element exists: <div id="weatherDisplay"></div>
  document.getElementById("weatherDisplay").innerText =
    `City: ${data.city} | Temperature: ${data.temp}°C | Condition: ${data.condition}`;
}

// Simulate data fetching on page load
fetchWeather("New York");
