---
name: swvnv-records-workbook
description: Manage SWVNV V&V Records Workbook files. Use when exporting records/*.yaml to Excel, importing workbook edits back to YAML, adding or reviewing Git-tracked workbooks under workbooks/, checking workbook/YAML sync, or explaining the controlled workbook workflow for Record Item changes.
---

# SWVNV V&V Records Workbook

Use this skill when V&V Records are handled through an Excel workbook. Treat the workbook as a controlled review artifact and `records/*.yaml` as the canonical machine source.

## Core Rules

- Store tracked workbooks under `workbooks/`.
- Use `workbooks/vnv-records.xlsx` for the current controlled V&V Records Workbook.
- Keep `records/*.yaml` and the tracked workbook semantically aligned.
- Do not rely on binary Excel diff alone; report YAML diffs and validation results.
- Do not change V&V Records from workbook import unless the user explicitly asks for the import/update.

## Export Workflow

1. Export the current canonical records:

   ```sh
   uv run python scripts/export_records_workbook.py --output workbooks/vnv-records.xlsx
   ```

2. Validate the workbook can be imported:

   ```sh
   uv run python scripts/import_records_workbook.py workbooks/vnv-records.xlsx --dry-run
   ```

3. Run the normal records checks:

   ```sh
   uv run python scripts/validate_records.py
   uv run python scripts/validate_context.py
   uv run python scripts/check_records_traceability.py
   ```

4. Include `workbooks/vnv-records.xlsx` in Git when the user wants the workbook tracked.

## Import Workflow

1. Import to a preview directory first:

   ```sh
   uv run python scripts/import_records_workbook.py workbooks/vnv-records.xlsx --output-dir /private/tmp/swvnv-records-preview
   ```

2. Compare preview YAML against `records/` before replacing canonical records.
3. If the user approves the import, run:

   ```sh
   uv run python scripts/import_records_workbook.py workbooks/vnv-records.xlsx
   ```

4. Re-run validation and traceability commands.
5. Summarize changed Record Items from the YAML diff, not from the Excel binary diff.

## Git Review Guidance

- A Record Item change through Excel should usually include both `workbooks/vnv-records.xlsx` and the affected `records/*.yaml`.
- A workbook-only change usually means YAML import was skipped.
- A YAML-only Record Item change usually means workbook export was skipped.
- Schema, script, or documentation-only changes may intentionally omit workbook updates.

## Output

Report the workbook path, whether import/export passed, whether YAML and workbook are aligned, validation commands run, and any Record Item changes that need human review.
