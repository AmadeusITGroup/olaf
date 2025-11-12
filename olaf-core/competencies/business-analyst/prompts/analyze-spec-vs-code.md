---
name: analyze-spec-vs-code
description: Propose–Act protocol to compare an EARS specification against the codebase, produce Phase 1 gaps, Phase 2 impact analysis, and Phase 3 remediation plan.
tags: [business-analyst, requirements, EARS, gap-analysis, impact-analysis, remediation-plan, propose-act]
---

CRITICAL: Ensure OLAF condensed framework is loaded: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read .olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.

## Time Retrieval
Use the common helper only when saving timestamped files: `olaf-core/competencies/common/prompts/time-retrieval.md`.
If unavailable, use `scripts/now/bin/now-<os>-<arch> -format "20060102-1504"` (Windows: `now-windows-amd64.exe`).

## Input Parameters
- ears_spec_path: string — Path to the decision-aligned EARS spec (Step 2)
- code_roots: string[] — One or more root folders to scan (e.g., ["scripts/olaf", "vscode-extension/src"]) 
- languages: string[] — Languages of interest (e.g., ["go", "ts", "md"])
- output_folder: string — Folder to write findings (e.g., `spec-<channel>-<model>` or `olaf-data/findings`)
- strict_template_compliance: boolean — Enforce template structure (default: true)

## Protocol (Propose–Act)
For each phase, follow: Propose → Act → Confirm.
- Propose: Outline the structure using the template + which tools/scans you will run.
- Act: Generate the output file with a fresh timestamp (YYYYMMDD-HHMM) in `[output_folder]`.
- Confirm: Summarize outcomes and list any open questions.

## Phase 1 — Spec vs Code: Gap Analysis
Template: `olaf-core/competencies/business-analyst/templates/spec-gap-analysis-template.md`
- Parse the EARS spec (Trigger/Condition/Response/Measure) and enumerate REQ-IDs.
- Perform static scan on `[code_roots]` to locate places implementing flags/behaviors/logging/exit codes.
- Populate a Traceability Matrix (req → status: Implemented / Missing / Diverged) with evidence (file:line) and short notes.
- Capture “Open Questions” where ambiguity prevents classification.
- Save as: `phase1-gap-analysis-<timestamp>.md`

## Phase 1B — Process & Workflow Alignment
Template: `olaf-core/competencies/business-analyst/templates/spec-process-workflow-template.md`
- Map the end-to-end execution flow with file:line evidence (flags → anchoring → registry → selection → plan → TMP → swap → refresh/update).
- Identify process UX issues (help/version, confirmation gates, precedence visibility, dry-run ordering, retries/backoff, lock handling).
- Save as: `phase1b-process-workflow-<timestamp>.md`

## Phase 1C — Data Model Alignment
Template: `olaf-core/competencies/business-analyst/templates/spec-data-model-template.md`
- Enumerate struct/JSON shapes and their locations; map to spec expectations (config schema, registry presence, provenance, schema versioning).
- Recommend schema/artifact changes (e.g., traceability JSON, source fields).
- Save as: `phase1c-data-model-<timestamp>.md`

## Phase 2 — Impact Analysis
Template: `olaf-core/competencies/business-analyst/templates/spec-impact-analysis-template.md`
- For Missing and Diverged items, assess impacts:
  - Change type (New/Modify/Deprecate/Remove)
  - Business/Technical impacts and risk
  - Affected modules/APIs/CLI flags, data/config/schema
  - Effort estimation and sequencing/rollback
  - Test impacts (affected/new ATs/VCs)
- Save as: `phase2-impact-analysis-<timestamp>.md`

## Phase 3 — Remediation Plan
Template: `olaf-core/competencies/business-analyst/templates/spec-remediation-plan-template.md`
- Propose a sequenced Work Breakdown by capability/domain to close gaps and resolve divergences.
- Define acceptance criteria per workstream and risk management.
- Identify communication cadence and Definition of Done (spec refresh if needed).
- Save as: `phase3-remediation-plan-<timestamp>.md`

## Outputs to USER
- Display each phase report in markdown.
- Provide a concise status summary: counts of Implemented / Missing / Diverged; top risks; ETA for plan.
- Confirm save locations under `[output_folder]`.

## Notes
- Prefer deterministic mapping between REQ-IDs and code evidence.
- Verify Measures when possible (timings, exit codes, log lines).
- If Steps 3–5 decisions evolved after the EARS spec, add a TODO to refresh Step 2 and re-run Phase 1.
## Notes for Phases 1B/1C
- Keep Phase 1 concise; place deep rationale in 1B (process) and 1C (data model).
- Cross-link Phase 1 matrix rows to 1B/1C sections where applicable.
