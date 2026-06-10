---
name: swvnv-guide-start
description: Route broad SWVNV requests. Use when the user asks where to start, what to do next, whether drafting is ready, or which SWVNV skill should run first.
---

# SWVNV Guide Start

Use this navigator skill as the first stop for broad SWVNV questions. It assesses the repository state, identifies the user's likely intent, and recommends the next workflow skill without editing files.

## Workflow

1. Read the project overview and agent rules: `README.md`, `AGENTS.md`, and `contexts/registry.yaml`.
2. Identify the current project V&V Records and document structure.
3. Inspect current readiness:
   - V&V Records exists under `records/`.
   - Context Materials registry exists and has useful entries beyond internal project notes.
   - Validation and traceability are likely needed before drafting.
   - Requested output depends on Typst or PDF Context Materials tools.
4. Classify the user request:
   - New material or reference source -> `$swvnv-context-add`
   - Evidence lookup -> `$swvnv-context-retrieval`
   - Context Materials suggest V&V Records change -> `$swvnv-context-records-findings`
   - Data integrity check -> `$swvnv-records-validation`
   - Traceability check -> `$swvnv-records-traceability`
   - Draft or revise document text -> `$swvnv-doc-drafting`
   - Review draft/generated documents -> `$swvnv-doc-consistency-review`
   - Git commit message or repository operation -> `$swvnv-dev-git`
   - Python, uv, or Ruff issue -> `$swvnv-dev-python`
   - Typst or document build issue -> `$swvnv-dev-typst`
   - OS setup question -> `docs/development.md`
5. Recommend a short sequence of next steps and explain why.

## Routing Defaults

- If Context Materials are sparse, recommend adding Context Materials before drafting.
- If V&V Records has not been validated, recommend `$swvnv-records-validation` before document work.
- If the user asks about relationships between requirements, design, risk, and tests, recommend `$swvnv-records-traceability`.
- If the user wants to write or revise a document section, recommend validation, context retrieval, then `$swvnv-doc-drafting`.
- If the user asks whether Context Materials should change V&V Records, recommend `$swvnv-context-records-findings` and keep the result as finding or open question.

## Guardrails

- Do not edit V&V Records, Context Materials, registry, or document files.
- Do not decide that Context Materials evidence is V&V Records.
- Do not draft full document text; hand off to `$swvnv-doc-drafting`.
- Keep the answer operational: current state, likely blocker, next skill, and next command or action.

## Output

Return a compact readiness summary, the recommended next workflow skill, and a numbered sequence of next actions.
