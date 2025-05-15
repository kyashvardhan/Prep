#!/usr/bin/env python3
"""
abacus_simulator.py
"""

def display_abacus(number):
    """
    Displays a number on an ASCII Abacus.
    Each digit is represented by beads (o) and spaces.
    """
    abacus = ""
    str_num = str(number)

    print("\n🧮 Abacus Simulation 🧮")
    print("Each row represents a digit (top = highest place value):\n")
    
    for digit in str_num:
        bead_count = int(digit)
        beads = "o " * bead_count
        empty = ". " * (9 - bead_count)
        abacus += f"| {beads}{empty}|\n"

    print(abacus)

def main():
    print("Welcome to the Abacus Simulator!")
    try:
        num = int(input("Enter a positive number to visualize on the abacus: "))
        if num < 0:
            print("❌ Please enter a non-negative number!")
            return
        display_abacus(num)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
