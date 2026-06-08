# Development Notes

This page records local setup notes that do not need an agent skill.

## Supported Paths

- macOS and Linux are the primary development paths.
- Windows users should use WSL2.
- Windows native PowerShell is not the recommended path for this repository.

## Codex Desktop On Windows

- Configure the Codex agent to run in WSL.
- Restart Codex Desktop after changing the agent environment.
- Keep the repository in the Linux filesystem, such as `~/code/hg-swvnv`.
- Avoid `/mnt/c/...` for active work when possible.

## Useful Tools

- `uv` runs Python scripts and manages dependencies.
- `typst` builds generated PDFs.
- `git` manages repository changes.
- Poppler tools can help inspect PDF files outside the core workflow.
