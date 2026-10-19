#!/usr/bin/env python3
"""Check local Markdown links, anchors, and MkDocs navigation targets.

By default only local links are checked. Use --external to probe HTTP(S)
links as well; many standards sites block automated clients, so external
checking is intentionally opt-in.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "site", "node_modules", "__pycache__"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class MkDocsLoader(yaml.SafeLoader):
    """Safe loader that tolerates MkDocs' !!python/name: tags."""


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda loader, suffix, node: suffix,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--config", type=Path, default=ROOT / "mkdocs.yml")
    parser.add_argument("--external", action="store_true", help="probe external URLs")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def slugify(text: str) -> str:
    """Approximate MkDocs/Python-Markdown heading anchors."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("`", "")
    text = text.strip().lower()
    text = "".join(char if char.isalnum() or char in " -_" else "" for char in text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def headings(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if not match:
            continue
        base = slugify(match.group(2))
        if not base:
            continue
        count = counts.get(base, 0)
        anchors.add(base if count == 0 else f"{base}_{count}")
        counts[base] = count + 1
    return anchors


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_symlink():
            continue
        files.append(path)
    return sorted(files)


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Drop an optional Markdown title: (url "title")
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return target


def resolve_link(source: Path, target: str) -> tuple[bool, str]:
    if target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
        return True, "external"
    if target.startswith("/"):
        return True, "site-absolute"
    path_part, _, anchor = target.partition("#")
    path_part = urllib.parse.unquote(path_part)
    if path_part:
        destination = (source.parent / path_part).resolve()
        if destination.is_dir():
            for index_name in ("index.md", "README.md"):
                candidate = destination / index_name
                if candidate.exists():
                    destination = candidate
                    break
        if not destination.exists():
            return False, f"missing file: {path_part}"
        if anchor and destination.suffix.lower() == ".md":
            if anchor not in headings(destination):
                return False, f"missing anchor: #{anchor}"
        return True, "local"
    if anchor and anchor not in headings(source):
        return False, f"missing anchor: #{anchor}"
    return True, "local"


def check_external(url: str, timeout: float) -> tuple[bool, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Cybersecurity-Academy-LinkCheck/1.0"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return 200 <= response.status < 400, f"HTTP {response.status}"
    except urllib.error.HTTPError as error:
        if error.code in (403, 404, 405):
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "Cybersecurity-Academy-LinkCheck/1.0"},
            )
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return 200 <= response.status < 400, f"HTTP {response.status}"
            except Exception as nested:  # noqa: BLE001 - report status text
                return False, str(nested)
        return False, f"HTTP {error.code}"
    except Exception as error:  # noqa: BLE001 - report status text
        return False, str(error)


def nav_targets(config: Path) -> list[str]:
    data = yaml.load(config.read_text(encoding="utf-8"), Loader=MkDocsLoader) or {}
    docs_dir = (config.parent / data.get("docs_dir", "docs")).resolve()
    found: list[str] = []

    def walk(item) -> None:
        if isinstance(item, str):
            found.append(item)
        elif isinstance(item, list):
            for child in item:
                walk(child)
        elif isinstance(item, dict):
            for child in item.values():
                walk(child)

    walk(data.get("nav", []))
    missing = []
    for target in found:
        if target.startswith(("http://", "https://")):
            continue
        if not (docs_dir / target).exists():
            missing.append(target)
    return missing


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    files = markdown_files(root)
    checked = 0
    skipped_external = 0
    broken: list[tuple[Path, int, str, str]] = []

    for source in files:
        in_fence = False
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r"`[^`]*`", "", line)
            for match in LINK_RE.finditer(line):
                target = clean_target(match.group(1))
                checked += 1
                if target.startswith(("http://", "https://")):
                    if not args.external:
                        skipped_external += 1
                        continue
                    ok, detail = check_external(target, args.timeout)
                else:
                    ok, detail = resolve_link(source, target)
                if not ok:
                    broken.append((source, line_number, target, detail))

    missing_nav = nav_targets(args.config)

    if not args.quiet:
        print("Link check")
        print(f"  Markdown files: {len(files)}")
        print(f"  links checked:  {checked}")
        if args.external:
            print("  external mode:  enabled")
        else:
            print(f"  external links skipped: {skipped_external}")
        print(f"  nav entries:    {len(missing_nav)} missing")

    for source, line_number, target, detail in broken:
        print(f"ERROR: {source.relative_to(root)}:{line_number}: {target} ({detail})", file=sys.stderr)
    for target in missing_nav:
        print(f"ERROR: mkdocs.yml nav target missing: {target}", file=sys.stderr)

    if broken or missing_nav:
        print(f"FAILED: {len(broken)} broken link(s), {len(missing_nav)} missing nav target(s)", file=sys.stderr)
        return 1
    print("OK: local links, anchors, and navigation targets are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
