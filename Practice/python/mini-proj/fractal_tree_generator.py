#!/usr/bin/env python3
"""
fractal_tree_generator.py

Interactive Fractal Tree Generator using Tkinter

This program creates a fractal tree using recursive branch drawing on a Tkinter canvas.
Each new branch is drawn with a randomized angle variance to produce unique trees each time.
Press the "Generate New Tree" button to see a new fractal.

Usage:
    python fractal_tree_generator.py
"""

import tkinter as tk
import random
import math

# Fractal tree parameters.
INITIAL_LENGTH = 120       # Starting branch length
ANGLE_VARIANCE = 20        # Degrees to vary the branch splitting
LENGTH_SCALE = 0.7         # Scale factor for branch reduction
MIN_LENGTH = 5             # Minimum branch length to stop recursion

def draw_tree(canvas, x, y, angle, length):
    """
    Recursively draws branches of the fractal tree.
    """
    if length < MIN_LENGTH:
        return
    # Calculate the end coordinates for the current branch.
    rad = math.radians(angle)
    x_end = x + length * math.cos(rad)
    y_end = y - length * math.sin(rad)
    
    # Draw the branch (line width scaled by branch length).
    canvas.create_line(x, y, x_end, y_end, width=length / 10, fill="brown")
    
    # Apply a randomized angular variation.
    angle_variation = random.uniform(ANGLE_VARIANCE - 5, ANGLE_VARIANCE + 5)
    new_length = length * LENGTH_SCALE
    # Draw left and right branches.
    draw_tree(canvas, x_end, y_end, angle - angle_variation, new_length)
    draw_tree(canvas, x_end, y_end, angle + angle_variation, new_length)

def generate_tree():
    """
    Clears the canvas and generates a new fractal tree.
    """
    canvas.delete("all")
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    # Start at the bottom-center of the canvas.
    x_start = width / 2
    y_start = height - 10
    draw_tree(canvas, x_start, y_start, 90, INITIAL_LENGTH)

# Set up the Tkinter UI.
root = tk.Tk()
root.title("Fractal Tree Generator")

canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

generate_button = tk.Button(root, text="Generate New Tree", command=generate_tree)
generate_button.pack()

# Draw an initial tree after a short delay to ensure canvas dimensions are set.
root.after(100, generate_tree)

root.mainloop()
