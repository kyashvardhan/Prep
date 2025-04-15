#!/usr/bin/env python3
"""
murder_mystery.py

Interactive Murder Mystery Text Adventure Game

Story:
  A notorious murder has occurred in the old Ravenswood Mansion.
  You, a determined detective, must explore various rooms,
  gather clues, and piece together the identity of the culprit.
  
Commands:
  - go <direction>: Move between rooms (e.g., "go north")
  - search         : Search the current room for clues
  - inventory      : Show collected clues
  - solve          : Attempt to solve the mystery
  - help           : Display available commands
  - quit           : Exit the game
"""

import sys

# Define the mansion's layout as a dictionary of rooms.
rooms = {
    'Foyer': {
        'description': 'You stand in the foyer of Ravenswood Mansion. The atmosphere is tense.',
        'exits': {'north': 'Library', 'east': 'Kitchen'},
        'clue': None
    },
    'Library': {
        'description': 'Rows of dusty books line the walls. A portrait of the late owner hangs crookedly.',
        'exits': {'south': 'Foyer', 'east': 'Study'},
        'clue': 'A torn piece of a diary reading "I know the secret..."'
    },
    'Kitchen': {
        'description': 'The kitchen is cold. Pots and pans are strewn about, and something is missing from the counter.',
        'exits': {'west': 'Foyer', 'north': 'Dining Room'},
        'clue': 'A strange glove left behind. It doesn’t match the uniforms of the staff.'
    },
    'Study': {
        'description': 'The study is cluttered with papers and evidence of a struggle. A broken vase lies on the floor.',
        'exits': {'west': 'Library'},
        'clue': 'A set of fingerprints on a glass, distinct from those of the household.'
    },
    'Dining Room': {
        'description': 'An opulent dining room now feels empty and ominous. The table is set for a meal that will never be served.',
        'exits': {'south': 'Kitchen', 'east': 'Basement'},
        'clue': 'A note tucked under a plate: "It was all planned, and I had no choice."'
    },
    'Basement': {
        'description': 'The basement is dark and eerie. You sense that secrets here are best left undisturbed.',
        'exits': {'west': 'Dining Room'},
        'clue': 'A bloodstained letter with the initials "J.D."'
    }
}

# Global game state variables.
current_room = 'Foyer'
inventory = []  # Clues collected by the player.

def show_help():
    print("\nAvailable commands:")
    print("  go <direction>  : Move in a direction (north, south, east, west)")
    print("  search          : Search the room for clues")
    print("  inventory       : Show collected clues")
    print("  solve           : Make an accusation and solve the mystery")
    print("  help            : Show this help message")
    print("  quit            : Exit the game")

def move(direction):
    global current_room
    if direction in rooms[current_room]['exits']:
        new_room = rooms[current_room]['exits'][direction]
        current_room = new_room
        print(f"\nYou move {direction} to the {new_room}.")
        describe_room()
    else:
        print(f"\nYou can't go {direction} from here.")

def describe_room():
    room = rooms[current_room]
    print(f"\n-- {current_room} --")
    print(room['description'])
    exits = ', '.join(room['exits'].keys())
    print(f"Exits: {exits}")

def search_room():
    room = rooms[current_room]
    if room.get('clue'):
        if room['clue'] not in inventory:
            print("\nYou search the room and find a clue!")
            print("Clue: " + room['clue'])
            inventory.append(room['clue'])
        else:
            print("\nYou've already collected the clue from this room.")
    else:
        print("\nThere is nothing of interest here.")

def show_inventory():
    if inventory:
        print("\nCollected clues:")
        for idx, clue in enumerate(inventory, start=1):
            print(f"  {idx}. {clue}")
    else:
        print("\nYou haven't collected any clues yet.")

def attempt_solve():
    print("\nTime to solve the mystery!")
    print("Based on the clues, who do you think is the murderer?")
    suspect = input("Enter the suspect's initials (e.g., J.D.): ").strip()
    # In this narrative, the murderer is 'J.D.' based on the basement clue.
    if suspect.upper() == "J.D.":
        print("\nCongratulations, Detective! You have solved the mystery.")
        print("Your careful investigation led to the arrest of the culprit.")
        sys.exit(0)
    else:
        print("\nThat's not correct. The investigation continues...")

def game_loop():
    global current_room
    print("Welcome to Ravenswood Mansion Murder Mystery!")
    describe_room()
    show_help()
    while True:
        command = input("\n> ").strip().lower()
        if command.startswith("go "):
            direction = command.split()[1]
            move(direction)
        elif command == "search":
            search_room()
        elif command == "inventory":
            show_inventory()
        elif command == "help":
            show_help()
        elif command == "solve":
            attempt_solve()
        elif command == "quit":
            print("\nExiting the game. Goodbye!")
            sys.exit(0)
        else:
            print("Unknown command. Type 'help' to see the list of commands.")

if __name__ == "__main__":
    game_loop()
