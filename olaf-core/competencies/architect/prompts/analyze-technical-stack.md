---
name: analyze-technical-stack
description: Chapter-based technical stack analysis with automated discovery, assessment, and reporting across multiple sessions
tags: [analysis, technical-stack, discovery, chapter-based]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

Use terminal commands, not training data.

## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **project_root**: string - (Required) Path to the project root directory for automated analysis
- **project_name**: string - (Required) Name of the project for report naming
- **chapter**: string - (Optional) Specific chapter to execute (discovery, analysis, assessment, reporting)


## Chapter-Based Workflow

### Chapter 1: Discovery
**Prerequisites**: None
**Objective**: Automated discovery of technical stack components

**Process**:
1. **Verify Prerequisites**: No previous chapters required
2. **Initialize Report File**: Create `[id:findings_dir]technical-stack-analysis-for-<project_name>-YYYYMMDD-NNN.md`
3. **Automated Discovery**:
   - Scan directory structure to identify project type (web, mobile, backend, etc.)
   - Parse package manager files (package.json, requirements.txt, pom.xml, etc.)
   - Detect framework and library usage from source code
   - Identify build tools and configuration files
   - Find database configuration and ORM usage
   - Discover CI/CD configuration and deployment scripts
   - Detect containerization (Docker, Kubernetes)
   - Identify testing frameworks and tools
4. **Save Chapter Results**: Write discovery findings to report file under "# Chapter 1: Discovery"
5. **Chapter Status**: "Chapter 1 Done - Start new session and enter 'analyze tech stack' to continue with Chapter 2"

### Chapter 2: Analysis
**Prerequisites**: Chapter 1 must be completed and saved
**Objective**: Deep analysis of discovered components

**Process**:
1. **Verify Prerequisites**: Check that Chapter 1 exists in the report file
2. **Load Previous Results**: Read discovery findings from Chapter 1
3. **Component Analysis**:
   - Identify version and compatibility for each component
   - Check for known vulnerabilities (CVE database)
   - Assess maintenance status and community support
   - Evaluate performance characteristics
   - Check documentation availability and quality
   - Analyze dependency relationships and conflicts
4. **Save Chapter Results**: Append analysis findings to report file under "# Chapter 2: Analysis"
5. **Chapter Status**: "Chapter 2 Done - Start new session and enter 'analyze tech stack' to continue with Chapter 3"

### Chapter 3: Assessment
**Prerequisites**: Chapters 1 and 2 must be completed and saved
**Objective**: Comprehensive assessment and gap analysis

**Process**:
1. **Verify Prerequisites**: Check that Chapters 1 and 2 exist in the report file
2. **Load Previous Results**: Read discovery and analysis findings
3. **Comprehensive Assessment**:
   - Evaluate architecture patterns and design quality
   - Identify technical debt and code quality issues
   - Assess security posture and vulnerabilities
   - Evaluate scalability and performance bottlenecks
   - Check test coverage and quality metrics
   - Analyze deployment and operational readiness
4. **Gap Analysis**:
   - Identify missing components or capabilities
   - Assess compliance with industry standards
   - Evaluate team skill requirements
5. **Save Chapter Results**: Append assessment findings to report file under "# Chapter 3: Assessment"
6. **Chapter Status**: "Chapter 3 Done - Start new session and enter 'analyze tech stack' to continue with Chapter 4"

### Chapter 4: Reporting
**Prerequisites**: Chapters 1, 2, and 3 must be completed and saved
**Objective**: Generate final comprehensive report with recommendations

**Process**:
1. **Verify Prerequisites**: Check that Chapters 1, 2, and 3 exist in the report file
2. **Load Previous Results**: Read all previous chapter findings
3. **Report Generation**:
   - Create executive summary
   - Compile detailed technical analysis
   - Generate recommendations and action items
   - Create migration paths and upgrade strategies
   - Document resource requirements
   - Include visual dependency graphs
   - Add risk assessment matrix
4. **Save Chapter Results**: Append final report to file under "# Chapter 4: Final Report"
5. **Use Template**: Follow the structure defined in `[id:templates_dir]architect/tech-stack-template.md`
6. **Chapter Status**: "Chapter 4 Done - Technical stack analysis complete. Report available at: [id:findings_dir]technical-stack-analysis-for-<project_name>-YYYYMMDD-NNN.md"

## Execution Logic

**Chapter Detection**:
1. Check if report file exists for the project
2. If file exists, determine last completed chapter
3. Execute next chapter in sequence
4. If no file exists, start with Chapter 1

**Chapter Verification**:
- Before starting any chapter (except Chapter 1), verify previous chapters are completed
- Read the report file and check for chapter completion markers
- If prerequisites not met, inform user and stop execution

## Output Format

**Report File Structure**:
```markdown
# Technical Stack Analysis for <project_name>
**Generated**: YYYYMMDD-HHmm CEDT
**Status**: [In Progress/Complete]

## Executive Summary
[Populated in Chapter 4]

# Chapter 1: Discovery
[Discovery findings]
**Status**: Complete

# Chapter 2: Analysis
[Analysis findings]
**Status**: Complete

# Chapter 3: Assessment
[Assessment findings]
**Status**: Complete

# Chapter 4: Final Report
[Final report and recommendations]
**Status**: Complete
```

## Session Management
- Each chapter should be executed in a separate session
- User must start new session between chapters
- Use command "analyze tech stack" to continue workflow
- System will automatically detect and execute next chapter

## Domain-Specific Rules
- Rule 1: Always verify chapter prerequisites before execution
- Rule 2: Save results after each chapter completion
- Rule 3: Provide clear status messages for session management
- Rule 4: Never skip chapters or execute out of order
- Rule 5: Always load previous chapter results before proceeding
