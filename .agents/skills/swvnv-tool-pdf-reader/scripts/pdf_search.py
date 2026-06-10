#!/usr/bin/env python3
"""Search context PDFs and return likely pages for text or visual review."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import fitz
import yaml

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
    "checklist",
    "그림",
    "도표",
    "흐름도",
    "절차",
    "표",
    "체크리스트",
)


def load_registry(registry: Path) -> dict[str, dict[str, Any]]:
    if not registry.exists():
        return {}
    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    entries = data.get("contexts", [])
    return {entry.get("source_path", ""): entry for entry in entries}


def discover_pdfs(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.rglob("*.pdf"))


def score_page(text: str, query_terms: list[str]) -> tuple[int, bool]:
    lowered = text.lower()
    score = 0
    for term in query_terms:
        score += lowered.count(term.lower()) * 10
    visual_hint = any(term.lower() in lowered for term in VISUAL_TERMS)
    if visual_hint:
        score += 2
    if len(text.strip()) < 250:
        score += 2
        visual_hint = True
    return score, visual_hint


def snippet_for(text: str, query_terms: list[str], max_len: int = 260) -> str:
    compact = " ".join(text.split())
    lowered = compact.lower()
    positions = [
        lowered.find(term.lower()) for term in query_terms if lowered.find(term.lower()) >= 0
    ]
    if not positions:
        return compact[:max_len]
    start = max(0, min(positions) - 80)
    return compact[start : start + max_len]


def search_pdf(
    pdf: Path,
    query_terms: list[str],
    registry_entries: dict[str, dict[str, Any]],
    repo_root: Path,
    top_pages: int,
) -> dict[str, Any] | None:
    doc = fitz.open(pdf)
    try:
        page_hits = []
        for page_index, page in enumerate(doc):
            text = page.get_text("text")
            score, visual_hint = score_page(text, query_terms)
            if score <= 0:
                continue
            page_hits.append(
                {
                    "page": page_index + 1,
                    "score": score,
                    "text_chars": len(text.strip()),
                    "visual_hint": visual_hint,
                    "snippet": snippet_for(text, query_terms),
                }
            )

        if not page_hits:
            return None

        source_path = str(pdf.relative_to(repo_root)) if pdf.is_relative_to(repo_root) else str(pdf)
        entry = registry_entries.get(source_path, {})
        return {
            "context_id": entry.get("id"),
            "title": entry.get("title") or doc.metadata.get("title") or pdf.name,
            "path": source_path,
            "page_count": doc.page_count,
            "hits": sorted(page_hits, key=lambda item: item["score"], reverse=True)[:top_pages],
        }
    finally:
        doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--root", type=Path, default=Path("contexts"), help="PDF file or directory")
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("contexts/registry.yaml"),
        help="Context Materials registry YAML",
    )
    parser.add_argument("--top-docs", type=int, default=8)
    parser.add_argument("--top-pages", type=int, default=5)
    args = parser.parse_args()

    repo_root = Path.cwd()
    registry_entries = load_registry(args.registry)
    query_terms = [term for term in args.query.split() if term]
    results = []
    for pdf in discover_pdfs(args.root):
        result = search_pdf(pdf, query_terms, registry_entries, repo_root, args.top_pages)
        if result:
            results.append(result)

    results.sort(key=lambda item: sum(hit["score"] for hit in item["hits"]), reverse=True)
    print(json.dumps(results[: args.top_docs], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
