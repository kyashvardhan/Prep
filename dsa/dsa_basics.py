#!/usr/bin/env python3
"""
dsa_basics.py

- Array operations
- Stack (using list)
- Queue (using deque)
- Linear search
- Bubble sort
"""

from collections import deque

# --- Array Basics ---
def array_operations():
    print("\n📚 Array Operations")
    arr = [10, 20, 30, 40]
    print("Original array:", arr)

    arr.append(50)
    print("After append(50):", arr)

    arr.remove(20)
    print("After remove(20):", arr)

    print("Element at index 2:", arr[2])

# --- Stack Basics ---
def stack_operations():
    print("\n📚 Stack Operations (LIFO)")
    stack = []
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print("Stack after pushes:", stack)

    top = stack.pop()
    print(f"Popped item: {top}")
    print("Stack now:", stack)

# --- Queue Basics ---
def queue_operations():
    print("\n📚 Queue Operations (FIFO)")
    queue = deque()
    queue.append('X')
    queue.append('Y')
    queue.append('Z')
    print("Queue after enqueues:", queue)

    front = queue.popleft()
    print(f"Dequeued item: {front}")
    print("Queue now:", queue)

# --- Linear Search ---
def linear_search(arr, target):
    print(f"\n🔍 Linear Search for {target} in {arr}")
    for index, value in enumerate(arr):
        if value == target:
            print(f"Found {target} at index {index}")
            return index
    print(f"{target} not found")
    return -1

# --- Bubble Sort ---
def bubble_sort(arr):
    print(f"\n🔄 Bubble Sort: Original array: {arr}")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array:", arr)
    return arr

# --- Main Function ---
def main():
    array_operations()
    stack_operations()
    queue_operations()

    nums = [5, 2, 9, 1, 5, 6]
    linear_search(nums, 5)
    linear_search(nums, 7)

    bubble_sort(nums)

if __name__ == "__main__":
    main()
