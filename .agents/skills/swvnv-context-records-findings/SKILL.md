---
name: swvnv-context-records-findings
description: Review Context Materials evidence for possible V&V Records changes. Use when Context Materials evidence appears to conflict with, extend, or reveal gaps in current V&V Records.
---

# SWVNV Context-to-Records Findings

Use this workflow skill when Context Materials suggest a possible V&V Records change. The output is a finding or open question for human review, not a V&V Records patch.

## Workflow

1. Identify the Context Materials evidence and cite context IDs, source paths, and pages when available.
2. Read the relevant current Record Items under `records/`.
3. Compare Context Materials evidence against V&V Records facts.
4. Classify each issue as:
   - `mismatch`: Context Materials appear to conflict with current V&V Records.
   - `missing_coverage`: Context Materials suggest an item not represented in V&V Records.
   - `ambiguity`: Context Materials are unclear or authority is insufficient.
   - `review_question`: Human judgment is needed before any V&V Records change.
5. Report findings ordered by regulatory, risk, or document impact.

## Guardrails

- Do not edit V&V Records files.
- Do not decide whether Context Materials evidence should become V&V Records.
- Do not rewrite document text as part of this workflow; hand document work to `$swvnv-doc-drafting`.

## Output

Return findings with Context Materials evidence, affected Record Item IDs, impact, uncertainty, and recommended human review questions.
