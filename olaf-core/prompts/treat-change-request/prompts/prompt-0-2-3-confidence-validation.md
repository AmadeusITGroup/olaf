---
name: validate-confidence-change-request-sizing
description: Validate the size decision and identify any additional investigation needs before routing to the size-specific orchestrator
tags: [change-request, validation, confidence, sizing, routing]
---

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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **artifacts_path**: string - Path to directory containing artifacts 1-5 from Workflows 0-1 and 0-2 (REQUIRED)
- **final_size_decision_file**: string - Path to 5-final-size-decision.md file from Prompt 0-2-2 (REQUIRED)
- **confidence_threshold**: number - Minimum confidence percentage for routing approval (OPTIONAL, default: 80)
- **investigation_threshold**: number - Confidence threshold below which investigation is mandatory (OPTIONAL, default: 60)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for confidence validation due to analytical nature

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate that Workflow 0-2 (Size Evaluation) was completed successfully
2. You WILL validate expected outcomes from previous step:
   - All artifacts 1-5 exist and are accessible
   - 5-final-size-decision.md contains complete size classification
   - Size evaluation matrix has been properly calculated
   - Confidence score has been determined

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate that all artifacts 1-5 from Workflows 0-1 and 0-2 exist
- Check access to 5-final-size-decision.md file
- Verify file contains required size classification and confidence data

### 2. Execution Phase

<!-- <confidence_review> -->
**Confidence Level Assessment:**
You WILL extract from 5-final-size-decision.md:
- Size Classification: [XS/S/M/L/XL]
- Confidence Score: [XX%]
- Confidence Level: [High/Medium/Low]

You MUST apply validation thresholds:
- High (>=80%): Proceed to routing, no additional investigation needed
- Medium (60-79%): Acceptable, but document assumptions clearly
- Low (<60%): Additional investigation recommended before routing
<!-- </confidence_review> -->

<!-- <evidence_quality_validation> -->
**Evidence Quality Assessment:**
You WILL review artifacts 1-5 and validate:

**Artifact 1: Change Request Summary**
- Business context is clear and specific
- Requirements are well-defined
- Stakeholders identified
- No major ambiguities exist

**Artifact 2: Technical Scope Analysis**
- File/LOC estimates are evidence-based (not guessed)
- Codebase search tools were used (semantic_search, grep_search)
- Modules are specifically identified (not generic)
- API and database changes are concrete

**Artifact 3: Risk Assessment**
- Risks are specific (not generic boilerplate)
- Each risk has clear mitigation
- Risk levels are justified
- Top risks are prioritized

**Artifact 4: Size Evaluation Matrix**
- All 5 dimensions scored with evidence
- Justifications reference specific facts
- Scoring aligns with matrix criteria
- Total score is calculated correctly

**Artifact 5: Final Size Decision**
- Size classification matches matrix score
- Confidence factors are documented
- Key assumptions are identified
- Unknown factors are listed

You WILL assign Evidence Quality Assessment: [High / Medium / Low]
<!-- </evidence_quality_validation> -->

<!-- <critical_unknowns_analysis> -->
**Critical Unknowns Identification:**
You WILL review all artifacts and identify unknowns that could significantly change the size:

**Technical Unknowns:**
- Modules whose existence is uncertain
- Integration points not yet confirmed
- Technology choices still undecided

**Scope Unknowns:**
- Requirements that are ambiguous
- Dependencies that are not well understood
- External systems whose capabilities are unclear

**Risk Unknowns:**
- Risks that haven't been fully assessed
- Compliance requirements not yet investigated
- Operational impacts not yet understood

You MUST assess impact for each unknown:
- Could it change size by 1 category? (e.g., M -> L)
- Could it change size by 2+ categories? (e.g., M -> XL)

You WILL list Critical Unknowns (could change size by 1+ categories)
<!-- </critical_unknowns_analysis> -->

<!-- <assumptions_review> -->
**Key Assumptions Review:**
You WILL review all key assumptions from 5-final-size-decision.md:

For each assumption you MUST assess:
- How confident are we? (High/Medium/Low)
- What if we're wrong? (Impact analysis)
- Can we validate before routing? (Yes/No)

You WILL identify High-Risk Assumptions (Low confidence + High impact)
<!-- </assumptions_review> -->

<!-- <investigation_recommendations> -->
**Additional Investigation Assessment:**
If confidence is <80% or critical unknowns exist, you WILL provide:

**Investigation Recommendations:**
For each recommended investigation you MUST specify:
- Why: What unknown/assumption does this address?
- How: What tool/method to use?
- Expected Outcome: What will this tell us?
- Impact on Size: Could change from X to Y
<!-- </investigation_recommendations> -->

<!-- <routing_decision> -->
**Final Routing Decision:**
You WILL make decision based on confidence level and evidence quality:

**Decision Options:**
1. **APPROVE FOR ROUTING** (confidence >=80%)
   - All evidence is strong
   - No critical unknowns
   - Assumptions are reasonable
   - Action: Proceed to Workflow 0-3 (Routing)

2. **APPROVE WITH CAUTIONS** (confidence 60-79%)
   - Evidence is acceptable
   - Some unknowns or assumptions
   - Mitigations are in place
   - Action: Proceed to Workflow 0-3, document cautions

3. **INVESTIGATE BEFORE ROUTING** (confidence <60%)
   - Evidence is weak
   - Critical unknowns exist
   - High-risk assumptions
   - Action: Perform recommended investigations, then re-run sizing

You MUST select Final Decision: [Option 1, 2, or 3]
<!-- </routing_decision> -->

### 3. Validation Phase
You WILL validate results:
- Confirm confidence level has been properly assessed
- Verify evidence quality evaluation is complete
- Ensure critical unknowns have been identified
- Validate final routing decision aligns with evidence

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Update 5-final-size-decision.md with confidence validation section
- Validation results: Complete assessment of all artifacts and decision rationale
- Investigation recommendations: Specific actions if confidence is insufficient

## User Communication

### Progress Updates
- Confirmation when confidence level is extracted and validated
- Confirmation when evidence quality assessment is completed
- Confirmation when critical unknowns analysis is finished
- Status of final routing decision with clear rationale

### Completion Summary
- Summary of confidence validation results
- Evidence quality assessment across all artifacts
- Critical unknowns identified (if any)
- Final routing decision with justification
- Investigation recommendations (if applicable)

### Next Steps
You WILL clearly define:
- If APPROVED: Ready for Workflow 0-3 (Routing & Dispatch)
- If INVESTIGATION REQUIRED: Specific investigation actions needed
- Files updated with validation results
- Dependencies for next step completion

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER approve routing with confidence below defined thresholds without explicit justification
- Rule 2: You MUST identify and document all critical unknowns that could change size classification
- Rule 3: You WILL provide specific investigation recommendations rather than generic suggestions
- Rule 4: Evidence quality assessment MUST be based on actual artifact content, not assumptions
- Rule 5: Final routing decision MUST align with confidence score and evidence quality
- Rule 6: You MUST preserve all original content in 5-final-size-decision.md when updating
- Rule 7: Investigation recommendations MUST specify tools, methods, and expected outcomes
- Rule 8: Assumptions review MUST assess both confidence level and potential impact

## Success Criteria
You WILL consider the task complete when:
- [ ] Confidence level validated from 5-final-size-decision.md
- [ ] Evidence quality assessed across all artifacts 1-5
- [ ] Critical unknowns identified and impact assessed
- [ ] High-risk assumptions reviewed and documented
- [ ] Investigation recommendations provided (if confidence <80%)
- [ ] Final routing decision made with clear justification
- [ ] 5-final-size-decision.md updated with validation section
- [ ] Rationale is clear and evidence-based

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute confidence validation following systematic analysis
3. Generate comprehensive validation assessment
4. Update final size decision file with validation results
5. Define next steps based on routing decision

## Error Handling
You WILL handle these scenarios:
- **Missing Artifacts**: Provide clear error message identifying which artifacts are missing and request paths
- **Incomplete Size Decision File**: Request completion of size evaluation before proceeding
- **Invalid Confidence Data**: Request re-execution of Prompt 0-2-2 with proper confidence calculation
- **File Access Issues**: Provide alternative file access methods and troubleshooting steps
- **Ambiguous Evidence**: Request clarification on specific evidence points rather than making assumptions
- **Threshold Configuration Issues**: Use default thresholds and document the decision
- **Template Access Issues**: Provide manual validation format as fallback

** Critical Requirements**
- MANDATORY: Follow systematic validation of all five artifacts
- MANDATORY: Base routing decision on actual evidence, not assumptions
- NEVER approve routing without proper confidence validation
- NEVER make routing decisions without reviewing critical unknowns
- ALWAYS document investigation recommendations with specific actions
- ALWAYS preserve original file content when updating
- ALWAYS provide clear rationale for routing decisions
- ALWAYS validate that confidence score aligns with evidence quality
