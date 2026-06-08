---
name: swvnv-guide-start
description: Route broad SWVNV requests. Use when the user asks where to start, what to do next, whether drafting is ready, or which SWVNV skill should run first.
---

# SWVNV Guide Start

Use this navigator skill as the first stop for broad SWVNV questions. It assesses the repository state, identifies the user's likely intent, and recommends the next workflow skill without editing files.

## Workflow

1. Read the project overview and agent rules: `README.md`, `AGENTS.md`, and `contexts/registry.yaml`.
2. Identify the current project SoT and document structure.
3. Inspect current readiness:
   - SoT exists under `sot/`.
   - Context registry exists and has useful entries beyond internal project notes.
   - Validation and traceability are likely needed before drafting.
   - Requested output depends on Typst or PDF context tools.
4. Classify the user request:
   - New material or reference source -> `$swvnv-context-add`
   - Evidence lookup -> `$swvnv-context-retrieval`
   - Context suggests SoT change -> `$swvnv-context-sot-findings`
   - Data integrity check -> `$swvnv-sot-validation`
   - Traceability check -> `$swvnv-sot-traceability`
   - Draft or revise document text -> `$swvnv-doc-drafting`
   - Review draft/generated documents -> `$swvnv-doc-consistency-review`
   - Git commit message or repository operation -> `$swvnv-dev-git`
   - Python, uv, or Ruff issue -> `$swvnv-dev-python`
   - Typst or document build issue -> `$swvnv-dev-typst`
   - OS setup question -> `docs/development.md`
5. Recommend a short sequence of next steps and explain why.

## Routing Defaults

- If context is sparse, recommend adding context before drafting.
- If SoT has not been validated, recommend `$swvnv-sot-validation` before document work.
- If the user asks about relationships between requirements, design, risk, and tests, recommend `$swvnv-sot-traceability`.
- If the user wants to write or revise a document section, recommend validation, context retrieval, then `$swvnv-doc-drafting`.
- If the user asks whether context should change SoT, recommend `$swvnv-context-sot-findings` and keep the result as finding or open question.

## Guardrails

- Do not edit SoT, Context, registry, or document files.
- Do not decide that context evidence is canonical truth.
- Do not draft full document text; hand off to `$swvnv-doc-drafting`.
- Keep the answer operational: current state, likely blocker, next skill, and next command or action.

## Output

Return a compact readiness summary, the recommended next workflow skill, and a numbered sequence of next actions.
