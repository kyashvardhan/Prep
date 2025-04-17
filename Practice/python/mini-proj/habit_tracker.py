#!/usr/bin/env python3
"""
habit_tracker.py

CLI Habit Tracker with Streak Calculation and Visualization

Commands:
  - add <habit>         : Define a new habit to track
  - log <habit>         : Log completion of a habit for today
  - streak <habit>      : Show current streak for a habit
  - history <habit>     : List all log dates for a habit
  - plot <habit>        : Plot your habit log history

Usage:
  python habit_tracker.py add "Exercise"
  python habit_tracker.py log "Exercise"
  python habit_tracker.py streak "Exercise"
  python habit_tracker.py history "Exercise"
  python habit_tracker.py plot "Exercise"
"""

import sqlite3
import sys
import argparse
import datetime
import matplotlib.pyplot as plt

DB = "habits.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            habit_id INTEGER,
            date TEXT,
            PRIMARY KEY (habit_id, date),
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
    """)
    conn.commit()
    conn.close()

def add_habit(name):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO habits (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Habit '{name}' added.")
    except sqlite3.IntegrityError:
        print(f"Habit '{name}' already exists.")
    conn.close()

def log_habit(name):
    today = datetime.date.today().isoformat()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id FROM habits WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        print(f"No such habit: '{name}'.")
    else:
        hid = row[0]
        try:
            c.execute("INSERT INTO logs (habit_id, date) VALUES (?, ?)", (hid, today))
            conn.commit()
            print(f"Logged '{name}' for {today}.")
        except sqlite3.IntegrityError:
            print(f"Already logged '{name}' for {today}.")
    conn.close()

def show_streak(name):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id FROM habits WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        print(f"No such habit: '{name}'.")
        conn.close(); return
    hid = row[0]
    c.execute("SELECT date FROM logs WHERE habit_id=? ORDER BY date DESC", (hid,))
    dates = [datetime.date.fromisoformat(r[0]) for r in c.fetchall()]
    conn.close()
    streak = 0
    today = datetime.date.today()
    for d in dates:
        if d == today - datetime.timedelta(days=streak):
            streak += 1
        else:
            break
    print(f"Current streak for '{name}': {streak} day(s)")

def show_history(name):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id FROM habits WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        print(f"No such habit: '{name}'.")
        conn.close(); return
    hid = row[0]
    c.execute("SELECT date FROM logs WHERE habit_id=? ORDER BY date", (hid,))
    rows = c.fetchall()
    conn.close()
    if not rows:
        print(f"No logs for '{name}'.")
    else:
        print(f"History for '{name}':")
        for r in rows:
            print(" ", r[0])

def plot_history(name):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id FROM habits WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        print(f"No such habit: '{name}'.")
        conn.close(); return
    hid = row[0]
    c.execute("SELECT date FROM logs WHERE habit_id=? ORDER BY date", (hid,))
    rows = c.fetchall()
    conn.close()
    if not rows:
        print(f"No logs to plot for '{name}'.")
        return

    dates = [datetime.date.fromisoformat(r[0]) for r in rows]
    counts = list(range(1, len(dates) + 1))
    plt.figure(figsize=(8, 4))
    plt.plot(dates, counts, marker='o')
    plt.title(f"Progress for '{name}'")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Logs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("add", help="Add a new habit").add_argument("name")
    sub.add_parser("log", help="Log completion of a habit").add_argument("name")
    sub.add_parser("streak", help="Show current streak").add_argument("name")
    sub.add_parser("history", help="Show log history").add_argument("name")
    sub.add_parser("plot", help="Plot habit history").add_argument("name")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help(); sys.exit(1)
    if args.cmd == "add":
        add_habit(args.name)
    elif args.cmd == "log":
        log_habit(args.name)
    elif args.cmd == "streak":
        show_streak(args.name)
    elif args.cmd == "history":
        show_history(args.name)
    elif args.cmd == "plot":
        plot_history(args.name)

if __name__ == "__main__":
    main()
