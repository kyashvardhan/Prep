#!/usr/bin/env python3
"""
advanced_app.py

A unified task manager that works in two modes:
1. Web API mode: Run a FastAPI server to manage tasks.
2. CLI mode: Use the command-line interface to add, list, complete, or delete tasks.

Features:
- SQLite database for persistent task storage.
- REST API endpoints for task management.
- Background scheduler that logs the count of pending tasks every 30 seconds.
- CLI for quick task management.
"""

import sqlite3
import asyncio
import logging
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import uvicorn
import argparse
import sys
from datetime import datetime

# ------------------------------
# Logging Configuration
# ------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ------------------------------
# Database Setup and Operations
# ------------------------------
DATABASE = "tasks.db"

def init_db():
    """Initialize the SQLite database and create the tasks table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    logging.info("Database initialized.")

def add_task(description: str) -> int:
    """Add a new task to the database and return its ID."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    logging.info(f"Task added with ID: {task_id}")
    return task_id

def get_tasks() -> list:
    """Retrieve all tasks from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed, created_at FROM tasks ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "description": row[1],
            "completed": bool(row[2]),
            "created_at": row[3]
        })
    return tasks

def complete_task(task_id: int):
    """Mark a task as completed."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise ValueError("Task not found")
    conn.commit()
    conn.close()
    logging.info(f"Task {task_id} marked as completed.")

def delete_task(task_id: int):
    """Delete a task from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise ValueError("Task not found")
    conn.commit()
    conn.close()
    logging.info(f"Task {task_id} deleted.")

# Initialize the database on module load.
init_db()

# ------------------------------
# FastAPI Application
# ------------------------------
app = FastAPI(title="Unified Task Manager")

@app.get("/tasks", response_class=JSONResponse)
def read_tasks():
    """Retrieve all tasks via REST API."""
    tasks = get_tasks()
    return {"tasks": tasks}

@app.post("/tasks", response_class=JSONResponse)
def create_task(description: str, background_tasks: BackgroundTasks):
    """Create a new task via REST API."""
    task_id = add_task(description)
    background_tasks.add_task(log_task_creation, task_id, description)
    return {"message": "Task created", "task_id": task_id}

def log_task_creation(task_id: int, description: str):
    """Background task to log task creation."""
    logging.info(f"Background log: Task {task_id} with description '{description}' was created.")

@app.put("/tasks/{task_id}/complete", response_class=JSONResponse)
def mark_task_complete(task_id: int):
    """Mark a task as complete via REST API."""
    try:
        complete_task(task_id)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    return {"message": f"Task {task_id} marked as complete."}

@app.delete("/tasks/{task_id}", response_class=JSONResponse)
def remove_task(task_id: int):
    """Delete a task via REST API."""
    try:
        delete_task(task_id)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    return {"message": f"Task {task_id} deleted."}

# ------------------------------
# Background Scheduler
# ------------------------------
async def pending_tasks_logger():
    """Periodically log the number of pending (incomplete) tasks."""
    while True:
        tasks = get_tasks()
        pending = sum(1 for t in tasks if not t["completed"])
        logging.info(f"Pending tasks count: {pending}")
        await asyncio.sleep(30)  # Log every 30 seconds

# ------------------------------
# Command-Line Interface (CLI)
# ------------------------------
def cli_interface():
    parser = argparse.ArgumentParser(description="Unified Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="CLI commands")

    # Add task command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    # Complete task command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as complete")
    parser_complete.add_argument("task_id", type=int, help="ID of the task to mark complete")

    # Delete task command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        task_id = add_task(args.description)
        print(f"Task added with ID: {task_id}")
    elif args.command == "list":
        tasks = get_tasks()
        if not tasks:
            print("No tasks found.")
        for t in tasks:
            status = "✔" if t["completed"] else "✘"
            print(f"[{t['id']}] {status} {t['description']} (Created: {t['created_at']})")
    elif args.command == "complete":
        try:
            complete_task(args.task_id)
            print(f"Task {args.task_id} marked as complete.")
        except ValueError as ve:
            print(f"Error: {ve}")
    elif args.command == "delete":
        try:
            delete_task(args.task_id)
            print(f"Task {args.task_id} deleted.")
        except ValueError as ve:
            print(f"Error: {ve}")
    else:
        parser.print_help()

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    # If the first CLI argument is "server", run the web server.
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        # Remove the "server" argument and run the FastAPI server.
        sys.argv.pop(1)
        loop = asyncio.get_event_loop()
        loop.create_task(pending_tasks_logger())
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        # Otherwise, use the CLI interface.
        cli_interface()
