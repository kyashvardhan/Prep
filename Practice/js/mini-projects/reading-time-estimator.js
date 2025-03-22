function estimateReadingTime(text, wpm = 200) {
    const words = text.trim().split(/\s+/).length;
    const time = Math.ceil(words / wpm);
    return `⏱ Estimated Reading Time: ${time} min`;
}

// Example usage
const article = `
  JavaScript is a powerful language used in modern web development.
  It allows you to build dynamic and interactive web experiences.
  Mastering it opens doors to frontend and backend opportunities.
`;

console.log(estimateReadingTime(article));
