---
name: swvnv-dev-git
description: Manage SWVNV Git workflow rules. Use when writing or reviewing commit messages, branch names, fork workflow, or repository operation guidance.
---

# SWVNV Dev Git

Use this skill for Git operation rules in this repository.

## Commit Messages

Use Conventional Commits:

```text
<type>(<scope>): <summary>
```

Allowed types:

- `feat`: new user-facing capability, skill, or workflow.
- `fix`: bug fix.
- `docs`: documentation-only change.
- `refactor`: structure change without intended behavior change.
- `test`: test or validation change.
- `chore`: dependency, config, or repository maintenance.

Preferred scopes:

- `skills`
- `context`
- `records`
- `docs`
- `typst`
- `python`
- `git`
- `repo`

## Summary Rules

- Use lowercase English.
- Use imperative present tense.
- Keep it under 72 characters when practical.
- Do not end with a period.

## Examples

```text
feat(skills): add swvnv-dev-git commit rules
refactor(skills): split typst build guidance from python rules
docs(repo): remove make shortcut references
chore(python): prune unused dependencies
```

## Guardrails

- Inspect the actual changes before suggesting a commit message.
- Choose one primary intent when changes mix types.
- Use `BREAKING CHANGE:` in the body for breaking changes.
- Do not create commits unless the user explicitly asks.
- Branch and fork workflows will be added later.
