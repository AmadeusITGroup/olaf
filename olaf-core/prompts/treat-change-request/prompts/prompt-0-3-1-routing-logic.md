---
name: route-change-request-to-orchestrator
description: Determine the correct size-specific orchestrator and prepare the machine-readable context package for handoff
tags: [routing, orchestrator, context-package, change-request]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
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
- artifacts_path: string - Path to directory containing artifacts 1-5 from workflows 0-1 and 0-2 (REQUIRED)
- orchestrators_path: string - Path to orchestrators directory (REQUIRED, default: "../orchestrators/")
- output_path: string - Path for generated context package YAML file (OPTIONAL, default: "6-context-package.yaml")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for routine routing operations with clear validation

## Prerequisites (if applicable)
You MUST verify these prerequisites before execution:
- All artifacts 1-5 exist and are accessible in the specified artifacts path
- Final size classification exists in 5-final-size-decision.md
- Orchestrators directory exists and contains size-specific orchestrator files
- Write access to output directory for context package generation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all artifacts 1-5 exist and are readable
- Validate 5-final-size-decision.md contains required size classification
- Check orchestrators directory accessibility
- Verify write permissions for output file generation

You MUST read and validate these required artifacts:
- 1-change-request-summary.md - Business context and requirements
- 2-technical-scope-analysis.md - Technical analysis and scope metrics
- 3-risk-assessment.md - Risk profile and assessment details
- 4-size-evaluation-matrix.md - Sizing matrix scores and breakdown
- 5-final-size-decision.md - Final size classification and confidence

### 2. Execution Phase

Size Classification Extraction:
You MUST extract from 5-final-size-decision.md:
- Size Classification: [XS / S / M / L / XL]
- Confidence Score: [XX%]
- Effort Estimate: [XX-YY person-days]
You WILL validate that all required fields are present and properly formatted

Orchestrator Selection:
You MUST use this routing decision table to select the correct orchestrator:

| Size | Orchestrator File | Effort Range | Characteristics |
|------|------------------|--------------|----------------|
| XS | orchestrator-XS-extra-small.md | 1-3 days | Single file/component, no API changes, low risk |
| S | orchestrator-S-small.md | 3-7 days | Few files, simple API changes, low-medium risk |
| M | orchestrator-M-medium.md | 7-15 days | Multiple modules, moderate complexity, medium risk |
| L | orchestrator-L-large.md | 15-30 days | Cross-module changes, architecture impact, medium-high risk |
| XL | orchestrator-XL-extra-large.md | 30+ days | System-wide changes, major refactoring, high risk |

You WILL verify the selected orchestrator file exists in the orchestrators directory
You MUST report an error if the orchestrator file is missing

Context Package Generation:
You MUST gather all essential information from artifacts 1-5:

Change Request Information:
- Change Request ID (from 1-change-request-summary.md)
- Change Title/Description
- Requestor and Stakeholders
- Priority and Due Date

Size Classification:
- Size: [XS/S/M/L/XL]
- Confidence: [XX%]
- Total Matrix Score: [XX/25]

Scope Metrics:
- Estimated Effort: [XX-YY days]
- Files Affected: [XX-YY]
- Modules Affected: [X]
- Estimated LOC: [X,XXX-Y,YYY]

Risk Summary:
- Business Risk: [H/M/L]
- Technical Risk: [H/M/L]
- Security Risk: [H/M/L]
- Operational Risk: [H/M/L]

Dependencies:
- Internal Integrations: [list]
- External Integrations: [list]

YAML Generation:
You MUST create the machine-readable handoff package using this exact structure:

change_request:
  id: "[EXTRACTED_ID]"
  title: "[EXTRACTED_TITLE]"
  requestor: "[EXTRACTED_REQUESTOR]"
  priority: "[EXTRACTED_PRIORITY]"
  due_date: "[EXTRACTED_DATE]"

sizing:
  classification: "[EXTRACTED_SIZE]"
  confidence_score: [EXTRACTED_CONFIDENCE]
  matrix_score: [EXTRACTED_MATRIX_SCORE]
  effort_estimate:
    min_days: [EXTRACTED_MIN_DAYS]
    max_days: [EXTRACTED_MAX_DAYS]

routing:
  target_orchestrator: "[SELECTED_ORCHESTRATOR_FILE]"
  routing_timestamp: "[CURRENT_TIMESTAMP_ISO]"
  routed_by: "route-change-request-to-orchestrator"
  workflow_version: "2.0"

### 3. Validation Phase
You WILL validate the generated context package meets all requirements:
- All required fields populated with actual data from artifacts
- YAML syntax is valid and properly formatted
- Selected orchestrator file exists and is accessible
- All artifacts are properly referenced
- Risk profile is complete and accurate
- Dependencies are comprehensively listed
- Handoff instructions are specific and actionable

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete context package YAML file saved as 6-context-package.yaml
- Routing summary: Selected orchestrator and confidence metrics
- Validation report: Confirmation of all data extraction and file generation
- Handoff status: Ready for next workflow step with target orchestrator

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Artifacts validation completed successfully
- Size classification extracted: [SIZE] with [XX%] confidence
- Target orchestrator selected: [ORCHESTRATOR_FILE]
- Context package YAML generated and validated
- All data fields populated from source artifacts

### Completion Summary
You WILL provide this completion information:
- Routing Decision: [SIZE] to [ORCHESTRATOR_FILE]
- Confidence Level: [XX%] based on [XX/25] matrix score
- Context Package: Generated as 6-context-package.yaml
- Next Step: Proceed to selected orchestrator workflow
- Handoff Ready: All required information packaged for target orchestrator

### Next Steps
You WILL clearly define:
- Context package ready for handoff to selected orchestrator
- Target orchestrator file: [ORCHESTRATOR_FILE]
- All artifacts and metrics successfully packaged
- Workflow ready to proceed to specification phase

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed without validating all 5 required artifacts exist
- Rule 2: NEVER select an orchestrator without confirming the file exists
- Rule 3: NEVER generate incomplete YAML - all fields MUST be populated
- Rule 4: NEVER use placeholder values - extract actual data from artifacts
- Rule 5: NEVER proceed if size classification is missing or invalid
- Rule 6: Context package MUST include all artifacts as references
- Rule 7: Risk profile MUST be complete with all four risk dimensions
- Rule 8: Dependencies MUST be extracted from technical scope analysis

## Success Criteria
You WILL consider the task complete when:
- All 5 artifacts successfully read and validated
- Size classification extracted from artifact 5
- Target orchestrator selected using routing table
- Orchestrator file existence confirmed
- Context package YAML generated with all fields populated
- YAML syntax validated as correct
- All artifacts properly referenced in package
- Risk profile completely extracted and summarized
- Dependencies comprehensively listed
- Handoff instructions are specific and actionable
- Output file 6-context-package.yaml created successfully
- Routing decision documented and ready for next workflow step

## Error Handling
You WILL handle these scenarios:
- Missing Artifacts: Report specific missing files and request artifact generation
- Invalid Size Classification: Report format issues and request artifact correction
- Missing Orchestrator File: Report missing orchestrator and request file creation
- YAML Generation Failure: Provide specific syntax errors and correction guidance
- Incomplete Data Extraction: Report missing fields and source artifact issues
- File Write Permissions: Provide alternative output methods and troubleshooting
- Invalid Risk Assessment: Request risk assessment completion or correction
- Missing Dependencies: Report incomplete technical analysis and request updates

Critical Requirements
- MANDATORY: All 5 artifacts MUST be validated before processing
- MANDATORY: Size classification MUST be valid (XS/S/M/L/XL) with confidence score
- MANDATORY: Selected orchestrator file MUST exist in orchestrators directory
- MANDATORY: Context package YAML MUST contain all required fields populated with real data
- NEVER generate context package with placeholder or missing values
- NEVER proceed to orchestrator selection without confirmed size classification
- ALWAYS validate YAML syntax before declaring completion
- ALWAYS extract actual data from artifacts rather than using template examples