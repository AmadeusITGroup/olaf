---
name: calculate-change-request-size-classification
description: Convert matrix score to final size classification with confidence level and effort estimate for change requests
tags: [change-request, size-calculation, effort-estimation, confidence-assessment]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: Get-Date -Format "yyyyMMdd-HHmm"
- Unix/Linux/macOS: date +"%Y%m%d-%H%M"

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **size_evaluation_matrix_path**: string - Path to 4-size-evaluation-matrix.md from previous step (REQUIRED)
- **change_evaluation_matrix_path**: string - Path to change-evaluation-matrix.md template (REQUIRED - default: ../olaf-templates/change-evaluation-matrix.md)
- **output_template_path**: string - Path to final size decision template (REQUIRED - default: ../templates/template-final-size-decision.md)
- **confidence_threshold**: number - Minimum confidence percentage for high confidence classification (OPTIONAL - default: 80)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for size calculation due to deterministic nature of scoring

## Prerequisites
You MUST verify the preceding phase was completed:
1. You WILL validate that Step 2.1 (Size Evaluation Matrix) was completed
2. You MUST verify expected outcomes from previous step:
   - **4-size-evaluation-matrix.md** exists and contains total score
   - **Preliminary Size Classification** is present [XS/S/M/L/XL]
   - **Score breakdown** is documented with justifications

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm size evaluation matrix file exists and is accessible
- Validate change evaluation matrix template is available
- Check that output template exists
- Verify matrix contains valid total score (0-25 range)

### 2. Execution Phase

<!-- <score_extraction> -->
**Score Extraction**:
You WILL read the size evaluation matrix file and extract:
- **Total Score**: Numeric value between 0-25
- **Preliminary Size Classification**: Current classification [XS/S/M/L/XL]
- **Individual category scores**: For validation purposes
<!-- </score_extraction> -->

<!-- <size_confirmation> -->
**Size Classification Confirmation**:
You MUST apply the size bands from change-evaluation-matrix.md:

| Size | Score Range | Effort Range | Characteristics |
|------|-------------|--------------|-----------------|
| **XS** | 0-5 | 1-3 days | Single file, low complexity, no risk |
| **S** | 6-10 | 3-7 days | Few files, simple changes, low-medium risk |
| **M** | 11-15 | 7-15 days | Multiple modules, moderate complexity |
| **L** | 16-20 | 15-30 days | Cross-module, architecture impact |
| **XL** | 21-25 | 30+ days | System-wide, major refactoring |

You WILL confirm the size classification matches the total score range.
<!-- </size_confirmation> -->

<!-- <confidence_calculation> -->
**Confidence Score Calculation**:
You MUST assess confidence level based on evidence quality using these criteria:

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

You WILL evaluate these assessment factors:
1. **Evidence Quality**: Were codebase searches used? (semantic_search, grep_search)
2. **Estimation Method**: Are file/LOC counts based on data or guesses?
3. **Risk Specificity**: Are risks concrete or generic?
4. **Unknown Factors**: Are there unknowns that could change the size significantly?
5. **Assumptions**: How many critical assumptions were made?
<!-- </confidence_calculation> -->

<!-- <effort_estimation> -->
**Effort Estimate Calculation**:
You WILL calculate effort based on size classification and apply adjustments:

**Base Effort** (from size band):
- XS: 1-3 days
- S: 3-7 days
- M: 7-15 days
- L: 15-30 days
- XL: 30+ days

**Adjustments** (cumulative):
- **High Risk**: Add 20% buffer
- **Many Unknowns**: Add 15% buffer
- **Cross-team Coordination**: Add 10% buffer
- **Complex Integrations**: Add 10% buffer

You MUST document all adjustments applied with justification.
<!-- </effort_estimation> -->

<!-- <confidence_factors> -->
**Confidence Factors Identification**:
You WILL categorize factors affecting confidence:

**Positive Factors** (increase confidence):
- Evidence-based estimates from codebase analysis
- Similar past changes for comparison
- Clear module identification
- Specific risk assessment
- Team familiarity with affected areas

**Negative Factors** (decrease confidence):
- Assumptions without supporting evidence
- No historical comparisons available
- Uncertain scope boundaries
- Generic risk assessment
- Technology unknowns or new integrations
<!-- </confidence_factors> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for deterministic calculations
- Complete all calculation steps systematically
- Validate results against established criteria
- Document all assumptions and reasoning

### 3. Validation Phase
You WILL validate results meet all requirements:
- Confirm size classification aligns with total score
- Verify confidence score calculation methodology
- Validate effort estimate includes appropriate adjustments
- Ensure all factors are properly categorized and documented

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template ../templates/template-final-size-decision.md
- Include all calculated values with supporting rationale
- Document confidence factors and assessment methodology
- Provide clear effort estimate with adjustment breakdown

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when size evaluation matrix is successfully read
- Confirmation when size classification is validated against score bands
- Confirmation when confidence assessment is completed
- Confirmation when effort estimate is calculated with adjustments

### Completion Summary
- Final size classification with confidence level
- Effort estimate range with adjustment rationale
- Key confidence factors identified (positive and negative)
- Location of generated final size decision document

### Next Steps
You WILL clearly define:
- Step 2.2 complete status declaration
- Proceeding to Step 2.3 (Confidence Validation)
- Files provided to next phase: final-size-decision.md
- Dependencies for next step: confidence validation requirements

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Size classification MUST align exactly with total score range from matrix
- Rule 2: Confidence score MUST be calculated using established assessment factors
- Rule 3: Effort estimates MUST include base effort plus documented adjustments
- Rule 4: All assumptions and unknowns MUST be explicitly documented
- Rule 5: Output MUST follow template structure exactly without deviations
- Rule 6: Confidence factors MUST be categorized as positive or negative with rationale
- Rule 7: NEVER modify or override the total score from the evaluation matrix
- Rule 8: Exit criteria declaration MUST be exact: "Step 2.2 complete. Proceeding to Step 2.3 (Confidence Validation)."

## Success Criteria
You WILL consider the task complete when:
- [ ] Size evaluation matrix successfully read and total score extracted
- [ ] Size classification confirmed against score bands from change evaluation matrix
- [ ] Confidence score calculated using established assessment factors
- [ ] Confidence factors documented with positive and negative categorization
- [ ] Effort estimate calculated with base effort and documented adjustments
- [ ] Key assumptions and unknown factors explicitly identified
- [ ] Output generated following template structure exactly
- [ ] Exit criteria declared with exact wording specified

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute size calculation operations following Act protocol
3. Generate outputs in specified template format
4. Provide user communication and confirmations
5. Declare completion with exact exit criteria wording

## Error Handling
You WILL handle these scenarios:
- **Size Evaluation Matrix Not Found**: Provide clear error message and request valid file path from previous step
- **Invalid Total Score Range**: Stop process and request validation of matrix scoring (must be 0-25)
- **Missing Score Breakdown**: Request complete matrix with individual category scores for validation
- **Template File Access Issues**: Provide error message and request manual template specification
- **Confidence Assessment Incomplete**: Request additional evidence or explicitly document assumptions
- **Effort Calculation Errors**: Validate base effort ranges and adjustment percentages, recalculate if needed
- **Output Template Formatting Issues**: Use fallback structure maintaining all required sections

CRITICAL REQUIREMENTS
- MANDATORY: Follow Act protocol for deterministic size calculations
- MANDATORY: Size classification MUST match total score range exactly
- NEVER modify or recalculate the total score from evaluation matrix
- ALWAYS document all assumptions and confidence factors explicitly
- ALWAYS validate size classification against established score bands
- ALWAYS include effort estimate adjustments with clear justification
- ALWAYS declare exact exit criteria: "Step 2.2 complete. Proceeding to Step 2.3 (Confidence Validation)."
- ALWAYS preserve original scoring methodology and results from previous step
