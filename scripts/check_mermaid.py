#!/usr/bin/env python3
"""Structural and optional render validation for Mermaid fenced blocks.

Without --render, this only checks that each ```mermaid block is non-empty and
starts with a recognizable Mermaid diagram keyword. With --render, it invokes
the Mermaid CLI (mmdc) for each block. Rendering requires a working Chrome or
Chromium installation and is therefore optional.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "site", "node_modules", "__pycache__"}
DIAGRAM_STARTS = {
    "architecture-beta",
    "block-beta",
    "C4Context",
    "classDiagram",
    "erDiagram",
    "flowchart",
    "gantt",
    "gitGraph",
    "graph",
    "journey",
    "mindmap",
    "packet-beta",
    "pie",
    "quadrantChart",
    "requirementDiagram",
    "sankey-beta",
    "sequenceDiagram",
    "stateDiagram",
    "stateDiagram-v2",
    "timeline",
    "xychart-beta",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--mmdc", type=Path, default=None, help="path to the Mermaid CLI")
    parser.add_argument("--puppeteer-config", type=Path, default=None)
    parser.add_argument("--render", action="store_true", help="render every block with mmdc")
    parser.add_argument("--require-render", action="store_true", help="fail if mmdc is unavailable")
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def detect_chrome() -> str | None:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.parts) and not path.is_symlink()
    )


def extract_blocks(path: Path) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    in_block = False
    start_line = 0
    buffer: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not in_block and stripped == "```mermaid":
            in_block = True
            start_line = line_number
            buffer = []
            continue
        if in_block and stripped == "```":
            blocks.append((start_line, "\n".join(buffer).strip()))
            in_block = False
            continue
        if in_block:
            buffer.append(line)
    if in_block:
        blocks.append((start_line, "\n".join(buffer).strip()))
    return blocks


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    mmdc = args.mmdc or (Path(shutil.which("mmdc")) if shutil.which("mmdc") else None)
    if args.render and not mmdc:
        if args.require_render:
            print("ERROR: --render requested, but mmdc was not found on PATH", file=sys.stderr)
            return 1
        print("NOTE: mmdc was not found on PATH; rendering skipped", file=sys.stderr)
        print("SKIP: structural checks still ran")
        args.render = False

    errors: list[str] = []
    files = markdown_files(root)
    total = 0
    rendered = 0

    with tempfile.TemporaryDirectory(prefix="mermaid-check-") as temp_dir:
        temp = Path(temp_dir)
        puppeteer_config = args.puppeteer_config
        if args.render and not puppeteer_config:
            chrome = os.environ.get("PUPPETEER_EXECUTABLE_PATH") or detect_chrome()
            if chrome:
                puppeteer_config = temp / "puppeteer-config.json"
                puppeteer_config.write_text(
                    json.dumps(
                        {
                            "executablePath": chrome,
                            "args": ["--no-sandbox", "--disable-setuid-sandbox"],
                        }
                    ),
                    encoding="utf-8",
                )
        for path in files:
            for line_number, block in extract_blocks(path):
                total += 1
                location = f"{path.relative_to(root)}:{line_number}"
                if not block:
                    errors.append(f"{location}: empty mermaid block")
                    continue
                first = block.splitlines()[0].strip()
                keyword = first.split()[0].rstrip("{")
                if keyword not in DIAGRAM_STARTS:
                    errors.append(f"{location}: unrecognized Mermaid start {first!r}")
                    continue
                if not args.render:
                    continue
                source = temp / f"block-{total:03d}.mmd"
                output = temp / f"block-{total:03d}.svg"
                source.write_text(block + "\n", encoding="utf-8")
                command = [str(mmdc), "-i", str(source), "-o", str(output)]
                if puppeteer_config:
                    command.extend(["-p", str(puppeteer_config)])
                result = subprocess.run(command, capture_output=True, text=True, timeout=120)
                if result.returncode != 0:
                    detail = (result.stderr or result.stdout).strip().splitlines()[-5:]
                    errors.append(f"{location}: mmdc failed: {' | '.join(detail)}")
                else:
                    rendered += 1

    if not args.quiet:
        print("Mermaid check")
        print(f"  Markdown files: {len(files)}")
        print(f"  mermaid blocks: {total}")
        print(f"  rendered:       {rendered}" if args.render else "  rendering:      skipped (use --render)")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"FAILED: {len(errors)} Mermaid error(s)", file=sys.stderr)
        return 1
    print("OK: Mermaid blocks passed structural checks" + (" and rendered" if args.render else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
