#!/usr/bin/env python3
"""
big_bang_episode_recommender.py
"""

import random

# Database of episodes grouped by mood
EPISODES = {
    "funny": [
        ("The Pants Alternative", "S03E18"),
        ("The Adhesive Duck Deficiency", "S03E08"),
        ("The Dumpling Paradox", "S01E07"),
        ("The Staircase Implementation", "S03E22"),
        ("The Love Car Displacement", "S04E13"),
    ],
    "romantic": [
        ("The Romance Resonance", "S07E06"),
        ("The Prom Equivalency", "S08E08"),
        ("The Locomotion Manipulation", "S07E15"),
        ("The Commitment Determination", "S08E24"),
    ],
    "emotional": [
        ("The Bath Item Gift Hypothesis", "S02E11"),
        ("The Opening Night Excitation", "S09E11"),
        ("The Long Distance Dissonance", "S10E24"),
    ],
    "science-heavy": [
        ("The Large Hadron Collision", "S03E15"),
        ("The Space Probe Disintegration", "S08E12"),
        ("The Einstein Approximation", "S03E14"),
        ("The Higgs Boson Observation", "S06E03"),
    ],
    "classic": [
        ("Pilot", "S01E01"),
        ("The Nerdvana Annihilation", "S01E14"),
        ("The Peanut Reaction", "S01E16"),
        ("The Electric Can Opener Fluctuation", "S03E01"),
    ]
}

def suggest_episode(mood=None):
    if mood and mood.lower() in EPISODES:
        choice = random.choice(EPISODES[mood.lower()])
    else:
        all_eps = sum(EPISODES.values(), [])
        choice = random.choice(all_eps)

    episode_title, episode_code = choice
    print("\n🎬 Suggested Episode 🎬")
    print(f"  - {episode_title} ({episode_code})\n")
    print("Enjoy your binge! 🍿")

def list_moods():
    print("\nAvailable moods/themes:")
    for mood in EPISODES.keys():
        print(f"  - {mood.capitalize()}")

def main():
    print("🧠 Big Bang Theory Episode Recommender 🧠")
    list_moods()
    mood = input("\nHow are you feeling? (or press Enter for random): ").strip()

    suggest_episode(mood)

if __name__ == "__main__":
    main()
