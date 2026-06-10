---
name: swvnv-records-validation
description: Validate SWVNV V&V Records and Context Materials registry metadata. Use when checking structural integrity, known IDs, and registry references.
---

# SWVNV V&V Records Validation

Use this skill to validate V&V Records and Context Materials metadata structure.

## Workflow

1. Run V&V Records validation:

   ```sh
   uv run python scripts/validate_records.py
   ```

2. Run Context Materials registry validation:

   ```sh
   uv run python scripts/validate_context.py
   ```

3. Report failures as structural issues with file paths and IDs.

## Guardrails

- Do not interpret Context Materials content or recommend V&V Records changes.
- Do not edit V&V Records, Context Materials, or document files unless the user explicitly asks for a fix.
- If validation reveals a traceability gap, hand off to `$swvnv-records-traceability` or `$swvnv-doc-consistency-review` as appropriate.

## Output

Return validation status, failed checks, affected IDs, and exact commands run.
