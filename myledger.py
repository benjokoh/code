# myledger.py

# A simple ledger program to manage financial transactions

# Define a list to store transactions
ledger = []

# Function to add a transaction
def add_transaction(description, amount):
    transaction = {"description": description, "amount": amount}
    ledger.append(transaction)
    print("Transaction added!")

# Function to remove a transaction
def remove_transaction(description, amount):
    transaction = {"description": description, "amount": amount}
    ledger.remove(transaction)
    print("Transaction removed!")

# Function to view all transactions
def view_ledger():
    print("Ledger:")
    for transaction in ledger:
        print(f"{transaction['description']}: ${transaction['amount']}")

# Main menu
def main():
    while True:
        print("\nLedger Menu:")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. View Ledger")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_transaction(description, amount)
        elif choice == "2":
            description = input("Enter description of transaction to remove: ")
            amount = float(input("Enter amount of transaction to remove: "))
            remove_transaction(description, amount)
        elif choice == "3":
            view_ledger()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Add a test block to simulate removing a transaction
if __name__ == "__main__":
    # Add a transaction
    add_transaction("Test", 10.0)
    print("Ledger after adding:")
    view_ledger()
    # Remove the transaction
    sub_transaction("Test", 10.0)
    print("Ledger after removing:")
    view_ledger()
    # Comment out main menu for test
    # main()