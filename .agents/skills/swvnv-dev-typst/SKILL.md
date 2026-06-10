---
name: swvnv-dev-typst
description: Build and maintain SWVNV Typst documents. Use when working with Typst entrypoints, shared Typst templates, generated PDFs, or document build errors.
---

# SWVNV Dev Typst

Use this skill for Typst document sources and PDF builds.

## Workflow

1. Read document entrypoints under `documents/`.
2. Confirm `document-data.typ` and shared helpers resolve from the project root.
3. Read shared Typst helpers under `shared/` only when needed.
4. Build PDFs with:

   ```sh
   uv run python scripts/build_docs.py
   ```

5. Check generated PDFs under `build/pdf/`.

## Guardrails

- `typst` must be on `PATH` for PDF builds.
- Generated PDFs are build artifacts.
- Do not edit V&V Records data to fix Typst layout unless the user asks for a V&V Records change.
- Use `$swvnv-dev-python` for Python script, uv, Ruff, or dependency work.

## Output

Return the build command, output path, changed Typst files, and any build errors.
