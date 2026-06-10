---
name: swvnv-doc-consistency-review
description: Review SWVNV documents, V&V Records, and Context Materials evidence for mismatches, missing coverage, unresolved items, or traceability gaps.
---

# SWVNV Consistency Review

Use this document-level pipeline skill to find gaps and mismatches across V&V Records, Context Materials, drafts, and generated documents.

## Review Targets

- V&V Records cross-references and traceability
- Context Materials claims not reflected in V&V Records
- Record Items missing from draft or generated documents
- Unresolved review comments
- AI model limitations missing from requirements, risk controls, tests, or V&V summaries

## Workflow

1. Run `$swvnv-records-validation` when useful:

   ```sh
   uv run python scripts/validate_records.py
   uv run python scripts/validate_context.py
   ```

2. Run `$swvnv-records-traceability` when trace links are relevant.
3. Compare related V&V Records objects across requirements, design, risk controls, tests, AI models, datasets, and metrics.
4. Retrieve Context Materials linked to the target area with `$swvnv-context-retrieval`.
5. Identify mismatches as findings, not automatic edits.
6. Use `$swvnv-context-records-findings` for Context Materials-derived V&V Records change possibilities.

## Output

Return findings ordered by risk or document impact. Include file paths, Record Item IDs, context IDs, and recommended next actions.
