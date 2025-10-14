# Angular Update Analysis — Phase 1

## Goal
Analyze the current Angular project and generate a detailed migration path using `ng update` and dependency analysis.

## Preferred Approach (Automated)
1. **Angular Update Analysis**:
   ```bash
   # Check current Angular version
   ng version
   
   # Analyze available updates
   ng update
   
   # Get detailed update information
   ng update --all --dry-run
   ```

2. **Dependency Compatibility Check**:
   ```bash
   # Check npm outdated packages
   npm outdated
   
   # Analyze package compatibility
   npx npm-check-updates --target minor
   npx npm-check-updates --target major
   ```

3. **Generate Analysis Report**: Create structured analysis in findings directory

## Fallback Approach (Manual)
If automated analysis fails:
1. Manually check package.json for Angular version
2. Compare with Angular release schedule and LTS versions
3. Document third-party package compatibility manually
4. Create migration path based on Angular update guide

## Verification Commands
```bash
# Verify analysis files exist
ls -la olaf-data/findings/migrations/migration_*/analysis/ng_update_analysis.*

# Check Angular CLI is working
ng version --help

# Validate package.json is readable
cat package.json | jq '.dependencies."@angular/core"'
```

## Outputs
- **Primary**: `olaf-data/findings/migrations/migration_<ts>/analysis/ng_update_analysis.md`
- **Secondary**: `olaf-data/findings/migrations/migration_<ts>/analysis/dependency_compatibility.json`
- **Optional**: `olaf-data/findings/migrations/migration_<ts>/analysis/migration_path.md`

## Analysis Categories

### Angular Core Analysis
**Detection**: Current Angular version and available updates
**Information Gathered**:
1. Current Angular version (core, CLI, common, etc.)
2. Available update path (next minor, next major)
3. Breaking changes summary
4. Migration schematics available
**Output**: Structured version matrix and update recommendations

### Dependency Compatibility Analysis
**Detection**: Third-party package compatibility with target Angular version
**Information Gathered**:
1. Angular Material compatibility
2. Third-party UI library compatibility (PrimeNG, Nebular, etc.)
3. Testing framework compatibility (Jest, Cypress, etc.)
4. Build tool compatibility (Webpack, ESBuild, etc.)
**Output**: Compatibility matrix with recommended versions

### Breaking Changes Analysis
**Detection**: Potential breaking changes in target version
**Information Gathered**:
1. Deprecated APIs in current version
2. Removed APIs in target version
3. Changed behavior patterns
4. Migration schematics coverage
**Output**: Breaking changes impact assessment

### Custom Code Analysis
**Detection**: Project-specific migration challenges
**Information Gathered**:
1. Custom webpack configurations
2. Angular.json modifications
3. Custom schematics usage
4. Monorepo considerations (Nx, Lerna)
**Output**: Custom configuration impact assessment

## Issue Detection & Remediation

### Incompatible Dependencies (Severity: high)
**Detection Pattern**: Dependencies with no compatible version for target Angular
**Remediation**: 
1. Find alternative packages with Angular support
2. Check for beta/RC versions of packages
3. Consider forking and updating packages
4. Plan for custom implementation if needed
**Validation**: All dependencies have compatible versions documented

### Major Breaking Changes (Severity: high)
**Detection Pattern**: APIs removed or significantly changed in target version
**Remediation**:
1. Document all breaking changes affecting the project
2. Plan migration strategy for each breaking change
3. Identify migration schematics that can help
4. Create manual migration tasks for unsupported changes
**Validation**: All breaking changes have documented migration path

### Custom Configuration Conflicts (Severity: medium)
**Detection Pattern**: Custom webpack, build, or Angular configurations
**Remediation**:
1. Review custom configurations for compatibility
2. Update configurations for new Angular version
3. Test build process with new configurations
4. Document configuration changes needed
**Validation**: Custom configurations updated and tested

### Deprecated API Usage (Severity: medium)
**Detection Pattern**: Usage of APIs deprecated in current or target version
**Remediation**:
1. Scan codebase for deprecated API usage
2. Plan replacement with modern APIs
3. Use migration schematics where available
4. Create manual migration tasks for complex cases
**Validation**: No deprecated APIs remain in codebase

## Analysis Scripts

### Angular Version Detection
```bash
# Extract Angular version information
ng version --json > angular_versions.json

# Parse package.json for Angular dependencies
cat package.json | jq '.dependencies | to_entries | map(select(.key | startswith("@angular")))' > angular_deps.json
```

### Dependency Compatibility Check
```bash
# Check for Angular-specific packages
npm list | grep -E "@angular|angular-" > angular_packages.txt

# Check for potential compatibility issues
npm ls --depth=0 | grep -E "UNMET|invalid" > dependency_issues.txt
```

### Breaking Changes Detection
```bash
# Search for potentially problematic patterns
grep -r "HttpModule\|Http\|ReflectiveInjector" src/ > potential_breaking_changes.txt

# Check for deprecated imports
grep -r "import.*rxjs/add" src/ > rxjs_deprecated_imports.txt
```

## Success Criteria
- ✅ Angular update analysis completed and documented
- ✅ Dependency compatibility matrix created
- ✅ Breaking changes identified and migration planned
- ✅ Custom configuration impact assessed
- ✅ Migration path documented with specific steps
- ✅ High-risk items identified and mitigation planned