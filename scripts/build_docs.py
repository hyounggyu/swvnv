#!/usr/bin/env python3
"""Build the project's Typst document entrypoints into build/pdf."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCUMENTS = [
    ("documents/01-software-development-plan.typ", "01-software-development-plan.pdf"),
    (
        "documents/02-software-requirements-specification.typ",
        "02-software-requirements-specification.pdf",
    ),
    ("documents/03-software-architecture-design.typ", "03-software-architecture-design.pdf"),
    ("documents/04-software-detailed-design.typ", "04-software-detailed-design.pdf"),
    ("documents/05-unit-test.typ", "05-unit-test.pdf"),
    ("documents/06-integration-test.typ", "06-integration-test.pdf"),
    ("documents/07-system-test.typ", "07-system-test.pdf"),
    ("documents/08-sw-vv-report.typ", "08-sw-vv-report.pdf"),
]


def main(argv: list[str] | None = None) -> int:
    del argv

    typst = shutil.which("typst")
    if typst is None:
        print("Typst is not installed or not on PATH.")
        print("Install Typst, then run:")
        print("uv run python scripts/build_docs.py")
        return 1

    output = ROOT / "build" / "pdf"
    output.mkdir(parents=True, exist_ok=True)
    for source, target in DOCUMENTS:
        source_path = ROOT / source
        target_path = output / target
        print(f"Building {target}")
        subprocess.run(
            [typst, "compile", "--root", str(ROOT), str(source_path), str(target_path)],
            check=True,
        )
    print(f"Built {len(DOCUMENTS)} PDF documents in {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        raise SystemExit(exc.returncode) from exc
