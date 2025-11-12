# Detect Schema Drift

## Purpose
Identify inconsistencies, schema variations, and drift across OLAF framework artifacts to maintain consistency and prevent fragmentation as the framework evolves.

## Protocol
**Act** - Execute detection immediately and report findings

## Context Required
- Access to all OLAF competency packs and manifests
- Understanding of standard OLAF schemas and templates
- Knowledge of OLAF naming conventions and patterns

## What is Schema Drift?

Schema drift occurs when:
- Manifests use different field names for the same concept (id vs name vs package)
- Entry point structures vary across competency packs
- Documentation follows different organizational patterns
- Naming conventions are inconsistent
- Template structures diverge over time
- New fields are added without standardization

## Detection Scope

### 1. Manifest Schema Variations
Detect differences in:
- **Field naming**: id, name, package, identifier variations
- **Entry point structure**: Different field names or organizations
- **Required vs optional fields**: Inconsistent field presence
- **Data types**: String vs array, object vs string variations
- **Nested structures**: Different nesting patterns for same data
- **Metadata fields**: Inconsistent metadata organization

### 2. Documentation Structure Drift
Identify variations in:
- **Folder organization**: Different /docs structures
- **File naming**: Inconsistent naming patterns
- **README formats**: Different index file structures
- **Description formats**: Varying section orders or names
- **Tutorial structures**: Different step organizations
- **Link patterns**: Inconsistent cross-reference styles

### 3. Naming Convention Drift
Find inconsistencies in:
- **File naming**: kebab-case vs snake_case vs camelCase
- **ID formats**: Different identifier patterns
- **Command naming**: Inconsistent command structures
- **Folder naming**: Mixed naming conventions

### 4. Template Compliance Drift
Detect deviations from templates:
- **Missing sections**: Required sections omitted
- **Extra sections**: Non-standard additions
- **Section ordering**: Different sequence than template
- **Format variations**: Different markdown styles

## Execution Steps

1. **Collect All Artifacts**
   - Scan all competency-manifest.json files
   - Gather all documentation files
   - Collect all template files
   - Map folder structures

2. **Analyze Manifest Schemas**
   - Extract field names from all manifests
   - Compare entry_points structures
   - Identify field name variations
   - Detect data type inconsistencies
   - Map schema patterns

3. **Compare Documentation Structures**
   - Analyze /docs folder organizations
   - Compare README formats
   - Check description structures
   - Review tutorial patterns
   - Identify structural variations

4. **Check Naming Conventions**
   - Extract all file names
   - Extract all IDs and identifiers
   - Extract all command names
   - Identify naming pattern variations
   - Detect case inconsistencies

5. **Assess Template Compliance**
   - Compare artifacts against templates
   - Identify missing sections
   - Detect extra content
   - Check section ordering
   - Note format deviations

6. **Categorize Findings**
   - Group by drift type
   - Assess impact severity
   - Identify root causes
   - Suggest standardization approach

## Output Format

```markdown
# Schema Drift Detection Report

## Executive Summary
- Artifacts analyzed: X
- Drift patterns found: X
- High-impact drifts: X
- Standardization recommendations: X

## Manifest Schema Drift

### Field Naming Variations
[List different field names used for same concept]

### Entry Point Structure Variations
[Show different entry_points structures]

### Data Type Inconsistencies
[List fields with varying data types]

## Documentation Structure Drift

### Folder Organization Patterns
[Show different /docs structures]

### File Naming Patterns
[List naming convention variations]

### README Format Variations
[Show different index file formats]

## Naming Convention Drift

### File Naming Inconsistencies
[List files not following kebab-case]

### ID Format Variations
[Show different identifier patterns]

### Command Naming Patterns
[List command naming variations]

## Template Compliance Drift

### Missing Sections
[List artifacts missing required sections]

### Non-Standard Additions
[List extra content not in templates]

### Format Deviations
[Show formatting inconsistencies]

## Impact Analysis

### High Impact (Breaking Changes)
[Drifts that break tooling or automation]

### Medium Impact (Maintenance Issues)
[Drifts that complicate maintenance]

### Low Impact (Cosmetic)
[Minor inconsistencies]

## Standardization Recommendations

### Immediate Actions
[Critical fixes needed now]

### Short-term Actions
[Fixes for next release]

### Long-term Actions
[Architectural improvements]

## Migration Strategy
[Approach to standardize drifted artifacts]
```

## Analysis Techniques

### Pattern Recognition
- Use frequency analysis to identify dominant patterns
- Detect outliers that deviate from common patterns
- Identify evolution trends over time

### Comparative Analysis
- Compare against standard templates
- Cross-reference between competency packs
- Identify best practices vs anti-patterns

### Impact Assessment
- Evaluate effect on automation tools
- Assess maintenance burden
- Consider user experience impact

## Success Criteria
- All schema variations are identified
- Drift patterns are categorized by impact
- Root causes are understood
- Standardization path is clear
- Migration strategy is actionable

## Related Competencies
- **validate-olaf-artifacts**: Comprehensive validation
- **generate-validation-report**: Detailed QA reporting

## Notes
- Run this detection periodically (quarterly recommended)
- Use findings to update standards and templates
- Prioritize high-impact drifts for immediate correction
- Document decisions to prevent future drift
- Consider automation to prevent drift at creation time
