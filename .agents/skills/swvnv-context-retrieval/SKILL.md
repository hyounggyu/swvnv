---
name: swvnv-context-retrieval
description: Find SWVNV Context Materials evidence. Use when searching the registry and source files for evidence related to a Record Item, document section, review topic, or proposed change.
---

# SWVNV Context Materials Retrieval

Use this skill to find supporting evidence while preserving the boundary between V&V Records and Context Materials.

## Workflow

1. Read relevant V&V Records files under `records/` and identify the primary item plus directly linked items.
2. Search Record Item IDs before reading broader Context Materials.
3. Search `contexts/registry.yaml` for matching `related_records`, title, summary, type, and authority.
4. Read only the Context Materials source files needed for the request.
5. For PDFs, use `$swvnv-tool-pdf-reader`.
6. Summarize V&V Records facts separately from Context Materials evidence.
7. Report missing Context Materials, ambiguous authority, and possible V&V Records changes as open questions.

## Output

Return a compact list of:

- relevant Record Item IDs
- relevant context IDs and source paths
- evidence summary
- open questions or gaps

Do not update V&V Records during retrieval.
