class ResumeEvaluator {
    constructor(jobKeywords) {
        this.jobKeywords = jobKeywords.map(word => word.toLowerCase());
    }

    evaluate(resumeText) {
        let words = resumeText.toLowerCase().split(/\s+/);
        let score = 0;

        words.forEach(word => {
            if (this.jobKeywords.includes(word)) {
                score++;
            }
        });

        let percentage = ((score / this.jobKeywords.length) * 100).toFixed(2);
        return `Resume Match: ${percentage}%`;
    }
}

// Example usage
const jobKeywords = ["JavaScript", "React", "Node.js", "API", "Frontend", "Developer"];
const evaluator = new ResumeEvaluator(jobKeywords);

const resumeText = "I am a Frontend Developer skilled in JavaScript, React, and working with APIs.";
console.log(evaluator.evaluate(resumeText));
