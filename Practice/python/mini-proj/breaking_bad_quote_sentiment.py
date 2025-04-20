#!/usr/bin/env python3
"""
breaking_bad_quote_sentiment.py
"""

import requests
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import sys

QUOTES_API = "https://breakingbadapi.com/api/quotes"

def fetch_quotes():
    """Fetch all quotes from the Breaking Bad API."""
    resp = requests.get(QUOTES_API)
    resp.raise_for_status()
    return resp.json()

def analyze_sentiments(quotes):
    """
    For each character, compile their quotes and compute average sentiment.
    Returns a dict of {character: (average_score, count_of_quotes)}.
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = defaultdict(list)

    for q in quotes:
        author = q.get("author", "").strip()
        text = q.get("quote", "").strip()
        if author and text:
            vs = analyzer.polarity_scores(text)
            # use compound score for single metric
            scores[author].append(vs["compound"])

    # Compute averages
    avg_scores = {}
    for author, vals in scores.items():
        avg = sum(vals) / len(vals)
        avg_scores[author] = (avg, len(vals))
    return avg_scores

def plot_sentiment(avg_scores, min_quotes=5):
    """
    Plot average sentiment for characters with at least `min_quotes`.
    Bars ordered by descending average sentiment.
    """
    # Filter out characters with too few quotes
    filtered = {a: data for a, data in avg_scores.items() if data[1] >= min_quotes}
    if not filtered:
        print(f"No characters with ≥{min_quotes} quotes found.")
        return

    # Sort by average sentiment
    sorted_chars = sorted(filtered.items(), key=lambda x: x[1][0], reverse=True)
    authors = [a for a, _ in sorted_chars]
    avgs = [data[0] for _, data in sorted_chars]
    counts = [data[1] for _, data in sorted_chars]

    plt.figure(figsize=(10, 6))
    bars = plt.barh(authors, avgs, color='teal', alpha=0.7)
    plt.xlabel("Average Sentiment (compound)")
    plt.title(f"Breaking Bad Quote Sentiment (min {min_quotes} quotes)")
    plt.gca().invert_yaxis()  # highest at top

    # Annotate counts and scores
    for bar, count, score in zip(bars, counts, avgs):
        w = bar.get_width()
        plt.text(w + 0.01, bar.get_y() + bar.get_height()/2,
                 f"{score:.2f} ({count})", va='center')

    plt.tight_layout()
    plt.show()

def main():
    print("Fetching Breaking Bad quotes…")
    try:
        quotes = fetch_quotes()
    except requests.RequestException as e:
        print("Failed to fetch quotes:", e, file=sys.stderr)
        sys.exit(1)

    print(f"Analyzing sentiment for {len(quotes)} quotes…")
    avg_scores = analyze_sentiments(quotes)

    # Print top 5 characters by number of quotes
    top_by_count = sorted(avg_scores.items(), key=lambda x: x[1][1], reverse=True)[:5]
    print("\nTop 5 characters by quote count:")
    for author, (avg, cnt) in top_by_count:
        print(f"  {author}: {cnt} quotes, avg sentiment {avg:.2f}")

    # Plot for characters with at least 5 quotes
    plot_sentiment(avg_scores, min_quotes=5)

if __name__ == "__main__":
    main()
