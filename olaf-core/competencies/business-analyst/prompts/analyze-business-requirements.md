---

name: analyze-business-requirements-pml

description: Guide the process of reviewing a business requirements document to identify potential issues and generate clarifying questions

tags: [business, requirements, analysis, review, documentation]

---



CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 

.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.



## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **requirements_document**: string - Path to the business requirements document to analyze

- **strict_template_compliance**: boolean - Whether to strictly follow the template format (default: true)



## Process



1. **Source Analysis**:

   - Read file: `[requirements_document]`

   - Parse document structure and content

   - Identify key requirements and potential structural issues

   - Extract business objectives and functional requirements



2. **Best Practices Consultation**:

   - Read file: `[id:practices_dir]expressing-business-needs-to-developers.md`

   - Read file: `[id:practices_dir]reviewing-business-requirements-for-dev-and-test.md`

   - Apply established analysis frameworks and criteria

   - Reference industry standards for requirements quality



3. **Issue Identification and Categorization**:

   - Identify ambiguous requirements (unclear or multiple interpretations)

   - Detect incomplete requirements (missing critical details)

   - Find untestable requirements (lack of measurable criteria)

   - Flag inconsistencies or contradictions between requirements

   - Generate constructive clarifying questions for each identified issue



4. **Analysis Report Generation**:

   - Read file: `[id:competencies_dir][competency]/templates/business-analyst/requirements-analysis-report-template.md`

   - Structure findings according to template format

   - Categorize issues by severity and type

   - Provide actionable recommendations for improvement

   - Include specific section references for each issue



5. **Save Analysis Report**:

   - Generate filename in format: `business-requirements-analysis-YYYYMMDD-NNN.md`

   - Where NNN is a sequential serial number (001, 002, etc.)

   - Write file: `[id:findings_dir][generated_filename]`

   - Ensure kebab-case naming convention for clarity



## Output Format

Follow template structure: `[id:competencies_dir][competency]/templates/business-analyst/requirements-analysis-report-template.md`



## Output to USER

- Display analysis report in markdown format

- Summarize total number of issues found by category

- Highlight critical issues requiring immediate attention

- Confirm save location: `[id:findings_dir]business-requirements-analysis-YYYYMMDD-NNN.md`

- Next phase: Review findings with stakeholders and prioritize resolution



## Domain-Specific Rules

- Rule 1: Always reference specific sections when identifying issues

- Rule 2: Generate constructive questions that guide toward solutions

- Rule 3: Categorize issues by type (ambiguity, incompleteness, testability)

- Rule 4: Follow official template structure strictly for consistency

- Rule 5: Save report in olaf-data/findings with date-serial-kebab-case naming

- Rule 6: Focus on actionable feedback rather than criticism



## Required Actions

1. Read and thoroughly analyze the requirements document

2. Consult best practice guides for analysis criteria

3. Systematically identify and categorize requirements issues

4. Generate constructive clarifying questions for each issue

5. Produce formatted analysis report following official template

6. Save report to olaf-data/findings with proper naming convention



⚠️ **Critical Notes**

- Ensure all issues include specific document section references

- Focus on constructive feedback that guides improvement

- Maintain objectivity and avoid subjective judgments

- Verify template compliance before finalizing report

- Flag any missing critical requirement categories

- Report must be saved in olaf-data/findings directory with YYYYMMDD-NNN format

