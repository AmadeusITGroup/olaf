# Review Code

## Overview

This competency performs comprehensive code reviews with multiple input modes - manual selection, git-modified files, or batch processing - focusing on quality, security, maintainability, and adherence to coding standards.

## Purpose

Code reviews catch bugs early, ensure quality standards, share knowledge, and maintain codebase health. This competency provides thorough, consistent code reviews that check for security vulnerabilities, performance issues, code smells, and adherence to best practices, with support for both single-file and batch processing workflows.

## Usage

**Command**: `review code` (or aliases: `code review`, `examine code`, `check code`, `inspect code`, `review modified`, `review changes`, `modified files`, `changes review`, `git changes`, `review git`, `review branch`)

**Protocol**: Propose-Act

**When to Use**: Use for pre-commit reviews, pull request reviews, security audits, quality assessments, onboarding reviews, or periodic codebase health checks. Supports both targeted single-file reviews and comprehensive git-modified file batch processing.

## Parameters

### Required Inputs (Mode-Dependent)

**For Manual Mode:**
- **code_source**: What to review (copy-pasted code, file path, folder, or repository)
- **language**: Programming language

**For Git-Modified Mode (Auto-Discovery):**
- **branch_name**: Optional specific branch (defaults to current)
- **file_filter**: Optional file type filter (e.g., "*.cs,*.js,*.py")
- **batch_size**: Files per batch (default: 10)

### Optional Inputs (All Modes)
- **focus_areas**: Specific areas to emphasize (security, performance, style)
- **review_standards**: Custom coding standards or style guides
- **team_conventions**: Team-specific patterns or guidelines
- **compliance_requirements**: Specific compliance standards (OWASP, NIST)

### Context Requirements
- Access to code to be reviewed
- Relevant coding standards and team conventions
- Understanding of project context and requirements
- For git mode: working git repository

## Output

Generates comprehensive code review reports with findings and recommendations.

**Deliverables**:

**Single File/Manual Mode:**
- Critical issues (security, bugs, performance)
- Recommendations for improvements
- Positive feedback on good practices
- Code review report: `code-review-YYYYMMDD-HHmm.md`
- Curative action plan: `action-plan-YYYYMMDD-HHmm.md`

**Git-Modified Mode (Batch):**
- Individual review files for each analyzed file
- Summary report: `code-review-summary-YYYYMMDD-NNN.md`
- Aggregated findings by severity
- Common patterns across files
- Team-wide improvement recommendations

**Format**: Structured markdown following code-review template

## Examples

### Example 1: Pre-Commit Review

**Scenario**: Developer wants to review changes before committing

**Command**:
```
review code
```

**Input**:
```
code_source: src/services/payment-service.ts
language: TypeScript
focus_areas: ["security", "error-handling"]
```

**Result**: Identified SQL injection vulnerability, missing error handling for network failures, recommended input validation improvements, generated action plan with specific fixes.

### Example 2: Git-Modified Files Batch Review

**Scenario**: Review all changes in current branch before pull request

**Command**:
```
review modified files
```

**Input**:
```
branch_name: feature/user-authentication
file_filter: *.ts,*.tsx
```

**Result**: Processed 15 modified files in batches, generated individual reviews for each, created summary report showing 3 critical security issues, 8 code quality improvements, and 5 positive patterns to replicate.

### Example 3: Security Audit

**Scenario**: Security review of authentication module

**Command**:
```
review code
```

**Input**:
```
code_source: src/auth/
language: Java
focus_areas: ["security"]
compliance_requirements: ["OWASP Top 10"]
```

**Result**: Comprehensive security review identifying authentication bypass risk, weak password hashing, missing rate limiting, with detailed remediation steps and OWASP references.

## Related Competencies

- **fix-code-smells**: Implements improvements identified during review
- **improve-cyclomatic-complexity**: Addresses complexity issues found in review
- **review-github-pr**: Specialized review for pull requests with integration analysis
- **create-unit-tests**: Adds tests for code lacking coverage identified in review

## Tips & Best Practices

- Load universal and team-specific coding standards before reviewing
- Use git-modified mode for efficient branch reviews
- Specify focus areas for targeted reviews
- Always review generated action plans and prioritize fixes
- Run reviews before committing to catch issues early
- Use batch processing for large changesets
- Combine with automated testing for comprehensive quality checks
- Document and share common patterns found across reviews
- Review positive patterns to encourage good practices

## Limitations

- Cannot execute code or validate runtime behavior
- Effectiveness depends on coding standards clarity
- May miss context-dependent issues
- Cannot assess business logic correctness without domain knowledge
- Batch processing may hit session limits on very large changesets
- Cannot detect all security vulnerabilities (use specialized security tools)
- Review quality depends on specification completeness
- Cannot replace human judgment for architectural decisions
