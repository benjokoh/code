import sqlite3
from datetime import datetime

# myledger.py

# A simple ledger program to manage financial transactions

# Database setup
conn = sqlite3.connect('ledger.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')
conn.commit()

# Function to add a transaction with date
def add_transaction(description, amount):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO ledger (description, amount, date) VALUES (?, ?, ?)', (description, amount, date))
    conn.commit()
    print("Transaction added!")

# Function to remove a transaction
def remove_transaction(description, amount):
    cursor.execute('DELETE FROM ledger WHERE description = ? AND amount = ? LIMIT 1', (description, amount))
    if cursor.rowcount > 0:
        conn.commit()
        print("Transaction removed!")
    else:
        print("Transaction not found.")

# Function to view all transactions
def view_ledger():
    print("Ledger:")
    cursor.execute('SELECT date, description, amount FROM ledger')
    for date, description, amount in cursor.fetchall():
        print(f"{date} | {description}: ${amount}")

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