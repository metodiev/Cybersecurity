#!/usr/bin/env python3
"""Check that the expected SYS-02 evidence files exist and contain key fields."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED = [
    "environment.txt",
    "trace-success.txt",
    "trace-denied.txt",
    "status-fields.txt",
    "namespaces.txt",
    "cgroup.txt",
    "namespace-experiment.txt",
]
TRACE_MARKERS = ["openat", "open(", "read(", "write("]
STATUS_MARKERS = ["Uid:", "CapEff:", "Seccomp:"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", type=Path, default=Path("evidence"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    for name in REQUIRED:
        path = args.dir / name
        if not path.exists() or path.stat().st_size == 0:
            errors.append(f"missing or empty: {path}")

    trace = args.dir / "trace-success.txt"
    if trace.exists():
        text = trace.read_text(encoding="utf-8", errors="replace")
        if not any(marker in text for marker in TRACE_MARKERS):
            errors.append(f"{trace} does not contain a recognizable syscall line")

    status = args.dir / "status-fields.txt"
    if status.exists():
        text = status.read_text(encoding="utf-8", errors="replace")
        missing = [marker for marker in STATUS_MARKERS if marker not in text]
        if missing:
            errors.append(f"{status} is missing: {', '.join(missing)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"OK: required evidence present in {args.dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
