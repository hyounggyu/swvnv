#!/usr/bin/env python3
"""Inspect PDFs before deciding which pages need visual rendering."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import fitz

fitz.TOOLS.mupdf_display_errors(False)
fitz.TOOLS.mupdf_display_warnings(False)


VISUAL_TERMS = (
    "figure",
    "fig.",
    "diagram",
    "flow",
    "table",
    "matrix",
    "chart",
    "image",
    "illustration",
    "checklist",
    "form",
    "appendix",
    "그림",
    "도표",
    "흐름도",
    "절차",
    "표",
    "양식",
    "체크리스트",
    "별첨",
    "부록",
)


def page_visual_score(text: str) -> int:
    lowered = text.lower()
    score = sum(lowered.count(term.lower()) for term in VISUAL_TERMS)
    if len(text.strip()) < 250:
        score += 2
    if text.count("\n") > 45:
        score += 1
    return score


def inspect_pdf(path: Path) -> dict[str, Any]:
    doc = fitz.open(path)
    try:
        page_summaries = []
        for page_index, page in enumerate(doc):
            text = page.get_text("text")
            page_summaries.append(
                {
                    "page": page_index + 1,
                    "text_chars": len(text.strip()),
                    "visual_score": page_visual_score(text),
                }
            )

        metadata = {k: v for k, v in doc.metadata.items() if v}
        toc = [
            {"level": level, "title": title, "page": page}
            for level, title, page in doc.get_toc(simple=True)
        ]

        return {
            "path": str(path),
            "page_count": doc.page_count,
            "metadata": metadata,
            "toc": toc,
            "pages": page_summaries,
            "sparse_pages": [item["page"] for item in page_summaries if item["text_chars"] < 250],
            "likely_visual_pages": [
                item["page"] for item in page_summaries if item["visual_score"] >= 2
            ],
        }
    finally:
        doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", nargs="+", type=Path, help="PDF path(s) to inspect")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    results = [inspect_pdf(path) for path in args.pdf]
    print(json.dumps(results, ensure_ascii=False, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
