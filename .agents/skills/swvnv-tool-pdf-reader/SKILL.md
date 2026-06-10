---
name: swvnv-tool-pdf-reader
description: Search and inspect PDF files used by SWVNV workflows. Use when a workflow needs PDF metadata, table of contents, text hits, selected page images, or page-level evidence citations.
---

# SWVNV Tool PDF Reader

Use this low-level tool skill to read PDFs efficiently and cite page-level evidence. Prefer text search first; render page images only when visual layout may change the answer.

For Python setup, dependency, and execution commands, follow `$swvnv-dev-python` at `.agents/skills/swvnv-dev-python/SKILL.md`. Run the bundled scripts with `uv run python`.

## Workflow

1. Identify relevant PDFs from the calling workflow, registry metadata, filenames, or the user's query.
2. Probe relevant PDFs before reading deeply:

   ```sh
   uv run python .agents/skills/swvnv-tool-pdf-reader/scripts/pdf_probe.py path/to/file.pdf --pretty
   ```

3. Search the Context Materials PDFs for terms from the user request:

   ```sh
   uv run python .agents/skills/swvnv-tool-pdf-reader/scripts/pdf_search.py --query "keyword phrase"
   ```

4. Select a small set of pages. Prefer pages with strong text hits, table-of-contents matches, sparse text, or visual hints.
5. Render only the pages that need visual inspection:

   ```sh
   uv run python .agents/skills/swvnv-tool-pdf-reader/scripts/pdf_render_pages.py path/to/file.pdf --pages 3,7-8
   ```

6. Inspect rendered images with the available image-viewing tool when layout, figures, diagrams, forms, or complex tables matter.
7. Answer with source path, context id if available, page number, and reading mode: `text`, `image`, or `text+image`.

## When To Render Pages

Render page images when any of these are true:

- The answer depends on a figure, diagram, flowchart, screenshot, form, or visual procedure.
- The text extraction is sparse or garbled.
- A table has merged cells, multi-level headers, checkboxes, or layout-dependent relationships.
- Search hits are near words such as `figure`, `diagram`, `table`, `matrix`, `checklist`, `그림`, `도표`, `흐름도`, `표`, `양식`, or `체크리스트`.
- The conclusion depends on page position, grouping, arrows, boxes, captions, or visual hierarchy.

Default to at most 5 rendered pages per pass, then iterate if needed.

## Evidence Discipline

Treat PDF content as Context Materials evidence for the calling workflow, not V&V Records. If PDF evidence suggests a V&V Records change, return page-level evidence to the workflow that will produce findings or open questions. Do not edit V&V Records files from this tool skill.

Use this citation shape in final answers:

```text
Evidence:
- CTX-012, contexts/guides/example.pdf, p.14, text+image
- contexts/guides/other.pdf, p.27, text
```

State uncertainty when text and image readings disagree or when the relevant page is visually ambiguous.

## Script Notes

- `pdf_probe.py` returns page count, PDF metadata, table of contents, sparse pages, and likely visual pages.
- `pdf_search.py` searches PDFs under `contexts/` by default and joins results with `contexts/registry.yaml` when entries exist.
- `pdf_render_pages.py` writes PNG files under `contexts/.cache/pdf-images/` by default.
- `contexts/.cache/` is a derived artifact directory and should not be treated as source evidence.
- Use `$swvnv-dev-python` for Python dependency changes, script execution, formatting, linting, and script validation.
