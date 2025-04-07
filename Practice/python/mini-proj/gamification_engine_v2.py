#!/usr/bin/env python3
"""
gamification_engine_v2.py

Enhanced Gamification Engine (Version 2)

Features:
- Persistent storage with SQLite for users, tasks, and achievements.
- User registration and login with daily bonus points and streak tracking.
- Task management with varying difficulty levels that award points.
- Achievement system with multiple criteria:
    • First Task Completed
    • 100 Points Earned
    • Level 5 Reached
    • Daily Login Streak (≥3 days)
    • Quest Master (≥3 tasks completed in the past 7 days)
- Dual interface:
    • Interactive Command-Line Interface (CLI)
    • REST API using FastAPI (run with the "server" command-line argument)
- Leaderboard to showcase top users

Run in CLI mode:
    python gamification_engine_v2.py

Run as a web server:
    python gamification_engine_v2.py server
"""

import sqlite3
import datetime
import argparse
import sys
import asyncio
import uvicorn
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

DB_NAME = "gamification_v2.db"

# ------------------------------
# Database Initialization
# ------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Users table: username is unique. Fields for points, level, join_date, last_login, and streak.
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            points INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            join_date TEXT,
            last_login TEXT,
            streak INTEGER DEFAULT 0
        )
    """)
    # Tasks table: stores tasks associated with a user.
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            description TEXT,
            difficulty TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT,
            points INTEGER
        )
    """)
    # Achievements table: stores unlocked achievements per user.
    c.execute("""
        CREATE TABLE IF NOT EXISTS achievements (
            username TEXT,
            achievement TEXT,
            PRIMARY KEY (username, achievement)
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ------------------------------
# Gamification Engine V2 Class
# ------------------------------
class GamificationEngineV2:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    # Helper method to open a connection.
    def _get_conn(self):
        return sqlite3.connect(self.db_name)

    def register_user(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        now = datetime.datetime.now().isoformat()
        try:
            c.execute("INSERT INTO users (username, join_date, last_login) VALUES (?, ?, ?)",
                      (username, now, now))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError("User already exists.")
        conn.close()

    def get_user(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT username, points, level, join_date, last_login, streak FROM users WHERE username=?", (username,))
        row = c.fetchone()
        conn.close()
        return row

    def update_user(self, username: str, field: str, value):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute(f"UPDATE users SET {field}=? WHERE username=?", (value, username))
        conn.commit()
        conn.close()

    def login(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT username, points, level, join_date, last_login, streak FROM users WHERE username=?", (username,))
        row = c.fetchone()
        if not row:
            conn.close()
            raise ValueError("User not found. Please register first.")
        last_login = datetime.datetime.fromisoformat(row[4])
        now = datetime.datetime.now()
        today = now.date()
        last_login_date = last_login.date()
        new_streak = row[5]
        daily_bonus = 0
        if last_login_date < today:
            # If the last login was exactly yesterday, increment streak; otherwise, reset to 1.
            if (today - last_login_date).days == 1:
                new_streak += 1
            else:
                new_streak = 1
            daily_bonus = 20  # Award bonus points for a new day login.
            c.execute("UPDATE users SET points = points + ?, streak = ?, last_login = ? WHERE username=?",
                      (daily_bonus, new_streak, now.isoformat(), username))
        else:
            # Update last_login if already logged in today.
            c.execute("UPDATE users SET last_login = ? WHERE username=?", (now.isoformat(), username))
        conn.commit()
        # Refresh user data.
        c.execute("SELECT username, points, level, join_date, last_login, streak FROM users WHERE username=?", (username,))
        updated_user = c.fetchone()
        conn.close()
        self.update_level(username)
        return updated_user, daily_bonus

    def update_level(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT points FROM users WHERE username=?", (username,))
        points = c.fetchone()[0]
        level = points // 100 + 1
        c.execute("UPDATE users SET level=? WHERE username=?", (level, username))
        conn.commit()
        conn.close()

    def add_task(self, username: str, description: str, difficulty: str = "medium"):
        # Points awarded based on difficulty.
        points = {"easy": 10, "medium": 20, "hard": 30}.get(difficulty.lower(), 20)
        now = datetime.datetime.now().isoformat()
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("INSERT INTO tasks (username, description, difficulty, created_at, points) VALUES (?, ?, ?, ?, ?)",
                  (username, description, difficulty, now, points))
        conn.commit()
        task_id = c.lastrowid
        conn.close()
        return task_id, points

    def complete_task(self, username: str, task_id: int):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT status, points FROM tasks WHERE id=? AND username=?", (task_id, username))
        row = c.fetchone()
        if not row:
            conn.close()
            raise ValueError("Task not found.")
        if row[0] == "completed":
            conn.close()
            raise ValueError("Task is already completed.")
        points = row[1]
        c.execute("UPDATE tasks SET status='completed' WHERE id=?", (task_id,))
        c.execute("UPDATE users SET points = points + ? WHERE username=?", (points, username))
        conn.commit()
        conn.close()
        self.update_level(username)
        self.check_and_unlock_achievements(username)
        return points

    def get_tasks(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT id, description, difficulty, status, created_at, points FROM tasks WHERE username=? ORDER BY created_at DESC", (username,))
        rows = c.fetchall()
        conn.close()
        return rows

    def get_achievements(self, username: str):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT achievement FROM achievements WHERE username=?", (username,))
        rows = c.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_leaderboard(self):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT username, points, level FROM users ORDER BY points DESC")
        rows = c.fetchall()
        conn.close()
        return rows

    def check_and_unlock_achievements(self, username: str):
        """
        Check and unlock achievements for the user.
        Achievements:
          • First Task Completed: ≥1 completed task.
          • 100 Points Earned: points ≥ 100.
          • Level 5 Reached: level ≥ 5.
          • Daily Login Streak: streak ≥ 3.
          • Quest Master: ≥3 tasks completed in the past 7 days.
        """
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT achievement FROM achievements WHERE username=?", (username,))
        existing = {row[0] for row in c.fetchall()}
        new_achievements = []

        # Check "First Task Completed"
        c.execute("SELECT COUNT(*) FROM tasks WHERE username=? AND status='completed'", (username,))
        completed_count = c.fetchone()[0]
        if completed_count >= 1 and "First Task Completed" not in existing:
            new_achievements.append("First Task Completed")

        # Check "100 Points Earned"
        c.execute("SELECT points FROM users WHERE username=?", (username,))
        points = c.fetchone()[0]
        if points >= 100 and "100 Points Earned" not in existing:
            new_achievements.append("100 Points Earned")

        # Check "Level 5 Reached"
        c.execute("SELECT level FROM users WHERE username=?", (username,))
        level = c.fetchone()[0]
        if level >= 5 and "Level 5 Reached" not in existing:
            new_achievements.append("Level 5 Reached")

        # Check "Daily Login Streak" (streak ≥ 3)
        c.execute("SELECT streak FROM users WHERE username=?", (username,))
        streak = c.fetchone()[0]
        if streak >= 3 and "Daily Login Streak" not in existing:
            new_achievements.append("Daily Login Streak")

        # Check "Quest Master": ≥3 tasks completed in the past 7 days.
        seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()
        c.execute("SELECT COUNT(*) FROM tasks WHERE username=? AND status='completed' AND created_at >= ?", (username, seven_days_ago))
        recent_completed = c.fetchone()[0]
        if recent_completed >= 3 and "Quest Master" not in existing:
            new_achievements.append("Quest Master")

        for ach in new_achievements:
            c.execute("INSERT INTO achievements (username, achievement) VALUES (?, ?)", (username, ach))
        conn.commit()
        conn.close()
        return new_achievements

# Instantiate the engine.
engine = GamificationEngineV2()

# ------------------------------
# FastAPI Web API
# ------------------------------
app = FastAPI(title="Gamification Engine V2 API")

@app.post("/register", response_class=JSONResponse)
def api_register(username: str):
    try:
        engine.register_user(username)
        return {"message": f"User '{username}' registered successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login", response_class=JSONResponse)
def api_login(username: str):
    try:
        user, bonus = engine.login(username)
        return {"message": f"User '{username}' logged in.", "daily_bonus": bonus, "user": {
            "username": user[0],
            "points": user[1],
            "level": user[2],
            "streak": user[5]
        }}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tasks", response_class=JSONResponse)
def api_add_task(username: str, description: str, difficulty: str = "medium", background_tasks: BackgroundTasks = None):
    try:
        task_id, pts = engine.add_task(username, description, difficulty)
        return {"message": "Task added.", "task_id": task_id, "points": pts}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/tasks/{task_id}/complete", response_class=JSONResponse)
def api_complete_task(username: str, task_id: int):
    try:
        pts = engine.complete_task(username, task_id)
        return {"message": f"Task {task_id} completed.", "points_awarded": pts}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks", response_class=JSONResponse)
def api_get_tasks(username: str):
    tasks = engine.get_tasks(username)
    return {"tasks": tasks}

@app.get("/achievements", response_class=JSONResponse)
def api_get_achievements(username: str):
    achievements = engine.get_achievements(username)
    return {"achievements": achievements}

@app.get("/leaderboard", response_class=JSONResponse)
def api_leaderboard():
    leaderboard = engine.get_leaderboard()
    return {"leaderboard": leaderboard}

@app.get("/user", response_class=JSONResponse)
def api_user_info(username: str):
    user = engine.get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"user": {
        "username": user[0],
        "points": user[1],
        "level": user[2],
        "join_date": user[3],
        "last_login": user[4],
        "streak": user[5]
    }}

# ------------------------------
# Command-Line Interface (CLI)
# ------------------------------
def cli_interface():
    print("\n=== Gamification Engine V2 (CLI) ===")
    current_user = None
    while True:
        print("\nMenu Options:")
        print("1. Register")
        print("2. Login")
        print("3. Add Task")
        print("4. Complete Task")
        print("5. Show My Tasks")
        print("6. Show My Achievements")
        print("7. Show Leaderboard")
        print("8. Show My Info")
        print("9. Logout")
        print("0. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            username = input("Enter new username: ").strip()
            try:
                engine.register_user(username)
                print(f"User '{username}' registered successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            username = input("Enter username: ").strip()
            try:
                user, bonus = engine.login(username)
                current_user = username
                print(f"Logged in as '{username}'. Daily bonus: {bonus} points.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            if not current_user:
                print("Please login first.")
                continue
            description = input("Enter task description: ").strip()
            difficulty = input("Enter difficulty (easy, medium, hard) [default: medium]: ").strip() or "medium"
            task_id, pts = engine.add_task(current_user, description, difficulty)
            print(f"Task added (ID: {task_id}, Points: {pts}).")
        elif choice == "4":
            if not current_user:
                print("Please login first.")
                continue
            tasks = engine.get_tasks(current_user)
            if not tasks:
                print("No tasks found.")
                continue
            print("Your Tasks:")
            for t in tasks:
                print(f"[{t[0]}] {t[1]} - {t[3].capitalize()} - {t[3]} (Status: {t[3]}, Points: {t[5]})")
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                pts_awarded = engine.complete_task(current_user, task_id)
                print(f"Task {task_id} completed! You earned {pts_awarded} points.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            if not current_user:
                print("Please login first.")
                continue
            tasks = engine.get_tasks(current_user)
            if not tasks:
                print("No tasks found.")
            else:
                print("Your Tasks:")
                for t in tasks:
                    status = "✔" if t[3] == "completed" else "✘"
                    print(f"[{t[0]}] {t[1]} [{t[2].capitalize()}] {status} (Points: {t[5]})")
        elif choice == "6":
            if not current_user:
                print("Please login first.")
                continue
            achievements = engine.get_achievements(current_user)
            if not achievements:
                print("No achievements unlocked yet.")
            else:
                print("Your Achievements:")
                for ach in achievements:
                    print(f"- {ach}")
        elif choice == "7":
            leaderboard = engine.get_leaderboard()
            if not leaderboard:
                print("No users registered yet.")
            else:
                print("\n--- Leaderboard ---")
                for user in leaderboard:
                    print(f"{user[0]}: {user[1]} points (Level {user[2]})")
        elif choice == "8":
            if not current_user:
                print("Please login first.")
                continue
            user = engine.get_user(current_user)
            if user:
                print(f"User Info for '{user[0]}': Points: {user[1]}, Level: {user[2]}, Streak: {user[5]}")
            else:
                print("User not found.")
        elif choice == "9":
            current_user = None
            print("Logged out successfully.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    # If "server" is passed as a command-line argument, run the FastAPI server.
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        # Remove the "server" argument before launching uvicorn.
        sys.argv.pop(1)
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    else:
        cli_interface()
