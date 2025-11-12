---
name: review-prd-spec
description: Review evolution requests/PRDs for completeness, query user with improvement questions, and save in standardized template format
tags: [prd, review, specification, evolution-request]
---
CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **prd_content**: string - The evolution request/PRD content to review (REQUIRED)
- **project_name**: string - Name of the project/feature being evolved (REQUIRED)
- **review_depth**: string|basic,comprehensive,detailed - Level of review depth (OPTIONAL, default: comprehensive)
- **save_format**: boolean - Whether to save the reviewed document in template format (OPTIONAL, default: true)
- **template_type**: string|standard,agile,enterprise - PRD template format to use (OPTIONAL, default: standard)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for document review and improvement suggestions
- You WILL use Propose-Confirm-Act protocol for saving the final formatted document

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm PRD content is provided and readable
- Validate project name follows naming conventions
- Check access to PRD template files in `[id:templates_dir]/business-analyst/`
- Verify review depth parameter is valid

### 2. Execution Phase

<!-- <content_analysis> -->
**Content Analysis**: You WILL analyze the provided PRD content for:
- Business objectives and success metrics
- User stories and acceptance criteria
- Technical requirements and constraints
- Risk assessment and mitigation strategies
- Timeline and resource requirements
- Stakeholder identification and responsibilities
<!-- </content_analysis> -->

<!-- <completeness_review> -->
**Completeness Review**: You WILL evaluate each section against standard PRD requirements:
- Executive Summary: Clear problem statement and solution overview
- Business Case: Value proposition, ROI, and strategic alignment
- User Requirements: Personas, user journeys, and functional requirements
- Technical Specifications: Architecture, integrations, and performance requirements
- Implementation Plan: Phases, milestones, and dependencies
- Success Criteria: Measurable outcomes and KPIs
- Risk Management: Identified risks and mitigation plans
<!-- </completeness_review> -->

<!-- <gap_identification> -->
**Gap Identification**: You WILL identify missing or incomplete sections:
- Create prioritized list of gaps (Critical, Important, Nice-to-have)
- Generate specific questions to address each gap
- Provide examples of what complete sections should contain
- Suggest industry best practices for missing elements
<!-- </gap_identification> -->

<!-- <user_interaction> -->
**User Interaction**: You WILL engage with user to improve the document:
- Present findings using Propose-Act protocol
- Ask targeted questions to fill identified gaps
- Request clarification on ambiguous requirements
- Validate user responses and iterate as needed
<!-- </user_interaction> -->

<!-- <document_formatting> -->
**Document Formatting**: You WILL format the improved document:
- Apply selected PRD template structure
- Ensure consistent formatting and style
- Add proper section numbering and cross-references
- Include timestamp and version information
- Generate table of contents and appendices
<!-- </document_formatting> -->

### 3. Validation Phase
You WILL validate the final document:
- Confirm all critical gaps have been addressed
- Verify document follows template structure completely
- Check for internal consistency and clarity
- Validate that success criteria are measurable

## Output Format
You WILL generate outputs following this structure:
- **Review Summary**: Completeness assessment with gap analysis
- **Improvement Questions**: Categorized questions to address gaps
- **Formatted PRD**: Complete document following template `[id:templates_dir]/business-analyst/prd-template-[template_type].md`
- **Quality Checklist**: Validation results against PRD standards

## User Communication

### Progress Updates
- Confirmation when content analysis is complete
- Summary of identified gaps and their priority levels
- Status updates during user interaction phase
- Confirmation when document formatting is complete

### Completion Summary
- Total number of gaps identified and addressed
- Quality score improvement (before/after analysis)
- Final document location: `[id:product_docs_dir]/[project_name]-prd-[timestamp].md`
- Template compliance verification results

### Next Steps
You WILL clearly define:
- Document ready for stakeholder review
- Recommended next actions (approval process, technical review, etc.)
- Files created with full paths and access instructions
- Follow-up review schedule recommendations

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER approve incomplete PRDs - all critical gaps must be addressed
- Rule 2: Questions MUST be specific and actionable, not generic
- Rule 3: Template formatting MUST be applied consistently throughout document
- Rule 4: Success criteria MUST be measurable and time-bound
- Rule 5: Risk assessment MUST include both technical and business risks
- Rule 6: User stories MUST follow standard format (As a... I want... So that...)
- Rule 7: Document MUST include version control and change tracking information

## Success Criteria
You WILL consider the task complete when:
- [ ] PRD content thoroughly analyzed for completeness
- [ ] All critical gaps identified and prioritized
- [ ] User interaction completed with all questions answered
- [ ] Document formatted according to selected template
- [ ] Quality validation confirms 95%+ template compliance
- [ ] Final document saved with proper naming convention
- [ ] User approval obtained for final formatted version
- [ ] Next steps clearly defined and communicated

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute comprehensive content analysis and gap identification
3. Engage user with targeted improvement questions
4. Format document according to template standards
5. Validate final output quality and completeness

## Error Handling
You WILL handle these scenarios:
- **Incomplete PRD Content**: Request specific missing sections with examples
- **Unclear Project Requirements**: Ask clarifying questions before proceeding
- **Template Access Issues**: Provide manual template structure and formatting guidance
- **User Non-Response**: Provide default recommendations and flag areas needing attention
- **Formatting Failures**: Offer alternative formats and manual formatting instructions
- **Validation Failures**: Identify specific issues and provide correction guidance
- **Save Location Issues**: Suggest alternative save locations and naming conventions

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for review findings and Propose-Confirm-Act for final document
- MANDATORY: All critical gaps MUST be addressed before document completion
- NEVER skip gap analysis - incomplete PRDs lead to project failures
- NEVER use generic questions - all inquiries must be specific to the content
- ALWAYS ensure success criteria are measurable and achievable
- ALWAYS include risk assessment in final document
- ALWAYS validate template compliance before considering task complete
