# Step-by-Step Tutorial

**Review PRD Spec: Step-by-Step Tutorial**

**How to Execute the "Review PRD Spec" Workflow**

This tutorial shows exactly how to review Product Requirements Documents (PRDs) for completeness, identify gaps, and generate standardized formatted documents using the OLAF business-analyst competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to a PRD or evolution request document to review
- PRD template files available in the templates directory
- Understanding of PRD structure and standard sections
- Access to the business-analyst competency pack

## Step-by-Step Instructions

### Step 1: Prepare the PRD Content
[Ensure you have the PRD document ready for review]

**User Action:**
1. Locate the PRD or evolution request document you want to review
2. Ensure the document is accessible (file path or content string)
3. Identify the project name for proper document naming
4. Decide on review depth level (basic, comprehensive, or detailed)

**System Response:**
Document should be readable and accessible for processing.

### Step 2: Invoke the Review Command
**User Action:** Execute the OLAF command to start PRD review
```
olaf review prd spec
```

**Provide Parameters:**
- **prd_content**: [path/to/prd-document.md or content string] - The PRD to review
- **project_name**: [your-project-name] - Name for output file naming
- **review_depth**: [comprehensive] - Level of analysis (default: comprehensive)
- **save_format**: [true] - Whether to save formatted output (default: true)
- **template_type**: [standard] - Template format to use (default: standard)

### Step 3: Content Analysis Phase
**What OLAF Does:**
- Reads and parses the PRD content structure
- Analyzes business objectives and success metrics
- Reviews user stories and acceptance criteria
- Evaluates technical requirements and constraints
- Assesses risk management and mitigation strategies
- Checks timeline and resource requirements
- Validates stakeholder identification

**You Should See:** Progress messages indicating content analysis is underway

### Step 4: Completeness Review and Gap Identification
**What OLAF Does:**
- Evaluates each PRD section against standard requirements:
  - Executive Summary (problem statement, solution overview)
  - Business Case (value proposition, ROI, strategic alignment)
  - User Requirements (personas, journeys, functional requirements)
  - Technical Specifications (architecture, integrations, performance)
  - Implementation Plan (phases, milestones, dependencies)
  - Success Criteria (measurable outcomes, KPIs)
  - Risk Management (identified risks, mitigation plans)
- Creates prioritized gap list (Critical, Important, Nice-to-have)
- Generates specific questions to address each gap
- Provides examples of complete sections

**You Should See:** Categorized list of gaps with priority levels and specific questions

### Step 5: User Interaction for Improvements
**What OLAF Does:**
- Presents findings using Propose-Act protocol
- Asks targeted questions to fill identified gaps
- Requests clarification on ambiguous requirements
- Validates user responses iteratively
- Ensures all critical gaps are addressed

**User Action:**
1. Review the identified gaps and their priority levels
2. Answer the targeted improvement questions
3. Provide clarification for ambiguous sections
4. Confirm when critical gaps have been addressed

**You Should See:** Interactive question-and-answer session with specific, actionable questions

### Step 6: Document Formatting
**What OLAF Does:**
- Applies selected PRD template structure (standard/agile/enterprise)
- Ensures consistent formatting and style throughout
- Adds proper section numbering and cross-references
- Includes timestamp and version information
- Generates table of contents and appendices
- Validates internal consistency and clarity

**You Should See:** Formatted document preview following template structure

### Step 7: Quality Validation and Final Output
**What OLAF Does:**
- Confirms all critical gaps have been addressed
- Verifies document follows template structure completely
- Checks for internal consistency and clarity
- Validates that success criteria are measurable
- Calculates quality score and template compliance percentage
- Saves final document using Propose-Confirm-Act protocol

**User Action:**
Review and approve the final formatted document for saving

**You Should See:**
- Complete formatted PRD document
- Quality checklist with validation results
- Template compliance score (target: 95%+)
- File save confirmation: `[product_docs_dir]/[project_name]-prd-[timestamp].md`

## Verification Checklist

✅ **PRD content thoroughly analyzed for completeness**
✅ **All critical gaps identified and prioritized**
✅ **Targeted improvement questions generated and answered**
✅ **Document formatted according to selected template**
✅ **Quality validation confirms 95%+ template compliance**
✅ **Success criteria are measurable and time-bound**
✅ **Risk assessment includes both technical and business risks**
✅ **Final document saved with proper naming convention**
✅ **User approval obtained for final formatted version**

## Troubleshooting

**If PRD content cannot be read:**
- Verify the file path is correct and accessible
- Ensure the document format is supported
- Check file permissions

**If template files are not found:**
```
Check templates directory: [templates_dir]/business-analyst/
Verify template_type parameter matches available templates
```

**If critical gaps remain unaddressed:**
- Review the prioritized gap list systematically
- Engage subject matter experts for technical sections
- Consider scheduling stakeholder workshops for complex gaps

**If template compliance is below 95%:**
- Review sections flagged in quality validation
- Ensure all required sections are present
- Verify formatting consistency throughout document

## Key Learning Points

1. **Systematic Gap Analysis:** The workflow uses a structured approach to identify missing or incomplete PRD sections across all standard categories
2. **Prioritized Improvements:** Gaps are categorized by severity (Critical, Important, Nice-to-have) to focus efforts efficiently
3. **Interactive Refinement:** The Propose-Act protocol ensures collaborative improvement rather than automated assumptions
4. **Template Standardization:** Applying consistent templates ensures organizational alignment and reduces review friction

## Next Steps to Try

- Share the formatted PRD with stakeholders for approval
- Use analyze-business-requirements to validate detailed requirement sections
- Apply improve-spec to add technical diagrams and data models
- Schedule technical review with development team
- Track PRD quality metrics over multiple projects to improve process

## Expected Timeline

- **Total review time:** 10-20 minutes depending on PRD size and gap count
- **User input required:** Answering improvement questions, providing clarifications, approving final document
- **OLAF execution time:** Automated analysis, gap identification, formatting, and validation
- **Interactive phases:** Gap discussion and document approval require active user participation
