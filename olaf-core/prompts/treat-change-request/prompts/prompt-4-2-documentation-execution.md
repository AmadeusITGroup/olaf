---
name: convert-documentation-execution
description: Convert the Documentation Execution prompt to standardized template, preserving code-first documentation generation and validation
tags: [prompt, conversion, documentation, execution]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **doc_plan_path**: path - `DOCUMENTATION_PLAN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **design_path**: path - `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Implemented codebase location (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and documentation execution

## Process

### 1. Validation Phase
- Confirm all inputs exist
- Verify access to implemented codebase

### 2. Execution Phase
**Core Logic**:
- Perform code-first analysis (classes, APIs, workflows, config)
- Map implemented features to requirements; generate user journeys and examples
- Produce user guides, API reference, install guide, developer guide, operations manual per plan

### 3. Validation Phase
- Verify examples and procedures run against actual system
- Ensure accuracy, completeness, and usability standards

## Output Format
- Documentation files set as defined in `../templates/template-documentation-plan.md`

## User Communication
- Progress: artifact generation status
- Completion: docs created and validated against implementation

## Domain-Specific Rules
- Rule 1: All examples MUST be runnable or based on real outputs
- Rule 2: Align content with stakeholder knowledge levels

## Success Criteria
- [ ] Docs reflect actual implementation
- [ ] All required doc types generated
- [ ] Validation checks passed

## Error Handling
- **Environment/Access Issues**: Provide troubleshooting and request paths
- **Outdated Content**: Update or mark TODO with rationale

⚠️ **Critical Requirements**
- MANDATORY: Code-aligned documentation
- NEVER include speculative examples
