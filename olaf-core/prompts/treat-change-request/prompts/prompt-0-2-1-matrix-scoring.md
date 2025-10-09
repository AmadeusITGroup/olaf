---
name: evaluate-change-request-matrix-scoring
description: Score change request across 5 dimensions using objective criteria from evaluation matrix to determine size classification
tags: [evaluation, matrix, scoring, change-request, sizing]
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
- **change_request_summary_path**: string - Path to change request summary file from Workflow 0-1 (REQUIRED)
- **technical_scope_analysis_path**: string - Path to technical scope analysis file from Workflow 0-1 (REQUIRED)
- **risk_assessment_path**: string - Path to risk assessment file from Workflow 0-1 (REQUIRED)
- **evaluation_matrix_path**: string - Path to change evaluation matrix criteria file (OPTIONAL, default: "../olaf-templates/change-evaluation-matrix.md")
- **project_complexity_path**: string - Path to project complexity rating file (OPTIONAL, default: "../olaf-templates/project-complexity-rating.md")

## User Interaction Protocol
You WILL use the Act protocol for this scoring operation as it follows objective criteria with minimal interpretation required.

## Prerequisites
You MUST verify the preceding workflow was completed:
1. You WILL validate expected outcomes from Workflow 0-1:
   - Change request summary file exists and is complete
   - Technical scope analysis file exists with modules, files, LOC estimates
   - Risk assessment file exists with all 4 risk dimensions evaluated
2. You WILL confirm access to evaluation matrix and project complexity files

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all three input artifact files from Workflow 0-1 exist and are readable
- Validate evaluation matrix file contains 5-dimension scoring criteria
- Check project complexity rating file for BIRD project classification
- Ensure all evidence sources are available for justification

### 2. Execution Phase

#### Step 2.1: Load Evaluation Matrix Structure
You WILL read the change evaluation matrix file to understand:
- **5 Dimensions**: Each scored 0-5 points for total of 25 points maximum
- **Size Mapping**: XS (0-5), S (6-10), M (11-15), L (16-20), XL (21-25)
- **Scoring Criteria**: Specific point thresholds for each dimension

#### Step 2.2: Score Dimension 1 - Scope & Scale (0-5 points)
You WILL apply these criteria from the evaluation matrix:
- **0 points**: Single file, <50 LOC
- **1 point**: 1-5 files, <500 LOC
- **2 points**: 5-15 files, 500-2000 LOC
- **3 points**: 15-30 files, 2000-5000 LOC
- **4 points**: 30-50 files, 5000-10000 LOC
- **5 points**: >50 files, >10000 LOC

**Evidence Source**: Technical scope analysis - Files Affected and LOC Estimate sections
You MUST provide specific justification referencing exact evidence from the technical scope analysis.

#### Step 2.3: Score Dimension 2 - Technical Complexity (0-5 points)
You WILL apply these criteria from the evaluation matrix:
- **0 points**: Configuration change only, no code
- **1 point**: Simple code change, 1 module, no API changes
- **2 points**: Moderate code change, 2-3 modules, simple API changes
- **3 points**: Complex code change, 3-5 modules, API + DB changes
- **4 points**: Very complex, >5 modules, architecture changes
- **5 points**: System-wide refactoring, architectural redesign

**Evidence Source**: Technical scope analysis - Modules, API Changes, DB Changes, Architecture Impact sections
You MUST reference specific evidence from the technical scope analysis to justify the score.

#### Step 2.4: Score Dimension 3 - Risk Profile (0-5 points)
You WILL apply these criteria from the evaluation matrix:
- **0 points**: All risks Low
- **1 point**: Mostly Low risks, 1-2 Medium
- **2 points**: Mix of Low and Medium risks
- **3 points**: Mostly Medium risks, 1-2 High
- **4 points**: Multiple High risks
- **5 points**: Critical risks, high-visibility, compliance concerns

**Evidence Source**: Risk assessment - Business, Technical, Security, Operational Risk Levels
You MUST reference specific risk levels from the risk assessment document.

#### Step 2.5: Score Dimension 4 - Dependencies & Integration (0-5 points)
You WILL apply these criteria from the evaluation matrix:
- **0 points**: No dependencies
- **1 point**: 1-2 internal dependencies, no external
- **2 points**: 3-5 internal dependencies, simple integrations
- **3 points**: 5-8 internal dependencies, 1-2 external systems
- **4 points**: >8 internal dependencies, multiple external systems
- **5 points**: Complex cross-system dependencies, external APIs, event-driven

**Evidence Source**: Technical scope analysis - Integration Points section
You MUST reference specific integration points from the technical scope analysis.

#### Step 2.6: Score Dimension 5 - Project Context (0-5 points)
You WILL apply these criteria from the evaluation matrix:
- **0 points**: Simple project, team expert, no constraints
- **1 point**: Simple project, team familiar, few constraints
- **2 points**: Moderate project, team capable, some constraints
- **3 points**: Complex project, team learning, multiple constraints
- **4 points**: Very complex project, team new, significant constraints
- **5 points**: Highly complex project, team unfamiliar, critical constraints

**Evidence Source**: Project complexity rating file (BIRD = Complex) and change request summary for constraints
You MUST reference the project complexity rating and any constraints identified.

#### Step 2.7: Calculate Total Score
You WILL calculate the total score by summing all 5 dimension scores:
**Total Score** = Dimension 1 + Dimension 2 + Dimension 3 + Dimension 4 + Dimension 5
**Range**: 0-25 points total

### 3. Validation Phase
You WILL validate the scoring results:
- Confirm all 5 dimensions have been scored with values 0-5
- Verify each score has clear justification with evidence quoted from input artifacts
- Ensure total score is calculated correctly
- Validate preliminary size classification aligns with score ranges

## Output Format
You WILL generate the output using the template structure from `../templates/template-size-evaluation-matrix.md`.

**Save Output**: Create file with timestamp: `4-size-evaluation-matrix-YYYYMMDD-HHmm.md`

## Output to USER
- Dimensions scored: [5/5 dimensions completed]
- Total matrix score: [X/25 points]
- Preliminary size classification: [XS/S/M/L/XL based on score]
- Evidence quality: [All scores justified with specific evidence]
- Next step: Proceeding to size calculation and confidence assessment

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER assign scores without specific evidence from the input artifacts
- Rule 2: ALWAYS quote exact text from evidence sources to justify scores
- Rule 3: NEVER round scores or use partial points - use whole numbers 0-5 only
- Rule 4: ALWAYS calculate total score mathematically - no estimation
- Rule 5: NEVER skip any of the 5 dimensions - all must be scored
- Rule 6: ALWAYS reference the project complexity rating for Dimension 5
- Rule 7: NEVER interpret evidence beyond what is explicitly stated in the artifacts

## Success Criteria
You WILL consider the task complete when:
- [ ] All 5 dimensions scored with values 0-5 and clear justification
- [ ] Each score references specific evidence from input artifacts with quotes
- [ ] Total score calculated correctly (sum of all 5 dimensions)
- [ ] Preliminary size classification determined based on score ranges
- [ ] Output follows template structure exactly
- [ ] File saved with proper timestamp naming convention

## Required Actions
1. Load and validate all input artifacts from Workflow 0-1
2. Read evaluation matrix criteria for accurate scoring
3. Score each dimension systematically with evidence-based justification
4. Calculate total score and determine preliminary size classification
5. Generate structured output following template format

## Error Handling
You WILL handle these scenarios:
- **Input Artifact Missing**: Stop execution and request the missing file path
- **Evidence Insufficient**: Request clarification or additional analysis before scoring
- **Evaluation Matrix Inaccessible**: Request alternative matrix file or manual criteria
- **Score Calculation Error**: Recalculate and verify mathematical accuracy
- **Template Format Issues**: Follow standard markdown structure if template unavailable

**Critical Requirements**
- MANDATORY: All scores MUST be justified with specific evidence from input artifacts
- MANDATORY: Total score MUST be mathematically correct sum of all 5 dimensions
- NEVER assign scores based on assumptions or general knowledge
- ALWAYS reference exact text from evidence sources in justifications
- ALWAYS use the objective criteria from the evaluation matrix exactly as written