---
name: swvnv-context-sot-findings
description: Review context evidence for possible SoT changes. Use when context evidence appears to conflict with, extend, or reveal gaps in current SoT.
---

# SWVNV Context SoT Findings

Use this workflow skill when Context suggests a possible SoT change. The output is a finding or open question for human review, not a SoT patch.

## Workflow

1. Identify the context evidence and cite context IDs, source paths, and pages when available.
2. Read the relevant current SoT items under `sot/`.
3. Compare context evidence against canonical SoT facts.
4. Classify each issue as:
   - `mismatch`: Context appears to conflict with current SoT.
   - `missing_coverage`: Context suggests an item not represented in SoT.
   - `ambiguity`: Context is unclear or authority is insufficient.
   - `review_question`: Human judgment is needed before any SoT change.
5. Report findings ordered by regulatory, risk, or document impact.

## Guardrails

- Do not edit SoT files.
- Do not decide whether context evidence should become canonical truth.
- Do not rewrite document text as part of this workflow; hand document work to `$swvnv-doc-drafting`.

## Output

Return findings with context evidence, affected SoT IDs, impact, uncertainty, and recommended human review questions.
