#!/usr/bin/env python3
"""Print a compact traceability overview for the project."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_data.py"

spec = importlib.util.spec_from_file_location("validate_data", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def main() -> int:
    items = validator.collect_items()
    errors = validator.validate_references(
        items, validator.collect_ai_ids()
    ) + validator.validate_coverage(items)
    for requirement in [item for item in items.values() if item["id"].startswith("SR-")]:
        print(
            f"{requirement['id']} -> "
            f"SA:{', '.join(requirement.get('related_architecture', [])) or 'N/A'} | "
            f"SD:{', '.join(requirement.get('related_design', [])) or 'N/A'} | "
            f"ST:{', '.join(requirement.get('verified_by', [])) or 'N/A'}"
        )
    if errors:
        print("\nTraceability issues:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nTraceability check passed for project.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
