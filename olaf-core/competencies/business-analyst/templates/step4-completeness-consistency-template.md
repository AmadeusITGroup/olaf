# Step 4: Completeness & Consistency Analysis

Date: <YYYY-MM-DD HH:MM>
Sources: <step2 file>, <raw rules>
Process: Deep analysis with numbered decisions

## 1) Missing Scenarios
- <area>
  - Gap: <what is missing>
  - Options:
    1. <choice 1>
    2. <choice 2>

Example (from spec-windsurf-gpt5lr Step 4)
- Config precedence layering: CLI > config > defaults vs CLI > env > config > defaults
- Authenticated registries: token/credential helper or fail-fast with docs
- Partial failures in multi-repo: continue + non-zero vs stop on first error

## 2) Edge Cases
- <edge>
  - Options:
    1. <choice 1>
    2. <choice 2>

Example
- Existing files in .olaf: overwrite vs skip vs backup
- Temp dir failures: allow --tmp-dir/OLAF_TMPDIR override vs fail with guidance
- Locked file retry: single fixed retry vs configurable retries

## 3) Terminology Consistency
- <term set>
  - Options:
    1. <choice 1>
    2. <choice 2>

Example
- Flag naming conventions: short -x and long --flag
- Registry vs seed: prefer "registry repo"; `--registry-repo`

## 4) Alignment & Determinism
- <ordering/precedence>
  - Options:
    1. <choice 1>
    2. <choice 2>

Example
- Registry processing order: explicit/stable order (e.g., JSON order) vs priority key
- Conflict tie-break for duplicates in same registry: first occurrence wins vs fail

---

## Decisions (Recorded)
- <decision key>: <option>
- Conflicts: <conflict summary + chosen resolution>

Notes
- Capture conflicts explicitly and record resolution policy.
- Trigger Step 2 refresh if terminology/flags change.

Example reference (best):
- spec-windsurf-gpt5lr/step4-YYYYMMDD-HHMM.md (decisions + conflict handling)
