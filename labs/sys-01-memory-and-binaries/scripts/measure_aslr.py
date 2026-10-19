#!/usr/bin/env python3
"""Measure observed address variation across repeated executions.

This script does not estimate ASLR entropy. It reports how many distinct
page-aligned bases were observed in a small sample, which is evidence about
the sample, not about the underlying distribution.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from pathlib import Path

LABELS = {
    "code": r"^add\(\)\s+(0x[0-9a-fA-F]+)$",
    "static": r"^static\s+(0x[0-9a-fA-F]+)$",
    "data": r"^global init\s+(0x[0-9a-fA-F]+)$",
    "bss": r"^global bss\s+(0x[0-9a-fA-F]+)$",
    "heap": r"^heap\s+(0x[0-9a-fA-F]+)$",
    "stack": r"^stack\s+(0x[0-9a-fA-F]+)$",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", type=Path, default=Path("./layout"))
    parser.add_argument("--runs", type=int, default=30)
    parser.add_argument("--csv", type=Path, default=Path("aslr-observations.csv"))
    parser.add_argument("--timeout", type=float, default=10.0)
    return parser.parse_args()


def parse_output(text: str) -> dict[str, int]:
    values: dict[str, int] = {}
    for line in text.splitlines():
        for key, pattern in LABELS.items():
            match = re.match(pattern, line.strip())
            if match:
                values[key] = int(match.group(1), 16)
    missing = sorted(set(LABELS) - set(values))
    if missing:
        raise ValueError(f"could not parse fields: {', '.join(missing)}")
    return values


def main() -> int:
    args = parse_args()
    if args.runs < 2:
        print("ERROR: --runs must be at least 2", file=sys.stderr)
        return 2
    binary = args.binary.resolve()
    if not binary.exists():
        print(f"ERROR: binary not found: {args.binary}", file=sys.stderr)
        return 2

    page_size = os.sysconf("SC_PAGE_SIZE")
    rows: list[dict[str, object]] = []
    for run in range(1, args.runs + 1):
        result = subprocess.run(
            [str(binary)],
            capture_output=True,
            text=True,
            timeout=args.timeout,
        )
        if result.returncode != 0:
            print(f"ERROR: run {run} exited {result.returncode}: {result.stderr.strip()}", file=sys.stderr)
            return 1
        values = parse_output(result.stdout)
        row: dict[str, object] = {"run": run, "page_size": page_size}
        for key, value in values.items():
            row[key] = f"0x{value:x}"
            row[f"{key}_page"] = value // page_size
        rows.append(row)

    with args.csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary: dict[str, object] = {"runs": args.runs, "page_size": page_size, "regions": {}}
    for key in LABELS:
        pages = {int(row[f"{key}_page"]) for row in rows}
        summary["regions"][key] = {
            "distinct_pages": len(pages),
            "min_page": min(pages),
            "max_page": max(pages),
        }

    print(json.dumps(summary, indent=2))
    print(f"wrote {args.csv}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
