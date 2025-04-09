#!/usr/bin/env python3
"""
netflix_recommender.py
-by yash

Advanced Netflix Recommendation Engine (2025 Edition)

This project recommends Netflix shows/movies by analyzing their content including
description, genres, and cast using TF-IDF vectorization and cosine similarity.
It supports two modes:
  • CLI mode: Interactive recommendation based on user query.
  • REST API mode: Exposes an endpoint to get recommendations via FastAPI.

Usage:
    CLI mode:
      python netflix_recommender.py
    REST API mode:
      python netflix_recommender.py server
"""

import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

# ------------------------------
# Sample Netflix Dataset (2025 Edition)
# ------------------------------
# In a production setting, this data might come from a database or CSV.
# Here, we use a sample dataset to demonstrate functionality.
data = [
    {
        "title": "Stranger Worlds",
        "genres": "Sci-fi, Thriller, Adventure",
        "description": "A mind-bending journey into parallel universes where every choice alters reality.",
        "cast": "Ava DuVernay, John Cho, Zendaya",
        "release_year": 2025
    },
    {
        "title": "The Last Kingdom",
        "genres": "Historical, Drama, Action",
        "description": "In a tumultuous era, a lost prince battles to reclaim his heritage while redefining honor.",
        "cast": "Idris Elba, Gemma Chan, Daniel Kaluuya",
        "release_year": 2025
    },
    {
        "title": "Digital Shadows",
        "genres": "Crime, Thriller, Drama",
        "description": "A gripping narrative where cybercrime collides with corporate espionage in the digital age.",
        "cast": "Rami Malek, Lupita Nyong'o, Tessa Thompson",
        "release_year": 2025
    },
    {
        "title": "Heart of the Forest",
        "genres": "Fantasy, Adventure, Family",
        "description": "An enchanting tale set in a mystical forest where legends come alive and magic thrives.",
        "cast": "Millie Bobby Brown, Tom Holland, Saoirse Ronan",
        "release_year": 2025
    },
    {
        "title": "Echoes of Tomorrow",
        "genres": "Sci-fi, Mystery, Drama",
        "description": "A time-travel drama that blurs the line between destiny and free will in a futuristic society.",
        "cast": "Chris Hemsworth, Brie Larson, Donald Glover",
        "release_year": 2025
    },
    {
        "title": "Urban Legends",
        "genres": "Horror, Thriller, Mystery",
        "description": "A chilling anthology that uncovers the dark secrets lurking behind urban myth and folklore.",
        "cast": "Toni Collette, Lakeith Stanfield, Florence Pugh",
        "release_year": 2025
    }
]

# Convert the sample data to a DataFrame.
df_netflix = pd.DataFrame(data)

# Create a combined content field for recommendations.
df_netflix['content'] = df_netflix['description'] + " " + df_netflix['genres'] + " " + df_netflix['cast']

# ------------------------------
# TF-IDF Vectorization & Cosine Similarity
# ------------------------------
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df_netflix['content'])

def recommend_netflix(query: str, top_n: int = 3):
    """
    Recommend Netflix titles based on a user query using content-based filtering.

    Args:
        query (str): User description or preferences (e.g., "sci-fi thriller with time travel").
        top_n (int): The number of top recommendations to return.

    Returns:
        List[dict]: Recommendations including title, genres, description, cast, and similarity score.
    """
    # Transform the query into the TF-IDF vector space.
    query_vec = vectorizer.transform([query])
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    # Get indices of the most similar titles.
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    recommendations = []
    for idx in top_indices:
        rec = df_netflix.iloc[idx].to_dict()
        rec['similarity'] = float(cosine_sim[idx])
        recommendations.append(rec)
    return recommendations

# ------------------------------
# FastAPI REST API Setup
# ------------------------------
app = FastAPI(title="Netflix Recommendation Engine (2025 Edition)")

@app.get("/recommend", response_class=JSONResponse)
def api_recommend(query: str, top_n: int = 3):
    """
    API endpoint to get Netflix recommendations.

    Example:
        /recommend?query=sci-fi+thriller+time+travel&top_n=3
    """
    recommendations = recommend_netflix(query, top_n)
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found.")
    return {"query": query, "recommendations": recommendations}

# ------------------------------
# Command-Line Interface (CLI)
# ------------------------------
def cli_interface():
    print("=== Netflix Recommendation System (2025 Edition) ===")
    query = input("Describe your favorite type of show (e.g., 'fantasy adventure magic'): ").strip()
    top_n_input = input("How many recommendations would you like? [default: 3]: ").strip()
    try:
        top_n = int(top_n_input) if top_n_input else 3
    except ValueError:
        top_n = 3
    recommendations = recommend_netflix(query, top_n)
    print("\nRecommended Titles:")
    for rec in recommendations:
        print(f"\nTitle: {rec['title']} ({rec['release_year']})")
        print(f"Genres: {rec['genres']}")
        print(f"Description: {rec['description']}")
        print(f"Cast: {rec['cast']}")
        print(f"Similarity Score: {rec['similarity']:.2f}")

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    # Run FastAPI server if "server" is provided as an argument.
    if len(sys.argv) > 1 and sys.argv[1].lower() == "server":
        sys.argv.pop(1)
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        cli_interface()
