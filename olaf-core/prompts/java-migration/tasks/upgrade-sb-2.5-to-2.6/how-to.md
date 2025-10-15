# Upgrade Spring Boot 2.5 → 2.6 — Phase 1

## Goal
Upgrade from Spring Boot 2.5.x to 2.6.15 handling path pattern matching, property renames, and metrics/logging adjustments while keeping compile + unit tests green.

## Prerequisites
- Spring Boot 2.5.x active and functional
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
   mvn versions:update-parent -DparentVersion=2.6.15 -DgenerateBackupPoms=false
   
   # Remove explicit versions managed by new BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Build and Test**:
   ```bash
   # Rebuild with new version
   mvn clean compile -q
   
   # Run unit tests
   mvn test -q
   
   # Run focused web layer tests
   mvn test -Dtest="*ControllerTest" -q
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit pom.xml parent version to 2.6.15
2. Update path matching strategy configuration manually
3. Address deprecated AntPathMatcher usage
4. Update security configuration for new matcher patterns

## Verification Commands
```bash
# Confirm Spring Boot 2.6.15 active
mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout | grep "2.6.15"

# Validate compilation
mvn clean compile -q

# Validate tests
mvn test -q

# Check for path matching configuration
grep -r "spring.mvc.pathmatch.matching-strategy" src/main/resources/ || echo "Using default path matching"

# Test web endpoints (if applicable)
mvn test -Dtest="*ControllerTest" -q
```

## Issue Detection & Remediation

### Path Matching Strategy Changes (Severity: medium)
**Detection Pattern**: 404 errors or handler not found for routes
**Remediation**:
1. Configure path matching strategy in application.yml: `spring.mvc.pathmatch.matching-strategy: path_pattern_parser`
2. Update controller path patterns for PathPatternParser compatibility
3. Fix regex patterns in @RequestMapping annotations
**Validation**: All web endpoints respond correctly, no 404 errors

### Deprecated AntPathMatcher Usage (Severity: low)
**Detection Pattern**: AntPathMatcher deprecation warnings in logs
**Remediation**:
1. Update security configuration to use new path matching
2. Replace deprecated antMatchers with requestMatchers
3. Update custom path matching logic
**Validation**: No deprecation warnings for AntPathMatcher in logs

### Configuration Property Renames (Severity: low)
**Detection Pattern**: Deprecated property warnings in application startup
**Remediation**:
1. Update renamed properties per Spring Boot 2.6 migration guide
2. Replace deprecated actuator property names
3. Update logging configuration properties
**Validation**: No deprecated property warnings in application startup

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `upgrade-sb-2.5-to-2.6-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, web, config, security
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-critical warnings)

## Success Criteria
- ✅ Spring Boot 2.6.15 parent version active
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0
- ✅ Web endpoints respond correctly (no 404 errors)
- ✅ No HIGH severity path matching or security issues remain OPEN
