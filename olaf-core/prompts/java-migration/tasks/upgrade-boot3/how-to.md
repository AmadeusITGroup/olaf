# Upgrade to Spring Boot 3.x — Phase 2

## Goal
Switch project from Boot 2.7.x to target Boot 3.x version with successful compile + unit tests prior to Jakarta namespace refactor.

## Prerequisites
- Boot 3 readiness assessment completed
- JDK 17 active and validated
- No WebSecurityConfigurerAdapter usage remaining

## Preferred Approach (Automated)
1. **Version Update**:
   ```bash
   # Update Spring Boot parent version
   mvn versions:update-parent -DparentVersion=3.4.0 -DgenerateBackupPoms=false
   
   # Or manually update pom.xml parent version
   sed -i 's/<version>2\.7\.[0-9]*<\/version>/<version>3.4.0<\/version>/' pom.xml
   ```

2. **Dependency Cleanup**:
   ```bash
   # Remove explicit versions managed by Boot 3 BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Compilation Test**:
   ```bash
   # Expect javax namespace failures (acceptable)
   mvn clean compile -q
   
   # Run tests (collect failures for analysis)
   mvn test -q || true
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit `pom.xml` parent version to 3.4.0
2. Remove explicit dependency versions one by one
3. Update `<java.version>` to 17 if not already set
4. Address immediate compilation blockers (non-javax issues)

## Verification Commands
```bash
# Confirm Spring Boot 3.x version active
mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout | grep "3\."

# Check for javax namespace issues (expected)
mvn compile 2>&1 | grep "package javax" | wc -l

# Validate no critical non-javax compilation errors
mvn compile 2>&1 | grep -v "package javax" | grep "ERROR" || echo "No critical errors"

# Test execution (failures expected, collect for analysis)
mvn test -q || echo "Test failures expected during Boot 3 upgrade"
```

## Issue Detection & Remediation

### WebSecurityConfigurerAdapter Usage (Severity: high)
**Detection Pattern**: `extends WebSecurityConfigurerAdapter\|WebSecurityConfigurerAdapter`
**Remediation**:
1. Replace with `@Bean SecurityFilterChain` approach
2. Convert `configure(HttpSecurity)` to `SecurityFilterChain` bean
3. Update authentication configuration to use `AuthenticationManager` beans
**Validation**: No references to `WebSecurityConfigurerAdapter` in codebase

### Dependency Upgrade Required (Severity: critical)
**Detection Pattern**: `ClassNotFoundException` for relocated/removed classes
**Remediation**:
1. Update Oracle JDBC driver to 21.9.0.0+ for JDK 17 compatibility
2. Update BouncyCastle to 1.70+ for Jakarta compatibility
3. Replace removed Spring Boot starters with new equivalents
**Validation**: `mvn dependency:tree` shows compatible versions, compilation succeeds

### Configuration Property Removed (Severity: medium)
**Detection Pattern**: `Unknown property` warnings in application startup
**Remediation**:
1. Update `application.yml`/`application.properties` for Boot 3 property changes
2. Replace removed `spring.jpa.hibernate.use-new-id-generator-mappings`
3. Update actuator endpoint configurations
**Validation**: Application starts without property warnings

### Jakarta Namespace Missing (Deferred to jakarta-migration)
**Detection Pattern**: `package javax.* does not exist`
**Remediation**: DEFERRED - Will be resolved in jakarta-migration task
**Validation**: Defer validation until jakarta-migration completion

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `upgrade-boot3-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, config, dependency, jakarta
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (jakarta namespace issues)

## Defer Rules
- javax namespace import errors → Deferred to jakarta-migration task
- Configuration property deprecation warnings → Can defer if non-blocking
- Test failures due to javax imports → Deferred to jakarta-migration task

## Success Criteria
- ✅ Spring Boot 3.4.0 parent version active
- ✅ Project compiles (javax errors acceptable and deferred)
- ✅ No HIGH severity non-javax issues remain OPEN
- ✅ Critical dependencies updated for Boot 3 compatibility
