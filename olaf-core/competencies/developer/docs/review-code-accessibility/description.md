# Review Code Accessibility

**Source**: olaf-core/competencies/developer/prompts/review-code-accessibility.md

## Overview

Analyze code for WCAG 2.1 accessibility compliance and provide remediation guidance. Evaluates web code against accessibility standards with specific recommendations.

## Purpose

Accessibility compliance is essential for inclusive web applications but often overlooked during development. This competency systematically analyzes code against WCAG 2.1 guidelines, identifies violations, and provides specific remediation guidance with code examples. It helps teams build accessible applications that work for all users.

## Usage

**Command**: `accessibility review`

**Protocol**: Act

**When to Use**:
- During code review for web applications
- Before release to ensure accessibility compliance
- When addressing accessibility audit findings
- For accessibility-first development validation
- To educate team on accessibility best practices

## Parameters

### Required Inputs
- **code_files**: List of files to analyze for accessibility compliance
- **project_name**: Project name for findings report filename

### Optional Inputs
- **accessibility_standard**: WCAG version to validate against (default: "2.1")
- **compliance_level**: AA|AAA compliance level (default: "AA")
- **output_format**: report|checklist|recommendations (default: "report")

### Context Requirements
- Web-related code files (HTML, CSS, JavaScript, React, etc.)
- Optional: accessibility testing tools (pa11y, axe-core)
- Understanding of WCAG guidelines

## Output

Comprehensive accessibility compliance report with specific violations and remediation guidance.

**Deliverables**:
- Accessibility violations identified with line references
- WCAG 2.1 compliance assessment per principle
- Specific remediation code examples
- Compliance checklist
- Actionable findings report

**Format**: Markdown report saved to `[id:findings_dir]reports/[project_name]-accessibility-review-[YYYYMMDD-HHmm].md`

## Examples

### Example 1: React Component Accessibility Review

**Scenario**: Reviewing React components for WCAG AA compliance

**Command**:
```
accessibility review
```

**Input**:
- code_files: ["src/components/Button.tsx", "src/components/Form.tsx"]
- project_name: "web-app"
- compliance_level: "AA"

**Result**: Identified 8 violations including missing ARIA labels, insufficient color contrast, and keyboard navigation issues with specific fixes

### Example 2: Full Application Audit

**Scenario**: Pre-release accessibility audit

**Command**:
```
accessibility review
```

**Input**:
- code_files: ["src/**/*.tsx", "src/**/*.css"]
- project_name: "customer-portal"
- compliance_level: "AAA"
- output_format: "report"

**Result**: Comprehensive report with 23 findings across all WCAG principles, prioritized by severity with remediation examples

## Related Competencies

- **review-code**: Use for general code review including accessibility
- **fix-code-smells**: Apply to refactor accessibility issues
- **review-github-pr**: Include accessibility review in PR process

## Tips & Best Practices

- Review accessibility early in development cycle
- Use automated tools (pa11y, axe-core) for initial scan
- Test with screen readers for validation
- Focus on keyboard navigation and ARIA labels
- Ensure sufficient color contrast ratios
- Provide text alternatives for non-text content
- Make interactive elements keyboard accessible
- Test with assistive technologies
- Document accessibility patterns for team

## Limitations

- Automated analysis cannot catch all accessibility issues
- Requires manual testing with assistive technologies
- Some violations require user experience judgment
- Context-specific accessibility needs may not be detected
- Compliance level affects strictness of evaluation
