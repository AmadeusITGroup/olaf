# Developer Competency Package - Documentation

**Version**: 1.0.0  
**Status**: Public Beta  
**Created**: October 21, 2025  

---

## Overview

The Developer Competency Package provides comprehensive capabilities for software development workflows. It aggregates 11 core competencies focused on code review, analysis, refactoring, testing, and quality improvement.

**Primary User**: Software Developers  
**Classification**: Kernel (Core Framework)  
**Framework Version**: OLAF 1.6.0+  

---

## Competencies

### 1. Review Code
**Protocol**: Act  
**File**: `prompts/review-code.md`

Comprehensive code review with quality and maintainability assessment.

**Entry Aliases**: 
- review code
- code review
- examine code
- check code
- inspect code

**Use When**: Reviewing code for quality issues, patterns, maintainability

---

### 2. Review Code Accessibility
**Protocol**: Act  
**File**: `prompts/review-code-accessibility.md`

WCAG compliance validation and accessibility standards check.

**Entry Aliases**:
- accessibility review
- wcag review
- accessibility check
- accessibility compliance

**Use When**: Validating web/UI code meets accessibility standards

---

### 3. Review GitHub PR
**Protocol**: Act  
**File**: `prompts/review-github-pr.md`

Pull request analysis with integration and context evaluation.

**Entry Aliases**:
- review pr
- pull request review
- check pr
- github pr

**Use When**: Reviewing pull requests on GitHub

---

### 4. Review Modified Files
**Protocol**: Act  
**File**: `prompts/review-modified-files.md`

Inspect modified files and changes for quality and correctness.

**Entry Aliases**:
- review modified
- review changes
- modified files
- changes review

**Use When**: Validating recent changes before commit

---

### 5. Analyze Function Complexity
**Protocol**: Act  
**File**: `prompts/analyze-function-complexity.md`

Function complexity analysis with optimization recommendations.

**Entry Aliases**:
- analyze complexity
- function complexity
- complexity analysis

**Use When**: Assessing complexity of specific functions

---

### 6. Improve Cyclomatic Complexity
**Protocol**: Propose-Act  
**File**: `prompts/improve-cyclomatic-complexity.md`

Reduce cyclomatic complexity with refactoring suggestions.

**Entry Aliases**:
- improve complexity
- reduce complexity
- cyclomatic

**Use When**: Refactoring high-complexity functions

---

### 7. Fix Code Smells
**Protocol**: Propose-Act  
**File**: `prompts/fix-code-smells.md`

Identify and refactor code smells and anti-patterns.

**Entry Aliases**:
- fix code smells
- code smells
- refactor smells

**Use When**: Addressing code quality issues and patterns

---

### 8. Augment Code Unit Tests
**Protocol**: Propose-Act  
**File**: `prompts/augment-code-unit-test.md`

Enhance unit tests and improve test coverage.

**Entry Aliases**:
- augment tests
- augment unit test
- improve test coverage
- unit test augmentation

**Use When**: Expanding test coverage for existing code

---

### 9. Evolve Code Iteratively
**Protocol**: Act  
**File**: `prompts/evolve-code-iteratively.md`

Incrementally improve and refine code with iterative refinement.

**Entry Aliases**:
- evolve code
- iterative development
- improve iteratively

**Use When**: Continuously improving code quality

---

### 10. Generate Tech Spec from Code
**Protocol**: Act  
**File**: `prompts/generate-tech-spec-from-code.md`

Extract and generate technical specifications from code.

**Entry Aliases**:
- tech spec from code
- spec from code
- extract spec

**Use When**: Documenting code implementation as specification

---

### 11. Create Feature for PR
**Protocol**: Propose-Confirm-Act  
**File**: `prompts/create-feature-for-pr.md`

Create feature implementation for pull request with validation.

**Entry Aliases**:
- create feature
- feature for pr
- feature branch
- extract feature

**Use When**: Developing a new feature ready for PR submission

---

## Integration Points

### With Other Personas

| Persona | Integration | Purpose |
|---------|-------------|---------|
| Architect | Architecture review of implementation | Validate technical decisions |
| Business Analyst | Requirement validation | Ensure code meets requirements |
| Tester | Test planning coordination | Quality assurance alignment |
| Project Manager | Changelog entry creation | Change tracking and versioning |
| Prompt Engineer | AI-assisted coding optimization | Enhance prompt effectiveness |

### With Intent Packages

| Intent Package | Role | Integration |
|---|---|---|
| Java Migration | Primary user | Execute migration tasks |
| PDF Analysis | Secondary | Technology research support |

---

## Workflows

### Code Review Workflow

```
START: review-modified-files
  ↓
INPUT: List of modified files
  ↓
PROCESS: File-by-file review
  ↓
OUTPUT: Issues and recommendations
  ↓
NEXT: review-code (detailed analysis)
  ↓
DECISION: Quality acceptable?
  ├─ YES → Done
  └─ NO → improve-cyclomatic-complexity
```

### Quality Improvement Workflow

```
START: fix-code-smells
  ↓
IDENTIFY: Anti-patterns and code smells
  ↓
REFACTOR: Suggested improvements
  ↓
NEXT: augment-code-unit-test
  ↓
EXPAND: Test coverage
  ↓
NEXT: evolve-code-iteratively
  ↓
REFINE: Incremental improvements
  ↓
END: Quality improved
```

### Feature Development Workflow

```
START: create-feature-for-pr
  ↓
INPUT: Feature requirements and scope
  ↓
DEVELOP: Feature implementation
  ↓
NEXT: review-code-accessibility
  ↓
VALIDATE: Accessibility compliance
  ↓
NEXT: review-github-pr
  ↓
PREPARE: Ready for PR submission
  ↓
END: Feature ready
```

---

## Templates

The package includes standardized templates for common outputs:

- **code-review-report.md** - Structured code review findings
- **refactoring-plan.md** - Refactoring recommendations
- **test-coverage-plan.md** - Test enhancement strategy
- **feature-spec.md** - Feature specification template

---

## Tools

Supporting Python utilities for automated tasks:

- **analyze-complexity.py** - Function complexity metrics
- **extract-spec.py** - Specification extraction
- **validate-accessibility.py** - WCAG compliance checking

---

## Requirements

### Minimum
- OLAF Framework 1.6.0+
- Claude Sonnet 4.5 LLM or equivalent
- Git 2.30+

### Recommended
- Code analysis tools (language-specific)
- Optional: SonarQube for enhanced metrics

### Platforms
- Windows (PowerShell 5.1+)
- Linux (Bash/Zsh)
- macOS

---

## Troubleshooting

| Issue | Resolution |
|-------|-----------|
| LLM unable to analyze code | Ensure code is properly formatted and not too large |
| Accessibility review missing items | Update WCAG standard references in prompts |
| Test augmentation incomplete | Check test framework compatibility |

---

## Maintenance

**Team**: developer  
**Primary Maintainer**: OLAF Framework Core Team  
**Contact**: [Framework Team]

---

## Related Competencies

- **Architect Package**: Technical stack analysis and planning
- **Business Analyst Package**: Requirements clarification
- **Tester Package**: Test plan generation
- **Project Manager Package**: Job and changelog tracking
- **Prompt Engineer Package**: Workflow optimization

---

