# Step-by-Step Tutorial

**Analyze Business Requirements: Step-by-Step Tutorial**

**How to Execute the "Analyze Business Requirements" Workflow**

This tutorial shows exactly how to analyze business requirements documents to identify potential issues and generate clarifying questions using the OLAF business-analyst competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to a business requirements document to analyze
- Understanding of business requirements documentation standards
- Access to the business-analyst competency pack

## Step-by-Step Instructions

### Step 1: Prepare the Requirements Document
[Ensure you have the document ready for analysis]

**User Action:**
1. Locate the business requirements document you want to analyze
2. Ensure the document is accessible (local file path or readable format)
3. Note the full path to the document for the analysis command

**System Response:**
Document should be readable and accessible for processing.

### Step 2: Invoke the Analysis Command
**User Action:** Execute the OLAF command to start requirements analysis
```
olaf analyze business requirements
```

**Provide Parameters:**
- **requirements_document**: [path/to/your/requirements-document.md] - Full path to the document
- **strict_template_compliance**: [true/false] - Whether to follow strict template format (default: true)

### Step 3: Document Analysis Process
**What OLAF Does:**
- Reads and parses the requirements document structure and content
- Consults best practices from `expressing-business-needs-to-developers.md`
- References `reviewing-business-requirements-for-dev-and-test.md` guidelines
- Identifies key requirements and structural issues systematically

**You Should See:** Progress messages indicating document reading and analysis phases

### Step 4: Issue Identification and Categorization
**What OLAF Does:**
- Identifies ambiguous requirements (unclear or multiple interpretations)
- Detects incomplete requirements (missing critical details)  
- Finds untestable requirements (lack of measurable criteria)
- Flags inconsistencies or contradictions between requirements
- Generates constructive clarifying questions for each issue

**You Should See:** Categorized list of identified issues with specific section references

### Step 5: Analysis Report Generation
**What OLAF Does:**
- Loads the requirements analysis report template
- Structures findings according to the standard template format
- Categorizes issues by severity and type
- Provides actionable recommendations for improvement
- Includes specific section references for each issue

**You Should See:** Formatted analysis report following the official template structure

### Step 6: Report Saving and Output
**What OLAF Does:**
- Generates filename in format: `business-requirements-analysis-YYYYMMDD-NNN.md`
- Saves the report to `olaf-data/findings/` directory
- Displays the complete analysis report
- Provides summary of issues found by category

**You Should See:** 
- Complete analysis report in markdown format
- File save confirmation with location
- Summary of total issues found by category
- Highlighted critical issues requiring immediate attention

## Verification Checklist

✅ **Requirements document successfully analyzed**
✅ **Issues identified and categorized by type (ambiguity, incompleteness, testability)**
✅ **Constructive clarifying questions generated for each issue**
✅ **Analysis report saved to olaf-data/findings/ with proper naming convention**
✅ **Report follows official template structure**
✅ **All issues include specific document section references**

## Troubleshooting

**If document cannot be read:**
- Verify the file path is correct and accessible
- Ensure the document format is supported (markdown, text, etc.)
- Check file permissions

**If template compliance errors occur:**
- Set strict_template_compliance to false for more flexible analysis
- Verify the requirements analysis template exists in the competency pack

**If no issues are found:**
- This may indicate a well-written requirements document
- Review the analysis criteria in the best practices guides
- Consider if the document scope matches the analysis expectations

## Key Learning Points

1. **Systematic Analysis:** The workflow follows a structured approach using established best practices and templates
2. **Categorized Feedback:** Issues are systematically categorized (ambiguous, incomplete, untestable, inconsistent) for targeted improvement
3. **Actionable Output:** The analysis provides constructive questions and recommendations rather than just criticism

## Next Steps to Try

- Review the generated analysis report with stakeholders
- Prioritize resolution of critical issues identified in the analysis
- Use the clarifying questions to gather additional requirements details
- Apply the findings to improve the original requirements document

## Expected Timeline

- **Total analysis time:** 2-5 minutes depending on document size
- **User input required:** Providing document path and configuration parameters
- **OLAF execution time:** Automated analysis, template application, and report generation