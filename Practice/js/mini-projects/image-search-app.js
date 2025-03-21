const apiKey = "YOUR_UNSPLASH_API_KEY";
const searchQuery = "mountains";

async function fetchImages(query) {
    const url = `https://api.unsplash.com/search/photos?query=${query}&client_id=${apiKey}`;
    
    try {
        const response = await fetch(url);
        const data = await response.json();
        
        console.log(`📸 Images for: ${query}`);
        data.results.forEach((image, index) => {
            console.log(`${index + 1}. ${image.urls.small}`);
        });
    } catch (error) {
        console.error("Error fetching images:", error);
    }
}

// Example usage
fetchImages(searchQuery);
