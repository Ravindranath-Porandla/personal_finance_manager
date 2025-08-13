# src/finance_manager/reporting.py

from typing import List, Dict
from models import Transaction

def get_summary_by_category(transactions: List[Transaction]) -> Dict[str, float]:
    """
    Calculates the total spending for each category.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        A dictionary where keys are category names and values are the
        total amount spent in that category.
    """
    category_totals: Dict[str, float] = {}

    for t in transactions:
        # Get the current total for this category, defaulting to 0 if not yet seen
        current_total = category_totals.get(t.category, 0.0)
        
        # Add the transaction's amount to the total
        category_totals[t.category] = current_total + t.amount

    return category_totals