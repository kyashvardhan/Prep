let page = 1;
const container = document.getElementById("post-container");

async function fetchPosts() {
    const response = await fetch(`https://wptavern.com/wp-json/wp/v2/posts?page=${page}`);
    const posts = await response.json();

    posts.forEach(post => {
        const postElement = document.createElement("div");
        postElement.classList.add("post");
        postElement.innerHTML = `
            <h2>${post.title.rendered}</h2>
            <p>${post.excerpt.rendered}</p>
            <a href="${post.link}" target="_blank">Read More</a>
        `;
        container.appendChild(postElement);
    });

    page++;
}

window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 50) {
        fetchPosts();
    }
});

fetchPosts();
