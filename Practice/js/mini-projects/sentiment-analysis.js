function analyzeSentiment(input) {
    const positiveWords = ["happy", "love", "excellent", "great", "fantastic"];
    const negativeWords = ["bad", "terrible", "sad", "horrible", "angry"];

    let positiveCount = 0;
    let negativeCount = 0;

    input.toLowerCase().split(" ").forEach(word => {
        if (positiveWords.includes(word)) positiveCount++;
        if (negativeWords.includes(word)) negativeCount++;
    });

    if (positiveCount > negativeCount) {
        return "😊 Positive Sentiment";
    } else if (negativeCount > positiveCount) {
        return "😡 Negative Sentiment";
    } else {
        return "😐 Neutral Sentiment";
    }
}

// Example Usage
const userFeedback = "I love this product, it's fantastic!";
console.log(analyzeSentiment(userFeedback));
