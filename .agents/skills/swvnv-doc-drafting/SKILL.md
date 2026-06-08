---
name: swvnv-doc-drafting
description: Draft or revise SWVNV regulatory document sections from SoT and Context evidence. Use when producing document text, section revisions, or change proposals.
---

# SWVNV Document Drafting

Use this pipeline skill when drafting or revising regulatory document text.

## Workflow

1. Identify the target document, section, and related SoT IDs.
2. Read canonical SoT before drafting.
3. Run `$swvnv-sot-validation` when structural consistency matters.
4. Retrieve supporting context with `$swvnv-context-retrieval` when context is needed.
5. Use `$swvnv-context-sot-findings` when context appears to imply a SoT change.
6. Draft from SoT facts as the baseline.
7. Use Context for rationale, framing, review comment handling, and wording improvements.
8. List the SoT IDs and context IDs or source paths used.
9. Flag claims that appear only in Context as findings or open questions.

## Guardrails

- Do not silently promote Context into SoT.
- Report context-only claims as findings or open questions.
- When editing document sources, keep SoT references traceable.

## Output

Return the proposed section text or applied document change, cited SoT/context sources, and any open questions.
