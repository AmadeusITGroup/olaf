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

4. **Learn Better Prompting**:
   ```
   "coach prompts"
   Language: Python, Level: intermediate, Project: API endpoint
   ```

## What's Included

### 🎯 Core Competencies (15 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Code Review | `review-code` | Quality and maintainability assessment |
| Accessibility Review | `review-code-accessibility` | WCAG compliance validation |
| PR Review | `review-github-pr` | Pull request analysis |
| Complexity Analysis | `analyze-function-complexity` | Function complexity assessment |
| Improve Complexity | `improve-cyclomatic-complexity` | Cyclomatic complexity reduction |
| Fix Code Smells | `fix-code-smells` | Anti-pattern refactoring |
| Augment Tests | `augment-code-unit-test` | Test coverage improvement |
| Evolve Code | `evolve-code-iteratively` | Iterative code improvement |
| Tech Spec | `generate-tech-spec-from-code` | Specification extraction |
| Deepen Tech Spec | `deepen-tech-spec-developer` | Deep-dive technical analysis |
| Check TODOs | `check-todos-in-code` | TODO comment analysis and resolution |
| Assess Quality | `assess-code-quality-principles` | Code quality principles evaluation |
| Detect Test Directives | `detect-test-directives` | Test directive discovery |
| **Coach Prompts** | `coach-developers-to-prompt` | **Interactive prompt engineering training** |

### 📁 Structure

```
developer/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/
│   ├── developer-competency.md      # Full documentation
│   ├── review-code/                 # Code review docs
│   ├── fix-code-smells/             # Code smells docs
│   ├── coach-developers-to-prompt/  # Prompt training docs
│   └── ... (other competency docs)
├── prompts/
│   ├── review-code.md
│   ├── review-code-accessibility.md
│   ├── review-github-pr.md
│   ├── analyze-function-complexity.md
│   ├── improve-cyclomatic-complexity.md
│   ├── fix-code-smells.md
│   ├── augment-code-unit-test.md
│   ├── evolve-code-iteratively.md
│   ├── generate-tech-spec-from-code.md
│   ├── deepen-tech-spec-developer.md
│   ├── check-todos-in-code.md
│   ├── assess-code-quality-principles.md
│   ├── detect-test-directives.md
│   └── coach-developers-to-prompt   # NEW: Prompt training
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
✅ **Quality Assessment** - SOLID, DRY, YAGNI principles evaluation  
✅ **TODO Management** - TODO comment analysis and resolution  
✅ **Prompt Engineering Training** - Interactive coaching for better AI prompts  

## Common Workflows

### 1. Code Review Workflow
```
review-code 
  → improve-cyclomatic-complexity
  → assess-code-quality-principles
```

### 2. Quality Improvement
```
fix-code-smells
  → augment-code-unit-test
  → evolve-code-iteratively
```

### 3. Prompt Engineering Training
```
coach-developers-to-prompt
  → practice with real scenarios
  → apply learnings to actual development
```

### 4. TODO & Technical Debt
```
check-todos-in-code
  → fix-code-smells
  → review-code
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

- **Main Documentation**: `docs/developer-competency.md` - Comprehensive package documentation
- **Competency-Specific Docs**: `docs/<competency-name>/` - Individual competency guides
  - `description.md` - Overview, parameters, and usage
  - `tutorial.md` - Step-by-step tutorials and examples

**Featured Documentation**:
- `docs/coach-developers-to-prompt/` - Interactive prompt engineering training guide

---

**Version**: 1.0.0  
**Status**: Public Beta  
**Created**: October 21, 2025  
**Maintenance Team**: developer
