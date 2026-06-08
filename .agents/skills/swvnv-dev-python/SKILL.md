---
name: swvnv-dev-python
description: Manage SWVNV Python scripting, uv dependencies, Ruff formatting, linting, and script validation.
---

# SWVNV Dev Python

Use this skill for Python scripting and dependency work in SWVNV. `uv` is the project Python entrypoint; Ruff is the project formatter and linter.

## Command Rules

- Run project scripts through uv:

  ```sh
  uv run python path/to/script.py
  ```

- Run modules through uv:

  ```sh
  uv run python -m module_name
  ```

- Sync dependencies:

  ```sh
  uv sync
  ```

- Add or remove Python packages with uv so `pyproject.toml` and `uv.lock` stay aligned:

  ```sh
  uv add package-name
  uv remove package-name
  uv add --dev package-name
  ```

## Formatting And Linting

First confirm Ruff is available in the project, not just mentioned in documentation:

- `pyproject.toml` should include `ruff` in the `dev` dependency group.
- `pyproject.toml` should include `[tool.ruff]` settings.
- `uv.lock` should be changed only by uv commands, never by hand.

Use these commands:

```sh
uv run ruff format .
uv run ruff check .
```

Run `ruff check` before broad formatting when the user asks for review or risk assessment. Run `ruff format` only when the user wants formatting applied.

If `uv run ruff check .` fails because `ruff` cannot be spawned, classify it as a project setup issue, not a code style result. Add Ruff with uv, then configure `[tool.ruff]`:

```sh
uv add --dev ruff
```

## Script Validation

Use `py_compile` for changed Python scripts:

```sh
uv run python -m py_compile path/to/file.py
```

For bundled skill scripts, compile the concrete files that changed instead of relying only on broad project validation.

For broad Python checks, run validation commands directly.

## Avoid

- Do not use bare `python`, `python3`, `pip`, or ad hoc virtual environments when uv is available.
- Do not hand-edit `uv.lock`.
- Do not install project dependencies globally.
- Do not run formatters that rewrite files unless formatting is explicitly requested.

## Dependency Boundaries

If a Python import fails, first decide whether the dependency belongs in the project. Add Python packages with uv. Document or install native executables through the system package manager instead.

For this project, Python libraries such as `pymupdf`, `pyyaml`, and `ruff` belong in uv. Typst work belongs in `$swvnv-dev-typst`.

## Script Guidance

- Include a normal `if __name__ == "__main__": main()` entrypoint.
- Keep imports explicit and backed by `pyproject.toml`.
- Prefer structured parsers and APIs over ad hoc text manipulation.
- Keep tool scripts deterministic and runnable with `uv run python ...`.
