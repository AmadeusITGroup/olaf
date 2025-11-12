# Generate Validation Report

## Purpose
Create comprehensive quality assurance reports for OLAF framework artifacts, combining automated validation results with AI-assisted analysis to provide actionable insights for maintainers.

## Protocol
**Propose-Act** - Propose report structure and scope, then generate upon approval

## Context Required
- Results from validation scripts (manifest, template, documentation validators)
- Access to OLAF framework structure
- Understanding of OLAF quality standards
- Historical context of previous validation reports (if available)

## Report Scope

### 1. Validation Results Summary
Aggregate findings from:
- Manifest schema validation
- Documentation structure validation
- Template compliance checking
- File reference validation
- Schema drift detection

### 2. Quality Metrics
Calculate and report:
- **Completeness**: % of entry points with full documentation
- **Compliance**: % of artifacts following templates
- **Consistency**: % of manifests using standard schema
- **Integrity**: % of file references that resolve correctly
- **Coverage**: % of competency packs with complete docs

### 3. Issue Categorization
Organize issues by:
- **Severity**: Critical, High, Medium, Low
- **Type**: Schema, Documentation, Template, Reference, Naming
- **Impact**: Breaking, Degraded, Cosmetic
- **Effort**: Quick fix, Moderate, Significant

### 4. Trend Analysis
Compare with previous reports:
- Quality metrics over time
- New issues introduced
- Issues resolved
- Recurring patterns
- Improvement areas

### 5. Actionable Recommendations
Provide:
- Prioritized fix list
- Quick wins (high impact, low effort)
- Long-term improvements
- Process recommendations
- Automation opportunities

## Execution Steps

1. **Gather Validation Data**
   - Run or collect results from validation scripts
   - Execute schema drift detection
   - Perform template compliance checks
   - Validate file references
   - Check documentation completeness

2. **Calculate Quality Metrics**
   - Count total artifacts
   - Calculate compliance percentages
   - Measure completeness scores
   - Assess consistency levels
   - Track coverage metrics

3. **Categorize and Prioritize Issues**
   - Group issues by type and severity
   - Assess impact on users and maintainers
   - Estimate fix effort
   - Identify dependencies between issues
   - Prioritize based on impact/effort matrix

4. **Analyze Trends**
   - Compare with previous reports (if available)
   - Identify improvement or degradation
   - Spot recurring issues
   - Detect new patterns
   - Measure progress on previous recommendations

5. **Generate Recommendations**
   - Identify quick wins
   - Propose systematic fixes
   - Suggest process improvements
   - Recommend automation opportunities
   - Create action plan with timeline

6. **Format and Present Report**
   - Use validation report template
   - Include executive summary
   - Provide detailed findings
   - Add visual representations (charts, graphs)
   - Ensure actionability

## Report Structure

Use the validation report template at:
`olaf-core/competencies/olaf-specific-tools/templates/validation-report-template.md`

### Key Sections

1. **Executive Summary**
   - Overall quality score
   - Key findings
   - Critical issues count
   - Top recommendations

2. **Quality Metrics Dashboard**
   - Completeness: X%
   - Compliance: X%
   - Consistency: X%
   - Integrity: X%
   - Coverage: X%

3. **Detailed Findings**
   - Critical issues (must fix)
   - High priority issues (should fix)
   - Medium priority issues (nice to fix)
   - Low priority issues (optional)

4. **Issue Breakdown by Type**
   - Manifest issues
   - Documentation issues
   - Template compliance issues
   - File reference issues
   - Naming convention issues

5. **Trend Analysis**
   - Metrics over time
   - Progress on previous issues
   - New issues introduced
   - Quality trajectory

6. **Recommendations**
   - Immediate actions (this sprint)
   - Short-term actions (this quarter)
   - Long-term improvements (this year)
   - Process improvements
   - Automation opportunities

7. **Action Plan**
   - Prioritized task list
   - Estimated effort
   - Suggested owners
   - Dependencies
   - Timeline

## Output Format

The report should be saved as:
`olaf-data/validation-reports/validation-report-YYYY-MM-DD.md`

Include:
- Date of report generation
- OLAF version/commit hash
- Scope of validation
- Tools and scripts used
- Report author (AI + human reviewer)

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
- **90-100%**: Excellent - Minor issues only
- **75-89%**: Good - Some improvements needed
- **60-74%**: Fair - Significant issues to address
- **Below 60%**: Poor - Major quality concerns

## Visualization Recommendations

Include visual elements:
- Quality metrics radar chart
- Issue distribution pie chart
- Trend line graphs
- Priority matrix (impact vs effort)
- Compliance heatmap by competency pack

## Success Criteria
- Report is comprehensive and actionable
- All validation results are included
- Issues are properly categorized and prioritized
- Recommendations are specific and achievable
- Trends are identified and explained
- Action plan is clear and realistic

## Related Competencies
- **validate-olaf-artifacts**: Run comprehensive validation
- **detect-schema-drift**: Identify inconsistencies

## Usage Example

```
# In IDE or command line
olaf generate validation report

# AI will:
1. Propose report scope and structure
2. Wait for approval
3. Run all validation checks
4. Analyze results
5. Generate comprehensive report
6. Save to olaf-data/validation-reports/
```

## Notes
- Generate reports before major releases
- Compare reports over time to track quality trends
- Share reports with team for visibility
- Use reports to guide improvement efforts
- Archive reports for historical reference
- Consider automating report generation in CI/CD
