# Assess Code Quality Principles: Step-by-Step Tutorial

How to Execute the "Assess Code Quality Principles" Workflow

This tutorial shows exactly how to use the Developer competency's comprehensive code quality assessment workflow to evaluate codebases against established engineering principles (SOLID, DRY, YAGNI) with evidence-based scoring.

## Prerequisites

- Access to OLAF Framework with developer competency pack
- Complete codebase to assess (source code directory)
- Basic understanding of SOLID principles and code quality concepts
- Optional: Existing technical specification for additional context
- File system access to read source files and write assessment reports

## Step-by-Step Instructions

### Step 1: Initialize Quality Assessment

Brief description: Start the comprehensive code quality assessment workflow by invoking the developer competency with the assess quality command.

**User Action:**

1. Navigate to your project workspace
2. Execute the command: `olaf assess quality` or `assess code quality`
3. Prepare to provide application name and codebase path

**System Response:**
The system will prompt for required parameters using Propose-Act protocol and begin gathering assessment inputs.

### Step 2: Provide Assessment Parameters

**User Action:** Provide required parameters when prompted

**Provide Requirements/Parameters:**

- **application_name**: Name for file naming - we used "payment-service" (kebab-case format)
- **code_path**: Path to codebase - we used "./src" (relative or absolute path)
- **tech_spec_path**: Optional tech spec - we used "" (leave empty if not available)
- **focus_areas**: Optional focus - we used [] (empty for all categories)

**Example Input:**
```text
Application Name: payment-service
Code Path: ./src
Tech Spec Path: [press Enter to skip]
Focus Areas: [press Enter for all categories]
```

### Step 3: Codebase Discovery and Analysis

**What System Does:**

- Scans all source files in specified code path
- Identifies file types, languages, and architectural patterns
- Maps module structure and dependencies
- Extracts initial metrics (file count, LOC, complexity)
- Catalogs design patterns and anti-patterns

**You Should See:** Progress indicators showing file discovery and initial analysis completion

### Step 4: SOLID Principles Evaluation

**What System Does:**

- **Single Responsibility**: Analyzes classes for multiple responsibilities and cohesion
- **Open/Closed**: Evaluates extensibility patterns and modification hotspots
- **Liskov Substitution**: Checks inheritance hierarchies and interface implementations
- **Interface Segregation**: Assesses interface design and client dependencies
- **Dependency Inversion**: Evaluates abstraction usage and dependency injection

**You Should See:** SOLID principles assessment with specific code examples and violation counts

### Step 5: Code Quality Metrics Analysis

**What System Does:**

- **DRY Assessment**: Detects code duplication and quantifies impact
- **YAGNI Assessment**: Identifies unused code and over-engineering
- **Complexity Analysis**: Calculates cyclomatic and cognitive complexity
- **Naming Conventions**: Evaluates code readability and consistency
- **Maintainability**: Assesses overall code maintainability index

**You Should See:** Code quality metrics with specific measurements and violation examples

### Step 6: Testing Quality Evaluation

**What System Does:**

- Analyzes test coverage (line, branch, method coverage)
- Evaluates test quality and design patterns
- Assesses test maintainability and effectiveness
- Checks test pyramid compliance
- Identifies missing test scenarios

**You Should See:** Testing quality assessment with coverage percentages and test quality scores

### Step 7: Architecture and Security Assessment

**What System Does:**

**Architecture Quality:**
- Evaluates module structure and package organization
- Analyzes coupling and cohesion metrics
- Identifies circular dependencies
- Assesses layer separation and boundaries

**Security Practices:**
- Reviews input validation patterns
- Evaluates authentication/authorization implementation
- Identifies potential security vulnerabilities
- Assesses cryptographic usage

**Performance Patterns:**
- Detects performance anti-patterns
- Evaluates resource management
- Assesses caching strategies
- Reviews database interaction patterns

**You Should See:** Architecture, security, and performance assessments with specific findings

### Step 8: Evidence Collection and Scoring

**What System Does:**

- Collects specific code examples for each violation
- Quantifies impact of quality issues with metrics
- Calculates scores for each assessment category (A-F scale)
- Computes overall quality score
- Prioritizes findings by impact and effort

**You Should See:** Quality scorecard with grades and supporting evidence

### Step 9: Recommendations and Action Plan

**What System Does:**

- Generates prioritized improvement recommendations
- Provides specific code examples for problems and solutions
- Estimates implementation effort for each recommendation
- Creates action plan organized by priority (high/medium/low)
- Suggests quick wins and long-term improvements

**You Should See:** Comprehensive improvement plan with effort estimates and priorities

### Step 10: Report Generation and Review

**What System Does:**

- Compiles complete assessment report with all findings
- Formats report following OLAF standards
- Saves report to findings directory with timestamp
- Presents summary scorecard for user review
- Requests feedback and incorporates adjustments

**You Should See:** Complete assessment document saved to `olaf-data/findings/assessments/code-quality-assessment-{application_name}-YYYYMMDD-NNN.md`

## Verification Checklist

✅ **Parameters provided**: Application name and code path specified correctly
✅ **Codebase analyzed**: All source files discovered and scanned
✅ **SOLID principles evaluated**: Each principle assessed with evidence
✅ **Code quality measured**: DRY, YAGNI, complexity metrics calculated
✅ **Testing assessed**: Test coverage and quality evaluated
✅ **Architecture reviewed**: Module structure and coupling analyzed
✅ **Security checked**: Security practices and vulnerabilities identified
✅ **Scores calculated**: Grades assigned for each category (A-F scale)
✅ **Recommendations generated**: Prioritized improvement plan created
✅ **Report saved**: Assessment document created in findings directory

## Troubleshooting

**If codebase analysis fails:**

```bash
# Verify code path exists and is accessible
ls -la ./src
# Check file permissions
# Ensure path is relative to workspace root
```

**If assessment seems incomplete:**

- Verify all source files are in specified code_path
- Check that file types are recognized (common languages supported)
- Ensure sufficient file system permissions for reading
- Consider providing tech_spec_path for additional context

**If scores seem inaccurate:**

- Review specific code examples provided as evidence
- Check if focus_areas parameter limited assessment scope
- Verify codebase represents complete application (not partial)
- Consider running assessment on specific modules separately

**If report generation fails:**

```bash
# Verify findings directory exists
mkdir -p olaf-data/findings/assessments
# Check write permissions
# Ensure sufficient disk space
```

## Key Learning Points

1. **Evidence-based assessment**: All grades supported by specific code examples and metrics
2. **Comprehensive evaluation**: Covers SOLID, code quality, testing, architecture, security, and performance
3. **Actionable recommendations**: Prioritized improvements with effort estimates and code examples
4. **Objective scoring**: A-F grading scale with clear criteria for each category
5. **Baseline establishment**: Creates measurable baseline for tracking quality improvements over time

## Next Steps to Try

- Review high-priority recommendations and plan implementation
- Use **fix-code-smells** competency to address specific code smells identified
- Apply **improve-cyclomatic-complexity** to reduce complexity issues
- Use **augment-code-unit-test** to improve test coverage gaps
- Re-run assessment periodically to track quality improvements
- Share scorecard with team to build consensus on quality goals
- Integrate assessment into CI/CD pipeline for continuous monitoring

## Expected Timeline

- **Total assessment time:** 20-60 minutes depending on codebase size and complexity
- **User input required:** Parameter setup and review (5-10 minutes)
- **Codebase analysis:** File discovery and initial scanning (5-15 minutes)
- **Principle evaluation:** SOLID, quality, testing, architecture assessment (10-30 minutes)
- **Report generation:** Scoring, recommendations, and documentation (5-10 minutes)
- **Review and feedback:** User validation and adjustments (5-10 minutes)
