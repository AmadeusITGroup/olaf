# Analyze Technical Stack

## Overview

This competency performs comprehensive technical stack analysis through a chapter-based workflow that spans multiple sessions. It automatically discovers technology components, analyzes their characteristics, assesses architecture quality, and generates detailed reports with actionable recommendations.

## Purpose

Technical stack analysis is critical for understanding system architecture, identifying technical debt, assessing security vulnerabilities, and planning technology upgrades. This competency addresses the complexity of modern technology stacks by breaking the analysis into manageable chapters that can be executed across multiple sessions, allowing for thorough investigation without overwhelming context limits.

## Usage

**Command**: `analyze technical stack`

**Protocol**: Propose-Act

**When to Use**: Use this competency when evaluating a new codebase for acquisition or migration, conducting architecture reviews, planning technology upgrades, assessing technical debt, or documenting existing systems for new team members.

## Parameters

### Required Inputs
- **project_root**: Path to the project root directory for automated analysis
- **project_name**: Name of the project for report naming

### Optional Inputs
- **chapter**: Specific chapter to execute (discovery, analysis, assessment, reporting)

### Context Requirements
- Access to the project codebase and configuration files
- Read permissions for package manager files and source code
- Technical stack template automatically referenced from competency templates

## Output

This competency produces a comprehensive technical stack analysis report built incrementally across four chapters.

**Deliverables**:
- Technical stack analysis report saved to `olaf-data/findings/technical-stack-analysis-for-<project_name>-YYYYMMDD-NNN.md`
- Chapter-based markdown document with discovery, analysis, assessment, and final report sections

**Format**: Structured markdown document following the tech-stack-template with sections for component discovery, version analysis, security assessment, architecture evaluation, and actionable recommendations.

## Examples

### Example 1: New Codebase Evaluation

**Scenario**: A development team is evaluating an acquired application to understand its technology stack and identify modernization opportunities.

**Command**:
```
olaf analyze technical stack
```

**Input**:
```
project_root: /path/to/acquired-app
project_name: AcquiredApp
```

**Result**: 
- Chapter 1: Discovered Node.js backend, React frontend, PostgreSQL database, Docker containerization, Jenkins CI/CD
- Chapter 2: Identified outdated dependencies (React 16.x), security vulnerabilities in 3 packages, compatibility issues
- Chapter 3: Assessed architecture as monolithic with tight coupling, identified scalability bottlenecks, test coverage at 45%
- Chapter 4: Generated migration roadmap to React 18, microservices recommendations, security patch priorities

### Example 2: Architecture Review for Compliance

**Scenario**: An architect needs to document the technical stack for a compliance audit and identify security risks.

**Command**:
```
olaf analyze technical stack
```

**Result**: Comprehensive report documenting all technology components, versions, known vulnerabilities, security posture assessment, and compliance gap analysis with remediation recommendations.

## Related Competencies

- **generate-detailed-tech-spec**: Use after analysis to create detailed technical specifications for specific components
- **review-code**: Complements analysis by examining code quality and patterns
- **bootstrap-functional-spec-from-code**: Use to extract functional specifications from the analyzed codebase
- **create-decision-record**: Document architecture decisions identified during analysis

## Tips & Best Practices

- Execute one chapter per session to allow thorough analysis without context overflow
- Review chapter outputs before proceeding to ensure accuracy and completeness
- Use the discovery chapter to understand project structure before diving into detailed analysis
- Save the report between chapters to maintain progress across sessions
- Reference the tech-stack-template to understand the expected report structure
- Use chapter 4 recommendations to prioritize technical debt and upgrade planning

## Limitations

- Analysis quality depends on code organization and documentation quality
- Cannot evaluate runtime behavior or performance without actual execution
- Security vulnerability detection relies on known CVE databases (may miss zero-days)
- Requires access to all configuration files and dependencies for complete analysis
- Chapter-based approach requires multiple sessions for full analysis

---

**Source**: `olaf-core/competencies/architect/prompts/analyze-technical-stack.md`
