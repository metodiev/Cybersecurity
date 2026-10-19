#!/usr/bin/env python3
"""Validate the curriculum manifest against its schema and structural rules.

Checks:
  * JSON Schema conformance
  * unique module IDs and outcome IDs
  * prerequisite existence, no self-dependency, no cycles
  * level monotonicity
  * effort totals
  * path closure, capstone membership, module_count
  * orphan non-elective modules
  * every source ID is declared in REFERENCES.md

Exit code 0 means all checks passed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
LEVEL_ORDER = {f"L{i}": i for i in range(6)}
SOURCE_RE = re.compile(r"^- \*\*([A-Z]\d{2})\*\* —", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "manifest/course-manifest.yaml")
    parser.add_argument("--schema", type=Path, default=ROOT / "manifest/schema.json")
    parser.add_argument("--references", type=Path, default=ROOT / "REFERENCES.md")
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse as a mapping")
    return data


def validate_schema(manifest: dict, schema: dict) -> list[str]:
    validator_cls = Draft202012Validator
    validator = validator_cls(schema, format_checker=validator_cls.FORMAT_CHECKER)
    errors: list[str] = []
    for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path) or "<root>"
        errors.append(f"schema {location}: {error.message}")
    return errors


def validate_structure(manifest: dict, references_path: Path) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    modules = manifest.get("modules", [])
    paths = manifest.get("paths", [])
    by_id: dict[str, dict] = {}

    for module in modules:
        module_id = module.get("id", "<missing>")
        if module_id in by_id:
            errors.append(f"duplicate module id: {module_id}")
        by_id[module_id] = module

    for module in modules:
        module_id = module["id"]
        effort = module["effort_hours"]
        if effort["reading"] + effort["practice"] + effort["assessment"] != effort["total"]:
            errors.append(f"{module_id}: effort components do not sum to total")

        outcome_ids = [outcome["id"] for outcome in module["outcomes"]]
        if len(outcome_ids) != len(set(outcome_ids)):
            errors.append(f"{module_id}: duplicate outcome ids")
        for outcome_id in outcome_ids:
            if not outcome_id.startswith(f"{module_id}.O"):
                errors.append(f"{module_id}: outcome id {outcome_id} does not match module prefix")

        for prerequisite in module["prerequisites"]:
            if prerequisite not in by_id:
                errors.append(f"{module_id}: prerequisite {prerequisite} does not exist")
                continue
            if prerequisite == module_id:
                errors.append(f"{module_id}: self-dependency")
            if LEVEL_ORDER[by_id[prerequisite]["level"]] > LEVEL_ORDER[module["level"]]:
                errors.append(
                    f"{module_id}: prerequisite {prerequisite} is at a higher level"
                )

    # Cycle detection and path closure use the complete map.
    colour = {module_id: 0 for module_id in by_id}

    def visit(node: str, stack: list[str]) -> None:
        colour[node] = 1
        for prerequisite in by_id[node]["prerequisites"]:
            if prerequisite not in by_id:
                continue
            if colour[prerequisite] == 1:
                errors.append("cycle: " + " -> ".join(stack + [prerequisite]))
            elif colour[prerequisite] == 0:
                visit(prerequisite, stack + [prerequisite])
        colour[node] = 2

    for module_id in by_id:
        if colour[module_id] == 0:
            visit(module_id, [module_id])

    for path in paths:
        path_id = path["id"]
        members = path["modules"]
        member_set = set(members)
        if len(members) != len(member_set):
            errors.append(f"{path_id}: duplicate module entries")
        if path["module_count"] != len(members):
            errors.append(f"{path_id}: module_count does not match modules length")
        capstone = path["capstone"]
        if capstone not in by_id:
            errors.append(f"{path_id}: capstone {capstone} does not exist")
        elif by_id[capstone]["type"] != "capstone":
            errors.append(f"{path_id}: {capstone} is not a capstone")
        elif capstone not in member_set:
            errors.append(f"{path_id}: capstone {capstone} is not in the path")
        for module_id in members:
            if module_id not in by_id:
                errors.append(f"{path_id}: unknown module {module_id}")
                continue
            for prerequisite in by_id[module_id]["prerequisites"]:
                if prerequisite not in member_set:
                    errors.append(
                        f"{path_id}: {module_id} requires {prerequisite}, missing from path"
                    )

    for module in modules:
        if module["type"] != "elective" and not any(
            module["id"] in path["modules"] for path in paths
        ):
            errors.append(f"{module['id']}: non-elective module is not in any path")

    declared_sources = set(SOURCE_RE.findall(references_path.read_text(encoding="utf-8")))
    used_sources = {source for module in modules for source in module["sources"]}
    for source in sorted(used_sources - declared_sources):
        errors.append(f"source {source} is used but not declared in {references_path.name}")
    for source in sorted(declared_sources - used_sources):
        warnings.append(f"source {source} is declared but not used by a module")

    summary = {
        "modules": len(modules),
        "outcomes": sum(len(module["outcomes"]) for module in modules),
        "hours": sum(module["effort_hours"]["total"] for module in modules),
        "paths": len(paths),
        "sources_declared": len(declared_sources),
        "sources_used": len(used_sources),
    }
    return errors, warnings, summary


def main() -> int:
    args = parse_args()
    try:
        manifest = load_yaml(args.manifest)
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report and exit cleanly
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate_schema(manifest, schema)
    structural_errors, warnings, summary = validate_structure(manifest, args.references)
    errors.extend(structural_errors)

    if not args.quiet:
        print("Manifest validation")
        print(f"  manifest: {args.manifest}")
        print(f"  schema:   {args.schema}")
        print(f"  modules:  {summary['modules']}")
        print(f"  outcomes: {summary['outcomes']}")
        print(f"  effort:   {summary['hours']} h")
        print(f"  paths:    {summary['paths']}")
        print(f"  sources:  {summary['sources_used']} used / {summary['sources_declared']} declared")

    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"FAILED: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("OK: manifest schema and structural checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
