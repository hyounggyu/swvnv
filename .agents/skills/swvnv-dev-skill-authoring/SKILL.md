---
name: swvnv-dev-skill-authoring
description: Govern SWVNV skill additions and improvements. Use when adding, renaming, splitting, merging, or improving SWVNV skills.
---

# SWVNV Dev Skill Authoring

Use this skill before adding or changing SWVNV skills. Prefer improving an existing skill when it can satisfy the requested workflow.

## Workflow

1. Read the current skill inventory:

   ```sh
   find .agents/skills -maxdepth 2 -name SKILL.md | sort
   ```

2. Restate the requested capability as one workflow sentence.
3. Compare the request against existing skill frontmatter and workflows.
4. Decide one outcome:
   - `improve_existing`: an existing skill can cover the request with a small workflow, guardrail, routing, or metadata update.
   - `create_new`: the request introduces a distinct data layer, output layer, reusable tool, or stable independent workflow.
   - `defer`: the workflow is not stable enough to encode as a skill.
5. If creating a new skill, choose a name with `swvnv-<category>-<name>`.
6. Use `$skill-creator` conventions for the actual skill creation or update.
7. Validate the changed skill and search for stale references.

## Categories

- `swvnv-guide-*`: route broad requests and choose the next SWVNV workflow.
- `swvnv-context-*`: add, retrieve, or interpret Context evidence.
- `swvnv-sot-*`: validate, inspect, or manage canonical SoT workflows.
- `swvnv-doc-*`: orchestrate SoT and Context into document drafting or review workflows.
- `swvnv-tool-*`: provide reusable low-level tools used by multiple workflows.
- `swvnv-dev-*`: manage repository environment, dependency, skill authoring, and project operations.

## Existing-Skill First Rule

Treat a request as an existing-skill improvement when the trigger, data layer, output, and guardrails mostly match an existing skill. Examples:

- Better context ingestion metadata -> improve `$swvnv-context-add`.
- Better PDF probing or rendering behavior -> improve `$swvnv-tool-pdf-reader`.
- More pre-drafting checks -> improve `$swvnv-doc-drafting`.
- Better first-step guidance -> improve `$swvnv-guide-start`.
- Better Git workflow guidance -> improve `$swvnv-dev-git`.
- Better Typst build guidance -> improve `$swvnv-dev-typst`.

Create a new skill only when a separate, repeatable workflow would otherwise force unrelated responsibilities into an existing skill.

## Writing Rules

- Make every sentence concise and clear.
- Treat context as a limited resource for both humans and AI agents.
- Include only instructions that change agent behavior.
- Prefer short commands, guardrails, and decision rules over background explanation.
- Move optional detail to a referenced file only when the workflow truly needs it.

## Naming Rules

- Use lowercase letters, digits, and hyphens only.
- Keep the folder name, frontmatter `name`, and `$skill-name` references identical.
- Choose the narrowest correct category.
- Do not create skill names for non-core review artifacts.
- Do not create names that combine multiple layers, such as `swvnv-context-doc-*` or `swvnv-sot-tool-*`.

## Guardrails

- Do not create a skill only because the user said "new skill"; check existing fit first.
- Do not add `scripts/`, `references/`, or `assets/` unless the workflow truly needs reusable resources.
- Do not add README, changelog, installation guide, or other extra docs inside a skill.
- Do not let one skill own Context, SoT, Doc, Tool, and Dev responsibilities at once.

## Output

Return:

```text
Decision: improve_existing | create_new | defer
Target: <existing skill or new skill name>
Reason: <short rationale>
Implementation: <specific edits or creation steps>
Validation: <commands/searches to run>
```
