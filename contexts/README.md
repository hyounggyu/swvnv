# 인허가 문서 작성 Context Repository

이 디렉토리는 인허가 문서 작성을 위한 참고 자료를 관리합니다.

핵심 원칙은 단순합니다.

- `sot/`는 반복 사용되는 정규 정보의 기준입니다.
- `contexts/`는 문서 작성과 판단을 돕는 근거와 배경입니다.
- context에서 발견한 정보는 곧바로 SoT가 아닙니다.
- AI가 발견한 SoT 변경 가능성은 finding 또는 open question으로 보고합니다.

## Files

```text
contexts/
├── registry.yaml       Context 자료의 메타데이터와 관련 SoT 참조
├── source-documents/   기존 문서, 가이드, 법령, 지침, 외부 참고자료
├── meetings/           회의록, 전사 자료, 발표 자료
├── reviews/            내부/외부 리뷰와 코멘트
├── permit-documents/   제출 템플릿, 초안, 예시 문서
├── working-notes/      요약, 결정사항, 미해결 질문
└── archive/            보존 자료
```

## Registry

`registry.yaml`은 context 자료를 AI가 안전하게 찾고 해석할 수 있게 하는 색인입니다.

각 항목은 다음 필드를 가집니다.

- `id`: `CTX-###` 형식의 context ID
- `type`: `existing_doc`, `guide`, `regulation`, `meeting`, `review`, `template`, `working_note`
- `title`: 사람이 읽을 제목
- `source_path`: repository root 기준 파일 경로
- `status`: `active` 또는 `archived`
- `authority`: `canonical_reference`, `internal_reference`, `external_reference`, `working_context`
- `related_sot`: 관련 SoT ID 목록
- `summary`: AI 검색과 사람이 훑어보기에 필요한 짧은 요약

## Validation

다음 명령은 context metadata를 현재 SoT와 함께 검증합니다.

```sh
uv run python scripts/validate_context.py
```
