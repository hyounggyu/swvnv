#!/usr/bin/env python3
"""Validate context registry metadata."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTEXTS = ROOT / "contexts"
VALIDATOR_PATH = ROOT / "scripts" / "validate_data.py"

CTX_ID_PATTERN = re.compile(r"^CTX-\d{3}$")
CONTEXT_TYPES = {
    "existing_doc",
    "guide",
    "regulation",
    "meeting",
    "review",
    "template",
    "working_note",
}
CONTEXT_STATUSES = {"active", "archived"}
CONTEXT_AUTHORITIES = {
    "canonical_reference",
    "internal_reference",
    "external_reference",
    "working_context",
}

spec = importlib.util.spec_from_file_location("validate_data", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def load_yaml(path: Path) -> Any:
    if not path.is_file():
        raise FileNotFoundError(path)
    return validator.load_yaml(path)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def require_keys(item: dict[str, Any], keys: list[str], label: str, errors: list[str]) -> None:
    for key in keys:
        if key not in item:
            errors.append(f"{label} {item.get('id', '<missing id>')} missing required field: {key}")


def validate_registry(known_sot: set[str]) -> tuple[set[str], list[str]]:
    data = load_yaml(CONTEXTS / "registry.yaml") or {}
    ids: set[str] = set()
    errors: list[str] = []
    for item in data.get("contexts", []):
        item_id = item.get("id")
        require_keys(
            item,
            [
                "id",
                "type",
                "title",
                "source_path",
                "status",
                "authority",
                "related_sot",
                "summary",
            ],
            "context",
            errors,
        )
        if not item_id:
            continue
        if item_id in ids:
            errors.append(f"duplicate context id: {item_id}")
        ids.add(item_id)
        if not CTX_ID_PATTERN.match(item_id):
            errors.append(f"invalid context id format: {item_id}")
        if item.get("type") not in CONTEXT_TYPES:
            errors.append(f"{item_id} has invalid type: {item.get('type')}")
        if item.get("status") not in CONTEXT_STATUSES:
            errors.append(f"{item_id} has invalid status: {item.get('status')}")
        if item.get("authority") not in CONTEXT_AUTHORITIES:
            errors.append(f"{item_id} has invalid authority: {item.get('authority')}")
        source_path = item.get("source_path")
        if source_path and not (ROOT / source_path).is_file():
            errors.append(f"{item_id} source_path does not exist: {source_path}")
        for ref in as_list(item.get("related_sot")):
            if ref not in known_sot:
                errors.append(f"{item_id} references unknown SoT item: {ref}")
    return ids, errors


def main() -> int:
    try:
        ai_ids = validator.collect_ai_ids()
        known_sot = set(validator.collect_items())
        for ids in ai_ids.values():
            known_sot.update(ids)
        context_ids, errors = validate_registry(known_sot)
        if errors:
            print("Context validation failed:")
            for error in errors:
                print(f"- {error}")
            return 1
        message = (
            f"Context validation passed for project: "
            f"{len(context_ids)} context items checked."
        )
        print(message)
        return 0
    except Exception as exc:
        print(f"Context validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
