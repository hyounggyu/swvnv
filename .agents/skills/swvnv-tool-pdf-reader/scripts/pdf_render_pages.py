#!/usr/bin/env python3
"""Render selected PDF pages to PNG images."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz

fitz.TOOLS.mupdf_display_errors(False)
fitz.TOOLS.mupdf_display_warnings(False)


def parse_pages(spec: str, page_count: int) -> list[int]:
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))

    invalid = [page for page in pages if page < 1 or page > page_count]
    if invalid:
        raise SystemExit(f"Page(s) out of range 1-{page_count}: {invalid}")
    return sorted(pages)


def default_output_dir(pdf: Path) -> Path:
    digest = hashlib.sha1(str(pdf.resolve()).encode("utf-8")).hexdigest()[:10]
    return Path("contexts/.cache/pdf-images") / f"{pdf.stem}-{digest}"


def render_pages(pdf: Path, pages: list[int], output_dir: Path, dpi: int) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    try:
        zoom = dpi / 72
        matrix = fitz.Matrix(zoom, zoom)
        outputs = []
        for page_number in pages:
            page = doc.load_page(page_number - 1)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            output = output_dir / f"page-{page_number:03d}.png"
            pixmap.save(output)
            outputs.append(output)
        return outputs
    finally:
        doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="PDF to render")
    parser.add_argument("--pages", required=True, help="Pages, e.g. 1,3-5,9")
    parser.add_argument("--dpi", type=int, default=180, help="Render DPI")
    parser.add_argument("--output-dir", type=Path, help="Output directory")
    args = parser.parse_args()

    doc = fitz.open(args.pdf)
    try:
        pages = parse_pages(args.pages, doc.page_count)
    finally:
        doc.close()

    output_dir = args.output_dir or default_output_dir(args.pdf)
    outputs = render_pages(args.pdf, pages, output_dir, args.dpi)
    print(
        json.dumps(
            {
                "pdf": str(args.pdf),
                "dpi": args.dpi,
                "pages": pages,
                "outputs": [str(path) for path in outputs],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
