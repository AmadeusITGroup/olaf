# Accessibility Review Findings Report

**Project**: [project_name]  
**Review Date**: [YYYYMMDD-HHmm]  
**Standard**: WCAG [accessibility_standard]  
**Compliance Level**: [compliance_level]

## Executive Summary
- Total Violations: [count]
- Critical Issues: [count]
- Files Analyzed: [count]
- Compliance Score: [percentage]

## Actionable Issues

### Issue [#]: [Brief Description]
- **File**: `[filepath]:[line_number]`
- **WCAG Principle**: [Perceivable|Operable|Understandable|Robust]
- **Severity**: [Critical|High|Medium|Low]
- **Current Code**:
```language
[exact problematic code]
```
- **Corrected Code**:
```language
[exact corrected code]
```
- **Explanation**: [why this fixes the issue]

[Repeat for each issue found]

## Automated Testing Commands
- `pa11y [specific commands for this project]`
- `axe-core [specific commands for this project]`

## Next Steps
1. Apply the corrected code for each issue
2. Run the automated testing commands to verify fixes
3. Re-run accessibility review to confirm compliance
4. Integrate accessibility testing into CI/CD pipeline
