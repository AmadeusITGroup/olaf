# Review Code: Step-by-Step Tutorial

How to Execute the "Review Code" Workflow

This tutorial shows exactly how to use the Developer competency's comprehensive code review workflow with multiple input modes for quality, security, and maintainability analysis.

## Prerequisites

- Access to OLAF Framework with developer competency pack
- Code to review (files, git repository, or copy-paste)
- Basic understanding of code quality principles
- Git repository (optional, for git-modified mode)

## Step-by-Step Instructions

### Step 1: Initialize Code Review

Brief description: Start the comprehensive code review workflow by invoking the developer competency with the review code command.

**User Action:**

1. Navigate to your project workspace
2. Execute one of the commands: `olaf review code`, `code review`, `examine code`, `check code`, or `review modified`
3. Prepare to specify review mode and parameters

**System Response:**
The system will prompt for review mode selection and gather appropriate parameters using Propose-Act protocol.

### Step 2: Select Review Mode and Provide Parameters

**User Action:** Choose review mode and provide required parameters when prompted

**Option A - Manual Mode:**
```text
Source Mode: manual
Code Source: [file-path-folder-or-copy-paste]
Language: [programming-language]
Context: [optional-additional-context]
Focus Areas: [optional-security-performance-style]
```

**Option B - Git-Modified Mode:**
```text
Source Mode: git-modified
Branch Name: [optional-specific-branch]
File Filter: [optional-file-types]
Batch Size: [optional-batch-size]
Focus Areas: [optional-focus-areas]
```

**Provide Requirements/Parameters:**

- **source_mode**: Review approach - we used "git-modified" for automatic discovery
- **branch_name**: Optional branch - we used "" (current branch)
- **file_filter**: Optional file types - we used "*.js,*.ts" for JavaScript/TypeScript
- **batch_size**: Optional batch size - we used "10" (default)
- **focus_areas**: Optional focus - we used ["security", "performance"]

### Step 3: Code Discovery and Preparation

**What System Does:**

**For Git-Modified Mode:**
- Automatically discovers modified files in git repository
- Filters files based on specified file types
- Organizes files into batches for systematic review
- Identifies file changes and modification scope

**For Manual Mode:**
- Reads specified files or processes copy-pasted code
- Validates code syntax and structure
- Prepares code for comprehensive analysis

**You Should See:** Code discovery results showing files to be reviewed and batch organization

### Step 4: Systematic Code Analysis

**What System Does:**

- Performs comprehensive quality analysis on each file/batch
- Evaluates code against best practices and standards
- Identifies security vulnerabilities and potential issues
- Assesses maintainability and readability factors
- Checks for performance optimization opportunities

**You Should See:** Detailed analysis results for each reviewed file with specific findings

### Step 5: Security and Quality Assessment

**What System Does:**

- Conducts security-focused review for vulnerabilities
- Identifies potential injection attacks and data exposure
- Reviews authentication and authorization patterns
- Evaluates input validation and sanitization
- Assesses error handling and logging practices

**You Should See:** Security assessment results with risk levels and specific recommendations

### Step 6: Maintainability and Style Review

**What System Does:**

- Reviews code structure and organization
- Evaluates naming conventions and documentation
- Assesses code complexity and readability
- Identifies potential refactoring opportunities
- Checks adherence to coding standards

**You Should See:** Maintainability assessment with code quality metrics and improvement suggestions

### Step 7: Aggregated Report Generation

**What System Does:**

- Compiles findings from all reviewed files
- Creates prioritized list of issues by severity
- Generates actionable recommendations for improvements
- Provides summary statistics and quality metrics
- Saves comprehensive review report to findings directory

**You Should See:** Complete code review report with prioritized findings and actionable recommendations

### Step 8: Follow-up Action Planning

**What System Does:**

- Suggests next steps for addressing identified issues
- Provides implementation guidance for improvements
- Recommends tools and processes for ongoing quality
- Creates tracking mechanism for improvement progress
- Offers integration suggestions with development workflow

**You Should See:** Action plan with specific steps for code quality improvement and workflow integration

## Verification Checklist

✅ **Review mode selected**: Appropriate input mode chosen and configured
✅ **Code discovered**: Files or code identified and prepared for review
✅ **Quality analysis completed**: Comprehensive evaluation against best practices
✅ **Security assessment done**: Vulnerability and security pattern review completed
✅ **Maintainability evaluated**: Code structure and readability assessed
✅ **Issues prioritized**: Findings organized by severity and impact
✅ **Report generated**: Comprehensive review documentation created
✅ **Action plan provided**: Clear next steps for improvement identified

## Troubleshooting

**If git-modified mode fails:**

```bash
# Verify git repository status and modified files
git status
git diff --name-only
# Check branch and ensure there are modified files to review
```

**If code analysis seems incomplete:**

- Verify file paths are accessible and readable
- Check that specified programming language is supported
- Ensure focus areas match actual code characteristics
- Consider adjusting batch size for large repositories

**If security assessment misses issues:**

- Review focus areas to include specific security concerns
- Provide additional context about application security requirements
- Consider manual mode for sensitive code sections
- Supplement with specialized security tools if needed

## Key Learning Points

1. **Multiple input modes**: Review supports manual selection, git discovery, and batch processing
2. **Comprehensive analysis**: Covers quality, security, maintainability, and performance
3. **Batch processing**: Large codebases handled systematically through batching
4. **Actionable output**: Results include specific recommendations and implementation guidance
5. **Workflow integration**: Designed to fit into existing development and review processes

## Next Steps to Try

- Implement prioritized improvements from review findings
- Integrate code review workflow into development process
- Use git-modified mode for regular change reviews
- Apply focus areas for specialized review needs (security, performance)
- Establish regular review cycles for ongoing code quality

## Expected Timeline

- **Total review time:** 15-45 minutes depending on code volume and complexity
- **User input required:** Mode selection and parameter setup (3-5 minutes)
- **Code discovery:** File identification and preparation (2-5 minutes)
- **Analysis execution:** Comprehensive review and assessment (10-30 minutes)
- **Report generation:** Findings compilation and action planning (5-10 minutes)