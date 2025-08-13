# src/finance_manager/main.py

from datetime import datetime
from pathlib import Path

from pydantic import ValidationError

from models import Transaction
from storage import TransactionManager

# Define the path to our data file
DATA_DIR = Path.home() / ".finance_manager"
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"


def get_transaction_details() -> dict:
    """Gets transaction details from the user with validation."""
    details = {}
    
    # Get Date
    while True:
        date_str = input("Enter transaction date (YYYY-MM-DD): ")
        try:
            details['transaction_date'] = datetime.strptime(date_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Get Description
    while True:
        details['description'] = input("Enter description: ").strip()
        if details['description']:
            break
        print("Description cannot be empty.")

    # Get Amount
    while True:
        try:
            details['amount'] = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # Get Category
    while True:
        details['category'] = input("Enter category: ").strip()
        if details['category']:
            break
        print("Category cannot be empty.")
        
    return details


def add_new_transaction(manager: TransactionManager):
    """Handles the logic for adding a new transaction."""
    print("\n--- Add New Transaction ---")
    
    try:
        details = get_transaction_details()
        # Generate a new ID
        details['id'] = len(manager.get_all()) + 1
        
        transaction = Transaction.model_validate(details)
        manager.add(transaction)
        print("\nTransaction added successfully!")
        
    except ValidationError as e:
        print("\nError: Could not create transaction.")
        print(e)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def list_all_transactions(manager: TransactionManager):
    """Displays all stored transactions."""
    print("\n--- All Transactions ---")
    transactions = manager.get_all()
    
    if not transactions:
        print("No transactions found.")
        return

    for t in transactions:
        print(f"  ID: {t.id} | Date: {t.transaction_date} | Amount: ${t.amount:<8.2f} | Category: {t.category:<15} | Desc: {t.description}")
    print("------------------------\n")


def run():
    """The main application loop."""
    manager = TransactionManager(filepath=TRANSACTIONS_FILE)

    while True:
        print("\nWelcome to your Personal Finance Manager!")
        print("1. Add a new transaction")
        print("2. List all transactions")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_new_transaction(manager)
        elif choice == '2':
            list_all_transactions(manager)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run()