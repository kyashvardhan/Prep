# sentiment_analysis.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

sentiment_classifier = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_classifier(text)[0]
    return jsonify({
        "text": text,
        "sentiment": result['label'],
        "score": round(result['score'], 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
