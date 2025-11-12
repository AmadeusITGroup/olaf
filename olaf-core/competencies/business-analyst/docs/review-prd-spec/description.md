# Review PRD Spec

## Overview

This competency performs comprehensive reviews of Product Requirements Documents (PRDs) and evolution requests to ensure completeness, identify gaps, and format them according to standardized templates. It analyzes content systematically, generates targeted improvement questions, and produces professionally formatted PRD documents ready for stakeholder review.

## Purpose

PRDs often suffer from incomplete sections, missing success criteria, unclear requirements, or inconsistent formatting that lead to misaligned expectations and project delays. This competency addresses these issues by conducting thorough gap analysis, engaging users with specific improvement questions, and applying standardized templates to ensure all critical PRD elements are present and properly documented before stakeholder approval.

## Usage

**Command**: `review prd spec`

**Protocol**: Propose-Act (for review findings), Propose-Confirm-Act (for final document save)

**When to Use**: Use this competency when you have a draft PRD or evolution request that needs validation before stakeholder review, when preparing requirements for technical team handoff, or when standardizing PRD format across your organization.

## Parameters

### Required Inputs
- **prd_content**: The evolution request/PRD content to review (string or file path)
- **project_name**: Name of the project/feature being evolved

### Optional Inputs
- **review_depth**: Level of review depth - basic, comprehensive, or detailed (default: comprehensive)
- **save_format**: Whether to save the reviewed document in template format (default: true)
- **template_type**: PRD template format to use - standard, agile, or enterprise (default: standard)

### Context Requirements
- Access to PRD template files in templates directory
- Current timestamp for document versioning
- Product documentation directory for saving formatted output

## Output

This competency produces a comprehensive review analysis and a professionally formatted PRD document.

**Deliverables**:
- Review summary with completeness assessment and gap analysis
- Categorized improvement questions (Critical, Important, Nice-to-have)
- Formatted PRD document following selected template: `[product_docs_dir]/[project_name]-prd-[timestamp].md`
- Quality checklist with validation results

**Format**: Structured markdown documents following PRD template standards with proper section numbering, table of contents, and version control information.

## Examples

### Example 1: Pre-Stakeholder Review Validation

**Scenario**: A product manager has drafted a PRD for a new customer portal feature and needs to ensure all critical sections are complete before presenting to executives.

**Command**:
```
olaf review prd spec
```

**Input**:
```
prd_content: [path to draft PRD]
project_name: customer-portal-v2
review_depth: comprehensive
```

**Result**: Identified 5 critical gaps (missing success metrics, incomplete risk assessment), 8 important gaps (unclear technical constraints), generated 15 targeted questions, and produced formatted PRD with 95% template compliance.

### Example 2: Evolution Request Standardization

**Scenario**: Multiple teams submit evolution requests in different formats. Need to standardize a request for the approval process.

**Command**:
```
olaf review prd spec
```

**Input**:
```
prd_content: [evolution request content]
project_name: payment-integration-enhancement
template_type: enterprise
```

**Result**: Analyzed informal request, identified missing business case and ROI sections, engaged user to fill gaps, and produced enterprise-standard PRD document ready for governance review.

## Related Competencies

- **analyze-business-requirements**: Use this for detailed requirements validation after PRD review identifies requirement gaps
- **improve-spec**: Complements this by adding technical diagrams and detailed specifications to the reviewed PRD
- **extend-specification**: Use after PRD approval to add implementation-level technical details
- **generate-questionnaire**: Use to create structured stakeholder interviews for filling identified PRD gaps

## Tips & Best Practices

- Run this review before scheduling stakeholder approval meetings to avoid last-minute gaps
- Focus on critical gaps first—use the prioritized gap list to guide improvement efforts efficiently
- Engage subject matter experts for technical sections identified as incomplete
- Use the generated questions in collaborative sessions rather than as standalone surveys
- Save multiple review iterations to track PRD quality improvement over time
- Ensure success criteria are measurable and time-bound—this is the most commonly missed element
- Include both technical and business risks in the risk assessment section

## Limitations

- Cannot validate business viability or market fit—focuses on document completeness and structure
- Requires human judgment for strategic decisions and priority trade-offs
- Template compliance depends on availability of template files in the expected directory
- Does not replace stakeholder collaboration—use as a preparation tool, not a replacement for discussion
- Quality of improvement questions depends on clarity of the input PRD content

---

**Source**: `olaf-core/competencies/business-analyst/prompts/review-prd-spec.md`
