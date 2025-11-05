"""In-memory datasets used for demonstration and testing."""

from __future__ import annotations

from typing import List, Dict


def small_employee_dataset() -> List[Dict[str, str]]:
    """Return a compact dataset to exercise the analysis helpers."""

    return [
        {"employee": "Alicia", "department": "Engineering", "salary": "72000", "tenure_years": "3"},
        {"employee": "Bala", "department": "Engineering", "salary": "68000", "tenure_years": "2"},
        {"employee": "Chen", "department": "Data", "salary": "75000", "tenure_years": "4"},
        {"employee": "Dana", "department": "Data", "salary": "77000", "tenure_years": "5"},
        {"employee": "Esha", "department": "Analytics", "salary": "71000", "tenure_years": "3"},
    ]
