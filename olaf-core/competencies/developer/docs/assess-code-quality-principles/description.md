# Assess Code Quality Principles

**Source**: olaf-core/competencies/developer/prompts/assess-code-quality-principles.md

## Overview

Critical evaluation of codebase against established engineering principles (SOLID, DRY, YAGNI) with evidence-based scoring and specific improvement recommendations. Provides comprehensive quality scorecard with actionable insights.

## Purpose

Software projects often accumulate technical debt and quality issues over time. This competency provides systematic evaluation of code quality against industry-standard principles, helping teams identify areas for improvement, prioritize refactoring efforts, and maintain high code quality standards. It transforms subjective code reviews into objective, measurable assessments.

## Usage

**Command**: `assess quality`

**Protocol**: Propose-Act

**When to Use**: 
- Before major refactoring initiatives to establish baseline
- During technical debt assessment and planning
- For code quality audits and compliance reviews
- When onboarding to understand codebase quality
- To validate architecture and design decisions

## Parameters

### Required Inputs
- **application_name**: Name of the application for file naming (kebab-case format)
- **code_path**: Path to the codebase directory to assess

### Optional Inputs
- **tech_spec_path**: Path to existing technical specification for context
- **focus_areas**: Specific areas to focus assessment on (defaults to all categories)

### Context Requirements
- Access to complete codebase source files
- Ability to analyze file structure and dependencies
- Optional: existing technical documentation for context

## Output

Comprehensive quality assessment report with evidence-based scoring across multiple dimensions.

**Deliverables**:
- Quality scorecard with overall and category-specific grades (A-F scale)
- Detailed findings with specific code examples
- Prioritized improvement recommendations with effort estimates
- Metrics and measurements for each assessment category

**Format**: Markdown document saved to `[id:findings_dir]assessments/code-quality-assessment-{application_name}-YYYYMMDD-NNN.md`

## Examples

### Example 1: Full Codebase Assessment

**Scenario**: Evaluating overall code quality before major refactoring

**Command**:
```
assess quality
```

**Input**:
- application_name: "payment-service"
- code_path: "./src"

**Result**: Complete assessment report with grades for SOLID principles (B), Code Quality (C), Testing (D), Architecture (B), Security (B), and Performance (C), including 15 prioritized recommendations

### Example 2: Focused SOLID Assessment

**Scenario**: Evaluating design principles compliance

**Command**:
```
assess quality
```

**Input**:
- application_name: "user-management"
- code_path: "./src"
- focus_areas: ["SOLID Principles", "Architecture Quality"]

**Result**: Targeted assessment focusing on design principles and architecture with detailed violation examples and refactoring suggestions

## Related Competencies

- **review-code**: Use for detailed code review after identifying quality issues
- **fix-code-smells**: Apply to address specific code smells identified in assessment
- **improve-cyclomatic-complexity**: Use to reduce complexity issues found
- **augment-code-unit-test**: Apply to improve test coverage gaps identified
- **generate-tech-spec-from-code**: Create specification to document current architecture

## Tips & Best Practices

- Run assessment before planning major refactoring to establish baseline metrics
- Focus on high-impact, low-effort improvements first for quick wins
- Use assessment results to guide technical debt prioritization
- Re-run periodically to track quality improvements over time
- Share scorecard with team to build consensus on quality goals
- Combine with tech spec analysis for comprehensive understanding

## Limitations

- Assessment quality depends on codebase accessibility and completeness
- Some metrics require static analysis tools for precise calculation
- Subjective elements in grading despite evidence-based approach
- May not capture runtime behavior or performance issues
- Requires understanding of assessed principles for interpretation
