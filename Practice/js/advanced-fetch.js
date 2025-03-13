async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    return null;
  }
}

// Self-invoking function for testing
(async () => {
  const data = await fetchData("https://jsonplaceholder.typicode.com/posts/1");
  console.log("Fetched Data:", data);
})();
