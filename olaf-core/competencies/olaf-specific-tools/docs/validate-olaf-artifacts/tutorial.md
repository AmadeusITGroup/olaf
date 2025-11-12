# Tutorial: Validate OLAF Artifacts

This tutorial walks you through using the Validate OLAF Artifacts competency to ensure your OLAF framework maintains quality and consistency.

## Prerequisites

- OLAF framework installed and accessible
- Basic understanding of OLAF structure (competency packs, manifests, documentation)
- Access to IDE or command line with OLAF loaded
- Familiarity with OLAF manifest schema (optional but helpful)

## Scenario

You're preparing to release OLAF v1.7.0 and need to ensure all competency packs meet quality standards. You want to validate manifests, check documentation completeness, and verify all file references before publishing.

## Step 1: Invoke the Validation Competency

In your IDE or command line with OLAF loaded, invoke the competency:

```
olaf validate olaf artifacts
```

The AI will immediately begin scanning your OLAF framework structure.

## Step 2: Review the Validation Report

The AI will generate a comprehensive report. Here's what to look for:

### Summary Section

```markdown
## Summary
- Total competency packs scanned: 15
- Total manifests validated: 15
- Total documentation files checked: 87
- Critical issues: 2
- Warnings: 8
- Info items: 5
```

**What it means**:
- **Critical issues**: Must be fixed before release (breaks functionality)
- **Warnings**: Should be fixed (quality issues)
- **Info items**: Nice to have (suggestions for improvement)

### Critical Issues Section

```markdown
## Critical Issues
1. architect/competency-manifest.json: Missing required field 'entry_points'
2. researcher/docs/challenge-me/description.md: File not found
```

**Action**: Fix these immediately. They prevent competencies from working correctly.

### Warnings Section

```markdown
## Warnings
1. prompt-engineer/competency-manifest.json: Recommended field 'id' missing
2. architect/docs/README.md: Broken link to analyze-technical-stack/tutorial.md
3. competency-creation: Description exceeds 2-page guideline (850 words)
```

**Action**: Address before release for quality and consistency.

### Informational Section

```markdown
## Informational
1. Consider adding 'tags' field to 5 manifests for better discoverability
2. 3 tutorials missing troubleshooting sections
```

**Action**: Optional improvements for future releases.

## Step 3: Fix Critical Issues

Let's fix the critical issues identified:

### Issue 1: Missing 'entry_points' field

**Problem**: `architect/competency-manifest.json` is missing the required `entry_points` array.

**Fix**:
1. Open `olaf-core/competencies/architect/competency-manifest.json`
2. Add the `entry_points` array with all entry point definitions:

```json
{
  "name": "Architect",
  "version": "1.0.0",
  "description": "...",
  "category": "architecture",
  "entry_points": [
    {
      "name": "Analyze Technical Stack",
      "command": "analyze technical stack",
      "file": "prompts/analyze-technical-stack.md",
      "protocol": "Act",
      "use_case": "Evaluate current technology landscape"
    }
  ]
}
```

3. Save the file

### Issue 2: Missing documentation file

**Problem**: `researcher/docs/challenge-me/description.md` doesn't exist but is referenced.

**Fix**:
1. Create the missing file: `olaf-core/competencies/researcher/docs/challenge-me/description.md`
2. Use the description template to populate it
3. Or use the competency-creation pack to generate it properly

## Step 4: Address Warnings

### Fix Broken Links

**Problem**: `architect/docs/README.md` has a broken link.

**Fix**:
1. Open `olaf-core/competencies/architect/docs/README.md`
2. Find the broken link: `[Tutorial](analyze-technical-stack/tutorial.md)`
3. Verify the correct path (should it be `./analyze-technical-stack/tutorial.md`?)
4. Update the link
5. Save the file

### Add Recommended Fields

**Problem**: Several manifests missing recommended `id` field.

**Fix**:
1. Open each manifest mentioned
2. Add the `id` field with kebab-case identifier:

```json
{
  "id": "prompt-engineer",
  "name": "Prompt Engineer",
  ...
}
```

## Step 5: Re-Validate After Fixes

After making fixes, run validation again to confirm:

```
olaf validate olaf artifacts
```

Expected output:

```markdown
## Summary
- Total competency packs scanned: 15
- Critical issues: 0
- Warnings: 3
- Info items: 5

All critical checks passed. Ready for release.
```

## Step 6: Review Remaining Issues

With critical issues resolved, review remaining warnings and info items:

**Decision points**:
- Can warnings be fixed quickly? → Fix them now
- Do warnings affect user experience? → Prioritize for this release
- Are info items valuable? → Schedule for next release

## Step 7: Document Validation Results

Save the validation report for your records:

1. Copy the validation output
2. Save to `olaf-data/validation-reports/validation-report-2025-10-27.md`
3. Include in release notes if relevant

## Common Scenarios

### Scenario A: New Competency Pack Validation

After creating a new competency pack:

```
olaf validate olaf artifacts
```

Focus on issues related to your new pack. Common issues:
- Missing manifest fields
- Incomplete documentation
- File reference errors
- Template non-compliance

### Scenario B: Quarterly Quality Check

Run validation quarterly to catch drift:

```
olaf validate olaf artifacts
```

Look for patterns:
- Multiple packs with similar issues (indicates need for better templates)
- Increasing warnings over time (indicates quality degradation)
- New types of issues (indicates evolving standards)

### Scenario C: CI/CD Integration

For automated validation in CI/CD, use Python scripts instead:

```bash
python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --all --strict
python olaf-core/competencies/olaf-specific-tools/scripts/validate-docs-structure.py --all
```

These provide exit codes for build pipelines.

## Troubleshooting

### Issue: Too Many Warnings

**Problem**: Validation reports 50+ warnings, overwhelming to fix.

**Solution**:
1. Focus on critical issues first
2. Group warnings by type
3. Fix one type at a time (e.g., all missing 'id' fields)
4. Use Python scripts to batch-fix similar issues

### Issue: False Positives

**Problem**: Validation reports issues that aren't actually problems.

**Solution**:
1. Review the specific issue carefully
2. Check if your artifact follows a newer standard
3. Update validation scripts if standards have evolved
4. Document exceptions in validation report

### Issue: Validation Takes Too Long

**Problem**: Validation of large OLAF installations is slow.

**Solution**:
1. Use Python scripts for faster automated checks
2. Validate specific competency packs: modify scripts to target specific directories
3. Run full validation less frequently (e.g., before releases only)
4. Use AI validation for semantic checks, scripts for syntax checks

## Best Practices

1. **Validate before committing**: Quick check before pushing changes
2. **Validate before releases**: Comprehensive check before publishing
3. **Fix critical issues immediately**: Don't let them accumulate
4. **Track warnings over time**: Monitor quality trends
5. **Document exceptions**: Note why certain warnings are acceptable
6. **Automate where possible**: Use Python scripts in CI/CD
7. **Share reports**: Keep team informed of quality status

## Next Steps

After validating artifacts:

1. **Generate comprehensive report**: Use `olaf generate validation report` for detailed QA analysis
2. **Detect schema drift**: Run `olaf detect schema drift` to find inconsistencies
3. **Fix issues systematically**: Address critical, then high-priority issues
4. **Re-validate**: Confirm fixes resolved issues
5. **Document results**: Save reports for historical tracking

## Related Tutorials

- [Detect Schema Drift Tutorial](../detect-schema-drift/tutorial.md)
- [Generate Validation Report Tutorial](../generate-validation-report/tutorial.md)
- [Create Competency Pack Tutorial](../../competency-creation/docs/create-competency-pack/tutorial.md)

## Summary

You've learned how to:
- Invoke the Validate OLAF Artifacts competency
- Interpret validation reports
- Fix critical issues and warnings
- Re-validate after fixes
- Integrate validation into your workflow

Regular validation ensures OLAF maintains high quality and consistency as it grows.
