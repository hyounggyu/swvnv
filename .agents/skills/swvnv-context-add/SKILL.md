---
name: swvnv-context-add
description: Add supporting Context material to SWVNV. Use when classifying a new source, choosing a contexts/ location, inspecting PDFs, updating registry metadata, or validating context metadata.
---

# SWVNV Context Add

Use this workflow skill to ingest supporting material into `contexts/` while keeping Context separate from canonical SoT.

## Workflow

1. Read the current project overview and SoT structure.
2. Classify the source type: `guide`, `regulation`, `existing_doc`, `meeting`, `review`, `template`, or `working_note`.
3. Choose the target directory based on the source type:
   - `contexts/source-documents/`
   - `contexts/guides/`
   - `contexts/meetings/`
   - `contexts/reviews/`
   - `contexts/permit-documents/`
   - `contexts/working-notes/`
   - `contexts/archive/`
4. Choose a stable lowercase filename with a date or source prefix when useful.
5. If the source is a PDF, use `$swvnv-tool-pdf-reader` to inspect metadata, table of contents, text hits, and selected pages.
6. Add or update the `contexts/registry.yaml` entry with `id`, `type`, `title`, `source_path`, `status`, `authority`, `related_sot`, and `summary`.
7. Run validation:

   ```sh
   uv run python scripts/validate_context.py
   ```

## Guardrails

- Do not change canonical SoT files under `sot/`.
- Do not treat registry summaries as source facts; summaries are search metadata.
- `related_sot` is registry metadata, not a SoT change.
- If the new context suggests a SoT change, hand off to `$swvnv-context-sot-findings`.

## Output

Return the added or proposed context path, registry metadata, validation result, and any follow-up findings or open questions.
