# OLAF Validation Tools

This directory contains comprehensive validation tools for OLAF framework artifacts.

## Available Validation Scripts

### 1. validate-manifest-schema.py

Validates competency manifest files against the standard schema.

**Usage:**
```bash
# Validate all manifests
python scripts/validate-manifest-schema.py --all

# Validate specific manifest
python scripts/validate-manifest-schema.py --manifest path/to/competency-manifest.json

# Generate report file
python scripts/validate-manifest-schema.py --all --report validation-report.txt

# Strict mode (fail on warnings)
python scripts/validate-manifest-schema.py --all --strict
```

**Checks:**
- Required fields (name, version, description, category)
- Recommended fields (id, author, created, updated, tags, etc.)
- Entry points structure and required fields
- Protocol values (Act, Propose-Act, Propose-Confirm-Act)
- Version format (semantic versioning)
- Classification, target_users, and compatibility structures

### 2. migrate-manifest-schema.py

Semi-automated migration tool for updating non-compliant manifests to the standard schema.

**Usage:**
```bash
# Preview migrations (dry run)
python scripts/migrate-manifest-schema.py --all --dry-run

# Migrate specific manifest
python scripts/migrate-manifest-schema.py --manifest path/to/competency-manifest.json

# Migrate all with auto-approval (use with caution)
python scripts/migrate-manifest-schema.py --all --auto-approve

# Skip backup creation (not recommended)
python scripts/migrate-manifest-schema.py --all --no-backup
```

**Features:**
- Detects schema variants (id/name/package, entry_points formats)
- Creates backups before applying changes
- Requires human approval by default
- Preserves all existing data
- Handles field renames, additions, and restructuring

### 3. validate-template-compliance.py

Validates that documentation artifacts comply with their respective templates.

**Usage:**
```bash
# Validate all competency pack documentation
python scripts/validate-template-compliance.py --all

# Validate specific competency pack
python scripts/validate-template-compliance.py --competency path/to/competency-pack

# Generate report file
python scripts/validate-template-compliance.py --all --report compliance-report.txt

# Strict mode
python scripts/validate-template-compliance.py --all --strict
```

**Checks:**
- **Competency Descriptions**: Required sections (Overview, Purpose, Usage, Parameters, Output, Examples, Related Competencies)
- **Tutorials**: Required sections (Prerequisites, Step-by-Step Instructions, Verification Checklist, Troubleshooting, etc.)
- **README files**: Required sections (Overview, Entry Points with links)
- **Document length**: Warns if documents exceed recommended length (~750 words)
- **Usage sections**: Validates presence of Command and Protocol fields

### 4. validate-docs-structure.py

Validates documentation structure and integrity across the entire OLAF framework.

**Usage:**
```bash
# Validate all documentation folders
python scripts/validate-docs-structure.py --all

# Validate specific docs folder
python scripts/validate-docs-structure.py --docs-path path/to/docs

# Generate report file
python scripts/validate-docs-structure.py --all --report structure-report.txt

# Strict mode
python scripts/validate-docs-structure.py --all --strict
```

**Checks:**
- **Link validity**: Validates all markdown links [text](url)
- **File references**: Validates #[[file:path]] references
- **Broken links**: Reports links to non-existent files
- **Orphaned files**: Identifies files not referenced by any other documentation
- **Naming conventions**: Validates kebab-case naming for files
- **Document length**: Warns if documents exceed 5-minute read time (~750 words)
- **Markdown structure**: Checks for proper heading hierarchy

**Note:** This script includes file reference validation functionality, which covers the requirements for the validate-file-references.py tool mentioned in the design document.

## Integration with OLAF Workflow

These validation tools are part of the `olaf-specific-tools` competency pack and can be used:

1. **During development**: Run validators before committing changes
2. **In CI/CD pipelines**: Automate validation as part of build process
3. **For quality assurance**: Generate comprehensive reports for review
4. **During migration**: Use migration tools to update legacy manifests

## Exit Codes

All validation scripts follow standard exit code conventions:

- `0`: Success (all validations passed)
- `1`: Failure (errors found, or warnings found in strict mode)

## Report Formats

All validation scripts generate human-readable reports with:

- Summary statistics (total items, valid/invalid counts)
- Issue counts by severity (ERROR, WARNING, INFO)
- Detailed issue listings with:
  - File/location information
  - Issue description
  - Actionable suggestions for fixes

## Best Practices

1. **Run validators regularly**: Catch issues early in development
2. **Use dry-run mode**: Preview changes before applying migrations
3. **Create backups**: Always backup before running migration tools
4. **Review reports**: Don't just look at pass/fail, review specific issues
5. **Fix errors first**: Address ERROR-level issues before WARNING-level
6. **Use strict mode in CI**: Enforce high quality standards in automated builds

## Future Enhancements

Planned additions to the validation toolkit:

- AI-assisted validation prompts (validate-olaf-artifacts.md, detect-schema-drift.md)
- Validation report templates
- Integration with IDE/editor plugins
- Automated fix suggestions and application
