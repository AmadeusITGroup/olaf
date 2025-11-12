# Tutorial: Detect Schema Drift

This tutorial guides you through using the Detect Schema Drift competency to identify and address inconsistencies across your OLAF framework.

## Prerequisites

- OLAF framework installed with multiple competency packs
- Basic understanding of OLAF manifest structure
- Access to IDE or command line with OLAF loaded
- Familiarity with OLAF naming conventions (helpful but not required)

## Scenario

Your OLAF framework has grown to 15 competency packs with contributions from multiple developers. You want to ensure consistency across all packs before the next major release. You'll use drift detection to identify inconsistencies and plan standardization efforts.

## Step 1: Invoke Drift Detection

In your IDE or command line with OLAF loaded:

```
olaf detect schema drift
```

The AI will scan all competency packs and analyze patterns.

## Step 2: Review the Executive Summary

The report starts with a high-level overview:

```markdown
## Executive Summary
- Artifacts analyzed: 15 competency packs
- Drift patterns found: 12
- High-impact drifts: 3
- Medium-impact drifts: 6
- Low-impact drifts: 3
```

**What it means**:
- **High-impact**: Breaks automation or causes functional issues
- **Medium-impact**: Creates maintenance burden or inconsistent UX
- **Low-impact**: Cosmetic issues that don't affect functionality

## Step 3: Analyze Manifest Schema Drift

Review manifest-related drift:

```markdown
## Manifest Schema Drift

### Field Naming Variations
Found 3 different field names for primary identifier:
- 'id': 10 packs (architect, researcher, prompt-engineer, ...)
- 'name': 3 packs (data-analyst, security-auditor, devops)
- 'package': 2 packs (legacy-pack-1, legacy-pack-2)

Recommendation: Standardize on 'id' (most common, matches template)

### Entry Point Structure Variations
Pattern A (12 packs): {name, command, file, protocol, use_case}
Pattern B (2 packs): {name, invoke, path, mode, description}
Pattern C (1 pack): {title, cmd, file, type}

Recommendation: Migrate all to Pattern A (standard template)
```

**Action**: Note which packs need migration and what changes are required.

## Step 4: Review Documentation Structure Drift

Check documentation organization inconsistencies:

```markdown
## Documentation Structure Drift

### Folder Organization Patterns
Pattern A (10 packs): /docs/[entry-point-name]/description.md + tutorial.md
Pattern B (3 packs): /docs/[entry-point-name].md (single file)
Pattern C (2 packs): /documentation/guides/[entry-point-name]/

### File Naming Patterns
- 12 packs use kebab-case
- 2 packs use snake_case
- 1 pack uses camelCase

Recommendation: Standardize on Pattern A with kebab-case naming
```

**Action**: Identify packs with non-standard documentation structure.

## Step 5: Check Naming Convention Drift

Review naming inconsistencies:

```markdown
## Naming Convention Drift

### File Naming Inconsistencies
Kebab-case (standard): 12 packs
Snake_case: 2 packs (data_analyst, security_auditor)
camelCase: 1 pack (legacyPack)

### Command Naming Patterns
Verb-noun pattern: 10 packs ("analyze technical stack", "generate report")
Noun-verb pattern: 3 packs ("technical stack analysis", "report generation")
Mixed: 2 packs

Recommendation: Enforce kebab-case for files, verb-noun for commands
```

**Action**: List files and commands that need renaming.

## Step 6: Assess Impact

Review the impact analysis section:

```markdown
## Impact Analysis

### High Impact (Breaking Changes)
1. Entry point structure variations break documentation generator
   - Affects: data-analyst, security-auditor, legacy-pack-1
   - Impact: Generator can't parse entry points correctly
   - Fix effort: Medium (requires manifest restructuring)

2. Field naming inconsistencies prevent automated validation
   - Affects: 5 packs using 'name' or 'package' instead of 'id'
   - Impact: Validation scripts fail to find identifier
   - Fix effort: Low (simple field rename)

### Medium Impact (Maintenance Issues)
1. Documentation structure variations complicate navigation
   - Affects: 5 packs with non-standard /docs structure
   - Impact: Users can't find documentation consistently
   - Fix effort: Medium (requires file reorganization)
```

**Decision point**: Prioritize high-impact issues for immediate action.

## Step 7: Review Standardization Recommendations

The report provides actionable recommendations:

```markdown
## Standardization Recommendations

### Immediate Actions (This Sprint)
1. Migrate entry_points structure in 3 packs to standard format
2. Rename 'name'/'package' fields to 'id' in 5 manifests
3. Fix file naming in 3 packs (snake_case → kebab-case)

### Short-term Actions (This Quarter)
1. Reorganize documentation in 5 packs to standard structure
2. Standardize command naming patterns across all packs
3. Update templates to prevent future drift

### Long-term Actions (This Year)
1. Implement automated drift detection in CI/CD
2. Create contribution guidelines emphasizing standards
3. Add pre-commit hooks to enforce conventions
```

**Action**: Create tasks for each recommendation based on priority.

## Step 8: Plan Migration Strategy

Review the suggested migration approach:

```markdown
## Migration Strategy

### Phase 1: High-Impact Fixes (Week 1)
1. Run validate-manifest-schema.py to identify all non-compliant manifests
2. Use migrate-manifest-schema.py --dry-run to preview changes
3. Review and approve migration plan
4. Execute migrations with backups
5. Re-validate all manifests

### Phase 2: Documentation Standardization (Week 2-3)
1. Reorganize /docs folders in affected packs
2. Rename files to follow kebab-case
3. Update cross-references and links
4. Validate documentation structure

### Phase 3: Prevention (Week 4)
1. Update templates with clear standards
2. Add validation to CI/CD pipeline
3. Document standards in contribution guide
4. Train contributors on conventions
```

**Action**: Adapt this strategy to your timeline and resources.

## Step 9: Execute Fixes

Start with high-impact issues:

### Fix 1: Standardize Entry Point Structure

For packs using non-standard entry point structure:

1. Open the manifest (e.g., `data-analyst/competency-manifest.json`)
2. Locate the `entry_points` array
3. Restructure each entry point to standard format:

**Before**:
```json
{
  "name": "Analyze Dataset",
  "invoke": "analyze dataset",
  "path": "prompts/analyze-dataset.md",
  "mode": "Act",
  "description": "Perform statistical analysis on datasets"
}
```

**After**:
```json
{
  "name": "Analyze Dataset",
  "command": "analyze dataset",
  "file": "prompts/analyze-dataset.md",
  "protocol": "Act",
  "use_case": "Perform statistical analysis on datasets"
}
```

4. Save and validate

### Fix 2: Rename Identifier Fields

For manifests using 'name' or 'package' instead of 'id':

1. Open the manifest
2. Add 'id' field with kebab-case value
3. Keep existing 'name' field for human-readable name

**Before**:
```json
{
  "package": "data-analyst",
  "version": "1.0.0",
  ...
}
```

**After**:
```json
{
  "id": "data-analyst",
  "name": "Data Analyst",
  "version": "1.0.0",
  ...
}
```

### Fix 3: Standardize File Naming

For files using snake_case or camelCase:

1. Rename files to kebab-case:
   - `analyze_dataset.md` → `analyze-dataset.md`
   - `generateReport.md` → `generate-report.md`

2. Update all references to renamed files:
   - Manifest entry_points
   - Documentation links
   - Cross-references

## Step 10: Validate After Fixes

After making changes, validate to confirm drift is resolved:

```
olaf validate olaf artifacts
```

Then run drift detection again:

```
olaf detect schema drift
```

Expected result:

```markdown
## Executive Summary
- Artifacts analyzed: 15 competency packs
- Drift patterns found: 3 (down from 12)
- High-impact drifts: 0 (down from 3)

Significant improvement. Remaining drift is low-impact cosmetic issues.
```

## Step 11: Document and Monitor

1. **Save the report**: Store in `olaf-data/drift-reports/drift-report-2025-10-27.md`
2. **Track metrics**: Note drift count and severity for trend analysis
3. **Schedule next check**: Set quarterly reminder for drift detection
4. **Update guidelines**: Document standards to prevent future drift

## Common Scenarios

### Scenario A: After Onboarding New Contributors

New contributors may not follow established patterns:

```
olaf detect schema drift
```

Look for:
- New packs with non-standard structures
- Naming convention violations
- Template deviations

**Action**: Provide feedback to contributors and update onboarding docs.

### Scenario B: Before Major Release

Ensure consistency before publishing:

```
olaf detect schema drift
```

**Decision criteria**:
- High-impact drift: Must fix before release
- Medium-impact drift: Fix if time permits
- Low-impact drift: Schedule for next release

### Scenario C: Framework Evolution

When introducing new standards:

```
olaf detect schema drift
```

Identify packs still using old patterns and plan migration.

## Troubleshooting

### Issue: Too Many Drift Patterns

**Problem**: Report shows 30+ drift patterns, overwhelming to address.

**Solution**:
1. Focus on high-impact drift first
2. Group similar patterns (e.g., all naming issues)
3. Fix one pattern type at a time
4. Use automated migration tools where possible

### Issue: Unclear Which Pattern is "Correct"

**Problem**: Multiple patterns exist, unclear which to standardize on.

**Solution**:
1. Check the official template in competency-creation pack
2. Use the most common pattern (majority wins)
3. Consider which pattern best supports automation
4. Document the decision for future reference

### Issue: Breaking Changes Required

**Problem**: Standardization requires breaking changes to existing packs.

**Solution**:
1. Plan migration carefully with version bumps
2. Support legacy patterns temporarily during transition
3. Communicate changes to users
4. Provide migration guide for affected users

## Best Practices

1. **Run quarterly**: Regular drift detection catches issues early
2. **Fix high-impact first**: Prioritize issues that break functionality
3. **Automate prevention**: Add validation to CI/CD to prevent new drift
4. **Document standards**: Clear guidelines prevent drift at creation
5. **Track trends**: Monitor drift metrics over time
6. **Communicate**: Share findings with team and contributors
7. **Be pragmatic**: Not all drift needs immediate fixing

## Next Steps

After detecting drift:

1. **Prioritize fixes**: Use impact analysis to guide priorities
2. **Execute migration**: Use migration tools to standardize artifacts
3. **Validate results**: Confirm drift is resolved
4. **Prevent recurrence**: Update templates and add validation
5. **Generate report**: Use `olaf generate validation report` for comprehensive QA

## Related Tutorials

- [Validate OLAF Artifacts Tutorial](../validate-olaf-artifacts/tutorial.md)
- [Generate Validation Report Tutorial](../generate-validation-report/tutorial.md)
- [Migrate Manifest Schema (Python script usage)](../../README.md#migration-scripts)

## Summary

You've learned how to:
- Invoke drift detection
- Interpret drift reports
- Assess impact of drift patterns
- Plan standardization efforts
- Execute fixes systematically
- Validate results
- Prevent future drift

Regular drift detection keeps OLAF consistent and maintainable as it evolves.
