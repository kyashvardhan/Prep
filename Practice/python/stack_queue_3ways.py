#!/usr/bin/env python3
"""
stack_queue_3ways.py

Implements Stack and Queue in 3 different ways:
  - Using list
  - Using collections.deque
  - Using custom class
"""

from collections import deque

# ====================
# Stack Implementations
# ====================

def stack_with_list():
    print("\n📦 Stack using list")
    stack = []
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("Stack:", stack)
    print("Popped:", stack.pop())
    print("Stack after pop:", stack)

def stack_with_deque():
    print("\n📦 Stack using deque")
    stack = deque()
    stack.append(100)
    stack.append(200)
    stack.append(300)
    print("Stack:", list(stack))
    print("Popped:", stack.pop())
    print("Stack after pop:", list(stack))

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop() if not self.is_empty() else "Underflow"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else "Empty"

    def display(self):
        print("Stack:", self.items)

def stack_with_class():
    print("\n📦 Stack using class")
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    s.display()
    print("Popped:", s.pop())
    s.display()

# ====================
# Queue Implementations
# ====================

def queue_with_list():
    print("\n🚚 Queue using list (not recommended for performance)")
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("Queue:", queue)
    print("Dequeued:", queue.pop(0))
    print("Queue after dequeue:", queue)

def queue_with_deque():
    print("\n🚚 Queue using deque (recommended)")
    queue = deque()
    queue.append("X")
    queue.append("Y")
    queue.append("Z")
    print("Queue:", list(queue))
    print("Dequeued:", queue.popleft())
    print("Queue after dequeue:", list(queue))

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        return self.items.popleft() if not self.is_empty() else "Underflow"

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0] if not self.is_empty() else "Empty"

    def display(self):
        print("Queue:", list(self.items))

def queue_with_class():
    print("\n🚚 Queue using class")
    q = Queue()
    q.enqueue("Apple")
    q.enqueue("Banana")
    q.enqueue("Cherry")
    q.display()
    print("Dequeued:", q.dequeue())
    q.display()

# ====================
# Main
# ====================

def main():
    print("=== STACK IMPLEMENTATIONS ===")
    stack_with_list()
    stack_with_deque()
    stack_with_class()

    print("\n=== QUEUE IMPLEMENTATIONS ===")
    queue_with_list()
    queue_with_deque()
    queue_with_class()

if __name__ == "__main__":
    main()
