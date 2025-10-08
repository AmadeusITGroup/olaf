# Workflow 0-2: Size Evaluation

## Overview

**Purpose**: Calculate objective size classification using the change evaluation matrix

**Input**: Three information gathering artifacts (from Workflow 0-1)

**Output**: Size classification (XS/S/M/L/XL) with confidence score and supporting documentation

---

## Prompt Execution

**Execute all prompts in sequence - no skipping**

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

## Completion Criteria

✅ **Workflow complete when**:

1. Both output files exist (4-5)
2. Final size classification clearly stated
3. Confidence score and rationale documented
4. Ready to hand off to Workflow 0-3

---

## Handoff

**Next workflow**: `workflow-0-3-routing-dispatch.md`

**Provides**: Files 1-5, final size classification, confidence score
