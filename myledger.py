from datetime import datetime

# myledger.py

# A simple ledger program to manage financial transactions

# Define a list to store transactions
ledger = []

# Function to add a transaction with date
def add_transaction(description, amount):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {"description": description, "amount": amount, "date": date}
    ledger.append(transaction)
    print("Transaction added!")

# Function to remove a transaction
def remove_transaction(description, amount):
    for transaction in ledger:
        if transaction["description"] == description and transaction["amount"] == amount:
            ledger.remove(transaction)
            print("Transaction removed!")
            return
    print("Transaction not found.")

# Function to view all transactions
def view_ledger():
    print("Ledger:")
    for transaction in ledger:
        print(f"{transaction['date']} | {transaction['description']}: ${transaction['amount']}")

# Main menu
def main():
    while True:
        print("\nLedger Menu:")
        print("_____________________")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. View Ledger")
        print("4. Exit")
        print("_____________________")
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
if __name__ == "__main__":
    main()