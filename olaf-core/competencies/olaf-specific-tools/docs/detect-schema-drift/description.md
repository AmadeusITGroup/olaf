# Detect Schema Drift

## Overview

The Detect Schema Drift competency identifies inconsistencies, schema variations, and drift across OLAF framework artifacts to maintain consistency and prevent fragmentation as the framework evolves. It analyzes manifests, documentation, naming conventions, and templates to find patterns of divergence.

## Purpose

As OLAF grows with multiple contributors and competency packs, schemas and patterns can drift over time. Different packs may use different field names, structures, or conventions, leading to:

- Fragmented schemas that break automation tools
- Inconsistent user experiences across competency packs
- Maintenance burden from supporting multiple patterns
- Difficulty onboarding new contributors
- Quality degradation over time

This competency detects drift early so it can be corrected before it becomes widespread.

## What is Schema Drift?

Schema drift occurs when artifacts deviate from standard patterns:

- **Field naming variations**: Some manifests use `id`, others use `name` or `package`
- **Structure differences**: Entry points organized differently across packs
- **Naming convention inconsistencies**: Mix of kebab-case, snake_case, camelCase
- **Template deviations**: Documentation following different structures
- **Metadata variations**: Different approaches to categorization or tagging

## When to Use

Use this competency:

- **Quarterly reviews**: Regular drift detection to catch issues early
- **After major contributions**: Check for inconsistencies from new contributors
- **Before standardization efforts**: Identify what needs to be standardized
- **During framework evolution**: Ensure new patterns don't fragment existing ones
- **Quality audits**: Comprehensive consistency checks

## Usage

**Command**: `olaf detect schema drift`

**Protocol**: Act (executes immediately and reports findings)

**Context Required**:
- Access to all OLAF competency packs and manifests
- Understanding of standard OLAF schemas and templates
- Knowledge of OLAF naming conventions and patterns

## What It Detects

### 1. Manifest Schema Variations

Identifies differences in manifest structure:
- **Field naming**: Different names for same concept (id vs name vs package)
- **Entry point structure**: Varying organizations of entry_points arrays
- **Required vs optional fields**: Inconsistent field presence across packs
- **Data types**: String vs array, object vs string variations
- **Nested structures**: Different nesting patterns for same data
- **Metadata organization**: Inconsistent categorization approaches

### 2. Documentation Structure Drift

Finds variations in documentation organization:
- **Folder structure**: Different /docs hierarchies
- **File naming**: Inconsistent naming patterns
- **README formats**: Different index file structures
- **Description formats**: Varying section orders or names
- **Tutorial structures**: Different step organizations
- **Link patterns**: Inconsistent cross-reference styles

### 3. Naming Convention Drift

Detects inconsistencies in naming:
- **File naming**: Mix of kebab-case, snake_case, camelCase
- **ID formats**: Different identifier patterns
- **Command naming**: Inconsistent command structures
- **Folder naming**: Mixed naming conventions

### 4. Template Compliance Drift

Identifies deviations from templates:
- **Missing sections**: Required sections omitted
- **Extra sections**: Non-standard additions
- **Section ordering**: Different sequence than template
- **Format variations**: Different markdown styles

## Output

The competency generates a comprehensive drift detection report with:

- **Executive Summary**: Total artifacts analyzed, drift patterns found
- **Manifest Schema Drift**: Field naming, structure, and data type variations
- **Documentation Structure Drift**: Folder, file, and format variations
- **Naming Convention Drift**: Inconsistencies in naming patterns
- **Template Compliance Drift**: Deviations from standard templates
- **Impact Analysis**: Severity assessment (high/medium/low impact)
- **Standardization Recommendations**: Prioritized actions to resolve drift
- **Migration Strategy**: Approach to standardize drifted artifacts

Example output structure:

```markdown
# Schema Drift Detection Report

## Executive Summary
- Artifacts analyzed: 15 competency packs
- Drift patterns found: 12
- High-impact drifts: 3
- Standardization recommendations: 8

## Manifest Schema Drift

### Field Naming Variations
- 8 packs use 'id', 5 use 'name', 2 use 'package'
- Recommendation: Standardize on 'id' field

### Entry Point Structure Variations
Pattern A (10 packs): {name, command, file, protocol, use_case}
Pattern B (3 packs): {name, invoke, path, mode, description}
Pattern C (2 packs): {title, cmd, file, type}

## Impact Analysis

### High Impact (Breaking Changes)
1. Entry point structure variations break documentation generator
2. Field naming inconsistencies prevent automated validation

### Medium Impact (Maintenance Issues)
1. Documentation structure variations complicate navigation
2. Naming convention drift reduces discoverability

## Standardization Recommendations

### Immediate Actions
1. Standardize entry_points structure across all manifests
2. Migrate 'name' and 'package' fields to 'id'
3. Enforce kebab-case for all file names

### Migration Strategy
1. Use migrate-manifest-schema.py to standardize manifests
2. Update documentation generator to handle legacy patterns temporarily
3. Phase out deprecated patterns over 2 releases
```

## Parameters

This competency requires no parameters. It automatically:
- Scans all competency packs in olaf-core/competencies/
- Analyzes all manifests for schema patterns
- Compares documentation structures
- Checks naming conventions
- Assesses template compliance

## Analysis Techniques

### Pattern Recognition
- Uses frequency analysis to identify dominant patterns
- Detects outliers that deviate from common patterns
- Identifies evolution trends over time

### Comparative Analysis
- Compares against standard templates
- Cross-references between competency packs
- Identifies best practices vs anti-patterns

### Impact Assessment
- Evaluates effect on automation tools
- Assesses maintenance burden
- Considers user experience impact

## Success Criteria

Detection is successful when:
- All schema variations are identified
- Drift patterns are categorized by impact
- Root causes are understood
- Standardization path is clear
- Migration strategy is actionable

## Examples

### Example 1: Quarterly Drift Check

Running quarterly drift detection:

```
User: olaf detect schema drift

AI: [Analyzes all competency packs]

# Schema Drift Detection Report

## Executive Summary
- Artifacts analyzed: 15 competency packs
- Drift patterns found: 8
- High-impact drifts: 2

## Key Findings

### High Impact
1. Entry point structure: 3 different patterns detected
   - 10 packs use standard structure
   - 3 packs use legacy structure
   - 2 packs use custom structure

2. Manifest field naming: 'id' vs 'name' inconsistency
   - 12 packs use 'id'
   - 3 packs use 'name'

### Recommendations
1. Migrate 3 legacy manifests to standard structure
2. Rename 'name' to 'id' in 3 manifests
3. Update documentation generator to handle transition
```

### Example 2: After Major Contribution

After multiple contributors add new competency packs:

```
User: olaf detect schema drift

AI: [Detects new drift patterns]

# Schema Drift Detection Report

## New Drift Patterns Detected

### Documentation Structure
- 3 new packs use non-standard /docs organization
- Tutorial files named inconsistently (tutorial.md vs guide.md vs walkthrough.md)

### Naming Conventions
- 2 new packs use snake_case instead of kebab-case
- Command names don't follow verb-noun pattern

### Impact
- Medium: Breaks documentation generator for new packs
- Low: Inconsistent user experience

### Immediate Actions
1. Standardize /docs structure in new packs
2. Rename files to follow kebab-case convention
3. Update command names to follow pattern
4. Add validation to prevent future drift
```

## Related Competencies

- **validate-olaf-artifacts**: Validates compliance with current standards
- **generate-validation-report**: Creates comprehensive QA reports with trend analysis
- **competency-creation/create-competency-pack**: Use validated templates to prevent drift

## Integration with Migration Tools

This competency identifies drift; use migration tools to fix it:

1. **Detect drift**: Use this competency to find inconsistencies
2. **Review findings**: Assess impact and prioritize fixes
3. **Plan migration**: Determine standardization approach
4. **Execute migration**: Use `migrate-manifest-schema.py` to fix manifests
5. **Validate**: Use `validate-olaf-artifacts` to confirm fixes
6. **Monitor**: Run drift detection quarterly to prevent recurrence

## Notes

- Run this detection periodically (quarterly recommended)
- Use findings to update standards and templates
- Prioritize high-impact drifts for immediate correction
- Document decisions to prevent future drift
- Consider automation to prevent drift at creation time
- Share reports with contributors to raise awareness
- Track drift metrics over time to measure improvement
