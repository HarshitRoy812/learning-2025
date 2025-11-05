"""Unit tests for the dataset summary helpers."""

from __future__ import annotations

import math
import unittest

from python.dataset_summary import compute_numeric_summary, summarise_dataset
from python.demo_data import small_employee_dataset


class TestDatasetSummary(unittest.TestCase):
    def test_compute_numeric_summary_basic(self) -> None:
        rows = small_employee_dataset()
        summary = compute_numeric_summary(rows, "salary")

        self.assertEqual(summary.count, 5)
        self.assertTrue(math.isclose(summary.mean, 72600, rel_tol=1e-6))
        self.assertEqual(summary.median, 72000)
        self.assertGreater(summary.stdev, 0)

    def test_compute_numeric_summary_missing_column(self) -> None:
        rows = small_employee_dataset()
        with self.assertRaises(ValueError):
            compute_numeric_summary(rows, "missing")

    def test_compute_numeric_summary_non_numeric(self) -> None:
        rows = small_employee_dataset()
        rows_with_text = [dict(row, salary="not a number") for row in rows]
        with self.assertRaises(ValueError):
            compute_numeric_summary(rows_with_text, "salary")

    def test_summarise_dataset_filters_numeric_columns(self) -> None:
        rows = small_employee_dataset()
        summaries = summarise_dataset(rows)

        self.assertEqual(set(summaries.keys()), {"salary", "tenure_years"})
        self.assertEqual(summaries["tenure_years"].median, 3)


if __name__ == "__main__":
    unittest.main()
