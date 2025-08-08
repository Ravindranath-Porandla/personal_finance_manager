# src/finance_manager/main.py

from datetime import date  # noqa: I001
from models import Transaction
from pydantic import ValidationError


def run():
    """
    The main function that runs the Personal Finance Manager application.
    """
    print("Welcome to your Personal Finance Manager!")

    # --- Let's test our Transaction model ---

    # 1. A valid transaction
    try:
        t1 = Transaction(
            id=1,
            transaction_date=date.today(),
            description="Morning Coffee",
            amount=4.50,
            category="Food & Drink"
        )
        print("\nSuccessfully created a valid transaction:")
        print(t1)
        print(f"Transaction amount is: ${t1.amount:.2f}")

    except ValidationError as e:
        print(e)


    # 2. An invalid transaction (amount is 0)
    print("\n---")
    print("Attempting to create an invalid transaction (amount = 0)...")
    try:
        t2 = Transaction(
            id=2,
            transaction_date=date.today(),
            description="Free Newspaper",
            amount=0,
            category="Entertainment"
        )
    except ValidationError as e:
        print("Caught expected error:")
        print(e)

if __name__ == "__main__":
    run()