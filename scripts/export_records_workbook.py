#!/usr/bin/env python3
"""Export records/*.yaml to the V&V Records Workbook format."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

from records_workbook import DEFAULT_WORKBOOK, RECORDS_DIR, export_workbook


def main() -> int:
    parser = ArgumentParser(description="Export V&V Records YAML to an Excel workbook.")
    parser.add_argument(
        "--records-dir",
        type=Path,
        default=RECORDS_DIR,
        help="Directory containing V&V Records YAML files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_WORKBOOK,
        help="Output workbook path.",
    )
    args = parser.parse_args()

    export_workbook(args.records_dir.resolve(), args.output.resolve())
    print(f"Exported V&V Records Workbook: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
