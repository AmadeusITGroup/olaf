# Phase 1: Spec vs Code — Gap Analysis

Date: <YYYY-MM-DD HH:MM>
Spec: <path to EARS spec>
Code roots: <paths>
Language(s): <e.g., Go/TS>
Provenance: repo=<org/repo> branch=<branch> commit=<sha>
Details: Phase 1B=<path or N/A> Phase 1C=<path or N/A>

## Scope & Method
- Spec style: EARS (Trigger, Condition, Response, Measure)
- Code scan: grep/static analysis across code roots
- Optional: build/run to confirm behaviors

## Traceability Matrix (Excerpt)
| REQ-ID | Title | Status | Evidence | Notes | Details |
|--------|-------|--------|----------|-------|---------|
| REQ-CLI-012 | Dry Run Mode | Implemented / Missing / Diverged | <files:lines> | <summary> | See 1B:<section> / 1C:<section> |

Status legend
- Implemented: Code clearly implements Response under stated Trigger/Condition.
- Missing: No evidence of behavior.
- Diverged: Implemented but mismatches spec (flags, messages, timing, outputs).

## Implemented (Spec → Code)
- <REQ-ID> — <evidence: files:lines> — <notes>

## Missing (Spec → Code)
- <REQ-ID> — Expected: <behavior summary>

## Diverged (Spec ↔ Code)
- <REQ-ID> — Spec: <expected> — Code: <observed> — Impact: <high/med/low>

## Open Questions (for stakeholders)
- <REQ-ID>: <specific clarifying question>

## Risks & Assumptions (Phase 1)
- <risk/assumption>

Notes
- Prefer exact code references (file:line). Attach snippets where helpful.
- For Measures, verify logs/timing/exit codes if feasible.
- Use Details column to reference Phase 1B/1C sections when deeper rationale exists.
