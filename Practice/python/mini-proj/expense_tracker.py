import csv
from datetime import datetime

def add_expense(amount, category):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), amount, category])
    print(f"Added ₹{amount} to {category}")

def show_expenses():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses yet!")

# Example
add_expense(500, "Food")
add_expense(1200, "Gadgets")
show_expenses()
