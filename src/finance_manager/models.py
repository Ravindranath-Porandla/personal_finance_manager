# src/finance_manager/models.py

from datetime import date

from pydantic import BaseModel, Field, field_validator


class Transaction(BaseModel):
    """
    Represents a single financial transaction.
    """

    id: int
    transaction_date: date
    description: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)  # gt=0 means "greater than 0"
    category: str = Field(..., min_length=1, max_length=50)

    @field_validator("description", "category")
    @classmethod
    def must_not_be_empty(cls, v: str) -> str:
        """Ensures the description and category fields are not just whitespace."""
        if not v.strip():
            raise ValueError("must not be empty")
        return v
