# Tester API (Path B-first)

Hybrid API testing toolkit prioritizing Postman/Newman with GenAI-assisted workflow proposals and Markdown documentation.

## Prerequisites
- Node.js installed (for Portman, Newman, Mermaid CLI)
- Python 3.9+

## Install

Node deps:
```bash
npm install
```

Python deps:
```bash
pip install -r requirements.txt
```

## Quick Start

1) Build Postman collection from OpenAPI (via Portman):
```bash
python tester-api/scripts/build_tests.py --spec specs/openapi.yaml --out .tester/postman/base.collection.json
```

2) Propose workflows (deterministic stub; GenAI pluggable via env):
```bash
python tester-api/scripts/analyze_openapi_genai.py --spec specs/openapi.yaml --out .tester/workflows/proposals.yaml
```

3) Generate chosen workflow artifacts (Postman collection, Mermaid, Markdown):
```bash
python tester-api/scripts/generate_workflow.py \
  --proposal-id wf_001 \
  --engine postman \
  --collection-out .tester/postman/workflows/wf_001.collection.json \
  --mermaid-out .tester/diagrams/ \
  --docs-out docs/workflows/
```

4) Run tests (Newman):
```bash
python tester-api/scripts/run_tests.py \
  --collection .tester/postman/base.collection.json \
  --env tester-api/config/newman.env.json
```

## GenAI configuration
- Provider: AWS Bedrock (e.g., Anthropic Sonnet v4)
- Set environment variables (examples):
  - `BEDROCK_REGION=eu-west-1`
  - `BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20240620-v1:0` (example)
  - AWS credentials in your environment/credential chain
- If not set, the analyzer falls back to deterministic proposals.

## Output locations
- `.tester/index.json` — normalized operations graph
- `.tester/workflows/proposals.yaml` — proposed scenarios
- `.tester/postman/` — generated Postman collections
- `.tester/diagrams/` — Mermaid `.mmd` and rendered images
- `docs/workflows/` — Markdown reports + `INDEX.md`

## Notes
- Multiple specs are accepted on CLI, current Portman build processes the first; merging can be added later.
- Filters for partial runs are planned via Newman folders/tags.
