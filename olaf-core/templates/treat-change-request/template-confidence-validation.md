---

## Confidence Validation (Prompt 0-2-3)

### Evidence Quality Assessment: [High / Medium / Low]

**Artifact Review**:
- ✅ Change Request Summary: [assessment]
- ✅ Technical Scope Analysis: [assessment]
- ✅ Risk Assessment: [assessment]
- ✅ Size Evaluation Matrix: [assessment]

**Overall Evidence Quality**: [Strong / Acceptable / Weak]

---

### Critical Unknowns

**Unknowns that could change size classification**:

1. **[Unknown 1]**
   - **Impact**: [Could change from X to Y size]
   - **Mitigation**: [Recommendation]

2. **[Unknown 2]**
   - **Impact**: [Could change from X to Y size]
   - **Mitigation**: [Recommendation]

---

### High-Risk Assumptions

**Assumptions with low confidence and high impact**:

1. **[Assumption 1]**
   - **Confidence**: [High/Medium/Low]
   - **Impact if Wrong**: [description]
   - **Can Validate?**: [Yes/No - how?]

2. **[Assumption 2]**
   - **Confidence**: [High/Medium/Low]
   - **Impact if Wrong**: [description]
   - **Can Validate?**: [Yes/No - how?]

---

### Recommended Investigation (if confidence <80%)

**Additional investigation recommended**:

1. **[Investigation Action 1]**
   - **Purpose**: [What will this clarify?]
   - **Method**: [semantic_search, grep_search, read specific files]
   - **Expected Outcome**: [What will we learn?]
   - **Time Required**: [estimate]

2. **[Investigation Action 2]**
   - **Purpose**: [What will this clarify?]
   - **Method**: [tool or approach]
   - **Expected Outcome**: [What will we learn?]
   - **Time Required**: [estimate]

---

### Final Routing Decision

**Decision**: [APPROVE FOR ROUTING / APPROVE WITH CAUTIONS / INVESTIGATE BEFORE ROUTING]

**Rationale**:
[Explain the decision based on confidence level, evidence quality, and unknowns]

**If APPROVE FOR ROUTING or APPROVE WITH CAUTIONS**:
- Size Classification: **[XS / S / M / L / XL]** (CONFIRMED)
- Confidence: **[XX%]**
- Target Orchestrator: `orchestrator-[SIZE]-[name].md`
- **Action**: Proceed to Workflow 0-3 (Routing & Dispatch)

**If INVESTIGATE BEFORE ROUTING**:
- **Action**: Complete recommended investigations
- **Then**: Re-run Workflow 0-2 (Size Evaluation) with new evidence
- **Expected Confidence After Investigation**: [XX%]

---

**Validation Completed By**: Prompt 0-2-3
**Date**: YYYY-MM-DD
