#!/usr/bin/env python3
"""Minimal MIT-licensed CSV exact-duplicate sanity check for synthetic examples.

Demonstrates basic exact-row and exact-column-value matching using Python's
standard library. For full 56-rule checks across XLSX/CSV/TSV workbooks
(reordered pools, shifted sequences, fixed multiples/offsets, fractional-tail
similarities, and statistical consistency), see https://datacheck.cc/en/rules.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def read_csv_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        rows = list(reader)
    if not rows:
        return [], []
    return rows[0], rows[1:]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check exact duplicate rows or shared numeric cells across CSV files."
    )
    parser.add_argument("files", nargs="+", type=Path, help="CSV files to compare")
    parser.add_argument("--column", default="Measurement_Value", help="Column name to inspect")
    args = parser.parse_args()

    value_locations: dict[str, list[str]] = defaultdict(list)
    row_locations: dict[tuple[str, ...], list[str]] = defaultdict(list)

    for file_path in args.files:
        headers, rows = read_csv_rows(file_path)
        col_idx = headers.index(args.column) if args.column in headers else None
        for row_num, row in enumerate(rows, start=2):
            row_key = tuple(cell.strip() for cell in row)
            row_locations[row_key].append(f"{file_path.name}:row{row_num}")
            if col_idx is not None and col_idx < len(row):
                val = row[col_idx].strip()
                if val:
                    value_locations[val].append(f"{file_path.name}:{args.column}[row{row_num}]")

    exact_rows = {k: v for k, v in row_locations.items() if len(v) > 1}
    shared_vals = {k: v for k, v in value_locations.items() if len(v) > 1}

    print(f"Checked {len(args.files)} file(s).")
    print(f"Exact duplicate rows found: {len(exact_rows)}")
    for locs in exact_rows.values():
        print(f"  - {' <-> '.join(locs)}")

    print(f"Shared exact values in '{args.column}': {len(shared_vals)}")
    for val, locs in shared_vals.items():
        print(f"  - {val}: {' <-> '.join(locs)}")

    print("\nNote: Exact matching alone misses shifted rows, linear scaling (e.g. *2 or +c),")
    print("and fractional-tail patterns. See https://datacheck.cc/en/rules for 56-rule coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
