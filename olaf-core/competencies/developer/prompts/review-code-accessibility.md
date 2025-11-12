---

name: review-code-accessibility

description: Analyze code for WCAG 2.1 accessibility compliance and provide remediation guidance

tags: [accessibility, wcag, compliance, code-review]

---



## Framework Validation
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.- <olaf-interaction-protocols> - Appropriate execution protocol

You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **code_files**: string[] - List of files to analyze for accessibility compliance (REQUIRED)

- **project_name**: string - Project name for findings report filename (REQUIRED)

- **accessibility_standard**: string - WCAG version to validate against (OPTIONAL, default: "2.1")

- **compliance_level**: string - AA|AAA compliance level (OPTIONAL, default: "AA")

- **output_format**: string - report|checklist|recommendations (OPTIONAL, default: "report")



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- Use Act protocol for accessibility analysis due to assessment nature



## Process



### 1. Validation Phase

You WILL verify all requirements:

- Confirm all required code files are accessible

- Validate accessibility standard and compliance level parameters

- Check that files contain web-related code (HTML, CSS, JavaScript, React, etc.)

- Verify access to findings template: `[id:competencies_dir][competency]/templates/developer/accessibility-findings-report.md`



### 2. Execution Phase



**File Operations**:

- Read code files: Analyze provided files for accessibility patterns

- Process file content according to WCAG 2.1 guidelines

- Read findings template: `[id:competencies_dir][competency]/templates/developer/accessibility-findings-report.md`

- Create findings report: `[id:findings_dir]reports/[project_name]-accessibility-review-[YYYYMMDD-HHmm].md`



**Tool Operations**:

- Validate accessibility tools: `npm list pa11y axe-core` or equivalent package manager

- Execute automated testing: `pa11y [url]` and `axe-core` analysis commands



**Core Logic**: Execute following protocol requirements

- Apply Act protocol for direct accessibility assessment



<!-- <wcag_analysis> -->

- Analyze code against WCAG 2.1 four core principles:

  1. **Perceivable**: Check text alternatives, captions, content adaptability, color contrast

  2. **Operable**: Verify keyboard accessibility, timing, seizure prevention, navigation

  3. **Understandable**: Validate readability, predictability, error handling

  4. **Robust**: Ensure compatibility with assistive technologies

<!-- </wcag_analysis> -->



- Generate specific recommendations for violations found

- Provide code examples for remediation



### 3. Validation Phase

You WILL validate results:

- Confirm all accessibility issues are identified with specific line references

- Verify recommendations include actionable code examples

- Ensure compliance level requirements are properly assessed



## Output Format

You WILL generate outputs following this structure:

- **Primary deliverable**: Accessibility compliance report with violations and recommendations

- **Actionable findings report**: Machine-readable findings file saved to `[id:findings_dir]reports/[project_name]-accessibility-review-[YYYYMMDD-HHmm].md`

- **Code examples**: Specific remediation code snippets for each violation

- **Checklist**: Summary of WCAG 2.1 compliance status per principle



### Actionable Findings Report Generation

You MUST create the findings report using the template: `[id:competencies_dir][competency]/templates/developer/accessibility-findings-report.md`

You WILL populate all template placeholders with actual findings data for model consumption.



## User Communication



### Progress Updates

- Confirmation when files are successfully analyzed

- Summary of accessibility violations found per file

- Timestamp identifier used: [YYYYMMDD-HHmm format]

- Confirmation when findings report is saved to `[id:findings_dir]reports/`



### Completion Summary

- Total violations found categorized by WCAG principle

- Priority recommendations for critical accessibility barriers

- Code examples provided for top priority fixes

- Actionable findings report saved: `[id:findings_dir]reports/[project_name]-accessibility-review-[YYYYMMDD-HHmm].md`



### Next Steps

You WILL clearly define:

- Immediate accessibility fixes required for compliance

- Testing recommendations using pa11y and axe-core tools

- Integration guidance for accessibility testing in development workflow



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: All HTML elements MUST have proper semantic meaning and ARIA attributes when needed

- Rule 2: All images MUST have appropriate alt text or be marked as decorative

- Rule 3: Color contrast MUST meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)

- Rule 4: All interactive elements MUST be keyboard accessible with visible focus indicators

- Rule 5: Form elements MUST have associated labels or aria-label attributes

- Rule 6: Dynamic content MUST use ARIA live regions for screen reader announcements

- Rule 7: Page structure MUST use proper heading hierarchy (h1-h6)

- Rule 8: Skip links MUST be provided for keyboard navigation



## Success Criteria

You WILL consider the task complete when:

- [ ] All required code files successfully analyzed

- [ ] WCAG 2.1 compliance assessment completed for all four principles

- [ ] Specific violations identified with file and line references

- [ ] Actionable remediation recommendations provided

- [ ] Code examples generated for critical accessibility fixes

- [ ] Testing guidance provided (pa11y, axe-core integration)

- [ ] Priority assessment completed for identified violations

- [ ] **Actionable findings report saved** to `[id:findings_dir]reports/[project_name]-accessibility-review-[YYYYMMDD-HHmm].md`

- [ ] User communication completed with clear next steps



## Required Actions

1. Validate all required input parameters and file accessibility

2. Execute accessibility analysis following WCAG 2.1 guidelines

3. Generate compliance report in specified format

4. **Create actionable findings report** in `[id:findings_dir]reports/` with machine-readable format

5. Provide specific code remediation examples

6. Define testing and integration next steps



## Error Handling

You WILL handle these scenarios:

- **Missing Code Files**: Request specific file paths and verify accessibility

- **Non-Web Code Files**: Inform user that accessibility analysis requires web-related code

- **Invalid WCAG Standard**: Default to WCAG 2.1 and inform user of standard used

- **File Access Issues**: Provide clear error message and request alternative file access

- **No Accessibility Issues Found**: Confirm compliance and recommend ongoing testing practices

- **Complex Framework Code**: Provide framework-specific accessibility guidance (React, Vue, Angular)



⚠️ **Critical Requirements**

- MANDATORY: Analyze against all four WCAG 2.1 principles (Perceivable, Operable, Understandable, Robust)

- MANDATORY: Provide specific line references for all violations found

- NEVER ignore color contrast violations - these are critical for users with visual impairments

- NEVER approve keyboard inaccessible interactive elements

- ALWAYS provide concrete code examples for remediation

- ALWAYS recommend automated testing integration (pa11y, axe-core)

- ALWAYS prioritize violations that completely block access for users with disabilities

