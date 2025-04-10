#!/usr/bin/env python3
"""
dungeon_generator.py
--by yvk

A Procedural Rogue-like Dungeon Generator using Cellular Automata

This script generates a dungeon layout based on cellular automata rules. 
Users can specify grid dimensions, wall probability, smoothing iterations, and an optional seed.
The generated dungeon is output to the console in an ASCII format and can optionally be saved as an image.

Usage:
    Run CLI:
        python dungeon_generator.py [--width WIDTH] [--height HEIGHT]
                                      [--wall_prob WALL_PROBABILITY]
                                      [--iterations ITERATIONS]
                                      [--seed SEED]
                                      [--save OUTPUT_IMAGE_FILENAME]
"""

import numpy as np
import argparse
import sys
import matplotlib.pyplot as plt

def initialize_grid(width: int, height: int, wall_prob: float, seed: int = None):
    """Initialize the dungeon grid with random walls based on wall probability."""
    if seed is not None:
        np.random.seed(seed)
    grid = np.random.rand(height, width) < wall_prob
    return grid.astype(int)

def count_wall_neighbors(grid: np.ndarray, x: int, y: int) -> int:
    """Count the number of wall neighbors for a given cell (including diagonals)."""
    height, width = grid.shape
    count = 0
    for j in range(max(0, y - 1), min(height, y + 2)):
        for i in range(max(0, x - 1), min(width, x + 2)):
            if i == x and j == y:
                continue
            count += grid[j, i]
    return count

def smooth_grid(grid: np.ndarray, threshold: int = 5) -> np.ndarray:
    """Apply one iteration of cellular automata smoothing rules."""
    height, width = grid.shape
    new_grid = grid.copy()
    for y in range(height):
        for x in range(width):
            walls = count_wall_neighbors(grid, x, y)
            if walls >= threshold:
                new_grid[y, x] = 1  # Wall
            else:
                new_grid[y, x] = 0  # Floor
    return new_grid

def generate_dungeon(width: int, height: int, wall_prob: float, iterations: int, seed: int = None):
    """Generate the dungeon grid after applying several smoothing iterations."""
    grid = initialize_grid(width, height, wall_prob, seed)
    for _ in range(iterations):
        grid = smooth_grid(grid)
    return grid

def print_ascii_dungeon(grid: np.ndarray):
    """Print the dungeon as an ASCII map: '#' for walls and '.' for floors."""
    height, width = grid.shape
    ascii_map = ""
    for y in range(height):
        row = ""
        for x in range(width):
            row += "#" if grid[y, x] == 1 else "."
        ascii_map += row + "\n"
    print(ascii_map)

def save_dungeon_image(grid: np.ndarray, filename: str):
    """Save a visual representation of the dungeon as an image."""
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='binary')
    plt.title("Procedurally Generated Dungeon")
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"Dungeon image saved as {filename}")

def parse_args():
    parser = argparse.ArgumentParser(description="Procedural Rogue-like Dungeon Generator")
    parser.add_argument("--width", type=int, default=50, help="Width of the dungeon grid (default: 50)")
    parser.add_argument("--height", type=int, default=30, help="Height of the dungeon grid (default: 30)")
    parser.add_argument("--wall_prob", type=float, default=0.45, help="Initial wall probability (default: 0.45)")
    parser.add_argument("--iterations", type=int, default=4, help="Number of smoothing iterations (default: 4)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility (default: None)")
    parser.add_argument("--save", type=str, default=None, help="Filename to save the dungeon image (optional)")
    return parser.parse_args()

def main():
    args = parse_args()
    grid = generate_dungeon(args.width, args.height, args.wall_prob, args.iterations, args.seed)
    
    print("=== Generated Dungeon Map ===")
    print_ascii_dungeon(grid)
    
    if args.save:
        save_dungeon_image(grid, args.save)

if __name__ == "__main__":
    main()
