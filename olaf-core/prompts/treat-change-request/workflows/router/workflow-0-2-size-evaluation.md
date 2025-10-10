---
name: workflow-0-2-size-evaluation
description: Calculate objective size classification and confidence using the evaluation matrix
tags: [workflow, sequential, treat-change-request]
---

# Workflow 0-2: Size Evaluation

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

## Workflow Overview

**Purpose**: Calculate objective size classification using the change evaluation matrix

**Input**: Three information gathering artifacts (from Workflow 0-1)

**Output**: Size classification (XS/S/M/L/XL) with confidence score and supporting documentation

---

## Input Requirements
- **Primary Input**: Files 1-3 from Workflow 0-1
- **Secondary Inputs**: `change-evaluation-matrix.md`, `project-complexity-rating.md`
- **Input Format**: Markdown documents

## Output Specifications
- **Primary Output**: `4-size-evaluation-matrix.md`, `5-final-size-decision.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all steps in sequence - no skipping

### Prompt 0-2-1: Matrix Scoring

**File**: `../prompts/prompt-0-2-1-matrix-scoring.md`

**Input**: Files 1-3 from Workflow 0-1, change-evaluation-matrix.md, project-complexity-rating.md

**Output**: `4-size-evaluation-matrix.md`

**Validation**: All 5 dimensions scored (0-5), total score calculated (0-25), evidence documented

---

### Prompt 0-2-2: Size Calculation

**File**: `../prompts/prompt-0-2-2-size-calculation.md`

**Input**: `4-size-evaluation-matrix.md`

**Output**: `5-final-size-decision.md`

**Validation**: Size classification assigned (XS/S/M/L/XL), confidence score calculated, effort estimate documented

---

### Prompt 0-2-3: Confidence Validation

**File**: `../prompts/prompt-0-2-3-confidence-validation.md`

**Input**: All artifacts (1-5)

**Output**: Updated `5-final-size-decision.md` with validation

**Validation**: Confidence level validated, size decision confirmed or adjusted, investigation needs documented if needed

---

## Data Flow Diagram
```text
[Files 1-3 from 0-1 + matrices] → [Step 0-2-1: Matrix Scoring] → 4-size-evaluation-matrix.md
                                               ↓
                                  [Step 0-2-2: Size Calculation] → 5-final-size-decision.md
                                               ↓
                                  [Step 0-2-3: Confidence Validation] → Updated 5-final-size-decision.md
```

## Error Handling
- **Step Failure**: Document missing inputs; stop and fix before proceeding
- **Recovery**: Correct inputs and resume from failed step
- **Rollback**: Keep previous decision files; regenerate after fixes

## Completion Criteria
- [ ] Both output files exist (4 and 5)
- [ ] Final size classification clearly stated
- [ ] Confidence score and rationale documented
- [ ] Ready to hand off to Workflow 0-3

## Next Steps
- Proceed to `workflow-0-3-routing-dispatch.md`

## Handoff

**Next workflow**: `workflow-0-3-routing-dispatch.md`

**Provides**: Files 1-5, final size classification, confidence score
