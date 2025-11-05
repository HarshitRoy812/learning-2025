"""Utility helpers for summarising tabular datasets.

This module contains lightweight helpers that demonstrate how Python
code in the Learning 2025 curriculum can be structured.  The functions
favour readability over micro-optimisations and are suitable for
beginners experimenting with unit tests and command line interfaces.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Dict, Iterable, List

import csv


@dataclass
class NumericSummary:
    """Describes simple descriptive statistics for a numeric feature."""

    count: int
    mean: float
    median: float
    stdev: float

    def as_dict(self) -> Dict[str, float]:
        """Represent the statistics as a serialisable dictionary."""

        return {
            "count": self.count,
            "mean": self.mean,
            "median": self.median,
            "stdev": self.stdev,
        }


def load_csv(path: str | Path) -> List[Dict[str, str]]:
    """Load a CSV file into a list of dictionaries.

    Parameters
    ----------
    path:
        File system path to a comma separated file.

    Returns
    -------
    list of dict
        Each row of the CSV file as a dictionary keyed by column name.
    """

    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def compute_numeric_summary(rows: Iterable[Dict[str, str]], column: str) -> NumericSummary:
    """Compute descriptive statistics for a numeric column.

    Missing values and blank strings are ignored automatically.  The
    function raises a :class:`ValueError` when the column cannot be
    located or none of the rows contain numeric values.
    """

    cleaned_values = []
    for index, row in enumerate(rows):
        if column not in row:
            available = ", ".join(sorted(row.keys()))
            raise ValueError(
                f"Column '{column}' not present in row {index}. "
                f"Available columns: {available or 'none'}"
            )

        value = row[column]
        if value in (None, ""):
            continue

        try:
            cleaned_values.append(float(value))
        except (TypeError, ValueError) as exc:  # defensive: values might not cast cleanly
            raise ValueError(f"Non-numeric value '{value}' in column '{column}'.") from exc

    if not cleaned_values:
        raise ValueError(f"Column '{column}' does not contain any numeric values.")

    return NumericSummary(
        count=len(cleaned_values),
        mean=mean(cleaned_values),
        median=median(cleaned_values),
        stdev=pstdev(cleaned_values) if len(cleaned_values) > 1 else 0.0,
    )


def summarise_dataset(rows: Iterable[Dict[str, str]]) -> Dict[str, NumericSummary]:
    """Produce summaries for every numeric-looking column in ``rows``.

    Non-numeric columns are skipped and the output is indexed by column
    name.  This mirrors the type of exploratory analysis performed in the
    *Applied Data Analysis* module.
    """

    numeric_columns: Dict[str, List[float]] = defaultdict(list)

    for row in rows:
        for key, value in row.items():
            if value in (None, ""):
                continue
            try:
                numeric_columns[key].append(float(value))
            except (TypeError, ValueError):
                # Ignore columns that cannot be converted to numbers.
                continue

    summaries: Dict[str, NumericSummary] = {}
    for column, values in numeric_columns.items():
        if not values:
            continue
        summaries[column] = NumericSummary(
            count=len(values),
            mean=mean(values),
            median=median(values),
            stdev=pstdev(values) if len(values) > 1 else 0.0,
        )

    return summaries
