# Step-by-Step Tutorial

**Analyze Technical Stack: Step-by-Step Tutorial**

**How to Execute the "Analyze Technical Stack" Workflow**

This tutorial shows exactly how to perform comprehensive technical stack analysis using the chapter-based workflow in the OLAF architect competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to the project codebase for analysis
- Understanding of software architecture and technology stacks
- Access to the architect competency pack

## Step-by-Step Instructions

### Step 1: Prepare the Project for Analysis
[Ensure you have access to the codebase]

**User Action:**
1. Locate the project root directory you want to analyze
2. Ensure you have read access to all project files
3. Note the full path to the project root
4. Decide on a project name for report naming

**System Response:**
Project should be accessible with all configuration files readable.

### Step 2: Start Chapter 1 - Discovery
**User Action:** Execute the OLAF command to start technical stack analysis
```
olaf analyze technical stack
```

**Provide Parameters:**
- **project_root**: [/path/to/project] - Full path to the project directory
- **project_name**: [ProjectName] - Name for report identification

### Step 3: Automated Discovery Process
**What OLAF Does:**
- Scans directory structure to identify project type (web, mobile, backend, etc.)
- Parses package manager files (package.json, requirements.txt, pom.xml, Gemfile, etc.)
- Detects frameworks and libraries from source code imports
- Identifies build tools and configuration files (webpack, gradle, maven, etc.)
- Finds database configuration and ORM usage
- Discovers CI/CD configuration (GitHub Actions, Jenkins, GitLab CI)
- Detects containerization setup (Docker, Kubernetes manifests)
- Identifies testing frameworks and tools

**You Should See:** 
- Progress messages for each discovery phase
- List of discovered components organized by category
- Report file created at `olaf-data/findings/technical-stack-analysis-for-<project_name>-YYYYMMDD-NNN.md`
- Chapter 1 completion status

### Step 4: Review Discovery Results
**User Action:**
1. Review the generated report's Chapter 1 section
2. Verify discovered components are accurate
3. Note any missing components for manual addition
4. Start a new session when ready for Chapter 2

**System Response:**
"Chapter 1 Done - Start new session and enter 'analyze tech stack' to continue with Chapter 2"

### Step 5: Start Chapter 2 - Analysis
**User Action:** In a new session, execute the command again
```
olaf analyze technical stack
```

**What OLAF Does:**
- Detects existing report file and last completed chapter
- Loads Chapter 1 discovery findings
- Analyzes each discovered component:
  - Identifies versions and compatibility
  - Checks for known vulnerabilities (CVE database)
  - Assesses maintenance status and community support
  - Evaluates performance characteristics
  - Checks documentation availability
  - Analyzes dependency relationships and conflicts

**You Should See:**
- Loading of previous chapter results
- Detailed analysis for each component
- Version compatibility matrix
- Security vulnerability report
- Chapter 2 appended to the report file

### Step 6: Start Chapter 3 - Assessment
**User Action:** In a new session, execute the command again
```
olaf analyze technical stack
```

**What OLAF Does:**
- Loads Chapters 1 and 2 findings
- Performs comprehensive assessment:
  - Evaluates architecture patterns and design quality
  - Identifies technical debt and code quality issues
  - Assesses security posture and vulnerabilities
  - Evaluates scalability and performance bottlenecks
  - Checks test coverage and quality metrics
  - Analyzes deployment and operational readiness
- Conducts gap analysis:
  - Identifies missing components or capabilities
  - Assesses compliance with industry standards
  - Evaluates team skill requirements

**You Should See:**
- Architecture quality assessment
- Technical debt identification
- Security posture evaluation
- Gap analysis with specific recommendations
- Chapter 3 appended to the report

### Step 7: Start Chapter 4 - Final Report
**User Action:** In a new session, execute the command again
```
olaf analyze technical stack
```

**What OLAF Does:**
- Loads all previous chapter findings
- Generates final comprehensive report:
  - Creates executive summary
  - Compiles detailed technical analysis
  - Generates prioritized recommendations
  - Creates migration paths and upgrade strategies
  - Documents resource requirements
  - Includes visual dependency graphs (if applicable)
  - Adds risk assessment matrix

**You Should See:**
- Complete executive summary
- Consolidated technical analysis
- Actionable recommendations with priorities
- Migration and upgrade roadmaps
- Final report completion message

## Verification Checklist

✅ **Chapter 1: All technology components discovered and documented**
✅ **Chapter 2: Version analysis and vulnerability assessment completed**
✅ **Chapter 3: Architecture and gap analysis performed**
✅ **Chapter 4: Final report with recommendations generated**
✅ **Report saved with proper naming convention and timestamp**
✅ **All chapters include specific findings and actionable insights**

## Troubleshooting

**If project cannot be analyzed:**
- Verify the project root path is correct and accessible
- Check file permissions for reading configuration files
- Ensure package manager files are present and valid

**If chapter prerequisites not met:**
- Verify previous chapters are completed in the report file
- Check that the report file exists in olaf-data/findings/
- Ensure chapter completion markers are present

**If discovery finds no components:**
- Verify the project structure matches expected patterns
- Check that package manager files are in standard locations
- Consider manually specifying component information

## Key Learning Points

1. **Chapter-Based Workflow:** Analysis is split into four manageable chapters executed across multiple sessions
2. **Incremental Progress:** Each chapter builds on previous findings, maintaining context across sessions
3. **Automated Discovery:** The system automatically identifies components without manual configuration
4. **Comprehensive Coverage:** Analysis covers discovery, version analysis, architecture assessment, and recommendations

## Next Steps to Try

- Review the final report with the development team
- Prioritize recommendations based on business impact
- Create decision records for major technology decisions
- Use generate-detailed-tech-spec to document specific components
- Plan migration or upgrade initiatives based on findings

## Expected Timeline

- **Chapter 1 (Discovery):** 3-5 minutes
- **Chapter 2 (Analysis):** 5-10 minutes
- **Chapter 3 (Assessment):** 5-10 minutes
- **Chapter 4 (Reporting):** 3-5 minutes
- **Total analysis time:** 16-30 minutes across 4 sessions
- **User input required:** Project path and name at start, session management between chapters
