---
name: swvnv-doc-consistency-review
description: Review SWVNV documents, SoT, and context evidence for mismatches, missing coverage, unresolved items, or traceability gaps.
---

# SWVNV Consistency Review

Use this document-level pipeline skill to find gaps and mismatches across SoT, Context, drafts, and generated documents.

## Review Targets

- SoT cross-references and traceability
- Context claims not reflected in SoT
- SoT items missing from draft or generated documents
- Unresolved review comments
- AI model limitations missing from requirements, risk controls, tests, or V&V summaries

## Workflow

1. Run `$swvnv-sot-validation` when useful:

   ```sh
   uv run python scripts/validate_data.py
   uv run python scripts/validate_context.py
   ```

2. Run `$swvnv-sot-traceability` when trace links are relevant.
3. Compare related SoT objects across requirements, design, risk controls, tests, AI models, datasets, and metrics.
4. Retrieve context linked to the target area with `$swvnv-context-retrieval`.
5. Identify mismatches as findings, not automatic edits.
6. Use `$swvnv-context-sot-findings` for context-derived SoT change possibilities.

## Output

Return findings ordered by risk or document impact. Include file paths, SoT IDs, context IDs, and recommended next actions.
