# OpenRewrite Dry Run — Phase 1

## Goal
Execute a no-impact OpenRewrite dry run to preview prospective recipe changes, validate plugin wiring, and capture baseline report.

## Prerequisites
- OpenRewrite plugin configured (rewrite-config task completed)
- Clean compilation succeeds
- No uncommitted local changes in workspace

## Preferred Approach (Automated)
1. **Workspace Validation**:
   ```bash
   # Confirm clean workspace
   git status --porcelain | wc -l  # Should be 0
   
   # Validate compilation
   mvn clean compile -DskipTests -q
   ```

2. **Dry Run Execution**:
   ```bash
   # Maven dry run
   mvn rewrite:dryRun -q
   
   # Gradle dry run (alternative)
   ./gradlew rewriteDryRun
   ```

3. **Results Collection**:
   ```bash
   # Check for generated patch file
   test -f target/rewrite/rewrite.patch && echo "Patch generated" || echo "No changes proposed"
   
   # Copy patch to findings if exists
   mkdir -p olaf-data/findings/migrations/migration_*/rewrite/
   cp target/rewrite/rewrite.patch olaf-data/findings/migrations/migration_*/rewrite/ 2>/dev/null || true
   ```

4. **Summary Generation**:
   ```bash
   # Count proposed changes
   if [ -f target/rewrite/rewrite.patch ]; then
     wc -l target/rewrite/rewrite.patch > rewrite-dry-run-stats.txt
   else
     echo "0 changes proposed" > rewrite-dry-run-stats.txt
   fi
   ```

## Fallback Approach (Manual)
If automated dry run fails:
1. Check plugin configuration in pom.xml/build.gradle
2. Resolve compilation issues before retrying
3. Manually inspect rewrite.yml for syntax errors
4. Run with verbose output to identify issues

## Verification Commands
```bash
# Verify dry run completed successfully
mvn rewrite:dryRun -q && echo "PASS: Dry run successful" || echo "FAIL: Dry run failed"

# Check for patch file existence
test -f target/rewrite/rewrite.patch && echo "PASS: Patch file generated" || echo "PASS: No changes (expected)"

# Validate workspace still clean
git status --porcelain | wc -l  # Should still be 0

# Check summary file created
test -f rewrite-dry-run-stats.txt && echo "PASS: Summary created" || echo "FAIL: Summary missing"
```

## Issue Detection & Remediation

### Plugin Execution Failure (Severity: high)
**Detection Pattern**: Dry run command fails with plugin errors
**Remediation**:
1. Check OpenRewrite plugin version compatibility
2. Resolve compilation issues that block plugin execution
3. Update plugin configuration in pom.xml/build.gradle
4. Verify rewrite.yml syntax is valid
**Validation**: `mvn rewrite:dryRun` executes without errors

### Unexpected Changes with No Recipes (Severity: medium)
**Detection Pattern**: Patch file generated when no recipes are active
**Remediation**:
1. Review rewrite.yml for accidentally enabled recipes
2. Check for inherited recipes from parent configurations
3. Verify plugin configuration doesn't auto-enable recipes
**Validation**: Empty patch file when no recipes are configured

### Format-Only Changes (Severity: low)
**Detection Pattern**: Patch contains only formatting/style changes
**Remediation**:
1. Review if formatting recipes are intentionally enabled
2. Disable formatting recipes if not approved for this phase
3. Document formatting changes for future style adoption
**Validation**: Patch contains only intended changes, no unwanted formatting

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `rewrite-dry-run-<YYYYMMDD-HHmm>.json`
- **Categories**: plugin, unexpected-diff, config, format-churn
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (formatting not yet approved)

## Success Criteria
- ✅ Dry run completes without build errors: `mvn rewrite:dryRun` exits 0
- ✅ Workspace remains clean: `git status --porcelain` returns empty
- ✅ Results documented: patch file and summary captured in findings
- ✅ No HIGH severity plugin issues remain OPEN
- ✅ Expected change count matches actual (0 if no recipes active)
