// Fetch latest posts from a given API and display dynamically
async function fetchLatestPosts(apiUrl) {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        
        const container = document.createElement("div");
        container.classList.add("post-container");

        data.forEach(post => {
            const postElement = document.createElement("div");
            postElement.classList.add("post");
            postElement.innerHTML = `
                <h2>${post.title.rendered}</h2>
                <p>${post.excerpt.rendered}</p>
                <a href="${post.link}" target="_blank">Read More</a>
            `;
            container.appendChild(postElement);
        });

        document.body.appendChild(container);
    } catch (error) {
        console.error("Error fetching posts:", error);
    }
}

// Example API call (Replace with real WP REST API)
fetchLatestPosts("https://wptavern.com/wp-json/wp/v2/posts");
