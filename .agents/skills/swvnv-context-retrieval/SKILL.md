---
name: swvnv-context-retrieval
description: Find SWVNV context evidence. Use when searching the registry and source files for evidence related to a SoT item, document section, review topic, or proposed change.
---

# SWVNV Context Retrieval

Use this skill to find supporting evidence while preserving the boundary between canonical SoT and Context.

## Workflow

1. Read relevant SoT files under `sot/` and identify the primary item plus directly linked items.
2. Search canonical SoT IDs before reading broader context.
3. Search `contexts/registry.yaml` for matching `related_sot`, title, summary, type, and authority.
4. Read only the context source files needed for the request.
5. For PDFs, use `$swvnv-tool-pdf-reader`.
6. Summarize SoT facts separately from context evidence.
7. Report missing context, ambiguous authority, and possible SoT changes as open questions.

## Output

Return a compact list of:

- relevant SoT IDs
- relevant context IDs and source paths
- evidence summary
- open questions or gaps

Do not update SoT during retrieval.
