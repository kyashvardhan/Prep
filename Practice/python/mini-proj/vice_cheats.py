#!/usr/bin/env python3
"""
vice_cheats.py
"""

import random
import argparse

CHEATS = [
    ("ASPIRINE", "Full health"),
    ("PRECIOUSPROTECTION", "Full armor"),
    ("THUGSTOOLS", "Weapon Set 1"),
    ("PROFESSIONALTOOLS", "Weapon Set 2"),
    ("NUTTERTOOLS", "Weapon Set 3"),
    ("PANZER", "Spawn a tank"),
    ("GETTHEREFAST", "Spawn a Sabre Turbo"),
    ("ROCKANDROLLCAR", "Spawn a limousine"),
    ("BIGBANG", "Blow up nearby cars"),
    ("LEAVEMEALONE", "Lower wanted level"),
    ("YOUWONTTAKEMEALIVE", "Raise wanted level"),
    ("SEAWAYS", "Cars can drive on water"),
    ("CATSANDDOGS", "Stormy weather"),
    ("ALOVELYDAY", "Sunny weather"),
    ("ONSPEED", "Faster gameplay"),
    ("BOOOOOORING", "Slower gameplay"),
    ("GRIPISEVERYTHING", "Better vehicle handling"),
    ("AHAIRDRESSERSCAR", "Spawn pink cars"),
    ("IWANTITPAINTEDBLACK", "Spawn black cars"),
    ("LIFEISPASSINGMEBY", "Speed up time"),
]

def generate_cheats(count=3):
    selected = random.sample(CHEATS, k=min(count, len(CHEATS)))
    print("\n🎮 GTA Vice City Random Cheats 🎮\n")
    for code, effect in selected:
        print(f"💡 Cheat: '{code}' - Effect: {effect}")
    print("\nHave fun wreaking havoc in Vice City! 🌴")

def main():
    parser = argparse.ArgumentParser(description="ViceCheats - GTA Vice City random cheat generator")
    parser.add_argument('--count', type=int, default=3, help='Number of cheats to generate (default: 3)')
    args = parser.parse_args()

    generate_cheats(args.count)

if __name__ == "__main__":
    main()
