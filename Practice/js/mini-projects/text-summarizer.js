function summarizeText(text) {
  const wordCount = text.trim().split(/\s+/).length;
  const charCount = text.replace(/\s/g, '').length;

  return {
    wordCount,
    charCount,
    summary: text.length > 100 ? text.substring(0, 100) + "..." : text,
  };
}

// Example
const inputText = "JavaScript is a versatile language used in both frontend and backend web development.";
const result = summarizeText(inputText);

console.log(`Words: ${result.wordCount}`);
console.log(`Characters: ${result.charCount}`);
console.log(`Summary: ${result.summary}`);
