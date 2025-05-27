"""A test script to simulate removing a transaction from the ledger"""	
import myledger
# testLedger.py
# Add a test block to simulate removing a transaction
if __name__ == "__main__":
    # Add a transaction
    myledger.add_transaction("Test", 10.0)
    print("Ledger after adding:")
    myledger.view_ledger()
    # Remove the transaction
    myledger.remove_transaction("Test", 10.0)
    print("Ledger after removing:")
    myledger.view_ledger()
    # Comment out main menu for test
    # myledger.main()

# Test block to check add and remove transaction functionality
if __name__ == "__main__":
    myledger.add_transaction("Groceries", 50.0)
    myledger.add_transaction("Books", 20.0)
    print("Ledger after adding transactions:")
    myledger.view_ledger()
    myledger.remove_transaction("Groceries", 50.0)
    print("Ledger after removing 'Groceries':")
    myledger.view_ledger()
    myledger.remove_transaction("Nonexistent", 99.0)
    print("Ledger after attempting to remove a nonexistent transaction:")
    myledger.view_ledger()