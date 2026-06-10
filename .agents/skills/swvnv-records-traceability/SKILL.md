---
name: swvnv-records-traceability
description: Check SWVNV V&V Records traceability. Use when inspecting trace links across requirements, design, tests, risk controls, AI models, datasets, and metrics.
---

# SWVNV V&V Records Traceability

Use this skill to inspect traceability across V&V Records objects.

## Workflow

1. Run the traceability check:

   ```sh
   uv run python scripts/check_records_traceability.py
   ```

2. Read relevant V&V Records files when a specific ID or gap needs explanation.
3. Report missing, weak, or suspicious links by Record Item ID.

## Guardrails

- Do not read Context Materials to decide whether a trace link should exist.
- Do not edit V&V Records files unless the user explicitly requests an approved change.
- If a missing trace is suggested by Context Materials evidence, hand off to `$swvnv-context-records-findings`.

## Output

Return traceability status, affected Record Item IDs, linked items, gaps, and recommended next review actions.
