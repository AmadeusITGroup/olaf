---
name: transform-raw-spec
description: Propose–Act protocol to transform a raw rules/spec document into a complete, testable specification via Steps 1–7, using curated templates, best examples, and timestamped outputs.
tags: [business-analyst, requirements, transformation, EARS, testability, mermaid, propose-act]
---

CRITICAL: Ensure OLAF condensed framework is loaded: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read .olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.

## Time Retrieval
Use the common helper only when saving files with timestamps: `olaf-core/competencies/common/prompts/time-retrieval.md`.
If the helper is unavailable, use `scripts/now/bin/now-<os>-<arch>` with `-format "20060102-1504"` (Windows: `now-windows-amd64.exe`).

## Input Parameters
- raw_rules_path: string — Path to the source rules/spec (e.g., scripts/olaf/rules.md)
- output_folder: string — Target folder to write step files (e.g., spec-<channel>-<model>)
- spec_name: string — Short name for the spec (used in headings)
- strict_template_compliance: boolean — Enforce templates strictly (default: true)

## Protocol (Propose–Act)
For each step:
- Propose: Show the planned structure using the template and cite the best example.
- Act: Generate the output file using a fresh timestamp (YYYYMMDD-HHMM) and save it under `[output_folder]`.
- Confirm: Summarize what was produced and any open decisions.

## Global Rules
- Each step file must use its own fresh timestamp (no shared timestamp).
- Timestamp format: `YYYYMMDD-HHMM`.
- Use templates under `olaf-core/competencies/business-analyst/templates/` and best examples to guide depth and structure.
- Record all user decisions in Steps 3–5 and trigger a Step 2 refresh if flags/terms/policies change.

## Templates and Best Examples
- Step 1 template: `olaf-core/competencies/business-analyst/templates/step1-clarify-group-template.md`
  - Best example: `spec-github-sonnet4/step1-<timestamp>.md`
- Step 2 template: `olaf-core/competencies/business-analyst/templates/step2-ears-template.md`
  - Best example: `spec-windsurf-gpt5lr/step2-<timestamp>.md` (decision-aligned EARS)
- Step 3 template: `olaf-core/competencies/business-analyst/templates/step3-quality-check-template.md`
  - Best example: `spec-windsurf-gpt5lr/step3-<timestamp>.md` (decisions + explicit policies)
- Step 4 template: `olaf-core/competencies/business-analyst/templates/step4-completeness-consistency-template.md`
  - Best example: `spec-windsurf-gpt5lr/step4-<timestamp>.md`
- Step 5 template: `olaf-core/competencies/business-analyst/templates/step5-challenge-template.md`
  - Best of: `spec-github-sonnet4/step5-<timestamp>.md` (challenge breadth) and `spec-windsurf-gpt5lr/step5-<timestamp>.md` (decision capture)
- Step 6 template: `olaf-core/competencies/business-analyst/templates/step6-visuals-template.md`
  - Best example: `spec-windsurf-gpt5lr/step6-<timestamp>.md`
- Step 7 template: Follow GitHub Sonnet4 style for testability depth
  - Best example: `spec-github-sonnet4/step7-<timestamp>.md`

## Process

1) Step 1 — Clarify & Group (Pre-EARS) [AUTOMATED]
- Propose: Show domains to be extracted and a short gaps list based on the template.
- Act: Save `step1-<timestamp>.md` with domain grouping and “Identified Gaps & Questions”.

2) Step 2 — Transform to EARS [AUTOMATED]
- Propose: Outline domains and planned REQ blocks with Trigger/Condition/Response/Measure.
- Act: Save `step2-<timestamp>.md` with strict EARS. Normalize flags (short `-x`, long `--flag`). Avoid policy claims pending Steps 3–5.

3) Step 3 — Basic Quality Check [USER ENGAGEMENT REQUIRED]
- Propose: List contradictions, duplicates, scope/clarification items with numbered choices.
- Act: Save `step3-<timestamp>.md` and record decisions in a "Decisions and Clarifications" section. If terms/flags/policies change, add TODO: Refresh Step 2.

4) Step 4 — Completeness & Consistency [USER ENGAGEMENT REQUIRED]
- Propose: Missing scenarios, edge cases, terminology consistency, alignment/determinism prompts.
- Act: Save `step4-<timestamp>.md` with Decisions recorded and any conflict resolution policy. If terminology/flags change, add TODO: Refresh Step 2.

5) Step 5 — Challenge, Simplify, Amplify [USER ENGAGEMENT REQUIRED]
- Propose: Web-researched challenge catalog: CLI UX, error taxonomy/exit codes, integrity/provenance, structured logging/redaction, retries/idempotency, multi-repo discovery safety, proxy/CA patterns, security hardening.
- Act: Save `step5-<timestamp>.md` with Challenge/Simplification/Amplification and numbered decision prompts; include MoSCoW priorities; cite 1–2 reputable sources per area.

6) Step 6 — Visual Documentation & Diagrams [AUTOMATED]
- IMPORTANT: Use a strong capable model for Mermaid (e.g., Sonnet 4). If a weaker model is used, mark output as baseline and schedule an upgrade.
- Propose: Diagram list and annotations drawn from Steps 1–5 decisions.
- Act: Save `step6-<timestamp>.md` with:
  - High-level architecture
  - Install flow (single-repo)
  - Multi-repo interactive flow (plan + confirm)
  - Retry/backoff state diagram
  - Deterministic merge/conflict resolution
  - Dry-run full plan
  - Potential extras (if discovered via Copilot or analysis): error handling trees, artifact lineage, environment matrix visualization

7) Step 2 Refresh (if needed)
- When Steps 3–5 alter flags/terms/policies, refresh Step 2 to keep EARS aligned. Overwrite the previous Step 2 with a new timestamped file and link decisions that motivated changes.

8) Step 7 — Testability Assessment [AUTOMATED]
- Propose: Coverage grid and acceptance criteria categories; CI blocks; environment matrix.
- Act: Save `step7-<timestamp>.md` following GitHub Sonnet4’s structure:
  - Verification criteria framework (per requirement group)
  - Installation process tests
  - Git integration tests
  - Performance benchmarks
  - Error condition tests
  - Security tests
  - Acceptance test scenarios (end-to-end)
  - Test automation framework and environment matrix
  - Quality metrics and success thresholds

## Outputs to USER
- Present each generated step as Markdown.
- Summarize decisions and outstanding prompts.
- Confirm save locations under `[output_folder]`.

## Domain-Specific Notes
- Mermaid generation quality depends on the model; prefer strong models for Step 6.
- Use deterministic ordering and explicit conflict/precedence to maximize test determinism.
- Use the time helper or `scripts/now/bin` binaries to ensure correct per-file timestamps.
