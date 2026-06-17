# SWVNV

SWVNV는 **V&V Records + Context Materials 기반 인허가 문서 AI Assistant**를 실험하는 reference implementation입니다.

목표는 AI가 인허가 문서를 임의로 대신 승인하거나 재작성하게 만드는 것이 아닙니다. 반복 사용되는 관리 기록과 문서 작성의 근거가 되는 Context Materials를 분리하고, AI가 이 둘을 구분해 읽으면서 문서 작성, 검토, 누락 탐지, 불일치 확인을 돕는 구조를 검증합니다.

현재 프로젝트는 가상의 독립형 CT 분석 소프트웨어를 대상으로 한 IEC 62304 스타일 Software V&V 문서 패키지입니다.

> 배경과 작업 과정을 먼저 보고 싶다면
> [SW V&V 문서 작성에 AI 에이전트 활용하기](https://hyounggyu.com/2026/06/17/sw-vv-writing-with-ai-agent/)를 참고하세요.

## 핵심 모델

SWVNV의 핵심 정보 계층은 두 가지입니다.

- **V&V Records**: V&V 문서 생성, 검증, 추적에 직접 사용되는 구조화된 관리 기록입니다. 요구사항, 아키텍처, 상세 설계, 위험 통제, 테스트, AI model metadata, dataset, performance metric, document metadata 같은 Record Item을 포함합니다.
- **Context Materials**: 문서 작성과 판단을 돕는 근거와 배경 자료입니다. 기존 문서, 규제 지침, 제출 템플릿, 회의록, 리뷰 코멘트, 작업 메모가 여기에 속합니다.

Context Materials는 중요하지만 곧바로 V&V Records가 아닙니다. Context Materials에서 V&V Records 변경 가능성이 발견되면 finding 또는 open question으로 보고합니다. V&V Records 변경은 사람이 승인한 뒤 별도로 반영합니다.

## Repository 구조

```text
AGENTS.md         AI agent가 따라야 할 repository 운영 규칙
.agents/          SWVNV 작업을 위한 agent skills
records/          YAML V&V Records
documents/        Typst document entrypoints
document-data.typ YAML loader used by Typst
contexts/         Context Materials registry와 참고 자료
scripts/          Validation, traceability, document build automation
schemas/          Schema roadmap과 lightweight schema descriptors
shared/           재사용 가능한 Typst renderer, table, template
```

## Product Scenario

CT Analysis Workstation은 CT DICOM import, image viewing, ROI/HU measurement, assistive AI segmentation overlay, measurement report export를 다루는 가상 소프트웨어입니다.

AI segmentation output은 보조 기능이며 자동 진단이 아닙니다. Intended user의 검토가 필요합니다.

생성 대상 문서는 다음 8개입니다.

- Software Development Plan
- Software Requirements Specification
- Software Architecture Design
- Software Detailed Design
- Unit Test
- Integration Test
- System Test
- Software Verification and Validation Report

## Setup

이 프로젝트는 Python 환경을 uv로 관리합니다.

필수 도구:

- uv

초기 설정:

```sh
uv sync
```

이 공개용 초기 버전은 외부 규제 가이드 PDF를 repository에 포함하지 않습니다. 필요한 reference PDF는 `contexts/registry.yaml`에 metadata를 추가한 뒤, 프로젝트의 배포 정책에 맞게 별도로 관리합니다.

Python script는 project environment를 쓰도록 uv로 실행합니다.

```sh
uv run python scripts/validate_context.py
```

## Quick Start

V&V Records를 검증합니다.

```sh
uv run python scripts/validate_records.py
```

Context Materials metadata를 검증합니다.

```sh
uv run python scripts/validate_context.py
```

Traceability overview를 출력합니다.

```sh
uv run python scripts/check_records_traceability.py
```

V&V Records Workbook을 생성합니다. Excel 파일은 사람이 검토하고 편집하기 위한 표면이며, `records/*.yaml`이 canonical source입니다.

```sh
uv run python scripts/export_records_workbook.py --output vnv-records.xlsx
```

편집한 V&V Records Workbook을 검증합니다. 이 명령은 YAML 파일을 변경하지 않습니다.

```sh
uv run python scripts/import_records_workbook.py vnv-records.xlsx --dry-run
```

검증을 통과한 workbook을 `records/*.yaml`에 반영합니다.

```sh
uv run python scripts/import_records_workbook.py vnv-records.xlsx
```

Python lint를 실행합니다.

```sh
uv run ruff check .
```

Python formatting을 적용합니다. 이 명령은 Python 파일을 수정할 수 있습니다.

```sh
uv run ruff format .
```

Typst 문서를 PDF로 빌드합니다. 이 명령은 `typst`가 PATH에 있어야 합니다.

```sh
uv run python scripts/build_docs.py
```

Generated PDFs는 `build/pdf/`에 생성됩니다. Build artifact이므로 Git에 commit하지 않습니다.

## AI Agent 작업 방식

AI Agent는 V&V Records와 Context Materials를 구분해 읽습니다.

- V&V Records는 관리 기록이며, 문서에는 script/rendering path를 통해 반영합니다.
- Context Materials는 evidence/background이며, 설명 보완, rationale 작성, 리뷰 반영 여부 확인, 표현 개선에 사용합니다.
- V&V Records 변경 가능성은 finding 또는 open question으로 보고합니다.

Agent skills는 `swvnv-<category>-<name>` 규칙을 따릅니다.

- `swvnv-guide-start`: 프로젝트 상태를 확인하고 다음에 사용할 SWVNV skill을 안내합니다.
- `swvnv-context-add`: 새 Context Materials를 분류하고 registry metadata를 추가합니다.
- `swvnv-context-retrieval`: V&V Records 항목 또는 문서 섹션과 관련된 Context Materials evidence를 찾습니다.
- `swvnv-context-records-findings`: Context Materials evidence에서 V&V Records 변경 가능성을 finding 또는 open question으로 정리합니다.
- `swvnv-records-validation`: V&V Records와 Context Materials registry metadata를 검증합니다.
- `swvnv-records-traceability`: V&V Records 항목 사이의 traceability를 확인합니다.
- `swvnv-doc-drafting`: V&V Records와 Context Materials evidence를 조합해 문서 초안 또는 수정안을 작성합니다.
- `swvnv-doc-consistency-review`: 문서 산출물, V&V Records, Context Materials 사이의 불일치와 누락 가능성을 찾습니다.
- `swvnv-tool-pdf-reader`: PDF evidence를 검색하고 필요한 페이지만 시각적으로 확인합니다.
- `swvnv-dev-git`: Git commit message와 repository 운영 규칙을 다룹니다.
- `swvnv-dev-python`: uv, Ruff, Python script 규칙을 다룹니다.
- `swvnv-dev-typst`: Typst 문서와 PDF build 규칙을 다룹니다.
- `swvnv-dev-skill-authoring`: skill 추가/개선 규칙을 다룹니다.

## Current Status

SWVNV는 research/reference implementation입니다. Validated eQMS, ALM, RIM, complete regulatory submission platform이 아닙니다.

이 프로젝트는 structured regulatory documentation을 작은 software codebase처럼 관리하면서 AI-assisted drafting, review, traceability check, future productization experiment에 적합한 구조를 탐색합니다.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
