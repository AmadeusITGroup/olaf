---
name: validate-all-competency-packs
description: Discover all competency packs, run the pack validator on each, aggregate results, and propose numbered fixes per pack
protocol: Propose-Act
category: validation
tags: [validation, packs, aggregator, compliance]
---

# Validate All Competency Packs

## Objective
Discover all competency packs under `olaf-core/competencies/`, execute the validator for each pack, summarize results, and propose actionable, numbered fixes aligned with the pack rules.

## References
- Rules: `olaf-core/competencies/olaf-specific-tools/kb/competency-pack-rules.md`
- Validator: `olaf-core/competencies/olaf-specific-tools/tools/validate_competency_pack.py`
- Orchestrator tool: `olaf-core/competencies/olaf-specific-tools/tools/validate_all_packs.py`

## Steps
1. Run the orchestrator tool in JSON mode:
   - `python olaf-core/competencies/olaf-specific-tools/tools/validate_all_packs.py --json`
2. Parse results per pack and compute:
   - Counts: prompts, orchestrator, workflows, typical, entry_points
   - Rule statuses R01–R10 with details
3. Generate numbered fix proposals per pack:
   - R02: Filename rename suggestions (3–4 tokens)
   - R03: Missing docs layout (docs/README.md and docs/<prompt-stem>/files)
   - R06: Templates to reference and suggested target prompts
   - R08: Tools to reference and suggested target prompts
4. Present proposals grouped by pack with numbers. Ask for confirmation (e.g., "Apply 1,3 for developer", or "Apply all for X").
5. On approval, prepare diffs (read-only by default; execute only when explicitly instructed).

## Output
- Summary table of packs and rule pass/fail counts
- Detailed, per-pack numbered proposals with explicit file paths and suggested minimal edits
- Await user confirmation before generating patches

## Notes
- This competency is read-only by default. It proposes precise diffs but does not change files without approval.
- `kb/` is optional and ignored by validator; use it for internal guidance files.
