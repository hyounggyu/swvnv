#!/usr/bin/env python3
"""Validate the SWVNV V&V Records YAML without requiring Python packages."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"
ID_PATTERN = re.compile(r"^(SR|SA|SD|UT|IT|ST)-\d{3}$")
YAML_FILES = [
    "project.yaml",
    "documents.yaml",
    "software-development-plan.yaml",
    "requirements.yaml",
    "architecture.yaml",
    "detailed-design.yaml",
    "tests.yaml",
    "ai-models.yaml",
    "datasets.yaml",
    "performance-metrics.yaml",
    "risk-controls.yaml",
]

def load_yaml(path: Path) -> Any:
    try:
        import yaml  # type: ignore

        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except ModuleNotFoundError:
        if not shutil.which("ruby"):
            raise RuntimeError(
                "PyYAML is not installed and Ruby is unavailable. "
                "Install PyYAML or Ruby to parse YAML."
            ) from None
        script = "require 'yaml'; require 'json'; puts JSON.generate(YAML.load_file(ARGV[0]))"
        result = subprocess.run(
            ["ruby", "-e", script, str(path)],
            check=True,
            text=True,
            capture_output=True,
        )
        return json.loads(result.stdout)


def records_file(name: str) -> Any:
    path = RECORDS / name
    if not path.is_file():
        raise FileNotFoundError(path)
    return load_yaml(path)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def collect_items() -> dict[str, dict[str, Any]]:
    files = {
        "SR": ("requirements.yaml", "requirements"),
        "SA": ("architecture.yaml", "architecture_items"),
        "SD": ("detailed-design.yaml", "design_items"),
        "UT": ("tests.yaml", "unit_tests"),
        "IT": ("tests.yaml", "integration_tests"),
        "ST": ("tests.yaml", "system_tests"),
    }
    loaded: dict[str, Any] = {}
    items: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for prefix, (filename, key) in files.items():
        loaded.setdefault(filename, records_file(filename))
        for item in loaded[filename].get(key, []):
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{filename}:{key} has item without id")
                continue
            if item_id in items:
                errors.append(f"duplicate item id: {item_id}")
            if not ID_PATTERN.match(item_id):
                errors.append(f"invalid item id format: {item_id}")
            if not item_id.startswith(prefix + "-"):
                errors.append(f"{item_id} must use {prefix}-### prefix")
            items[item_id] = item
    if errors:
        raise ValueError("\n".join(errors))
    return items


def collect_ai_ids() -> dict[str, set[str]]:
    return {
        "models": {item["id"] for item in records_file("ai-models.yaml").get("ai_models", [])},
        "datasets": {item["id"] for item in records_file("datasets.yaml").get("datasets", [])},
        "metrics": {
            item["id"]
            for item in records_file("performance-metrics.yaml").get("performance_metrics", [])
        },
        "risk_controls": {
            item["id"] for item in records_file("risk-controls.yaml").get("risk_controls", [])
        },
    }


def require_fields(
    items: list[dict[str, Any]], fields: list[str], label: str, errors: list[str]
) -> None:
    for item in items:
        for field in fields:
            if field not in item or item[field] in (None, "", []):
                errors.append(
                    f"{label} {item.get('id', '<missing id>')} missing required field: {field}"
                )


def validate_references(items: dict[str, dict[str, Any]], ai_ids: dict[str, set[str]]) -> list[str]:
    errors: list[str] = []
    known = set(items)
    risk_controls = ai_ids["risk_controls"]
    models = ai_ids["models"]

    reference_fields = [
        "related_architecture",
        "related_design",
        "verified_by",
        "related_requirements",
        "verifies",
        "related_system_tests",
    ]
    for item_id, item in items.items():
        for field in reference_fields:
            for ref in as_list(item.get(field)):
                if ref not in known:
                    errors.append(f"{item_id} references unknown {field}: {ref}")
        for ref in as_list(item.get("risk_controls")):
            if ref not in risk_controls:
                errors.append(f"{item_id} references unknown risk control: {ref}")

    for model in records_file("ai-models.yaml").get("ai_models", []):
        require_fields(
            [model],
            ["id", "name", "version", "task", "related_requirements", "related_system_tests"],
            "ai model",
            errors,
        )
        for field in [
            "related_requirements",
            "related_architecture",
            "related_design",
            "related_system_tests",
        ]:
            for ref in as_list(model.get(field)):
                if ref not in known:
                    errors.append(f"{model['id']} references unknown {field}: {ref}")

    for dataset in records_file("datasets.yaml").get("datasets", []):
        require_fields(
            [dataset],
            ["id", "name", "purpose", "sample_count", "related_model", "related_system_tests"],
            "dataset",
            errors,
        )
        if dataset.get("related_model") not in models:
            errors.append(
                f"{dataset['id']} references unknown model: {dataset.get('related_model')}"
            )
        for ref in as_list(dataset.get("related_system_tests")):
            if ref not in known:
                errors.append(f"{dataset['id']} references unknown system test: {ref}")

    for metric in records_file("performance-metrics.yaml").get("performance_metrics", []):
        require_fields(
            [metric],
            ["id", "name", "acceptance_criterion", "related_model", "related_system_tests"],
            "metric",
            errors,
        )
        if metric.get("related_model") not in models:
            errors.append(f"{metric['id']} references unknown model: {metric.get('related_model')}")
        for ref in as_list(metric.get("related_system_tests")):
            if ref not in known:
                errors.append(f"{metric['id']} references unknown system test: {ref}")

    for control in records_file("risk-controls.yaml").get("risk_controls", []):
        require_fields(
            [control],
            ["id", "title", "risk", "control", "related_requirements", "verified_by"],
            "risk control",
            errors,
        )
        for field in ["related_requirements", "verified_by"]:
            for ref in as_list(control.get(field)):
                if ref not in known:
                    errors.append(f"{control['id']} references unknown {field}: {ref}")

    return errors


def validate_coverage(items: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for item_id, item in items.items():
        if item_id.startswith("SR-") and not any(
            str(ref).startswith("ST-") for ref in as_list(item.get("verified_by"))
        ):
            errors.append(f"{item_id} must be verified by at least one ST item")
        if item_id.startswith("SD-") and not any(
            str(ref).startswith("UT-") for ref in as_list(item.get("verified_by"))
        ):
            errors.append(f"{item_id} must be verified by at least one UT item")
        if item_id.startswith("SA-"):
            has_it = any(str(ref).startswith("IT-") for ref in as_list(item.get("verified_by")))
            has_sd = any(str(ref).startswith("SD-") for ref in as_list(item.get("related_design")))
            if not has_it and not has_sd:
                errors.append(f"{item_id} must link to at least one IT item or SD item")
    return errors


def main(argv: list[str] | None = None) -> int:
    global RECORDS

    parser = ArgumentParser(description="Validate SWVNV V&V Records YAML.")
    parser.add_argument(
        "--records-dir",
        type=Path,
        default=RECORDS,
        help="Directory containing V&V Records YAML files.",
    )
    args = parser.parse_args(argv)

    RECORDS = args.records_dir.resolve()

    try:
        if not RECORDS.is_dir():
            raise FileNotFoundError(f"project has no records directory: {RECORDS}")
        for filename in YAML_FILES:
            records_file(filename)
        items = collect_items()
        ai_ids = collect_ai_ids()
        errors = []
        errors.extend(validate_references(items, ai_ids))
        errors.extend(validate_coverage(items))
        if errors:
            print("Validation failed:")
            for error in errors:
                print(f"- {error}")
            return 1
        print(
            f"Records validation passed for project: "
            f"{len(items)} SR/SA/SD/UT/IT/ST Record Items checked."
        )
        return 0
    except Exception as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
