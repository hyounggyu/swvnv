---
name: swvnv-doc-drafting
description: Draft or revise SWVNV regulatory document sections from V&V Records and Context Materials evidence. Use when producing document text, section revisions, or change proposals.
---

# SWVNV Document Drafting

Use this pipeline skill when drafting or revising regulatory document text.

## Workflow

1. Identify the target document, section, and related Record Item IDs.
2. Read V&V Records before drafting.
3. Run `$swvnv-records-validation` when structural consistency matters.
4. Retrieve supporting Context Materials with `$swvnv-context-retrieval` when evidence is needed.
5. Use `$swvnv-context-records-findings` when Context Materials appear to imply a V&V Records change.
6. Draft from V&V Records facts as the baseline.
7. Use Context Materials for rationale, framing, review comment handling, and wording improvements.
8. List the Record Item IDs and context IDs or source paths used.
9. Flag claims that appear only in Context Materials as findings or open questions.

## Guardrails

- Do not silently promote Context Materials into V&V Records.
- Report Context Materials-only claims as findings or open questions.
- When editing document sources, keep V&V Records references traceable.

## Output

Return the proposed section text or applied document change, cited V&V Records and Context Materials sources, and any open questions.
