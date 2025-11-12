# Analyze Business Requirements

## Overview

This competency systematically reviews business requirements documents to identify potential issues, ambiguities, and gaps. It generates constructive clarifying questions and produces a comprehensive analysis report that helps improve requirements quality before development begins.

## Purpose

Business requirements documents often contain ambiguous language, incomplete specifications, or untestable criteria that lead to costly rework during development. This competency addresses this by applying established best practices to identify issues early, categorize them by severity, and generate actionable questions that guide stakeholders toward clearer, more complete requirements.

## Usage

**Command**: `analyze business requirements`

**Protocol**: Propose-Act

**When to Use**: Use this competency when you have a business requirements document that needs validation before development, when stakeholders need feedback on requirements quality, or when preparing requirements for technical review with development and testing teams.

## Parameters

### Required Inputs
- **requirements_document**: Path to the business requirements document to analyze (markdown format)

### Optional Inputs
- **strict_template_compliance**: Boolean flag to enforce strict template format adherence (default: true)

### Context Requirements
- Business requirements document should be accessible in the workspace
- Best practice guides are automatically loaded from olaf-data/practices/
- Analysis report template is automatically referenced from competency templates

## Output

This competency produces a structured analysis report that identifies and categorizes requirements issues.

**Deliverables**:
- Requirements analysis report saved to `olaf-data/findings/business-requirements-analysis-YYYYMMDD-NNN.md`
- Markdown-formatted report displayed to user

**Format**: Structured markdown document following the requirements-analysis-report-template with sections for issue categorization, severity assessment, clarifying questions, and actionable recommendations.

## Examples

### Example 1: Pre-Development Requirements Review

**Scenario**: A product manager has drafted requirements for a new user authentication feature and needs validation before sharing with the development team.

**Command**:
```
olaf analyze business requirements
```

**Input**:
```
requirements_document: olaf-data/product/auth-requirements-v1.md
```

**Result**: Generated analysis report identifying 8 ambiguous requirements, 3 incomplete specifications, and 5 untestable criteria, with specific clarifying questions for each issue. Report saved to findings directory with timestamp.

### Example 2: Stakeholder Requirements Validation

**Scenario**: Business stakeholders have provided requirements for a reporting dashboard, but the document lacks measurable acceptance criteria.

**Command**:
```
olaf analyze business requirements
```

**Result**: Analysis report highlighting missing testability criteria, inconsistent terminology usage, and gaps in error handling specifications. Includes prioritized recommendations for improvement.

## Related Competencies

- **improve-spec**: Use after addressing analysis findings to enhance the specification with diagrams and detailed data definitions
- **extend-specification**: Complements this by adding missing technical details once core requirements are validated
- **review-user-story**: Use for validating individual user stories derived from the analyzed requirements
- **generate-questionnaire**: Use to gather additional information from stakeholders for incomplete requirements

## Tips & Best Practices

- Run this analysis early in the requirements gathering phase to catch issues before they propagate
- Review the generated clarifying questions with stakeholders in a collaborative session rather than sending them via email
- Use the categorized findings to prioritize which requirements need immediate attention
- Reference the best practice guides (expressing-business-needs-to-developers.md) to understand the analysis criteria
- Save multiple analysis iterations to track requirements quality improvement over time

## Limitations

- Analysis quality depends on the clarity and completeness of the input document structure
- Cannot validate business logic correctness or feasibility—focuses on requirements quality and clarity
- Requires human judgment to determine which identified issues are critical vs. acceptable trade-offs
- Does not replace stakeholder collaboration—use findings as conversation starters, not final judgments

---

**Source**: `olaf-core/competencies/business-analyst/prompts/analyze-business-requirements.md`
