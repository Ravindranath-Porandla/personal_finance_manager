# src/finance_manager/main.py

from datetime import date
from pathlib import Path
from models import Transaction
from storage import TransactionManager

# Define the path to our data file
DATA_DIR = Path.home() / ".finance_manager"
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"

def run():
    """
    The main function that runs the Personal Finance Manager application.
    """
    print("Welcome to your Personal Finance Manager!")

    # Create a TransactionManager instance
    manager = TransactionManager(filepath=TRANSACTIONS_FILE)

    # --- Let's add a new transaction ---
    # In a real app, you would get this data from user input
    new_transaction = Transaction(
        id=len(manager.get_all()) + 1,
        transaction_date=date.today(),
        description="Weekly Groceries",
        amount=150.75,
        category="Groceries"
    )
    manager.add(new_transaction)
    print(f"\nAdded new transaction: {new_transaction.description}")

    # --- List all transactions ---
    all_transactions = manager.get_all()
    print("\n--- All Transactions ---")
    if not all_transactions:
        print("No transactions found.")
    else:
        for t in all_transactions:
            print(f"  - ID: {t.id}, Date: {t.transaction_date}, Desc: {t.description}, Amount: ${t.amount:.2f}, Category: {t.category}")
    print("------------------------")


if __name__ == "__main__":
    run()