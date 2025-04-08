#!/usr/bin/env python3
"""
game_recommender.py
-yash

Game Recommendation System:
- Recommends games based on user preferences using content-based filtering.
- Utilizes TF-IDF vectorization and cosine similarity.
- Contains a small, sample dataset of games.
- Supports both a Command-Line Interface (CLI) and a REST API via FastAPI.

Usage:
    CLI mode:
        python game_recommender.py
    REST API mode:
        python game_recommender.py server
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
# Sample Game Dataset
# ------------------------------
games_data = [
    {
        "title": "Elder Scrolls V: Skyrim",
        "genre": "RPG",
        "description": "An open-world action RPG with dragons, magic, and epic adventure.",
        "tags": "open world, fantasy, adventure, dragons"
    },
    {
        "title": "Portal 2",
        "genre": "Puzzle",
        "description": "A puzzle-platform game that challenges you with portal-based puzzles.",
        "tags": "puzzle, first person, sci-fi, narrative"
    },
    {
        "title": "Dark Souls III",
        "genre": "Action RPG",
        "description": "A challenging action RPG with intricate level design and unforgiving combat.",
        "tags": "challenging, dark fantasy, combat, adventure"
    },
    {
        "title": "Stardew Valley",
        "genre": "Simulation",
        "description": "A farming simulation game with RPG elements, relationships, and exploration.",
        "tags": "farming, simulation, relaxing, indie, RPG"
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "genre": "RPG",
        "description": "An open world RPG with compelling storytelling, monsters, and choices.",
        "tags": "open world, fantasy, narrative, adventure, choice"
    },
    {
        "title": "Rocket League",
        "genre": "Sports",
        "description": "A high-powered hybrid of arcade soccer and vehicular mayhem.",
        "tags": "sports, multiplayer, cars, competitive"
    },
    {
        "title": "Overwatch",
        "genre": "Shooter",
        "description": "A team-based multiplayer first-person shooter with colorful heroes.",
        "tags": "multiplayer, shooter, competitive, heroes"
    }
]

# Create a DataFrame from the sample data
df_games = pd.DataFrame(games_data)
# Combine description and tags for recommendation purposes.
df_games['content'] = df_games['description'] + " " + df_games['tags']

# ------------------------------
# TF-IDF Vectorization
# ------------------------------
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df_games['content'])

# ------------------------------
# Recommendation Function
# ------------------------------
def recommend_games(query: str, top_n: int = 3):
    """
    Recommend games based on the input query using content-based filtering.

    Args:
        query (str): User-provided text to describe game preferences.
        top_n (int): Number of recommendations to return.

    Returns:
        List[Dict]: List of recommended games with similarity scores.
    """
    # Transform the query into the TF-IDF vector space.
    query_vec = vectorizer.transform([query])
    # Compute cosine similarity between the query vector and all game content vectors.
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    # Get the indices of the top-n similar games.
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    recommendations = []
    for idx in top_indices:
        rec = df_games.iloc[idx].to_dict()
        rec['similarity'] = float(cosine_sim[idx])
        recommendations.append(rec)
    return recommendations

# ------------------------------
# FastAPI Web API
# ------------------------------
app = FastAPI(title="Game Recommendation API")

@app.get("/recommend", response_class=JSONResponse)
def api_recommend(query: str, top_n: int = 3):
    """
    API endpoint to get game recommendations based on a query.

    Example:
        /recommend?query=open+world+fantasy&top_n=3
    """
    recommendations = recommend_games(query, top_n)
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found.")
    return {"query": query, "recommendations": recommendations}

# ------------------------------
# Command-Line Interface (CLI)
# ------------------------------
def cli_interface():
    print("=== Game Recommendation System ===")
    query = input("Enter your game preferences (e.g., 'open world fantasy adventure'): ").strip()
    top_n_input = input("How many recommendations would you like? [default: 3]: ").strip()
    try:
        top_n = int(top_n_input) if top_n_input else 3
    except ValueError:
        top_n = 3
    recommendations = recommend_games(query, top_n)
    print("\nRecommended Games:")
    for rec in recommendations:
        print(f"- {rec['title']} (Genre: {rec['genre']}, Similarity: {rec['similarity']:.2f})")
        print(f"  Description: {rec['description']}")
        print(f"  Tags: {rec['tags']}\n")

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    # If "server" is passed as a command-line argument, run the FastAPI server.
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        sys.argv.pop(1)
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        cli_interface()
