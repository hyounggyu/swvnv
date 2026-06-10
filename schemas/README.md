# Schemas

This directory describes the schema roadmap for SWVNV.

The current repository uses lightweight validation scripts so the reference implementation can run without installing additional schema tooling. The long-term direction is stricter machine-readable schemas for V&V Records and Context Materials metadata.

## Schema Families

- **V&V Records schemas**: controlled regulatory Record Items such as requirements, architecture items, design items, tests, risk controls, AI models, datasets, performance metrics, and document metadata.
- **Context Materials registry schema**: metadata for reference materials used during drafting and review.
- **Document schema**: document identity, status, revision history, approvers, output mapping, and generated artifact metadata.

## Current Validation

The active validation entrypoints are:

```sh
uv run python scripts/validate_records.py
uv run python scripts/validate_context.py
```

These scripts check ID format, duplicate IDs, required fields, cross-reference integrity, and basic traceability coverage for the project.

## Future Direction

Future iterations can replace or supplement the script-based checks with JSON Schema or another schema system. The intent is to keep the validation transparent and agent-friendly while making the object model strict enough for larger documentation packages.
