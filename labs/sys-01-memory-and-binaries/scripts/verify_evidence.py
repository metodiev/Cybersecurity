#!/usr/bin/env python3
"""Validate the structure of an ASLR observation CSV produced by the lab."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED = ["run", "page_size", "code", "heap", "stack"]
HEX_FIELDS = ["code", "static", "data", "bss", "heap", "stack"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path("evidence/aslr-observations.csv"))
    parser.add_argument("--min-runs", type=int, default=30)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.csv.exists():
        print(f"ERROR: missing {args.csv}", file=sys.stderr)
        return 2
    with args.csv.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in REQUIRED if field not in (reader.fieldnames or [])]
        if missing:
            print(f"ERROR: missing columns: {', '.join(missing)}", file=sys.stderr)
            return 1
        rows = list(reader)

    if len(rows) < args.min_runs:
        print(f"ERROR: {len(rows)} runs, expected at least {args.min_runs}", file=sys.stderr)
        return 1
    for index, row in enumerate(rows, 1):
        if int(row["page_size"]) <= 0:
            print(f"ERROR: run {index} has invalid page_size", file=sys.stderr)
            return 1
        for field in HEX_FIELDS:
            value = row.get(field)
            if value is None:
                continue
            try:
                int(value, 16)
            except ValueError:
                print(f"ERROR: run {index} field {field} is not hex: {value}", file=sys.stderr)
                return 1

    print(f"OK: {len(rows)} runs, page_size={rows[0]['page_size']}, columns valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
