# Step 3: Basic Quality Check

Date: <YYYY-MM-DD HH:MM>
Sources: <step1 file>, <step2 file>, <raw rules>
Process: Quality check with numbered decisions

## Summary
- Objective: detect contradictions, duplicates, scope creep.
- Action: answer numbered choices; record final decisions.

---

## A. Contradictions
- A1. Branch flag naming
  - Issue: Both `-ref` and `--branch` referenced.
  - Options:
    1. Keep only `--branch` for branch selection.
    2. Keep only `-ref`.
    3. Support both as aliases (document `--branch`).

- A2. Seed-less branch flag
  - Issue: `--branch` without registry.
  - Options:
    1. Ignore.
    2. Apply to default registry.
    3. Error with guidance (recommended).

---

## B. Duplicates / Inconsistencies
- B1. Duplicate phrase lines
  - Issue: Repeated “for each registry”.
  - Options:
    1. Remove duplicate; keep single structured list per registry.

- B3. Flag dash conventions
  - Issue: `-xxxx` vs `---xxxx`.
  - Options:
    1. Short `-x`, long `--flag` (recommended).
    2. Single-dash for all (non-standard).

---

## C. Scope & Clarifications
- C1. Multi-repo installation breadth
  - Issue: Propagation beyond current repo.
  - Options:
    1. Optional with explicit confirmation (interactive plan + confirm).
    2. Separate subcommand/tool.
    3. Drop from MVP.

- C2. Query index generation
  - Issue: External behavior reference.
  - Options:
    1. Inline minimum behavior/format.
    2. Keep reference + add stable I/O contract.

---

## Decisions and Clarifications (Recorded)
- A1: 1 — Use only `--branch`. `-ref` deprecated.
- A2: 3 — Orphan `--branch` errors with guidance.
- B3: 1 — Adopt `-x` and `--flag` universally.
- C1 Policy (example):
  1. Prompt single vs multi-repo.
  2. Show plan and require confirmation.
  3. Exclude hidden/system dirs; skip repos with existing `.olaf` unless forced.
  4. Log per-repo status and final summary; dry-run prints full plan.

Notes
- Record explicit policies when choices affect behavior (e.g., precedence, discovery rules).
- Trigger Step 2 refresh if flags/terms/policies change.

Example reference (best):
- spec-windsurf-gpt5lr/step3-YYYYMMDD-HHMM.md (decisions recorded + explicit policies)
