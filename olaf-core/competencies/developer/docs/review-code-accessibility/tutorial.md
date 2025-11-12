# Step-by-Step Tutorial

**Review Code Accessibility: Step-by-Step Tutorial**

**How to Execute the "WCAG 2.1 Accessibility Compliance Analysis" Workflow**

This tutorial shows exactly how to execute a comprehensive accessibility code review using the OLAF developer competency's review-code-accessibility functionality. This workflow analyzes code for WCAG 2.1 accessibility compliance and provides remediation guidance.

## Prerequisites

- OLAF framework properly installed and configured
- Web-related code files to analyze (HTML, CSS, JavaScript, React, Vue, Angular, etc.)
- Basic understanding of web accessibility principles
- Access to project files or repository

## Step-by-Step Instructions

### Step 1: Initiate Accessibility Review
[Brief description: Start the accessibility review process by invoking the OLAF review-code-accessibility competency]

**User Action:**
1. Open your terminal or OLAF interface
2. Navigate to your project directory containing web-related code
3. Execute the OLAF review-code-accessibility competency using one of these methods:
   - Direct invocation: `olaf review-code-accessibility`
   - Via aliases: `olaf accessibility review`, `olaf wcag review`, `olaf accessibility check`

**OLAF Response:**
The system will prompt you to provide the required parameters for accessibility analysis.

### Step 2: Provide Required Parameters
**User Action:** Specify the accessibility analysis parameters
```
Required Parameters:
- code_files: List of files to analyze (HTML, CSS, JS, React components, etc.)
- project_name: Name for the findings report
- accessibility_standard: WCAG version (default: "2.1")
- compliance_level: AA or AAA (default: "AA") 
- output_format: report, checklist, or recommendations (default: "report")
```

**Provide Requirements/Parameters:**
- **code_files**: [Example - we used ["src/components/*.jsx", "public/index.html", "src/styles/*.css"]]
- **project_name**: [Example - we used "e-commerce-frontend"]
- **accessibility_standard**: [Example - we used "2.1"] (optional)
- **compliance_level**: [Example - we used "AA"] (optional)
- **output_format**: [Example - we used "report"] (optional)

### Step 3: File Validation and Template Loading
**What OLAF Does:**
- Validates that all specified code files are accessible
- Checks that files contain web-related code suitable for accessibility analysis
- Loads the accessibility findings report template
- Validates accessibility testing tools (pa11y, axe-core) if available
- Gets current timestamp for report generation

**You Should See:** Confirmation of files validated and template loaded successfully

### Step 4: WCAG 2.1 Compliance Analysis
**What OLAF Does:**
- Analyzes code against all four WCAG 2.1 core principles:
  1. **Perceivable**: Text alternatives, captions, content adaptability, color contrast
  2. **Operable**: Keyboard accessibility, timing, seizure prevention, navigation
  3. **Understandable**: Readability, predictability, error handling
  4. **Robust**: Compatibility with assistive technologies
- Identifies specific violations with file and line references
- Generates actionable remediation recommendations
- Creates code examples for critical fixes

**You Should See:** Progress updates for each WCAG principle analysis and violations found

### Step 5: Results Generation and Report Creation
**User Action:** Review the accessibility findings when presented

**What OLAF Does:**
- Creates comprehensive accessibility compliance report
- Generates timestamped findings file: `[project-name]-accessibility-review-YYYYMMDD-HHmm.md`
- Saves report to `olaf-data/findings/reports/` directory
- Provides specific code examples for remediation
- Creates priority assessment for identified violations

**You Should See:** File path of generated accessibility report and summary of critical violations

## Verification Checklist

✅ **All web-related code files successfully analyzed**
✅ **WCAG 2.1 compliance assessment completed for all four principles**
✅ **Specific violations identified with file and line references**
✅ **Actionable remediation recommendations provided with code examples**
✅ **Accessibility findings report saved to olaf-data/findings/reports/**
✅ **Priority assessment completed for accessibility barriers**

## Troubleshooting

**If no web-related code files found:**
```bash
find . -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.jsx" -o -name "*.vue" -o -name "*.ts" -o -name "*.tsx"
```

**If accessibility testing tools are not available:**
- Install pa11y: `npm install -g pa11y`
- Install axe-core: `npm install --save-dev @axe-core/cli`
- Verify installation: `pa11y --version` and `axe --version`

**If no accessibility issues found:**
- Verify that interactive elements exist in the analyzed code
- Check that the analysis included dynamic content and form elements
- Consider running automated tools on the rendered application

## Key Learning Points

1. **Four WCAG Principles:** All accessibility analysis covers Perceivable, Operable, Understandable, and Robust principles comprehensively
2. **Specific Line References:** Every violation includes exact file and line locations for efficient remediation
3. **Code Examples:** Concrete remediation code snippets are provided for each critical accessibility barrier

## Next Steps to Try

- Implement the priority fixes identified in the accessibility report
- Set up automated accessibility testing with pa11y and axe-core in your CI/CD pipeline
- Use the generated findings report to track accessibility improvements over time
- Review the accessibility findings template for understanding violation categorization

## Expected Timeline

- **Total accessibility review time:** 5-15 minutes (depending on codebase size and complexity)
- **User input required:** Parameter specification and file selection (1-2 minutes)
- **OLAF execution time:** WCAG analysis across all four principles (3-10 minutes)
- **Report generation:** Automatic findings report creation with code examples (1-3 minutes)