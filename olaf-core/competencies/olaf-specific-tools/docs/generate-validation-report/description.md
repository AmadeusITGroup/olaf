# Generate Validation Report

## Overview

The Generate Validation Report competency creates comprehensive quality assurance reports for OLAF framework artifacts by combining automated validation results with AI-assisted analysis. It provides actionable insights, quality metrics, trend analysis, and prioritized recommendations for maintainers.

## Purpose

While individual validation tools check specific aspects of OLAF (manifests, documentation, templates), this competency provides a holistic view of framework quality by:

- Aggregating results from multiple validation sources
- Calculating quality metrics and scores
- Analyzing trends over time
- Categorizing and prioritizing issues
- Providing actionable recommendations
- Creating executive summaries for stakeholders
- Tracking improvement progress

This comprehensive reporting helps maintainers make informed decisions about quality improvements and resource allocation.

## When to Use

Use this competency:

- **Before major releases**: Comprehensive quality assessment before publishing
- **Quarterly reviews**: Regular quality audits and trend analysis
- **After major contributions**: Assess impact of new features or packs
- **Quality planning**: Identify improvement priorities and estimate effort
- **Stakeholder reporting**: Communicate quality status to leadership
- **Historical tracking**: Document quality evolution over time

## Usage

**Command**: `olaf generate validation report`

**Protocol**: Propose-Act (proposes report structure and scope, then generates upon approval)

**Context Required**:
- Results from validation scripts (manifest, template, documentation validators)
- Access to OLAF framework structure
- Understanding of OLAF quality standards
- Historical context of previous validation reports (if available)

## Report Scope

### 1. Validation Results Summary

Aggregates findings from:
- Manifest schema validation
- Documentation structure validation
- Template compliance checking
- File reference validation
- Schema drift detection

### 2. Quality Metrics

Calculates and reports:
- **Completeness**: % of entry points with full documentation
- **Compliance**: % of artifacts following templates
- **Consistency**: % of manifests using standard schema
- **Integrity**: % of file references that resolve correctly
- **Coverage**: % of competency packs with complete docs

### 3. Issue Categorization

Organizes issues by:
- **Severity**: Critical, High, Medium, Low
- **Type**: Schema, Documentation, Template, Reference, Naming
- **Impact**: Breaking, Degraded, Cosmetic
- **Effort**: Quick fix, Moderate, Significant

### 4. Trend Analysis

Compares with previous reports:
- Quality metrics over time
- New issues introduced
- Issues resolved
- Recurring patterns
- Improvement areas

### 5. Actionable Recommendations

Provides:
- Prioritized fix list
- Quick wins (high impact, low effort)
- Long-term improvements
- Process recommendations
- Automation opportunities

## Output

The competency generates a comprehensive report saved to:
`olaf-data/validation-reports/validation-report-YYYY-MM-DD.md`

Report structure:

```markdown
# OLAF Validation Report - 2025-10-27

## Executive Summary
- Overall Quality Score: 82/100 (Good)
- Critical Issues: 2
- High Priority Issues: 8
- Medium Priority Issues: 15
- Low Priority Issues: 5

## Quality Metrics Dashboard
- Completeness: 85%
- Compliance: 78%
- Consistency: 90%
- Integrity: 95%
- Coverage: 80%

## Detailed Findings
[Categorized issues with descriptions and locations]

## Issue Breakdown by Type
[Manifest, Documentation, Template, Reference, Naming issues]

## Trend Analysis
[Comparison with previous reports, progress tracking]

## Recommendations
[Prioritized actions: immediate, short-term, long-term]

## Action Plan
[Specific tasks with effort estimates and priorities]
```

## Quality Scoring

### Overall Quality Score Calculation

```
Overall Score = (
  Completeness * 0.25 +
  Compliance * 0.25 +
  Consistency * 0.20 +
  Integrity * 0.20 +
  Coverage * 0.10
)
```

### Score Interpretation

- **90-100%**: Excellent - Minor issues only, ready for release
- **75-89%**: Good - Some improvements needed, acceptable for release
- **60-74%**: Fair - Significant issues to address before release
- **Below 60%**: Poor - Major quality concerns, not ready for release

## Workflow

### Step 1: Propose Report Scope

The AI proposes:
- Which validation checks to run
- Report structure and sections
- Comparison with previous reports (if available)
- Estimated time to complete

### Step 2: Wait for Approval

User reviews and can:
- Approve as proposed
- Request modifications to scope
- Add specific areas of focus
- Exclude certain checks

### Step 3: Execute Validation

The AI:
- Runs or collects validation results
- Executes schema drift detection
- Checks template compliance
- Validates file references
- Assesses documentation completeness

### Step 4: Analyze Results

The AI:
- Calculates quality metrics
- Categorizes and prioritizes issues
- Compares with historical data (if available)
- Identifies trends and patterns
- Generates recommendations

### Step 5: Generate Report

The AI:
- Formats report using template
- Includes visualizations (charts, graphs)
- Adds executive summary
- Provides actionable recommendations
- Saves to validation-reports directory

## Parameters

This competency accepts optional parameters during the proposal phase:

- **Scope**: Full (all checks) or Partial (specific areas)
- **Comparison**: Include trend analysis vs previous reports
- **Focus areas**: Specific competency packs or artifact types
- **Detail level**: Executive summary only or comprehensive details

## Success Criteria

Report generation is successful when:
- All requested validation checks are completed
- Quality metrics are calculated accurately
- Issues are properly categorized and prioritized
- Recommendations are specific and achievable
- Trends are identified and explained (if historical data available)
- Report is saved and accessible

## Examples

### Example 1: Pre-Release Comprehensive Report

Before OLAF v1.7.0 release:

```
User: olaf generate validation report

AI: I'll generate a comprehensive validation report for OLAF. This will include:
- Manifest schema validation (all 15 packs)
- Documentation completeness check
- Template compliance verification
- File reference validation
- Schema drift detection
- Quality metrics calculation
- Comparison with v1.6.0 report (if available)

Estimated time: 3-5 minutes

Proceed with this scope?

User: Yes

AI: [Executes all validations and generates report]

Report saved to: olaf-data/validation-reports/validation-report-2025-10-27.md

## Executive Summary
- Overall Quality Score: 85/100 (Good)
- Improvement from v1.6.0: +7 points
- Critical Issues: 0 (down from 3)
- Ready for release with minor improvements

## Key Findings
1. All critical issues from v1.6.0 resolved
2. Documentation completeness improved from 75% to 85%
3. 3 new competency packs added, all compliant
4. 2 high-priority issues remain (broken links)

## Recommendations
1. Fix 2 broken documentation links (quick win)
2. Add missing tutorials for 3 entry points
3. Consider automating validation in CI/CD
```

### Example 2: Focused Report on New Contributions

After adding 3 new competency packs:

```
User: olaf generate validation report focusing on the new data-analyst, security-auditor, and devops packs

AI: I'll generate a focused validation report for the 3 new competency packs:
- Manifest validation
- Documentation completeness
- Template compliance
- Comparison with existing pack quality

Proceed?

User: Yes

AI: [Validates new packs and generates report]

## Executive Summary - New Packs Assessment
- Packs evaluated: 3 (data-analyst, security-auditor, devops)
- Average quality score: 72/100 (Fair)
- Critical issues: 2
- Comparison: Below average (framework average: 85/100)

## Findings
1. data-analyst: Missing 'id' field in manifest (critical)
2. security-auditor: Incomplete documentation (3 entry points missing tutorials)
3. devops: Non-standard entry point structure (high priority)

## Recommendations
1. Fix critical manifest issue in data-analyst immediately
2. Complete documentation for security-auditor
3. Migrate devops manifest to standard structure
4. Re-validate after fixes to meet framework standards
```

## Related Competencies

- **validate-olaf-artifacts**: Runs comprehensive validation checks
- **detect-schema-drift**: Identifies inconsistencies for trend analysis
- **competency-creation/create-competency-pack**: Use standards to prevent issues

## Integration with Validation Tools

This competency orchestrates multiple validation tools:

### Python Scripts
- `validate-manifest-schema.py`: Automated manifest checks
- `validate-docs-structure.py`: Documentation validation
- `validate-template-compliance.py`: Template compliance

### AI Competencies
- `validate-olaf-artifacts`: Comprehensive AI-assisted validation
- `detect-schema-drift`: Schema consistency analysis

The report combines:
- Automated script results (precise, fast)
- AI analysis (contextual, semantic)
- Historical comparison (trend identification)
- Human-readable recommendations (actionable)

## Visualization Recommendations

Reports can include visual elements:
- **Quality metrics radar chart**: Shows 5 quality dimensions
- **Issue distribution pie chart**: Breakdown by severity
- **Trend line graphs**: Quality over time
- **Priority matrix**: Impact vs effort for issues
- **Compliance heatmap**: By competency pack

## Notes

- Generate reports before major releases for quality assurance
- Compare reports over time to track quality trends
- Share reports with team for visibility and alignment
- Use reports to guide improvement efforts and resource allocation
- Archive reports for historical reference and compliance
- Consider automating report generation in CI/CD for continuous monitoring
- Reports inform decision-making about release readiness
- Trend analysis helps identify systemic issues vs one-off problems
