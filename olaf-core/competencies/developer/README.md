# Developer Competency Package

Comprehensive developer competency package for software development workflows including code review, analysis, refactoring, testing, and quality improvement.

## Quick Start

1. **Code Review**:
   ```
   "review code" with your-file.ts
   ```

2. **Improve Quality**:
   ```
   "fix code smells" with problematic-function.py
   ```

3. **Enhance Tests**:
   ```
   "augment unit tests" with source-code.java
   ```

## What's Included

### 🎯 Core Competencies (11 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Code Review | `review-code` | Quality and maintainability assessment |
| Accessibility Review | `review-code-accessibility` | WCAG compliance validation |
| PR Review | `review-github-pr` | Pull request analysis |
| Modified Files Review | `review-modified-files` | Changes validation |
| Complexity Analysis | `analyze-function-complexity` | Function complexity assessment |
| Improve Complexity | `improve-cyclomatic-complexity` | Cyclomatic complexity reduction |
| Fix Code Smells | `fix-code-smells` | Anti-pattern refactoring |
| Augment Tests | `augment-code-unit-test` | Test coverage improvement |
| Evolve Code | `evolve-code-iteratively` | Iterative code improvement |
| Tech Spec | `generate-tech-spec-from-code` | Specification extraction |
| Create Feature | `create-feature-for-pr` | Feature development for PR |

### 📁 Structure

```
developer/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/
│   └── developer-competency.md      # Full documentation
├── prompts/
│   ├── review-code.md
│   ├── review-code-accessibility.md
│   ├── review-github-pr.md
│   ├── review-modified-files.md
│   ├── analyze-function-complexity.md
│   ├── improve-cyclomatic-complexity.md
│   ├── fix-code-smells.md
│   ├── augment-code-unit-test.md
│   ├── evolve-code-iteratively.md
│   ├── generate-tech-spec-from-code.md
│   └── create-feature-for-pr.md
├── templates/
│   ├── code-review-report.md
│   ├── refactoring-plan.md
│   ├── test-coverage-plan.md
│   └── feature-spec.md
└── tools/
    ├── analyze-complexity.py
    ├── extract-spec.py
    └── validate-accessibility.py
```

## Key Capabilities

✅ **Code Review** - Quality assessment, patterns, maintainability  
✅ **Accessibility** - WCAG compliance validation  
✅ **Complexity Analysis** - Function and cyclomatic complexity  
✅ **Refactoring** - Code smell detection and fixes  
✅ **Testing** - Unit test augmentation and coverage  
✅ **Specification Extraction** - Documentation from code  
✅ **Feature Development** - PR-ready implementation  

## Common Workflows

### 1. Code Review Workflow
```
review-modified-files 
  → review-code 
  → improve-cyclomatic-complexity
```

### 2. Quality Improvement
```
fix-code-smells
  → augment-code-unit-test
  → evolve-code-iteratively
```

### 3. Feature Development
```
create-feature-for-pr
  → review-code-accessibility
  → review-github-pr
```

## Requirements

- **LLM**: Claude Sonnet 4.5 or equivalent
- **Tools**: Git, language-specific tools
- **Platforms**: Windows, Linux, macOS
- **Framework Version**: OLAF 1.6.0+

## Integration Points

- **Architect Persona**: Architecture review and planning
- **Business Analyst**: Requirement validation
- **Tester**: Test planning coordination
- **Project Manager**: Changelog and job tracking
- **Prompt Engineer**: AI-assisted coding optimization

## Documentation

See `docs/developer-competency.md` for comprehensive documentation.

---

**Version**: 1.0.0  
**Status**: Public Beta  
**Created**: October 21, 2025  
**Maintenance Team**: developer
