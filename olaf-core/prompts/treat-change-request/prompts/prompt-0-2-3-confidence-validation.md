# Prompt 0-2-3: Confidence Validation

## Purpose

Validate the size decision and identify any additional investigation needs before routing to the size-specific orchestrator.

---

## Input

- **All artifacts 1-5** (from Workflows 0-1 and 0-2)
- **5-final-size-decision.md** (from Prompt 0-2-2)

---

## Task Instructions

### Step 1: Review Confidence Level

From `5-final-size-decision.md`, extract:
- **Size Classification**: [XS/S/M/L/XL]
- **Confidence Score**: [XX%]
- **Confidence Level**: [High/Medium/Low]

**Validation Thresholds**:
- **High (≥80%)**: Proceed to routing, no additional investigation needed
- **Medium (60-79%)**: Acceptable, but document assumptions clearly
- **Low (<60%)**: Additional investigation recommended before routing

### Step 2: Validate Evidence Quality

Review artifacts 1-5 and check:

**Artifact 1: Change Request Summary**
- [ ] Business context is clear and specific
- [ ] Requirements are well-defined
- [ ] Stakeholders identified
- [ ] No major ambiguities

**Artifact 2: Technical Scope Analysis**
- [ ] File/LOC estimates are evidence-based (not guessed)
- [ ] Codebase search tools were used (semantic_search, grep_search)
- [ ] Modules are specifically identified (not generic)
- [ ] API and database changes are concrete

**Artifact 3: Risk Assessment**
- [ ] Risks are specific (not generic boilerplate)
- [ ] Each risk has clear mitigation
- [ ] Risk levels are justified
- [ ] Top risks are prioritized

**Artifact 4: Size Evaluation Matrix**
- [ ] All 5 dimensions scored with evidence
- [ ] Justifications reference specific facts
- [ ] Scoring aligns with matrix criteria
- [ ] Total score is calculated correctly

**Artifact 5: Final Size Decision**
- [ ] Size classification matches matrix score
- [ ] Confidence factors are documented
- [ ] Key assumptions are identified
- [ ] Unknown factors are listed

**Evidence Quality Assessment**: [High / Medium / Low]

### Step 3: Identify Critical Unknowns

Review all artifacts and list any unknowns that could significantly change the size:

**Technical Unknowns**:
- Are there modules whose existence is uncertain?
- Are there integration points not yet confirmed?
- Are there technology choices still undecided?

**Scope Unknowns**:
- Are there requirements that are ambiguous?
- Are there dependencies that are not well understood?
- Are there external systems whose capabilities are unclear?

**Risk Unknowns**:
- Are there risks that haven't been fully assessed?
- Are there compliance requirements not yet investigated?
- Are there operational impacts not yet understood?

**Impact Assessment**:
For each unknown:
- **Could it change size by 1 category?** (e.g., M → L)
- **Could it change size by 2+ categories?** (e.g., M → XL)

**Critical Unknowns** (could change size by 1+ categories):
1. [Unknown 1]
2. [Unknown 2]
3. [Unknown 3]

### Step 4: Review Key Assumptions

From `5-final-size-decision.md`, review all key assumptions:

For each assumption:
- **How confident are we?** (High/Medium/Low)
- **What if we're wrong?** (Impact analysis)
- **Can we validate before routing?** (Yes/No)

**High-Risk Assumptions** (Low confidence + High impact):
1. [Assumption 1]: [Impact if wrong]
2. [Assumption 2]: [Impact if wrong]

### Step 5: Recommend Additional Investigation (if needed)

If confidence is <80% or critical unknowns exist:

**Investigation Recommendations**:
1. **[Investigation Action 1]**
   - **Why**: [What unknown/assumption does this address?]
   - **How**: [What tool/method to use?]
   - **Expected Outcome**: [What will this tell us?]
   - **Impact on Size**: [Could change from X to Y]

2. **[Investigation Action 2]**
   - **Why**: [What unknown/assumption does this address?]
   - **How**: [What tool/method to use?]
   - **Expected Outcome**: [What will this tell us?]
   - **Impact on Size**: [Could change from X to Y]

### Step 6: Make Final Routing Decision

Based on confidence level and evidence quality:

**Decision Options**:

1. **APPROVE FOR ROUTING** (confidence ≥80%)
   - All evidence is strong
   - No critical unknowns
   - Assumptions are reasonable
   - **Action**: Proceed to Workflow 0-3 (Routing)

2. **APPROVE WITH CAUTIONS** (confidence 60-79%)
   - Evidence is acceptable
   - Some unknowns or assumptions
   - Mitigations are in place
   - **Action**: Proceed to Workflow 0-3, document cautions

3. **INVESTIGATE BEFORE ROUTING** (confidence <60%)
   - Evidence is weak
   - Critical unknowns exist
   - High-risk assumptions
   - **Action**: Perform recommended investigations, then re-run sizing

**Final Decision**: [Option 1, 2, or 3]

---

## Output Format

Update `5-final-size-decision.md` with a new section at the end using **../templates/template-confidence-validation.md**.

---

## Success Criteria

- [ ] Confidence level validated (High/Medium/Low)
- [ ] Evidence quality assessed across all artifacts
- [ ] Critical unknowns identified (if any)
- [ ] High-risk assumptions reviewed (if any)
- [ ] Investigation recommendations provided (if confidence <80%)
- [ ] Final routing decision made (APPROVE / CAUTION / INVESTIGATE)
- [ ] Rationale is clear and justified
- [ ] Output appended to 5-final-size-decision.md

---

## Tools to Use

- `read_file`: Review all artifacts 1-5
- Analytical reasoning to assess evidence quality

---

## Exit Criteria

**If APPROVE FOR ROUTING or APPROVE WITH CAUTIONS**:
Declare: **"Step 2.3 complete. Workflow 0-2 finished. Size classification CONFIRMED: [X]. Ready for Workflow 0-3 (Routing & Dispatch)."**

**If INVESTIGATE BEFORE ROUTING**:
Declare: **"Step 2.3 complete. Additional investigation required. Perform recommended investigations before proceeding to Workflow 0-3."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Workflow**: `../workflows/workflow-0-3-routing-dispatch.md` (if approved for routing)
