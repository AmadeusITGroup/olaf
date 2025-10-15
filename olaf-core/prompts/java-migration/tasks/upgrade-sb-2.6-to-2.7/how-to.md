# Upgrade Spring Boot 2.6 → 2.7 — Phase 1

## Goal
Upgrade to final 2.x (Spring Boot 2.7.18) ensuring codebase is Boot 3 ready with minimal deprecated APIs and updated configuration.

## Prerequisites
- Spring Boot 2.6.x active and functional
- JDK 17 configured and active
- Baseline compile and unit tests passing

## Preferred Approach (Automated)
1. **Baseline Validation**:
   ```bash
   # Confirm current version and JDK 17
   mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout
   java -version | grep "17\."
   mvn clean compile test -q
   ```

2. **Version Update**:
   ```bash
   # Update Spring Boot parent version
   mvn versions:update-parent -DparentVersion=2.7.18 -DgenerateBackupPoms=false
   
   # Remove explicit versions managed by new BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Deprecated API Scan**:
   ```bash
   # Scan for deprecated security patterns
   grep -r "WebSecurityConfigurerAdapter" src/ || echo "No WebSecurityConfigurerAdapter found"
   grep -r "antMatchers" src/ || echo "No deprecated antMatchers found"
   
   # Document javax imports for Jakarta preparation
   grep -r "import javax\." src/ > javax-imports-pre-boot3.txt
   ```

4. **Build and Test**:
   ```bash
   # Rebuild with new version
   mvn clean compile -q
   
   # Run unit tests
   mvn test -q
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit pom.xml parent version to 2.7.18
2. Replace WebSecurityConfigurerAdapter with SecurityFilterChain manually
3. Update deprecated actuator properties one by one
4. Document javax imports manually for Jakarta migration planning

## Verification Commands
```bash
# Confirm Spring Boot 2.7.18 active
mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout | grep "2.7.18"

# Validate compilation
mvn clean compile -q

# Validate tests
mvn test -q

# Verify no WebSecurityConfigurerAdapter remains
grep -r "WebSecurityConfigurerAdapter" src/ && echo "FAIL: WebSecurityConfigurerAdapter found" || echo "PASS: No WebSecurityConfigurerAdapter"

# Check javax imports count for Jakarta preparation
wc -l javax-imports-pre-boot3.txt
```

## Issue Detection & Remediation

### WebSecurityConfigurerAdapter Usage (Severity: high)
**Detection Pattern**: `WebSecurityConfigurerAdapter\|extends.*WebSecurityConfigurerAdapter`
**Remediation**:
1. Replace WebSecurityConfigurerAdapter with SecurityFilterChain beans
2. Convert configure(HttpSecurity) methods to SecurityFilterChain configuration
3. Update authentication manager configuration
**Validation**: No WebSecurityConfigurerAdapter references in codebase

### Deprecated Actuator Properties (Severity: medium)
**Detection Pattern**: Deprecated actuator property warnings in logs
**Remediation**:
1. Update deprecated actuator endpoint properties
2. Replace removed property aliases with new names
3. Update metrics configuration properties
**Validation**: No deprecated actuator property warnings in logs

### Jakarta Preparation Inventory (Severity: low - informational)
**Detection Pattern**: javax imports present in codebase
**Remediation**:
1. Document all javax imports for Jakarta migration planning
2. Categorize imports by package (servlet, validation, persistence)
3. Create migration strategy based on import counts
**Validation**: Complete javax import inventory documented in findings

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `upgrade-sb-2.6-to-2.7-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, security, actuator, jakarta-prep
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (javax imports for Jakarta phase)

## Success Criteria
- ✅ Spring Boot 2.7.18 parent version active
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0
- ✅ No WebSecurityConfigurerAdapter usage: `grep -r "WebSecurityConfigurerAdapter" src/` returns empty
- ✅ Actuator configuration free of deprecated elements
- ✅ javax imports documented for Jakarta migration planning
