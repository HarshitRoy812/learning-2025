"""Command line entry point for working with the practice dataset."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Dict

from .dataset_summary import compute_numeric_summary, load_csv, summarise_dataset
from .demo_data import small_employee_dataset


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarise numeric columns in a dataset")
    parser.add_argument(
        "--csv",
        type=Path,
        help="Optional path to a CSV file. If omitted a demo dataset is used.",
    )
    parser.add_argument(
        "--column",
        help="When provided, only this column is summarised."
             " Otherwise every numeric column is returned.",
    )
    return parser.parse_args()


def _load_rows(args: argparse.Namespace) -> Iterable[Dict[str, str]]:
    if args.csv:
        return load_csv(args.csv)
    return small_employee_dataset()


def main() -> None:
    args = _parse_args()
    rows = list(_load_rows(args))

    if args.column:
        summary = compute_numeric_summary(rows, args.column)
        serialisable = {args.column: summary.as_dict()}
    else:
        summary = summarise_dataset(rows)
        serialisable = {key: value.as_dict() for key, value in summary.items()}

    print(json.dumps(serialisable, indent=2, sort_keys=True))


if __name__ == "__main__":  # pragma: no cover - manual entry point
    main()
