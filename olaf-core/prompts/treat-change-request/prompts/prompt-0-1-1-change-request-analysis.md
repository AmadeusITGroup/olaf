---
name: convert-change-request-analysis
description: Convert the Change Request Analysis prompt to enforce standardized template, protocols, and validations while preserving intent
tags: [prompt, conversion, change-request, analysis]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **source_document_ref**: string - JIRA ID (e.g., SACP-172207) or path to requirement/issue content (REQUIRED)
- **access_methods**: string[] - Allowed access methods (e.g., direct JIRA/Issue content, markdown file, business doc) (OPTIONAL)
- **output_dir**: path - Target output directory for generated summary (OPTIONAL, default: `olaf-works/demand/<DEMAND-ID>-analysis/`)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and output generation steps

## Prerequisites (if applicable)
1. You MUST verify whether a prerequisite change request already exists:
   - Check for file: `olaf-works/demand/<DEMAND-ID>-analysis/prerequisite-3-change-request.md`
2. You WILL validate expected contents of the prerequisite file:
   - Epic, Features, MVP Scope, Open Questions

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `source_document_ref` is provided
- Validate prerequisite file existence and completeness
- Check access to any referenced templates

### 2. Execution Phase
You WILL execute these operations as needed:

**File Operations**:
- Read prerequisite file if it exists to validate completeness
- If prerequisite file is COMPLETE:
  - You WILL SKIP creating `1-change-request-summary.md`
  - You WILL log validation that prerequisite is complete
  - You WILL proceed directly to technical scope analysis (see Next Steps)
- If prerequisite file is MISSING or INCOMPLETE:
  - You MUST STOP and return an error instructing to run the prerequisite phase

**Core Logic**:
- Apply Propose-Act protocol
- Enforce non-duplication of change request content when prerequisites are complete

### 3. Validation Phase
You WILL validate results:
- Confirm duplication was avoided when prerequisite exists and is complete
- Confirm proper error returned when prerequisites are missing/incomplete

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable:
  - If prerequisite exists and complete: Validation message confirming skip and next step
  - If prerequisite missing/incomplete: Clear error message and guidance to run prerequisites
- Documentation: Reference to next prompt `prompt-0-1-2-technical-scope-analysis.md`

## User Communication

### Progress Updates
- Confirmation when prerequisite file check completes
- Declaration of skip vs stop path

### Completion Summary
- Summary of validation outcome (skip or stop)
- Next prompt reference

### Next Steps (if part of workflow)
You WILL clearly define:
- If prerequisites complete: Proceed to `prompt-0-1-2-technical-scope-analysis.md`
- If not complete: Run `orchestrator-prerequisites.md` to generate prerequisite change request

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER duplicate change request content when prerequisites provide it
- Rule 2: ALWAYS validate Epic, Features, MVP, Open Questions before proceeding
- Rule 3: Use Propose-Act protocol for user confirmation

## Success Criteria
You WILL consider the task complete when:
- [ ] Prerequisite file existence and completeness validated
- [ ] Duplication avoided when prerequisites are complete
- [ ] Clear stop/error issued when prerequisites are missing/incomplete
- [ ] Next prompt guidance provided

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following Propose-Act protocol
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Prerequisite File Missing**: Stop and instruct to run prerequisites
- **Prerequisite Incomplete**: Stop and instruct to complete prerequisites
- **Source Access Issues**: Request a valid `source_document_ref`

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol
- NEVER recreate `1-change-request-summary.md` when prerequisites are complete
- ALWAYS preserve original intent: avoid duplication, route to technical scope analysis
