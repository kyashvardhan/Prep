#!/usr/bin/env python3
"""
gamification_engine.py

A Gamification Engine for Productivity:
- Users can register and login.
- Users add tasks with a chosen difficulty (easy, medium, hard).
- Completing tasks awards points and may unlock achievements.
- Points accumulate to level up the user.
- A leaderboard displays top users.

This single-file project demonstrates OOP, CLI design, and gamification mechanics.
"""

import datetime
import sys

# ------------------------------
# Data Classes
# ------------------------------
class Task:
    def __init__(self, description: str, difficulty: str = "medium"):
        self.description = description
        self.difficulty = difficulty.lower()
        self.status = "pending"
        self.created_at = datetime.datetime.now()
        # Points based on difficulty
        self.points = {"easy": 10, "medium": 20, "hard": 30}.get(self.difficulty, 20)

    def __str__(self):
        status_icon = "✔" if self.status == "completed" else "✘"
        return f"{self.description} [{self.difficulty.capitalize()}] - {status_icon} (Points: {self.points})"


class Achievement:
    def __init__(self, name: str, description: str, criteria_func):
        self.name = name
        self.description = description
        self.criteria_func = criteria_func  # Function to check achievement condition

    def __str__(self):
        return f"{self.name}: {self.description}"


class User:
    def __init__(self, username: str):
        self.username = username
        self.points = 0
        self.level = 1
        self.tasks = []
        self.achievements = set()
        self.join_date = datetime.datetime.now()

    def add_points(self, pts: int):
        self.points += pts
        self.update_level()

    def update_level(self):
        # For every 100 points, user levels up.
        self.level = self.points // 100 + 1

    def add_task(self, task: Task):
        self.tasks.append(task)

    def complete_task(self, task_index: int):
        if task_index < 0 or task_index >= len(self.tasks):
            raise ValueError("Invalid task index.")
        task = self.tasks[task_index]
        if task.status == "completed":
            raise ValueError("Task is already completed.")
        task.status = "completed"
        self.add_points(task.points)
        return task

    def __str__(self):
        return f"{self.username}: {self.points} points (Level {self.level})"


# ------------------------------
# Gamification Engine
# ------------------------------
class GamificationEngine:
    def __init__(self):
        self.users = {}  # username -> User instance
        self.achievements_catalog = []
        self.init_achievements()

    def init_achievements(self):
        # Achievement for completing the first task.
        self.achievements_catalog.append(
            Achievement(
                "First Task Completed",
                "Complete your very first task.",
                lambda user: any(task.status == "completed" for task in user.tasks)
            )
        )
        # Achievement for earning 100 points.
        self.achievements_catalog.append(
            Achievement(
                "100 Points Earned",
                "Accumulate at least 100 points.",
                lambda user: user.points >= 100
            )
        )
        # Achievement for reaching level 5.
        self.achievements_catalog.append(
            Achievement(
                "Level 5 Reached",
                "Achieve Level 5.",
                lambda user: user.level >= 5
            )
        )

    def register_user(self, username: str) -> User:
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def get_user(self, username: str) -> User:
        return self.users.get(username)

    def add_task_to_user(self, username: str, description: str, difficulty: str = "medium") -> Task:
        user = self.get_user(username)
        if not user:
            raise ValueError("User not found.")
        task = Task(description, difficulty)
        user.add_task(task)
        return task

    def complete_task_for_user(self, username: str, task_index: int) -> Task:
        user = self.get_user(username)
        if not user:
            raise ValueError("User not found.")
        task = user.complete_task(task_index)
        self.check_and_unlock_achievements(user)
        return task

    def check_and_unlock_achievements(self, user: User):
        unlocked = []
        for achievement in self.achievements_catalog:
            if achievement.name not in user.achievements and achievement.criteria_func(user):
                user.achievements.add(achievement.name)
                unlocked.append(achievement)
        return unlocked

    def get_leaderboard(self):
        # Sort users by points descending.
        return sorted(self.users.values(), key=lambda u: u.points, reverse=True)


# ------------------------------
# Command-Line Interface (CLI)
# ------------------------------
def main():
    engine = GamificationEngine()
    current_user = None

    def print_menu():
        print("\n=== Gamification Engine Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Add Task")
        print("4. Complete Task")
        print("5. Show My Tasks")
        print("6. Show My Achievements")
        print("7. Show Leaderboard")
        print("8. Logout")
        print("9. Exit")

    while True:
        print_menu()
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
            user = engine.get_user(username)
            if user:
                current_user = user
                print(f"Logged in as '{username}'.")
            else:
                print("User not found. Please register first.")
        elif choice == "3":
            if not current_user:
                print("Please login first.")
                continue
            description = input("Enter task description: ").strip()
            difficulty = input("Enter difficulty (easy, medium, hard) [default: medium]: ").strip() or "medium"
            try:
                task = engine.add_task_to_user(current_user.username, description, difficulty)
                print(f"Task added: {task}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            if not current_user:
                print("Please login first.")
                continue
            if not current_user.tasks:
                print("No tasks available.")
                continue
            print("Your Tasks:")
            for idx, task in enumerate(current_user.tasks):
                print(f"{idx}. {task}")
            try:
                index = int(input("Enter task index to mark as complete: ").strip())
                task = engine.complete_task_for_user(current_user.username, index)
                print(f"Task '{task.description}' completed! You earned {task.points} points.")
                unlocked = engine.check_and_unlock_achievements(current_user)
                if unlocked:
                    for ach in unlocked:
                        print(f"Achievement unlocked: {ach.name} - {ach.description}")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif choice == "5":
            if not current_user:
                print("Please login first.")
                continue
            if not current_user.tasks:
                print("No tasks found.")
            else:
                print("Your Tasks:")
                for idx, task in enumerate(current_user.tasks):
                    print(f"{idx}. {task}")
        elif choice == "6":
            if not current_user:
                print("Please login first.")
                continue
            if not current_user.achievements:
                print("No achievements unlocked yet.")
            else:
                print("Your Achievements:")
                for ach in current_user.achievements:
                    print(f"- {ach}")
        elif choice == "7":
            leaderboard = engine.get_leaderboard()
            if not leaderboard:
                print("No users registered yet.")
            else:
                print("\n--- Leaderboard ---")
                for user in leaderboard:
                    print(f"{user.username}: {user.points} points (Level {user.level})")
        elif choice == "8":
            current_user = None
            print("Logged out successfully.")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
