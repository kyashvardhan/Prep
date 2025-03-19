async function fetchGitHubRepos(username) {
    const response = await fetch(`https://api.github.com/users/${username}/repos`);
    const repos = await response.json();

    const portfolioContainer = document.getElementById("portfolio");
    portfolioContainer.innerHTML = ""; // Clear previous content

    repos.forEach(repo => {
        const repoElement = document.createElement("div");
        repoElement.classList.add("repo-card");
        repoElement.innerHTML = `
            <h3>${repo.name}</h3>
            <p>${repo.description ? repo.description : "No description available"}</p>
            <a href="${repo.html_url}" target="_blank">View on GitHub</a>
        `;
        portfolioContainer.appendChild(repoElement);
    });
}

document.getElementById("fetchPortfolio").addEventListener("click", () => {
    const username = document.getElementById("githubUsername").value;
    fetchGitHubRepos(username);
});
