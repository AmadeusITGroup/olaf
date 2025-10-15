# Angular Core Update — Phase 1

## Goal
Update Angular core packages to the target version using Angular's migration schematics and manual fixes.

## Preferred Approach (Automated)
1. **Pre-Update Validation**:
   ```bash
   # Ensure clean git state
   git status --porcelain
   
   # Verify current build works
   ng build --configuration=production
   ng test --watch=false --browsers=ChromeHeadless
   ```

2. **Angular Core Update**:
   ```bash
   # Update Angular core packages
   ng update @angular/core@<target-version>
   
   # Update Angular CLI if needed
   ng update @angular/cli@<target-version>
   
   # Update other Angular packages
   ng update @angular/common@<target-version>
   ng update @angular/forms@<target-version>
   ng update @angular/router@<target-version>
   ```

3. **Post-Update Validation**:
   ```bash
   # Install dependencies
   npm install
   
   # Verify build still works
   ng build --configuration=production
   
   # Run tests
   ng test --watch=false --browsers=ChromeHeadless
   ```

## Fallback Approach (Manual)
If `ng update` fails or is not available:
1. Manually update package.json Angular dependencies
2. Run `npm install` to install new versions
3. Fix compilation errors manually
4. Update imports and API usage based on migration guide

## Verification Commands
```bash
# Check Angular version after update
ng version

# Verify package.json has correct versions
cat package.json | jq '.dependencies | to_entries | map(select(.key | startswith("@angular")))'

# Ensure no peer dependency warnings
npm ls --depth=0 2>&1 | grep -i "peer dep" || echo "No peer dependency issues"

# Verify build works
ng build --configuration=production --verbose
```

## Outputs
- **Primary**: Updated package.json and package-lock.json
- **Secondary**: `olaf-data/findings/migrations/migration_<ts>/updates/core_update_<YYYYMMDD-HHmm>.md`
- **Logs**: Build and test output logs

## Update Categories

### Core Framework Update
**Packages**: @angular/core, @angular/common, @angular/platform-browser
**Process**:
1. Run `ng update @angular/core` with target version
2. Review and apply migration schematics
3. Fix any compilation errors
4. Update TypeScript if required
**Validation**: Application builds and basic functionality works

### Router and Forms Update
**Packages**: @angular/router, @angular/forms
**Process**:
1. Update router package with migration schematics
2. Update forms package and check for breaking changes
3. Test routing functionality
4. Validate form behavior
**Validation**: Navigation and forms work correctly

### HTTP Client Update
**Packages**: @angular/common/http
**Process**:
1. Update HTTP client package
2. Check for interceptor changes
3. Validate HTTP service functionality
4. Update error handling if needed
**Validation**: API calls work correctly

### Animation and CDK Update
**Packages**: @angular/animations, @angular/cdk (if used)
**Process**:
1. Update animation packages
2. Check for animation API changes
3. Update CDK if used by the project
4. Test animation functionality
**Validation**: Animations work as expected

## Issue Detection & Remediation

### Compilation Errors (Severity: high)
**Detection Pattern**: TypeScript compilation failures after update
**Remediation**: 
1. Review compilation error messages
2. Update TypeScript types and interfaces
3. Fix deprecated API usage
4. Update import statements if needed
**Validation**: `ng build` completes successfully

### Peer Dependency Conflicts (Severity: high)
**Detection Pattern**: npm peer dependency warnings or errors
**Remediation**:
1. Update conflicting packages to compatible versions
2. Use `npm install --legacy-peer-deps` if needed temporarily
3. Check for alternative packages if conflicts persist
4. Document any temporary workarounds
**Validation**: `npm ls` shows no peer dependency issues

### Migration Schematic Failures (Severity: medium)
**Detection Pattern**: `ng update` schematics fail to complete
**Remediation**:
1. Run schematics individually to isolate issues
2. Apply manual fixes based on Angular migration guide
3. Check for custom code that blocks automatic migration
4. Document manual changes needed
**Validation**: All intended migrations applied successfully

### Test Failures (Severity: medium)
**Detection Pattern**: Tests fail after Angular update
**Remediation**:
1. Update test imports and setup
2. Fix TestBed configuration changes
3. Update mock objects and test utilities
4. Check for testing framework compatibility
**Validation**: All tests pass with new Angular version

### Runtime Errors (Severity: high)
**Detection Pattern**: Application fails to start or has runtime errors
**Remediation**:
1. Check browser console for error messages
2. Update polyfills if needed
3. Fix service injection and dependency issues
4. Update component lifecycle methods
**Validation**: Application starts and runs without errors

## Update Scripts

### Pre-Update Backup
```bash
# Create backup branch
git checkout -b backup/pre-core-update
git push origin backup/pre-core-update
git checkout main

# Tag current state
git tag backup/angular-core-pre-update
git push origin backup/angular-core-pre-update
```

### Angular Update Execution
```bash
# Update with specific version
ng update @angular/core@17.0.0 --verbose

# Update CLI to match
ng update @angular/cli@17.0.0 --verbose

# Install dependencies
npm install

# Clear Angular cache
ng cache clean
```

### Post-Update Validation
```bash
# Build all configurations
ng build --configuration=development
ng build --configuration=production

# Run all tests
ng test --watch=false --code-coverage --browsers=ChromeHeadless
ng e2e

# Check bundle size
ng build --stats-json
npx webpack-bundle-analyzer dist/stats.json --mode static --report bundle-report.html
```

## Rollback Strategy

### Immediate Rollback
```bash
# Reset to pre-update state
git reset --hard backup/angular-core-pre-update

# Clean node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Selective Rollback
```bash
# Revert specific files
git checkout backup/angular-core-pre-update -- package.json package-lock.json

# Reinstall dependencies
npm install
```

## Success Criteria
- ✅ Angular core packages updated to target version
- ✅ Application builds successfully in all configurations
- ✅ All tests pass
- ✅ Application starts and runs without errors
- ✅ No peer dependency conflicts
- ✅ Migration schematics applied successfully
- ✅ Performance regression check passed