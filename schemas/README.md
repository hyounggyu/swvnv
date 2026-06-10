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
uv run python scripts/check_records_traceability.py
```

These scripts check ID format, duplicate IDs, required fields, cross-reference integrity, and basic traceability coverage for the project.

## V&V Records Workbook

`vnv-records.xlsx` is the human-editable Excel representation of `records/*.yaml`.
The YAML files remain canonical; workbook import reconstructs YAML and runs validation before
replacing the `records/` directory.

```sh
uv run python scripts/export_records_workbook.py --output vnv-records.xlsx
uv run python scripts/import_records_workbook.py vnv-records.xlsx --dry-run
uv run python scripts/import_records_workbook.py vnv-records.xlsx
```

The workbook schema is stored in hidden `_meta`, `_schema`, and `_lookups` sheets. List fields use
one value per line in a cell, and nested YAML objects use dotted column names such as
`input.modality` or `regulatory_context.primary_standard`.

## Future Direction

Future iterations can replace or supplement the script-based checks with JSON Schema or another schema system. The intent is to keep the validation transparent and agent-friendly while making the object model strict enough for larger documentation packages.
