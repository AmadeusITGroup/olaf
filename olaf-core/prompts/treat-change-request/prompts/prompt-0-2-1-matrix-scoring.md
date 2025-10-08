# Prompt 0-2-1: Matrix Scoring

## Purpose

Score the change request across all 5 dimensions of the evaluation matrix using objective criteria from the change-evaluation-matrix.md.

---

## Input

- **1-change-request-summary.md** (from Workflow 0-1)
- **2-technical-scope-analysis.md** (from Workflow 0-1)
- **3-risk-assessment.md** (from Workflow 0-1)
- **../olaf-templates/change-evaluation-matrix.md** (scoring criteria)
- **../olaf-templates/project-complexity-rating.md** (BIRD = Complex)

---

## Task Instructions

### Step 1: Load Evaluation Matrix

Read `../olaf-templates/change-evaluation-matrix.md` to understand scoring criteria.

**Matrix Structure**:
- **5 Dimensions**, each scored 0-5 points
- **Total Score**: 0-25 points
- **Size Mapping**: XS (0-5), S (6-10), M (11-15), L (16-20), XL (21-25)

### Step 2: Score Dimension 1 - Scope & Scale (0-5 points)

**Criteria** (from change-evaluation-matrix.md):
- **0 points**: Single file, <50 LOC
- **1 point**: 1-5 files, <500 LOC
- **2 points**: 5-15 files, 500-2000 LOC
- **3 points**: 15-30 files, 2000-5000 LOC
- **4 points**: 30-50 files, 5000-10000 LOC
- **5 points**: >50 files, >10000 LOC

**Evidence Source**: `2-technical-scope-analysis.md` - Files Affected, LOC Estimate

**Score**: [0-5]

**Justification**: [Reference specific evidence from technical scope analysis]

### Step 3: Score Dimension 2 - Technical Complexity (0-5 points)

**Criteria** (from change-evaluation-matrix.md):
- **0 points**: Configuration change only, no code
- **1 point**: Simple code change, 1 module, no API changes
- **2 points**: Moderate code change, 2-3 modules, simple API changes
- **3 points**: Complex code change, 3-5 modules, API + DB changes
- **4 points**: Very complex, >5 modules, architecture changes
- **5 points**: System-wide refactoring, architectural redesign

**Evidence Source**: `2-technical-scope-analysis.md` - Modules, API Changes, DB Changes, Architecture Impact

**Score**: [0-5]

**Justification**: [Reference specific evidence from technical scope analysis]

### Step 4: Score Dimension 3 - Risk Profile (0-5 points)

**Criteria** (from change-evaluation-matrix.md):
- **0 points**: All risks Low
- **1 point**: Mostly Low risks, 1-2 Medium
- **2 points**: Mix of Low and Medium risks
- **3 points**: Mostly Medium risks, 1-2 High
- **4 points**: Multiple High risks
- **5 points**: Critical risks, high-visibility, compliance concerns

**Evidence Source**: `3-risk-assessment.md` - Business, Technical, Security, Operational Risk Levels

**Score**: [0-5]

**Justification**: [Reference specific risk levels from risk assessment]

### Step 5: Score Dimension 4 - Dependencies & Integration (0-5 points)

**Criteria** (from change-evaluation-matrix.md):
- **0 points**: No dependencies
- **1 point**: 1-2 internal dependencies, no external
- **2 points**: 3-5 internal dependencies, simple integrations
- **3 points**: 5-8 internal dependencies, 1-2 external systems
- **4 points**: >8 internal dependencies, multiple external systems
- **5 points**: Complex cross-system dependencies, external APIs, event-driven

**Evidence Source**: `2-technical-scope-analysis.md` - Integration Points

**Score**: [0-5]

**Justification**: [Reference specific integration points from technical scope analysis]

### Step 6: Score Dimension 5 - Project Context (0-5 points)

**Criteria** (from change-evaluation-matrix.md):
- **0 points**: Simple project, team expert, no constraints
- **1 point**: Simple project, team familiar, few constraints
- **2 points**: Moderate project, team capable, some constraints
- **3 points**: Complex project, team learning, multiple constraints
- **4 points**: Very complex project, team new, significant constraints
- **5 points**: Highly complex project, team unfamiliar, critical constraints

**Evidence Source**: `../olaf-templates/project-complexity-rating.md` (BIRD = Complex)

**BIRD Project Context**:
- **Project Complexity**: Complex (multi-module Spring Boot + Angular + Flowable BPMN)
- **Technology Stack**: Spring Boot, Angular, PostgreSQL, Flowable, RabbitMQ, OpenShift
- **Team Familiarity**: [Infer from requirements - if novel feature, team may be learning]
- **Constraints**: [From `1-change-request-summary.md` - timeline, coordination, dependencies]

**Score**: [0-5]

**Justification**: [Reference project complexity rating and any constraints]

### Step 7: Calculate Total Score

**Total Score** = Dimension 1 + Dimension 2 + Dimension 3 + Dimension 4 + Dimension 5

**Total**: [0-25]

---

## Output Format

Use **../templates/template-size-evaluation-matrix.md** to structure the output.

---

## Success Criteria

- [ ] All 5 dimensions scored (0-5 each)
- [ ] Each score has clear justification with evidence
- [ ] Evidence is quoted/referenced from input artifacts
- [ ] Total score calculated correctly (0-25)
- [ ] Preliminary size classification determined
- [ ] Output follows template exactly

---

## Tools to Use

- `read_file`: Read change-evaluation-matrix.md for scoring criteria
- `read_file`: Read project-complexity-rating.md for BIRD context
- Use artifacts 1-3 as evidence sources

---

## Exit Criteria

Declare: **"Step 2.1 complete. Proceeding to Step 2.2 (Size Calculation)."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Prompt**: `prompt-0-2-2-size-calculation.md`
