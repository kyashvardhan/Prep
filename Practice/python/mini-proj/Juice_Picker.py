def display_menu():
    print("🧃 Welcome to Juice Picker!")
    print("Please choose a juice from the menu below:\n")
    juices = {
        1: ("Orange Juice", 50),
        2: ("Mango Juice", 60),
        3: ("Watermelon Juice", 45),
        4: ("Pineapple Juice", 55),
        5: ("Lime Soda", 40)
    }

    for key, (name, price) in juices.items():
        print(f"{key}. {name} - ₹{price}")

    return juices

def pick_juice(juices):
    try:
        choice = int(input("\nEnter the number of your choice: "))
        if choice in juices:
            name, price = juices[choice]
            print(f"\n✅ You selected: {name}")
            print(f"💰 Price: ₹{price}")
        else:
            print("\n❌ Invalid choice. Please select a valid number.")
    except ValueError:
        print("\n❌ Invalid input. Please enter a number.")

def main():
    juices = display_menu()
    pick_juice(juices)

if __name__ == "__main__":
    main()
