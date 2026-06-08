---
name: swvnv-sot-validation
description: Validate SWVNV canonical SoT and context registry metadata. Use when checking structural integrity, known IDs, and registry references.
---

# SWVNV SoT Validation

Use this skill to validate canonical SoT data and context metadata structure.

## Workflow

1. Run SoT validation:

   ```sh
   uv run python scripts/validate_data.py
   ```

2. Run context registry validation:

   ```sh
   uv run python scripts/validate_context.py
   ```

3. Report failures as structural issues with file paths and IDs.

## Guardrails

- Do not interpret context content or recommend SoT changes.
- Do not edit SoT, context, or document files unless the user explicitly asks for a fix.
- If validation reveals a traceability gap, hand off to `$swvnv-sot-traceability` or `$swvnv-doc-consistency-review` as appropriate.

## Output

Return validation status, failed checks, affected IDs, and exact commands run.
