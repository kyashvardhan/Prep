#!/usr/bin/env python3
"""
calendar_viewer.py
"""

import calendar
import datetime

def display_month(year, month):
    print("\n🗓️ Monthly Calendar\n")
    print(calendar.month(year, month))

def display_year(year):
    print("\n📆 Full Year Calendar\n")
    print(calendar.TextCalendar(firstweekday=0).formatyear(year, 2, 1, 1, 3))

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"❌ Enter a value between {min_val} and {max_val}")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    print("📘 Calendar Viewer")
    print("1. Show a specific month")
    print("2. Show full year")
    print("0. Exit")

    while True:
        choice = input("\nChoose an option (0-2): ")
        if choice == '1':
            year = get_valid_input("Enter year (e.g., 2025): ", 1, 9999)
            month = get_valid_input("Enter month (1-12): ", 1, 12)
            display_month(year, month)
        elif choice == '2':
            year = get_valid_input("Enter year (e.g., 2025): ", 1, 9999)
            display_year(year)
        elif choice == '0':
            print("👋 Exiting Calendar Viewer.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
