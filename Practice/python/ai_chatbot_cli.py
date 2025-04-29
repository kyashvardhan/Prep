#!/usr/bin/env python3
"""
ai_chatbot_cli.py

A command-line AI chatbot using OpenAI's ChatCompletion API with:

- Streaming responses (prints as tokens arrive).
- Rolling conversation memory (keeps last N messages).
- /reset command to clear context.
- Logs all conversations to a JSON file with timestamps.

Usage:
    export OPENAI_API_KEY="your_api_key"
    python ai_chatbot_cli.py
"""

import os
import sys
import json
import time
import datetime
import openai

# Configuration
MAX_MEMORY_MESSAGES = 10            # Keep last N messages plus system prompt
CHAT_LOG_FILE = "chat_history.json" # Append each session here
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful, concise AI assistant. "
               "Keep answers clear and to the point."
}

def load_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Error: Please set OPENAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)
    openai.api_key = key

def save_chat_log(session_messages):
    """Append the full session (with timestamps) to CHAT_LOG_FILE."""
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "messages": session_messages
    }
    try:
        with open(CHAT_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"Warning: failed to write chat log: {e}", file=sys.stderr)

def trim_memory(memory):
    """Keep the system prompt + last MAX_MEMORY_MESSAGES user/assistant pairs."""
    if len(memory) <= MAX_MEMORY_MESSAGES + 1:
        return memory
    # Always keep SYSTEM_PROMPT at index 0
    return [memory[0]] + memory[-MAX_MEMORY_MESSAGES:]

def chat():
    load_api_key()
    memory = [SYSTEM_PROMPT]
    session_log = []  # to log full timestamped session

    print("🗨️  AI Chatbot (type '/reset' to clear context, '/exit' to quit)\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not user_input:
            continue
        if user_input.lower() in ("/exit", "exit"):
            print("Goodbye!")
            break
        if user_input.lower() == "/reset":
            memory = [SYSTEM_PROMPT]
            print("🔄 Context reset.\n")
            continue

        # Add user message
        user_msg = {"role": "user", "content": user_input}
        memory.append(user_msg)
        session_log.append({"role": "user", "content": user_input, "timestamp": datetime.datetime.utcnow().isoformat() + "Z"})

        # Trim memory
        memory = trim_memory(memory)

        # Call OpenAI with streaming
        print("AI: ", end="", flush=True)
        assistant_msg = {"role": "assistant", "content": ""}
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # update to preferred model
                messages=memory,
                stream=True,
            )
            for chunk in response:
                token = chunk.choices[0].delta.get("content", "")
                print(token, end="", flush=True)
                assistant_msg["content"] += token
            print("\n")
        except Exception as e:
            print(f"\nError calling OpenAI API: {e}", file=sys.stderr)
            continue

        # Append assistant message to memory & session log
        memory.append(assistant_msg)
        session_log.append({"role": "assistant", "content": assistant_msg["content"], "timestamp": datetime.datetime.utcnow().isoformat() + "Z"})

    # At end of session, save log
    if session_log:
        save_chat_log(session_log)

if __name__ == "__main__":
    chat()
