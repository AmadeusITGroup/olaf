# Prompt 0-2-2: Size Calculation

## Purpose

Convert the matrix score to a final size classification with confidence level and effort estimate.

---

## Input

- **4-size-evaluation-matrix.md** (from Prompt 0-2-1)
- **../olaf-templates/change-evaluation-matrix.md** (size mapping rules)

---

## Task Instructions

### Step 1: Extract Total Score

From `4-size-evaluation-matrix.md`, extract:
- **Total Score**: [0-25]
- **Preliminary Size Classification**: [XS/S/M/L/XL]

### Step 2: Confirm Size Classification

Use the size bands from `change-evaluation-matrix.md`:

| Size | Score Range | Effort Range | Characteristics |
|------|-------------|--------------|-----------------|
| **XS** | 0-5 | 1-3 days | Single file, low complexity, no risk |
| **S** | 6-10 | 3-7 days | Few files, simple changes, low-medium risk |
| **M** | 11-15 | 7-15 days | Multiple modules, moderate complexity |
| **L** | 16-20 | 15-30 days | Cross-module, architecture impact |
| **XL** | 21-25 | 30+ days | System-wide, major refactoring |

**Confirmed Size Classification**: [XS / S / M / L / XL]

### Step 3: Calculate Confidence Score

Assess confidence level based on evidence quality:

**High Confidence (80-100%)**:
- All estimates based on codebase search results
- Similar past changes available for comparison
- All modules clearly identified
- Risks are specific and well-understood
- No significant unknowns

**Medium Confidence (60-79%)**:
- Most estimates evidence-based, some assumptions
- Some similar past changes available
- Most modules identified, some uncertainty
- Risks mostly specific, some generic
- Few unknowns with manageable impact

**Low Confidence (<60%)**:
- Estimates largely assumed (no codebase search)
- No similar past changes
- Module identification uncertain
- Risks are generic
- Significant unknowns

**Confidence Assessment Factors**:
1. **Evidence Quality**: Were codebase searches used? (semantic_search, grep_search)
2. **Estimation Method**: Are file/LOC counts based on data or guesses?
3. **Risk Specificity**: Are risks concrete or generic?
4. **Unknown Factors**: Are there unknowns that could change the size significantly?
5. **Assumptions**: How many critical assumptions were made?

**Confidence Score**: [XX%]

**Confidence Level**: [High / Medium / Low]

### Step 4: Calculate Effort Estimate

Based on size classification and complexity:

**Base Effort** (from size band):
- XS: 1-3 days
- S: 3-7 days
- M: 7-15 days
- L: 15-30 days
- XL: 30+ days

**Adjustments**:
- **High Risk**: Add 20% buffer
- **Many Unknowns**: Add 15% buffer
- **Cross-team Coordination**: Add 10% buffer
- **Complex Integrations**: Add 10% buffer

**Adjusted Effort Estimate**: [XX-YY person-days]

### Step 5: Identify Confidence Factors

List key factors affecting confidence:

**Positive Factors** (increase confidence):
- Evidence-based estimates
- Similar past changes
- Clear module identification
- Specific risk assessment
- Team familiarity

**Negative Factors** (decrease confidence):
- Assumptions without evidence
- No historical comparisons
- Uncertain scope
- Generic risk assessment
- Technology unknowns

---

## Output Format

Use **../templates/template-final-size-decision.md** to structure the output.

---

## Success Criteria

- [ ] Size classification confirmed from matrix score
- [ ] Confidence score calculated with justification
- [ ] Confidence factors documented (positive and negative)
- [ ] Effort estimate calculated with adjustments
- [ ] Key assumptions identified
- [ ] Unknown factors documented
- [ ] Output follows template exactly

---

## Tools to Use

- `read_file`: Read 4-size-evaluation-matrix.md
- `read_file`: Read change-evaluation-matrix.md for size mapping
- Analytical reasoning for confidence assessment

---

## Exit Criteria

Declare: **"Step 2.2 complete. Proceeding to Step 2.3 (Confidence Validation)."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Prompt**: `prompt-0-2-3-confidence-validation.md`
