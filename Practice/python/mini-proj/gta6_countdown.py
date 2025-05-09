#!/usr/bin/env python3
"""
gta6_countdown.py
"""

import datetime
import time
import sys
import os

GTA6_RELEASE_DATE = datetime.datetime(2025, 10, 22, 0, 0, 0)  # Rumored GTA 6 release date

ASCII_ART = r"""
   _____ _______       ___     __   
  / ____|__   __|/\   |__ \   / /   
 | |  __   | |  /  \     ) | / /_   
 | | |_ |  | | / /\ \   / / | '_ \  
 | |__| |  | |/ ____ \ / /_ | (_) | 
  \_____|  |_/_/    \_\____(_)___/  

"""

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_countdown(td):
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

def countdown():
    while True:
        clear_terminal()
        print(ASCII_ART)
        now = datetime.datetime.now()
        if now >= GTA6_RELEASE_DATE:
            print("🎉 GTA 6 has been released! 🎮🚗💨\n")
            break

        time_left = GTA6_RELEASE_DATE - now
        days, hours, mins, secs = format_countdown(time_left)

        print(f"⏳ GTA 6 Rumored Release Date Countdown ⏳\n")
        print(f"     {days} Days, {hours} Hours, {mins} Minutes, {secs} Seconds remaining!\n")
        print("       🚗 Get ready to hit the streets of Vice City again! 🌴")
        print("\n(Press Ctrl+C to exit.)")

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nCountdown stopped. Stay hyped! 🔥")
            sys.exit()

def main():
    countdown()

if __name__ == "__main__":
    main()
