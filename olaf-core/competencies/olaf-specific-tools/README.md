# OLAF-Specific Tools

Comprehensive quality assurance and validation tools for OLAF framework artifacts.

## Overview

The OLAF-Specific Tools competency pack provides a complete suite of validation, migration, and quality assurance utilities for maintaining consistency and integrity across the OLAF framework. This pack includes both automated Python scripts and AI-assisted validation prompts to ensure manifests, documentation, templates, and file references remain compliant with OLAF standards.

## Purpose

As OLAF grows, maintaining consistency across competency packs, manifests, documentation, and templates becomes critical. This pack centralizes all QA tooling to:

- Prevent schema drift and inconsistencies
- Validate manifest compliance with standard schema
- Ensure documentation completeness and integrity
- Check template compliance across artifacts
- Verify file references and links
- Generate comprehensive validation reports
- Migrate non-compliant artifacts to standard schemas

## Target Users

- **OLAF Maintainers**: Ensuring framework consistency and quality
- **Framework Developers**: Creating and maintaining competency packs
- **QA Engineers**: Validating artifacts before releases
- **Competency Creators**: Ensuring new competencies meet standards

## Entry Points

### 1. Validate OLAF Artifacts

**Command**: `olaf validate olaf artifacts`  
**Protocol**: Act  
**Use Case**: Comprehensive validation of manifests, documentation, and templates

Performs end-to-end validation of OLAF framework artifacts including manifest schema compliance, documentation completeness, template adherence, and file reference integrity.

- [Description](docs/validate-olaf-artifacts/description.md)
- [Tutorial](docs/validate-olaf-artifacts/tutorial.md)

### 2. Detect Schema Drift

**Command**: `olaf detect schema drift`  
**Protocol**: Act  
**Use Case**: Find inconsistencies and schema variations across OLAF artifacts

Identifies schema drift, naming convention inconsistencies, and structural variations across competency packs to maintain framework consistency over time.

- [Description](docs/detect-schema-drift/description.md)
- [Tutorial](docs/detect-schema-drift/tutorial.md)

### 3. Generate Validation Report

**Command**: `olaf generate validation report`  
**Protocol**: Propose-Act  
**Use Case**: Create comprehensive QA report for OLAF artifacts

Generates detailed quality assurance reports combining automated validation results with AI-assisted analysis, providing actionable insights and prioritized recommendations.

- [Description](docs/generate-validation-report/description.md)
- [Tutorial](docs/generate-validation-report/tutorial.md)

## Python Scripts

The pack includes automated validation and migration scripts located in the `scripts/` directory:

### Validation Scripts

#### validate-manifest-schema.py

Validates competency manifest files against the standard OLAF schema.

**Usage**:
```bash
# Validate all manifests
python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --all

# Validate specific manifest
python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --manifest path/to/manifest.json

# Generate report file
python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --all --report validation-report.txt

# Strict mode (fail on warnings)
python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --all --strict
```

**Checks**:
- Required fields presence (name, version, description, category)
- Recommended fields (id, author, tags, status, etc.)
- Entry points structure and completeness
- Protocol values (Act, Propose-Act, Propose-Confirm-Act)
- File references validity
- JSON syntax and data types
- Naming conventions (kebab-case for ids)

#### validate-template-compliance.py

Verifies that artifacts follow their respective template structures.

**Usage**:
```bash
# Check all competency packs
python olaf-core/competencies/olaf-specific-tools/scripts/validate-template-compliance.py --all

# Check specific competency pack
python olaf-core/competencies/olaf-specific-tools/scripts/validate-template-compliance.py --competency architect

# Generate detailed report
python olaf-core/competencies/olaf-specific-tools/scripts/validate-template-compliance.py --all --report compliance-report.txt
```

**Checks**:
- Competency descriptions match description template
- Tutorials follow tutorial template structure
- README files include required sections
- Manifests follow manifest template
- Required sections presence
- Section ordering consistency

#### validate-docs-structure.py

Ensures documentation integrity and completeness across competency packs.

**Usage**:
```bash
# Validate all documentation
python olaf-core/competencies/olaf-specific-tools/scripts/validate-docs-structure.py --all

# Check specific competency pack
python olaf-core/competencies/olaf-specific-tools/scripts/validate-docs-structure.py --competency researcher

# Check for broken links only
python olaf-core/competencies/olaf-specific-tools/scripts/validate-docs-structure.py --all --links-only
```

**Checks**:
- Documentation folder structure
- Entry point documentation completeness (description + tutorial)
- README.md index files
- Link validity (internal and cross-references)
- Orphaned files
- Naming conventions (kebab-case)
- File organization

### Migration Scripts

#### migrate-manifest-schema.py

Semi-automated migration of non-compliant manifests to standard schema.

**Usage**:
```bash
# Preview migrations (dry-run)
python olaf-core/competencies/olaf-specific-tools/scripts/migrate-manifest-schema.py --all --dry-run

# Migrate specific manifest
python olaf-core/competencies/olaf-specific-tools/scripts/migrate-manifest-schema.py --manifest path/to/manifest.json

# Migrate all with backup (recommended)
python olaf-core/competencies/olaf-specific-tools/scripts/migrate-manifest-schema.py --all

# Skip backup (not recommended)
python olaf-core/competencies/olaf-specific-tools/scripts/migrate-manifest-schema.py --all --no-backup
```

**Features**:
- Detects schema variants (id/name/package variations)
- Maps fields to standard schema
- Preserves all existing data
- Creates backups before applying changes
- Requires human approval (unless --auto-approve)
- Generates migration reports

**Migration Actions**:
- Rename fields (e.g., `package` → `name`)
- Add missing required fields (e.g., `id`)
- Restructure entry points to standard format
- Convert data types where needed
- Standardize naming conventions

## Templates

The pack includes templates for validation reports and other artifacts:

### validation-report-template.md

Standard template for comprehensive validation reports including:
- Executive summary with quality metrics
- Detailed findings by severity
- Issue categorization by type
- Trend analysis (if historical data available)
- Actionable recommendations
- Prioritized action plan

## Integration with OLAF Workflow

### Pre-Release Validation

Before any OLAF release:
1. Run `validate-manifest-schema.py --all` to check all manifests
2. Run `validate-docs-structure.py --all` to verify documentation
3. Run `validate-template-compliance.py --all` to check templates
4. Use `olaf generate validation report` to create comprehensive QA report
5. Address critical and high-priority issues
6. Re-validate after fixes

### Continuous Quality Assurance

Integrate into development workflow:
- Run validation scripts before committing changes
- Use `olaf detect schema drift` quarterly to catch inconsistencies
- Generate validation reports for team reviews
- Automate validation in CI/CD pipeline

### Creating New Competency Packs

When creating new competency packs:
1. Use standard templates from competency-creation pack
2. Validate manifest with `validate-manifest-schema.py`
3. Ensure documentation follows templates
4. Run `validate-docs-structure.py` to verify completeness
5. Use `olaf validate olaf artifacts` for final check

### Migrating Existing Artifacts

For non-compliant artifacts:
1. Run `validate-manifest-schema.py` to identify issues
2. Use `migrate-manifest-schema.py --dry-run` to preview changes
3. Review migration plan
4. Apply migrations with backup
5. Re-validate after migration
6. Test affected competencies

## Best Practices

### Validation Frequency

- **Before commits**: Quick validation of changed files
- **Before releases**: Comprehensive validation of all artifacts
- **Quarterly**: Schema drift detection and trend analysis
- **After major changes**: Full validation suite

### Handling Validation Issues

1. **Critical Issues**: Fix immediately, block releases
2. **High Priority**: Fix before next release
3. **Medium Priority**: Schedule for upcoming sprint
4. **Low Priority**: Address during maintenance windows

### Maintaining Quality

- Keep templates up to date
- Document schema changes
- Update validation scripts when standards evolve
- Share validation reports with team
- Track quality metrics over time
- Automate where possible

## Technical Requirements

- **Python**: 3.12 or higher
- **Dependencies**: Standard library only (json, pathlib, sys, dataclasses)
- **Platform**: Cross-platform compatible (Windows, macOS, Linux)
- **LLM**: Claude Sonnet 4.5 or higher (for AI-assisted prompts)

## Related Competencies

- **competency-creation**: Creating new competency packs with proper structure
- **prompt-engineer**: Generating tutorials and documentation
- **architect**: Designing competency pack architectures

## Maintenance

- **Team**: OLAF Framework Core Team
- **Status**: Public Beta
- **Created**: 2025-10-27
- **Last Updated**: 2025-10-27

## Quick Start

1. **Validate your OLAF installation**:
   ```bash
   python olaf-core/competencies/olaf-specific-tools/scripts/validate-manifest-schema.py --all
   ```

2. **Check documentation completeness**:
   ```bash
   python olaf-core/competencies/olaf-specific-tools/scripts/validate-docs-structure.py --all
   ```

3. **Generate comprehensive report**:
   ```
   olaf generate validation report
   ```

4. **Detect schema drift**:
   ```
   olaf detect schema drift
   ```

## Support

For issues, questions, or contributions related to OLAF-Specific Tools:
- Review existing validation reports in `olaf-data/validation-reports/`
- Check OLAF documentation in `docs/`
- Consult competency-creation pack for standards and templates

---

**Note**: This competency pack is for OLAF framework internal use. It ensures quality and consistency across all OLAF artifacts and should be used by maintainers and contributors to validate changes before committing.
