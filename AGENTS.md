# SWVNV Agent Rules

이 문서는 SWVNV repository에서 AI agent가 따라야 할 운영 규칙입니다. 사람용 개요는 `README.md`를 먼저 읽습니다.

## Core Model

- SWVNV의 core data class는 **SoT**와 **Context** 두 가지입니다.
- `sot/`는 canonical Source of Truth입니다.
- `contexts/`는 evidence, background, reference material입니다.
- Context는 중요하지만 자동으로 SoT가 되지 않습니다.

## Agent Boundary

- Agent는 regulatory approver가 아닙니다.
- Human approval 전에는 SoT를 변경하지 않습니다.
- Context에서 SoT 변경 가능성을 발견하면 finding 또는 open question으로 보고합니다.
- Generated PDFs와 cache는 source evidence로 취급하지 않습니다.

## Allowed Work Patterns

- **Guide start**: 넓은 요청에서 현재 repository 상태를 확인하고 다음 skill/workflow를 안내합니다.
- **Context add**: 새 context 자료를 분류하고 `contexts/registry.yaml` metadata를 추가합니다.
- **Context retrieval**: SoT 항목, 문서 섹션, 검토 주제와 관련된 context evidence를 찾습니다.
- **Context-derived SoT findings**: context에서 SoT 변경 가능성을 찾되 finding 또는 open question으로만 보고합니다.
- **SoT validation and traceability**: canonical SoT 구조와 trace link를 확인합니다.
- **Document drafting support**: SoT를 기준으로 문서 초안 또는 수정안을 작성하고, context는 rationale, framing, review response에 사용합니다.
- **Consistency review**: SoT, context, draft/generated documents 사이의 mismatch, missing coverage, unresolved review item을 finding으로 정리합니다.
- **Skill authoring**: SWVNV skill 추가 요청은 기존 skill 개선 가능성을 먼저 검토한 뒤 `swvnv-<category>-<name>` 규칙을 따릅니다.

## Source Handling

- Repo-local skills live under `.agents/skills/`.
- SoT facts는 `sot/`에서 먼저 확인합니다.
- Context 자료는 `contexts/registry.yaml`에서 metadata와 authority를 확인한 뒤 필요한 source만 읽습니다.
- PDF evidence는 `$swvnv-tool-pdf-reader`를 사용합니다.
- Git commit message는 `$swvnv-dev-git` 규칙을 따릅니다.
- Python 실행, dependency 변경, formatting, linting, script validation은 `$swvnv-dev-python` 규칙을 따릅니다.
- Typst 문서 작성과 PDF build는 `$swvnv-dev-typst` 규칙을 따릅니다.
- OS setup notes는 `docs/development.md`를 확인합니다.

## Skill Authoring Style

- Skill의 모든 문장은 간결하고 명확해야 합니다.
- 인간과 AI 모두 context가 한정된 자원이라고 가정합니다.
- Agent 행동을 바꾸지 않는 배경 설명은 skill 본문에 넣지 않습니다.
- 상세 설명은 꼭 필요할 때만 별도 reference로 분리합니다.

## Validation

```sh
uv run python scripts/validate_data.py
uv run python scripts/validate_context.py
uv run python scripts/check_traceability.py
uv run ruff check .
```

Python formatting은 명시적으로 요청된 경우에만 실행합니다.

```sh
uv run ruff format .
```

문서 빌드는 필요할 때만 실행합니다.

```sh
uv run python scripts/build_docs.py
```

## Editing Guidance

- SoT 변경은 사용자가 명시적으로 요청한 경우에만 수행합니다.
- Context-derived claim은 canonical fact처럼 쓰지 말고 출처와 불확실성을 함께 표시합니다.
- 문서 초안에는 사용한 SoT ID와 context ID 또는 source path를 남깁니다.
- Findings는 risk 또는 document impact가 큰 순서로 정리합니다.
