---
name: swvnv-sot-traceability
description: Check SWVNV canonical SoT traceability. Use when inspecting trace links across requirements, design, tests, risk controls, AI models, datasets, and metrics.
---

# SWVNV SoT Traceability

Use this skill to inspect traceability across canonical SoT objects.

## Workflow

1. Run the traceability check:

   ```sh
   uv run python scripts/check_traceability.py
   ```

2. Read relevant SoT files when a specific ID or gap needs explanation.
3. Report missing, weak, or suspicious links by SoT ID.

## Guardrails

- Do not read Context to decide whether a trace link should exist.
- Do not edit SoT files unless the user explicitly requests an approved change.
- If a missing trace is suggested by context evidence, hand off to `$swvnv-context-sot-findings`.

## Output

Return traceability status, affected SoT IDs, linked items, gaps, and recommended next review actions.
