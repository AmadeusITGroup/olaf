# Boot 3 Readiness Assessment — Phase 2

## Goal
Assess codebase for Spring Boot 3 + Jakarta migration: quantify javax usage, detect API/config risks, produce prioritized remediation plan.

## Prerequisites
- Spring Boot 2.7.x active
- JDK 17 configured and functional
- Project builds and unit tests pass

## Preferred Approach (Automated)
1. **Baseline Confirmation**:
   ```bash
   # Verify current versions
   mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout
   java -version
   mvn clean compile test -q
   ```

2. **javax Namespace Inventory**:
   ```bash
   # Count javax imports by category
   grep -r "import javax\." src/ | wc -l > javax-total-count.txt
   grep -r "import javax\.servlet" src/ | wc -l > javax-servlet-count.txt
   grep -r "import javax\.validation" src/ | wc -l > javax-validation-count.txt
   grep -r "import javax\.persistence" src/ | wc -l > javax-persistence-count.txt
   
   # Generate detailed inventory
   grep -r "import javax\." src/ > javax-detailed-inventory.txt
   ```

3. **Security Configuration Scan**:
   ```bash
   # Check for deprecated security patterns
   grep -r "WebSecurityConfigurerAdapter" src/ || echo "No WebSecurityConfigurerAdapter found"
   grep -r "antMatchers" src/ || echo "No deprecated antMatchers found"
   grep -r "authorizeRequests" src/ || echo "No deprecated authorizeRequests found"
   ```

4. **Dependency Analysis**:
   ```bash
   # Generate dependency tree and flag problematic dependencies
   mvn dependency:tree > dependency-tree-current.txt
   grep -E "(oracle|bouncycastle|javax)" dependency-tree-current.txt > flagged-dependencies.txt
   ```

## Fallback Approach (Manual)
If automated scanning fails:
1. Manually search codebase for javax imports using IDE
2. Review security configuration files manually
3. Check pom.xml for outdated dependency versions
4. Document findings in structured format

## Verification Commands
```bash
# Verify all inventory files created
ls -la javax-*-count.txt javax-detailed-inventory.txt dependency-tree-current.txt

# Validate javax count accuracy
wc -l javax-detailed-inventory.txt

# Check readiness report exists
test -f boot3-readiness-report.md && echo "PASS: Report created" || echo "FAIL: Report missing"

# Verify risk assessment completed
grep -q "Risk Level:" boot3-readiness-report.md && echo "PASS: Risk assessed" || echo "FAIL: Risk assessment missing"
```

## Issue Detection & Remediation

### High javax Usage (Severity: high if >100 imports)
**Detection Pattern**: javax import count exceeds thresholds
**Remediation**:
1. Document all javax packages in use for migration planning
2. Prioritize servlet and validation packages (most common)
3. Plan systematic replacement strategy
**Validation**: Complete inventory documented with counts and file locations

### Deprecated Security Configuration (Severity: high)
**Detection Pattern**: `WebSecurityConfigurerAdapter\|antMatchers\|authorizeRequests`
**Remediation**:
1. Plan migration to SecurityFilterChain approach
2. Document current security configuration patterns
3. Identify custom security components needing updates
**Validation**: All deprecated security patterns documented for remediation

### Outdated Dependencies (Severity: medium-high)
**Detection Pattern**: Dependencies without Jakarta support
**Remediation**:
1. Identify Jakarta-compatible versions for all dependencies
2. Flag proprietary libraries needing vendor updates
3. Plan dependency upgrade sequence
**Validation**: All dependencies assessed for Jakarta compatibility

### Plugin Version Compatibility (Severity: medium)
**Detection Pattern**: Plugin versions incompatible with Spring Boot 3
**Remediation**:
1. Document required plugin version updates
2. Check for Spring Boot 3 compatibility
3. Plan plugin upgrade sequence
**Validation**: All plugins assessed for Boot 3 compatibility

## Issue Collection
**Only collect issues if assessment reveals high-risk items**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `boot3-readiness-<YYYYMMDD-HHmm>.json`
- **Categories**: javax, security, actuator, dependency, plugin
- **Status**: OPEN (requires remediation), RESOLVED (acceptable risk), DEFERRED (vendor-dependent)

## Success Criteria
- ✅ Complete javax inventory with counts and file locations
- ✅ Security configuration patterns documented
- ✅ Dependency compatibility assessment completed
- ✅ Risk level computed and documented in report
- ✅ Readiness report created: `boot3-readiness-report.md`
- ✅ All required artifacts stored in findings directory
