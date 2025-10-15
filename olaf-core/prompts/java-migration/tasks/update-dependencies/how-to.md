# Update Dependencies for Boot 3 — Phase 2

## Goal
Align dependency and plugin versions with Spring Boot 3 BOM; remove obsolete overrides; upgrade third-party libraries for Jakarta & JDK 17+ compatibility without introducing convergence/conflict errors.

## Prerequisites
- Spring Boot 3 parent/BOM version applied
- Baseline compilation successful on previous version

## Preferred Approach (Automated)
1. **Capture Current State**:
   ```bash
   # Generate dependency tree snapshot
   mvn dependency:tree > dependency-tree-before.txt
   
   # List explicit version overrides
   grep -n "<version>" pom.xml | grep -v "SNAPSHOT" > explicit-overrides-before.txt
   
   # Check for available updates
   mvn versions:display-dependency-updates > dependency-updates-available.txt
   ```

2. **BOM Alignment**:
   ```bash
   # Remove versions managed by Spring Boot BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   
   # Update plugins to Boot 3 compatible versions
   mvn versions:display-plugin-updates
   ```

3. **Critical Dependency Updates**:
   ```bash
   # Update JDBC drivers for JDK 17/Jakarta compatibility
   mvn versions:use-dep-version -Dincludes=com.oracle.database.jdbc:ojdbc11 -DdepVersion=21.9.0.0
   
   # Update other Jakarta-compatible libraries
   mvn versions:use-dep-version -Dincludes=org.bouncycastle:* -DdepVersion=1.70
   ```

4. **Validation**:
   ```bash
   # Test compilation
   mvn clean compile -DskipTests
   
   # Run tests
   mvn test
   
   # Check for convergence issues
   mvn dependency:analyze-duplicate
   ```

## Fallback Approach (Manual)
If automated updates cause issues:
1. Revert to previous pom.xml: `git checkout pom.xml`
2. Update dependencies incrementally by category
3. Test compilation after each category update
4. Document forced overrides with rationale

## Verification Commands
```bash
# Generate post-update dependency tree
mvn dependency:tree > dependency-tree-after.txt

# Compare before/after explicit overrides
grep -n "<version>" pom.xml | grep -v "SNAPSHOT" > explicit-overrides-after.txt
diff explicit-overrides-before.txt explicit-overrides-after.txt

# Validate no convergence issues
mvn dependency:analyze-duplicate

# Test compilation and tests
mvn clean compile test -q

# Check enforcer rules (if configured)
mvn enforcer:enforce
```

## Issue Detection & Remediation

### Dependency Version Conflict (Severity: high)
**Detection Pattern**: `Dependency convergence error\|Version conflict`
**Remediation**:
1. Let Spring Boot BOM manage versions where possible
2. Add explicit `<dependencyManagement>` entries for conflicts
3. Use `mvn dependency:tree` to identify conflict sources
4. Apply exclusions for transitive dependencies causing conflicts
**Validation**: `mvn dependency:analyze-duplicate` reports no conflicts

### Dependency Jakarta Relocation (Severity: high)
**Detection Pattern**: `ClassNotFoundException` for relocated Jakarta classes
**Remediation**:
1. Update dependencies to Jakarta-compatible versions
2. Replace `javax.activation` with `jakarta.activation`
3. Update XML binding dependencies to Jakarta variants
4. Check vendor documentation for Jakarta migration guides
**Validation**: All dependencies use jakarta.* packages, no javax.* references

### Plugin Version Incompatible (Severity: high)
**Detection Pattern**: Plugin execution failures with Spring Boot 3
**Remediation**:
1. Update maven-compiler-plugin to ≥ 3.8.0
2. Update maven-surefire-plugin to ≥ 3.0.0
3. Update spring-boot-maven-plugin to match Boot version
4. Remove explicit plugin versions managed by Spring Boot parent
**Validation**: `mvn clean compile` succeeds without plugin errors

### Missing Transitive Dependency (Severity: medium)
**Detection Pattern**: `ClassNotFoundException` for previously transitive classes
**Remediation**:
1. Add explicit dependencies that were previously transitive
2. Check Spring Boot 3 migration guide for removed starters
3. Add `jakarta.servlet-api` if web functionality missing
**Validation**: Application starts without missing class errors

### Temporary Override Required (Severity: medium)
**Detection Pattern**: Upstream dependency not yet Boot 3 compatible
**Remediation**:
1. Document temporary override with rationale and timeline
2. Check for alternative compatible libraries
3. Consider excluding problematic transitive dependencies
4. Monitor upstream for Boot 3 compatible releases
**Validation**: Override documented in collected issues with removal plan

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `update-dependencies-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, convergence, plugin, jakarta
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (temporary overrides with timeline)

## Defer Rules
- Temporary explicit overrides allowed if upstream not Boot 3 compatible (document with timeline)
- Non-critical test failures in deprecated modules may defer to modernization phase
- Plugin updates may defer if not immediately blocking compilation

## Success Criteria
- ✅ Reduced explicit version declarations in pom.xml
- ✅ No unresolved convergence errors: `mvn dependency:analyze-duplicate` clean
- ✅ Tests pass: `mvn test` exits 0
- ✅ Before/after dependency trees captured in findings
- ✅ No HIGH severity dependency issues remain OPEN
