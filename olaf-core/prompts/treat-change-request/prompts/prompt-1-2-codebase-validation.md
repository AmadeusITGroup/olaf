## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
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
- **specification_document**: string - Path to initial specification document (REQUIRED)
- **codebase_access**: string - Path or access method to complete codebase (REQUIRED)
- **architectural_docs**: string - Path to existing architectural documentation (OPTIONAL)
- **project_id**: string - Project identifier for output naming (REQUIRED)
- **validation_depth**: string - Level of validation detail: "standard" or "comprehensive" (OPTIONAL, default: "standard")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for codebase validation due to moderate impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm specification document exists and is accessible
- Verify codebase access is available and complete
- Check architectural documentation availability
- Validate project identifier format
- Confirm validation depth requirements

### 2. Execution Phase

**Deep Feasibility Assessment:**
<!-- <feasibility_analysis> -->
You MUST analyze existing codebase to validate specification feasibility with EVIDENCE-BASED assessment:
- You WILL examine current architecture patterns and constraints
- You MUST identify technical dependencies and integration points
- You WILL assess data flow and storage requirements compatibility
- You MUST evaluate security and authentication framework alignment
- You WILL analyze performance and scalability implications
- You MUST check third-party service integration feasibility
<!-- </feasibility_analysis> -->

**Technical Constraint Analysis:**
<!-- <constraint_analysis> -->
You MUST identify and document technical constraints:
- You WILL catalog existing technology stack limitations
- You MUST assess framework and library compatibility
- You WILL evaluate database schema modification requirements
- You MUST analyze API contract and interface constraints
- You WILL identify deployment and infrastructure limitations
- You MUST assess testing framework and coverage requirements
<!-- </constraint_analysis> -->

**Implementation Reality Check:**
<!-- <implementation_analysis> -->
You WILL conduct comprehensive implementation assessment:
- You MUST validate each specification requirement against codebase reality
- You WILL identify requirements that need modification or clarification
- You MUST assess development effort and complexity for each feature
- You WILL flag potential breaking changes or backward compatibility issues
- You MUST evaluate resource and timeline implications
- You WILL provide alternative approaches for infeasible requirements
<!-- </implementation_analysis> -->

**Specification Refinement:**
<!-- <specification_refinement> -->
You MUST produce refined specification following validation:
- You WILL maintain original requirement intent while ensuring feasibility
- You MUST document all modifications with technical justification
- You WILL provide implementation recommendations and best practices
- You MUST include risk assessment for each requirement
- You WILL specify testing and validation approaches
- You MUST ensure compliance with existing architectural standards
<!-- </specification_refinement> -->

### 3. Validation Phase
You WILL validate the refined specification meets all requirements:
- Confirms technical feasibility within existing codebase constraints
- Documents all constraint-driven modifications with justification
- Includes comprehensive risk assessment and mitigation strategies
- Provides clear implementation guidance and recommendations
- Maintains original business intent while ensuring technical reality
- Contains measurable acceptance criteria for each requirement

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Refined specification document with validation results
- Feasibility assessment report with evidence-based conclusions
- Technical constraint documentation with impact analysis
- Implementation roadmap with effort estimates and risk factors
- File naming: `SPECIFICATION_VALIDATED_<PROJECT-ID>_<timestamp>.md`

## User Communication

### Progress Updates
- Confirmation when specification document is successfully loaded
- Status of codebase analysis and constraint identification
- Progress on feasibility assessment for each requirement
- Validation results and modification recommendations

### Completion Summary
- Refined specification presented for review via Propose-Act
- Summary of all modifications made with technical justification
- Risk assessment results with mitigation recommendations
- Implementation roadmap with effort and timeline estimates

### Next Steps
You WILL clearly define:
- Refined specification ready for design phase (pending user approval)
- Technical constraints documented for development team
- Risk mitigation strategies identified and prioritized
- Implementation recommendations ready for technical review

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify requirements without technical justification
- Rule 2: ALL feasibility assessments MUST be evidence-based from codebase analysis
- Rule 3: Refined specification MUST preserve original business intent
- Rule 4: ALL technical constraints MUST be documented with impact analysis
- Rule 5: Implementation recommendations MUST be specific and actionable
- Rule 6: Risk assessments MUST include probability and impact ratings
- Rule 7: Alternative approaches MUST be provided for infeasible requirements
- Rule 8: Validation results MUST be measurable and testable

## Success Criteria
You WILL consider the task complete when:
- [ ] Specification document successfully analyzed and understood
- [ ] Complete codebase assessment conducted with evidence gathering
- [ ] All technical constraints identified and documented
- [ ] Feasibility validation completed for every requirement
- [ ] Refined specification produced maintaining business intent
- [ ] Risk assessment completed with mitigation strategies
- [ ] Implementation roadmap created with effort estimates
- [ ] User approval obtained via Propose-Act protocol

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute codebase analysis following appropriate interaction protocol
3. Generate refined specification in specified format
4. Provide comprehensive validation documentation
5. Define next steps for design phase transition

## Error Handling
You WILL handle these scenarios:
- **Specification Document Access Failed**: Provide clear error message and request valid document path
- **Codebase Access Denied or Incomplete**: Request alternative access methods or partial analysis scope
- **Architectural Documentation Missing**: Proceed with code-only analysis and document assumptions
- **Invalid Project Identifier**: Request properly formatted project ID following conventions
- **Infeasible Requirements Identified**: Provide alternative approaches and modification recommendations
- **Technical Constraint Conflicts**: Prioritize constraints and provide resolution strategies
- **Validation Depth Specification Unclear**: Default to standard validation and confirm scope
- **User Rejection During Propose-Act**: Request specific feedback and iterate refinement

WARNING **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for specification modifications
- MANDATORY: All feasibility assessments MUST be evidence-based from actual codebase analysis
- NEVER modify requirements without clear technical justification
- NEVER sacrifice business intent for technical convenience
- ALWAYS preserve requirement traceability through refinement process
- ALWAYS provide alternative approaches for infeasible requirements
- ALWAYS validate refined specifications maintain original business value
- NEVER proceed without user approval for significant requirement modifications