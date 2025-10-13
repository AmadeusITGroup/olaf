# Upgrade Spring Boot 2.3 → 2.4 — Phase 1

## Goal
Incrementally upgrade Spring Boot from 2.3.x to 2.4.13 with green compile + unit test baseline and documented config/property changes.

## Prerequisites
- Current Spring Boot 2.3.x version active
- Baseline compile and unit tests passing
- JDK 17 configured and active

## Preferred Approach (Automated)
1. **Baseline Validation**:
   ```bash
   # Confirm current version and green baseline
   mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout
   mvn clean compile test -q
   ```

2. **Version Update**:
   ```bash
   # Update Spring Boot parent version
   mvn versions:update-parent -DparentVersion=2.4.13 -DgenerateBackupPoms=false
   
   # Remove explicit versions managed by new BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Build and Test**:
   ```bash
   # Rebuild with new version
   mvn clean compile -q
   
   # Run unit tests
   mvn test -q
   
   # Generate dependency report
   mvn dependency:tree > dependency-tree-2.4.txt
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit pom.xml parent version to 2.4.13
2. Remove explicit dependency versions one by one
3. Address configuration property changes manually
4. Update actuator endpoint configurations

## Verification Commands
```bash
# Confirm Spring Boot 2.4.13 active
mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout | grep "2.4.13"

# Validate compilation
mvn clean compile -q

# Validate tests
mvn test -q

# Check for deprecated properties
grep -r "spring.config.location" src/main/resources/ || echo "No deprecated config found"
```

## Issue Detection & Remediation

### Configuration Property Changes (Severity: medium)
**Detection Pattern**: `Failed to bind properties under\|Unknown property`
**Remediation**:
1. Update deprecated property names per Spring Boot 2.4 migration guide
2. Replace `spring.config.location` with `spring.config.import` where applicable
3. Update actuator endpoint exposure settings
**Validation**: Application starts without property binding errors

### Actuator Endpoint Changes (Severity: low)
**Detection Pattern**: Actuator endpoint 404 or unexpected behavior
**Remediation**:
1. Update endpoint exposure configuration in `application.yml`
2. Check for changed default endpoint paths
3. Update health indicator configurations
**Validation**: Actuator endpoints accessible and functional

### Dependency Version Conflicts (Severity: medium)
**Detection Pattern**: Maven dependency convergence warnings
**Remediation**:
1. Let Spring Boot 2.4 BOM manage dependency versions
2. Remove explicit versions for dependencies managed by BOM
3. Add exclusions for conflicting transitive dependencies
**Validation**: `mvn dependency:tree` shows no version conflicts

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `upgrade-sb-2.3-to-2.4-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, config, actuator, dependency
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-critical issues)

## Success Criteria
- ✅ Spring Boot 2.4.13 parent version active
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0
- ✅ No HIGH severity configuration issues remain OPEN
- ✅ Dependency tree generated and stored in findings
