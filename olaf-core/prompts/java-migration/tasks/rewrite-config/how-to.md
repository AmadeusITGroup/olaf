# OpenRewrite Configuration — Phase 1

## Goal
Configure OpenRewrite plugin and create baseline configuration file for future migration recipes.

## Prerequisites
- Project builds and unit tests pass on current baseline
- Java 17 toolchain available (for future recipes)

## Preferred Approach (Automated)
1. **Add OpenRewrite Plugin**:
   ```bash
   # Maven: Add plugin to pom.xml
   mvn org.openrewrite.maven:rewrite-maven-plugin:5.3.0:init
   
   # Gradle: Add to build.gradle
   echo 'plugins { id "org.openrewrite.rewrite" version "6.1.18" }' >> build.gradle
   ```

2. **Create Configuration File**:
   ```bash
   # Create minimal rewrite.yml
   cat > rewrite.yml << 'EOF'
   ---
   type: specs.openrewrite.org/v1beta/recipe
   name: com.example.migration.JavaMigration
   displayName: Java Migration Recipes
   description: Migration recipes for Java and Spring Boot upgrades
   recipeList: []
   EOF
   ```

3. **Validate Plugin Setup**:
   ```bash
   # Maven validation
   mvn rewrite:help
   
   # Gradle validation  
   ./gradlew rewriteDryRun
   ```

## Fallback Approach (Manual)
If automated setup fails:
1. Manually add rewrite plugin to build file with latest compatible version
2. Create empty `rewrite.yml` file at repository root
3. Test plugin execution with help/dry-run commands

## Verification Commands
```bash
# Verify plugin is properly configured
mvn rewrite:help || ./gradlew rewriteHelp

# Verify rewrite.yml exists and is valid
test -f rewrite.yml && echo "PASS: rewrite.yml exists" || echo "FAIL: rewrite.yml missing"

# Verify no recipes are accidentally active (should report 0 changes)
mvn rewrite:dryRun || ./gradlew rewriteDryRun

# Check plugin version
mvn help:describe -Dplugin=org.openrewrite.maven:rewrite-maven-plugin -Ddetail=false
```

## Issue Detection & Remediation

### Plugin Version Incompatible (Severity: high)
**Detection Pattern**: Plugin execution failures or version conflicts
**Remediation**:
1. Update to latest compatible rewrite plugin version
2. Check Maven/Gradle compatibility matrix
3. Update build tool version if needed
**Validation**: `mvn rewrite:help` executes without errors

### Corporate Maven Extension Resolution (Severity: medium)
**Detection Pattern**: Extension resolution failures in corporate environments
**Remediation**:
1. Configure Maven `settings.xml` with corporate mirrors/servers
2. Temporarily disable extension in `.mvn/extensions.xml` for testing
3. Restore extension after validation
**Validation**: Plugin commands execute in corporate environment

### Build Integration Conflicts (Severity: medium)
**Detection Pattern**: Build failures due to conflicting plugin executions
**Remediation**:
1. Adjust plugin execution phases to avoid conflicts
2. Configure plugin exclusions if needed
3. Update plugin configuration for compatibility
**Validation**: Full build succeeds: `mvn clean compile`

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `rewrite-config-<YYYYMMDD-HHmm>.json`
- **Categories**: plugin-load, config-file, build, corporate-extension
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-blocking warnings)

## Success Criteria
- ✅ OpenRewrite plugin configured and functional
- ✅ `rewrite.yml` exists at repository root and is tracked in git
- ✅ Plugin help/dry-run executes successfully: `mvn rewrite:help` exits 0
- ✅ No code changes from dry run (0 active recipes): `mvn rewrite:dryRun` reports 0 changes
- ✅ Plugin version documented in findings directory
