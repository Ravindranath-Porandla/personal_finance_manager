# src/finance_manager/storage.py

import json
from pathlib import Path
from typing import List

from pydantic import ValidationError

from models import Transaction

class TransactionManager:
    """Manages the storage and retrieval of transactions."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self._transactions: List[Transaction] = self._load()

    def _load(self) -> List[Transaction]:
        """Loads transactions from the JSON file."""
        if not self.filepath.exists():
            return []  # Return empty list if file doesn't exist yet
        
        try:
            with open(self.filepath, 'r') as f:
                # Handle case where file is empty
                content = f.read()
                if not content:
                    return []
                data = json.loads(content)
            
            # Convert list of dicts back into list of Transaction objects
            return [Transaction.model_validate(item) for item in data]
        
        except (IOError, ValidationError, json.JSONDecodeError) as e:
            print(f"Error loading transactions: {e}. Starting with an empty list.")
            return []

    def _save(self):
        """Saves the current list of transactions to the JSON file."""
        try:
            # Ensure parent directory exists
            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert list of Transaction objects to list of dicts
            data_to_save = [t.model_dump() for t in self._transactions]
            
            with open(self.filepath, 'w') as f:
                json.dump(data_to_save, f, indent=4, default=str)
        except IOError as e:
            print(f"Error saving transactions: {e}")

    def add(self, transaction: Transaction):
        """Adds a new transaction and saves the list."""
        self._transactions.append(transaction)
        self._save()

    def get_all(self) -> List[Transaction]:
        """Returns all transactions."""
        return self._transactions