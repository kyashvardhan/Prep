#!/usr/bin/env python3
"""
vice_mission_picker.py
"""

import random
import argparse

MISSIONS = [
    ("An Old Friend", "Sonny Forelli"),
    ("The Party", "Ken Rosenberg"),
    ("Back Alley Brawl", "Ken Rosenberg"),
    ("Jury Fury", "Ken Rosenberg"),
    ("Riot", "Ken Rosenberg"),
    ("Treacherous Swine", "Colonel Juan Cortez"),
    ("Mall Shootout", "Colonel Juan Cortez"),
    ("Guardian Angels", "Colonel Juan Cortez"),
    ("The Chase", "Ricardo Diaz"),
    ("Phnom Penh '86", "Ricardo Diaz"),
    ("Supply & Demand", "Ricardo Diaz"),
    ("Death Row", "Kent Paul"),
    ("Rub Out", "Lance Vance"),
    ("Shakedown", "Tommy Vercetti"),
    ("Bar Brawl", "Tommy Vercetti"),
    ("Cop Land", "Tommy Vercetti"),
    ("Cap the Collector", "Earnest Kelly"),
    ("Hit the Courier", "Print Works"),
    ("Check Out at the Check-In", "Mr. Black"),
    ("Loose Ends", "Mr. Black")
]

def pick_missions(count=1):
    selected = random.sample(MISSIONS, k=min(count, len(MISSIONS)))
    print("\n🎬 GTA Vice City Mission Suggestion 🎬\n")
    for mission, character in selected:
        print(f"🎯 Mission: '{mission}' | Given by: {character}")
    print("\nEnjoy your mission in Vice City! 🌴🚗")

def main():
    parser = argparse.ArgumentParser(description="ViceCityMissionPicker - Random GTA Vice City mission picker")
    parser.add_argument('--count', type=int, default=1, help='Number of missions to suggest (default: 1)')
    args = parser.parse_args()

    pick_missions(args.count)

if __name__ == "__main__":
    main()
