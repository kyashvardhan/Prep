#!/usr/bin/env python3
"""
dsa_operations.py
"""

from collections import deque

# -------------------------------
# Arrays (Python Lists)
# -------------------------------
def array_operations():
    arr = [10, 20, 30, 40]
    arr.append(50)
    arr.remove(20)
    print("🔹 Array:", arr)

# -------------------------------
# Stack (LIFO)
# -------------------------------
def stack_operations():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("🔹 Stack:", stack)
    print("Popped:", stack.pop())

# -------------------------------
# Queue (FIFO)
# -------------------------------
def queue_operations():
    queue = deque()
    queue.append('A')
    queue.append('B')
    print("🔹 Queue:", queue)
    print("Dequeued:", queue.popleft())

# -------------------------------
# Singly Linked List
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def display(self):
        curr = self.head
        print("🔹 Linked List:", end=" ")
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# -------------------------------
# Binary Search Tree (BST)
# -------------------------------
class BSTNode:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def insert_bst(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.val:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

def inorder_bst(root):
    if root:
        inorder_bst(root.left)
        print(root.val, end=' ')
        inorder_bst(root.right)

# -------------------------------
# Searching Algorithms
# -------------------------------
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# -------------------------------
# Sorting Algorithms
# -------------------------------
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# -------------------------------
# Main Driver
# -------------------------------
def main():
    print("\n✅ ARRAY")
    array_operations()

    print("\n✅ STACK")
    stack_operations()

    print("\n✅ QUEUE")
    queue_operations()

    print("\n✅ LINKED LIST")
    ll = LinkedList()
    for v in [10, 20, 30]:
        ll.insert(v)
    ll.display()

    print("\n✅ BST (Inorder Traversal)")
    bst = None
    for key in [40, 20, 60, 10, 30, 50, 70]:
        bst = insert_bst(bst, key)
    inorder_bst(bst)

    print("\n\n✅ SEARCHING")
    nums = [5, 8, 12, 20, 23]
    print("Linear search 20:", linear_search(nums, 20))
    print("Binary search 12:", binary_search(nums, 12))

    print("\n✅ SORTING")
    unsorted = [64, 25, 12, 22, 11]
    print("Bubble Sort:", bubble_sort(unsorted))
    print("Selection Sort:", selection_sort(unsorted))
    print("Insertion Sort:", insertion_sort(unsorted))

if __name__ == "__main__":
    main()
