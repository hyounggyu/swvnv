#!/usr/bin/env python3
"""Import a V&V Records Workbook into records/*.yaml."""

from __future__ import annotations

import shutil
import tempfile
from argparse import ArgumentParser
from pathlib import Path

from records_workbook import RECORDS_DIR, dump_records, import_workbook, validate_records_dir


def replace_records(preview_dir: Path, records_dir: Path) -> None:
    records_dir.mkdir(parents=True, exist_ok=True)
    for source in preview_dir.glob("*.yaml"):
        shutil.copy2(source, records_dir / source.name)


def main() -> int:
    parser = ArgumentParser(description="Import an Excel V&V Records Workbook into YAML.")
    parser.add_argument("workbook", type=Path, help="Path to vnv-records.xlsx.")
    parser.add_argument(
        "--records-dir",
        type=Path,
        default=RECORDS_DIR,
        help="Destination V&V Records YAML directory.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Write imported YAML to this directory instead of replacing records/.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and validate the workbook without replacing records/.",
    )
    args = parser.parse_args()

    records = import_workbook(args.workbook.resolve())

    if args.output_dir:
        preview_dir = args.output_dir.resolve()
        dump_records(records, preview_dir)
        validate_records_dir(preview_dir)
        print(f"Imported workbook preview validated: {preview_dir}")
        return 0

    with tempfile.TemporaryDirectory(prefix="swvnv-records-import-") as tmp:
        preview_dir = Path(tmp)
        dump_records(records, preview_dir)
        validate_records_dir(preview_dir)
        if args.dry_run:
            print("Workbook import dry run passed.")
            return 0
        replace_records(preview_dir, args.records_dir.resolve())
        validate_records_dir(args.records_dir.resolve())
        print(f"Imported V&V Records Workbook into: {args.records_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
