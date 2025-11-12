# Validate OLAF Artifacts

## Overview

The Validate OLAF Artifacts competency performs comprehensive end-to-end validation of OLAF framework artifacts to ensure consistency, completeness, and compliance with OLAF standards. It checks manifests, documentation, templates, and file references across all competency packs.

## Purpose

As OLAF grows with more competency packs and contributors, maintaining quality and consistency becomes challenging. This competency automates the validation process to:

- Catch schema violations and inconsistencies early
- Ensure all entry points have complete documentation
- Verify file references and links are valid
- Check template compliance across artifacts
- Prevent quality degradation over time
- Provide actionable feedback for fixes

## When to Use

Use this competency:

- **Before releases**: Validate all artifacts before publishing new OLAF versions
- **After major changes**: Verify integrity after significant framework updates
- **During code reviews**: Check that new competency packs meet standards
- **Troubleshooting**: Diagnose issues with manifests or documentation
- **Quality audits**: Periodic comprehensive quality checks

## Usage

**Command**: `olaf validate olaf artifacts`

**Protocol**: Act (executes immediately and reports findings)

**Context Required**:
- Access to OLAF framework structure (olaf-core, olaf-data, docs)
- Understanding of OLAF manifest schema
- Knowledge of documentation templates and standards

## What It Validates

### 1. Manifest Validation

Checks all `competency-manifest.json` files for:
- Required fields (id, name, description, category, entry_points)
- Schema compliance with standard structure
- Valid JSON syntax and data types
- Entry point completeness (name, command, file, protocol, use_case)
- Protocol values (Act, Propose-Act, Propose-Confirm-Act)
- File references in entry_points
- Naming conventions (kebab-case for ids)

### 2. Documentation Validation

Verifies documentation structure and completeness:
- Each entry point has description.md and tutorial.md
- Proper /docs folder hierarchy in competency packs
- README.md index files in each pack's docs folder
- All internal links resolve correctly
- Files follow kebab-case naming convention
- No orphaned or unreferenced files

### 3. Template Compliance

Ensures artifacts match their templates:
- Competency descriptions follow description template structure
- Tutorials follow tutorial template format
- README files include required sections
- Manifests follow manifest template structure
- Consistent section ordering

### 4. File Reference Integrity

Validates all file references:
- #[[file:...]] references in markdown documents resolve
- Manifest prompt file paths are valid
- Documentation links work correctly
- Cross-references between documents are valid

## Output

The competency generates a comprehensive validation report with:

- **Summary**: Total artifacts scanned, issues found by severity
- **Critical Issues**: Problems that break functionality or prevent usage
- **Warnings**: Issues that should be fixed but don't break functionality
- **Informational**: Suggestions for improvement
- **Recommendations**: Prioritized action items for fixes

Example output structure:

```markdown
# OLAF Artifacts Validation Report

## Summary
- Total competency packs scanned: 15
- Total manifests validated: 15
- Total documentation files checked: 87
- Critical issues: 2
- Warnings: 8
- Info items: 5

## Critical Issues
1. architect/competency-manifest.json: Missing required field 'entry_points'
2. researcher/docs/challenge-me/description.md: File not found

## Warnings
1. prompt-engineer/competency-manifest.json: Recommended field 'id' missing
2. architect/docs/README.md: Broken link to analyze-technical-stack/tutorial.md
...

## Recommendations
1. Fix critical manifest issues immediately
2. Add missing documentation files
3. Update broken links in README files
4. Add recommended fields to manifests
```

## Parameters

This competency requires no parameters. It automatically:
- Scans all competency packs in olaf-core/competencies/
- Validates all manifests found
- Checks all documentation in /docs folders
- Verifies all file references

## Success Criteria

Validation is successful when:
- All manifests are valid JSON and follow standard schema
- All entry points have complete documentation (description + tutorial)
- All file references resolve correctly
- No broken links in documentation
- Template compliance is verified
- No critical issues found

## Examples

### Example 1: Pre-Release Validation

Before releasing OLAF v1.7.0:

```
User: olaf validate olaf artifacts

AI: [Scans all competency packs and generates report]

# OLAF Artifacts Validation Report

## Summary
- Total competency packs scanned: 15
- Critical issues: 0
- Warnings: 3
- Info items: 2

All critical checks passed. Ready for release.

## Warnings
1. competency-creation: Missing 'updated' field in manifest
2. architect: Description for 'analyze-technical-stack' exceeds 2 pages
3. researcher: Tutorial for 'challenge-me' missing troubleshooting section

## Recommendations
- Update manifest timestamps before release
- Condense architect description to meet 2-page guideline
- Add troubleshooting section to researcher tutorial
```

### Example 2: After Adding New Competency Pack

After creating a new "data-analyst" competency pack:

```
User: olaf validate olaf artifacts

AI: [Validates all artifacts including new pack]

# OLAF Artifacts Validation Report

## Summary
- Total competency packs scanned: 16
- Critical issues: 3
- Warnings: 1

## Critical Issues
1. data-analyst/competency-manifest.json: Missing required field 'category'
2. data-analyst/docs/analyze-dataset/description.md: File not found
3. data-analyst/docs/analyze-dataset/tutorial.md: File not found

## Recommendations
1. Add 'category' field to data-analyst manifest
2. Create description.md for analyze-dataset entry point
3. Create tutorial.md for analyze-dataset entry point
4. Re-validate after fixes
```

## Related Competencies

- **detect-schema-drift**: Identifies schema variations and inconsistencies across artifacts
- **generate-validation-report**: Creates detailed QA reports with trend analysis
- **competency-creation/create-competency-pack**: Use validated templates when creating new packs

## Integration with Python Scripts

This AI-assisted competency complements the automated Python validation scripts:

- **validate-manifest-schema.py**: Automated manifest validation
- **validate-docs-structure.py**: Automated documentation checks
- **validate-template-compliance.py**: Automated template compliance

The AI competency provides:
- Semantic understanding of issues
- Contextual recommendations
- Prioritization of fixes
- Natural language explanations

Use Python scripts for:
- CI/CD automation
- Quick command-line checks
- Batch processing
- Detailed technical reports

## Notes

- This validation should be run before major releases
- Can be integrated into CI/CD pipeline using Python scripts
- Provides AI-assisted comprehensive review beyond automated checks
- Results can inform the generate-validation-report competency
- Regular validation helps maintain OLAF quality over time
