# Step 6: Visual Documentation & Diagrams

Date: <YYYY-MM-DD HH:MM>
Sources: <steps 1–5 files>
Process: Mermaid diagrams generation (automated)

Guidance
- IMPORTANT: Use a strong capable model (e.g., Sonnet 4) to generate high-quality Mermaid with non-trivial flows.
- If a weaker model is used, mark output as baseline and schedule a re-generation with a strong model.

Diagrams to produce
1) High-Level Architecture (sources → resolver → download → install → outputs)
2) Install Flow (single-repo)
3) Multi-Repo Interactive Flow (plan + confirm)
4) Retry & Backoff (state diagram)
5) Deterministic Merge & Conflicts
6) Dry-Run Full Plan

Potential extras (popular via Copilot and prior outputs)
- Error handling trees
- Artifact lineage (inputs → transforms → outputs)
- Environment matrix visualization (OS/Go/Git)
- Sequence for reference/bootstrapping distribution
- Decision annotations reflecting Steps 3–5

Example references
- spec-windsurf-gpt5lr/step6-<timestamp>.md (flows, retry, merge, dry-run)

Notes
- Keep diagrams self-sufficient and labeled.
- Cross-reference requirement IDs where helpful.
