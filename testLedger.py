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