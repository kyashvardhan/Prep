async function fetchWithCache(apiUrl, cacheKey, cacheDuration = 600000) {
    const cachedData = localStorage.getItem(cacheKey);
    const cachedTime = localStorage.getItem(`${cacheKey}_time`);

    if (cachedData && cachedTime && Date.now() - cachedTime < cacheDuration) {
        return JSON.parse(cachedData);
    }

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        localStorage.setItem(cacheKey, JSON.stringify(data));
        localStorage.setItem(`${cacheKey}_time`, Date.now());

        return data;
    } catch (error) {
        console.error("API Fetch Error:", error);
        return null;
    }
}

// Example
fetchWithCache("https://wptavern.com/wp-json/wp/v2/posts", "latest_posts")
    .then(data => console.log("Fetched Data:", data));
