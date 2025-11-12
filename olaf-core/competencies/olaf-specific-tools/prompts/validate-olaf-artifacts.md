# Validate OLAF Artifacts

## Purpose
Perform comprehensive validation of OLAF framework artifacts including manifests, documentation, templates, and file references to ensure consistency, completeness, and compliance with OLAF standards.

## Protocol
**Act** - Execute validation immediately and report findings

## Context Required
- Access to OLAF framework structure (olaf-core, olaf-data, docs)
- Understanding of OLAF manifest schema
- Knowledge of documentation templates and standards

## Validation Scope

### 1. Manifest Validation
Check all `competency-manifest.json` files for:
- **Required fields**: id, name, description, category, entry_points
- **Schema compliance**: Standard entry point structure (name, command, file, protocol, use_case)
- **Data integrity**: Valid JSON, correct data types, no null/empty required fields
- **File references**: All referenced prompt files exist
- **Consistency**: Naming conventions (kebab-case for ids), protocol values

### 2. Documentation Validation
Check documentation structure and content for:
- **Completeness**: Each entry point has description.md and tutorial.md
- **Structure**: Proper /docs folder hierarchy in competency packs
- **Templates**: Descriptions follow competency-description-template.md format
- **Links**: All internal links resolve correctly
- **Naming**: Files use kebab-case naming convention
- **Index files**: Each competency pack has docs/README.md listing entry points

### 3. Template Compliance
Verify artifacts match their templates:
- **Competency descriptions**: Match description template structure
- **Tutorials**: Follow tutorial template format
- **README files**: Include required sections
- **Manifests**: Follow manifest template structure

### 4. File Reference Integrity
Check all file references in:
- **Markdown documents**: #[[file:...]] references resolve
- **Manifests**: Prompt file paths are valid
- **Documentation links**: Relative paths work correctly
- **Cross-references**: Links between documents are valid

## Execution Steps

1. **Scan Repository Structure**
   - Identify all competency packs in olaf-core/competencies/
   - Locate all manifest files
   - Map documentation structure

2. **Validate Manifests**
   - Parse each competency-manifest.json
   - Check required fields and schema compliance
   - Verify entry point structure
   - Validate file references in entry_points

3. **Validate Documentation**
   - Check for /docs folders in competency packs
   - Verify entry point documentation exists
   - Validate README.md index files
   - Check documentation completeness

4. **Check Template Compliance**
   - Compare descriptions against template
   - Verify tutorial structure
   - Check for required sections

5. **Validate File References**
   - Parse all markdown files for #[[file:...]] syntax
   - Check manifest file references
   - Verify documentation links
   - Test cross-references

6. **Generate Report**
   - Summarize findings by category
   - List all issues with severity (critical, warning, info)
   - Provide actionable recommendations
   - Prioritize fixes

## Output Format

```markdown
# OLAF Artifacts Validation Report

## Summary
- Total competency packs scanned: X
- Total manifests validated: X
- Total documentation files checked: X
- Critical issues: X
- Warnings: X
- Info items: X

## Critical Issues
[Issues that break functionality or prevent usage]

## Warnings
[Issues that should be fixed but don't break functionality]

## Informational
[Suggestions for improvement]

## Recommendations
[Prioritized action items]
```

## Success Criteria
- All manifests are valid JSON and follow standard schema
- All entry points have complete documentation
- All file references resolve correctly
- No broken links in documentation
- Template compliance is verified

## Related Competencies
- **detect-schema-drift**: Find inconsistencies across artifacts
- **generate-validation-report**: Create detailed QA reports

## Notes
- This validation should be run before major releases
- Can be integrated into CI/CD pipeline
- Use Python validation scripts for automated checks
- This prompt provides AI-assisted comprehensive review
