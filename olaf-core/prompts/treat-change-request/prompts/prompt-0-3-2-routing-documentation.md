# Prompt 0-3-2: Routing Documentation

## Purpose

Generate CONCISE routing summary with copy-paste prompt for user to continue work in next orchestrator.

**Key Principle**: Keep it SHORT - user just needs to know which orchestrator and a ready-to-use prompt.

---

## Input

- **6-context-package.yaml** (from Prompt 0-3-1)
- **All artifacts 1-5** (from Workflows 0-1 and 0-2)

---

## Task Instructions

### Step 1: Extract Key Information

From `6-context-package.yaml`, extract:
- **Change Request ID**: [SACP-XXXXXX]
- **Size Classification**: [XS/S/M/L/XL]
- **Score**: [XX/25]
- **Confidence Score**: [XX%]
- **Target Orchestrator**: `orchestrator-[SIZE]-[name].md`
- **Effort Estimate**: [XX-YY person-days]
- **Duration**: [X-Y weeks]
- **Team Size**: [X-Y developers]
- **Risk Level**: [Low/Medium/High]
- **Modules**: [X]
- **Files**: [XX-YY]
- **LOC**: [X,XXX-Y,YYY]
- **Critical Pre-Actions**: (any blocking items from context package)

### Step 2: Create Copy-Paste Prompt for User

Generate a CONCISE prompt the user can copy-paste to continue in next orchestrator:

**Template**:
```
Execute Orchestrator-[SIZE] for change request [SACP-XXXXXX]:

- Change Request: [One-line description from prerequisite-3]
- Analysis Directory: olaf-works/demand/[SACP-XXXXXX]-analysis/
- Context Package: 6-context-package.yaml
- Size: [SIZE] ([XX]/25 points, [XX]% confidence)
- Effort: [XX-YY] person-days, [X-Y] weeks, [X-Y] developers

Critical Pre-Actions (if any):
[List ONLY blocking items from critical_highlights.blocking_items in context package - max 3 items]
[If none, write: "None - proceed directly to orchestrator"]

Read the context package (6-context-package.yaml) and begin specification workflow.
```

**Important**: This prompt should be SHORT and actionable. User should be able to copy-paste it into next session.

### Step 3: SKIP Verbose Documentation

**ELIMINATED** - All verbose documentation is already in artifacts 1-6. User just needs the prompt and basic stats.

---

---

## Output Format

Use **../templates/template-routing-summary.md** to structure the output.

**Output File**: `7-routing-summary.md`

---

## Success Criteria

- [ ] Summary is 1 page or less (CONCISE!)
- [ ] Copy-paste prompt is ready to use (no placeholders)
- [ ] Key stats visible at a glance (effort, duration, team, risk, modules, files, LOC)
- [ ] Reference files listed (so user knows what exists)
- [ ] Output follows template exactly
- [ ] Output file created: `7-routing-summary.md`
- [ ] User can immediately copy the prompt and continue work

---

## Tools to Use

- `read_file`: Read `6-context-package.yaml` and artifacts 1-5
- `create_file`: Generate `7-routing-summary.md`

---

## Exit Criteria

Declare: **"✅ Routing summary complete. File `7-routing-summary.md` created. User can copy the prompt to continue with Orchestrator-[SIZE]."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0
- **v2.0** (2025-10-08): Simplified to concise format - just routing decision + copy-paste prompt

---

**Key Change v2.0**: Eliminated verbose documentation. User gets: (1) which orchestrator, (2) key stats, (3) copy-paste prompt to continue. All details are in artifacts 1-6.
