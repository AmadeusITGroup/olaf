# Dependency Alignment — JDK 21 + Boot 3.x

## Goal
Ensure all dependencies and plugins are compatible with JDK 21 and Spring Boot 3.x, leveraging BOM management and upgrading critical libraries.

## Prerequisites
- Spring Boot 3.x and Jakarta namespace migration completed
- JDK 21 environment configured
- Project compiles and tests pass on JDK 17

## Preferred Approach (Automated)
1. **Baseline Capture**:
   ```bash
   # Record current Java version configuration
   grep -r "java.version\|maven.compiler" pom.xml > java-level-before.txt
   
   # Generate dependency tree
   mvn dependency:tree > dep-tree-before.txt
   
   # List critical libraries
   mvn dependency:tree | grep -E "(oracle|postgres|mysql|security|crypto)" > critical-libs-before.txt
   ```

2. **BOM and Override Cleanup**:
   ```bash
   # Check for explicit versions managed by Spring Boot BOM
   mvn versions:display-dependency-updates | grep "Spring Boot manages"
   
   # Remove unnecessary explicit versions
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Critical Library Updates**:
   ```bash
   # Update Oracle JDBC driver for JDK 21 compatibility
   mvn versions:use-dep-version -Dincludes=com.oracle.database.jdbc:ojdbc11 -DdepVersion=21.9.0.0
   
   # Update other critical libraries
   mvn versions:display-dependency-updates | grep -E "(security|crypto|xml)"
   ```

4. **Java Version Update**:
   ```bash
   # Update Java version to 21 in pom.xml
   mvn versions:set-property -Dproperty=java.version -DnewVersion=21
   
   # Compile with JDK 21
   mvn clean compile -DskipTests
   ```

5. **Testing Matrix**:
   ```bash
   # Test on JDK 21
   mvn test > test-summary-jdk21.txt
   
   # Full verification
   mvn clean verify
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually update pom.xml Java version to 21
2. Update critical dependencies one by one
3. Address compilation issues incrementally
4. Test each dependency update separately

## Verification Commands
```bash
# Verify Java 21 configuration
grep "java.version" pom.xml | grep "21"

# Check dependency tree for JDK 21 compatibility
mvn dependency:tree | grep -E "(oracle|postgres|mysql)" | head -5

# Validate compilation on JDK 21
mvn clean compile -q

# Run tests on JDK 21
mvn test -q

# Check for convergence issues
mvn dependency:analyze-duplicate
```

## Issue Detection & Remediation

### JDK 21 Incompatible Dependencies (Severity: high)
**Detection Pattern**: Compilation or runtime failures with JDK 21
**Remediation**:
1. Update Oracle JDBC driver to 21.9.0.0+ for JDK 21 support
2. Update BouncyCastle to 1.70+ for JDK 21 compatibility
3. Check vendor documentation for JDK 21 compatible versions
**Validation**: Dependencies work correctly with JDK 21

### Plugin JDK 21 Incompatibility (Severity: high)
**Detection Pattern**: Maven plugin execution failures with JDK 21
**Remediation**:
1. Update maven-compiler-plugin to ≥ 3.11.0 for JDK 21 support
2. Update maven-surefire-plugin to ≥ 3.0.0
3. Update other plugins to JDK 21 compatible versions
**Validation**: All plugins execute successfully with JDK 21

### Dependency Version Conflicts (Severity: medium)
**Detection Pattern**: Maven dependency convergence warnings
**Remediation**:
1. Let Spring Boot BOM manage dependency versions where possible
2. Add explicit dependency management for unmanaged libraries
3. Use exclusions to resolve transitive dependency conflicts
**Validation**: `mvn dependency:analyze-duplicate` reports no conflicts

### JPMS Module Issues (Severity: low)
**Detection Pattern**: Automatic module name warnings or JPMS issues
**Remediation**:
1. Add module-info.java if adopting JPMS
2. Use --add-opens JVM arguments for reflective access
3. Document JPMS warnings for future resolution
**Validation**: Application runs without module system errors

### Removed API Usage (Severity: medium)
**Detection Pattern**: Compilation errors for APIs removed in JDK 21
**Remediation**:
1. Replace removed sun.* internal APIs with public alternatives
2. Update deprecated security provider usage
3. Replace removed javax.xml.bind with jakarta.xml.bind
**Validation**: No compilation errors for removed APIs

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `dependency-alignment-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, runtime, convergence, plugin, jpms
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (vendor-dependent updates)

## Success Criteria
- ✅ Java 21 configured: `grep "java.version" pom.xml` shows 21
- ✅ Clean compilation: `mvn clean compile` exits 0 on JDK 21
- ✅ Tests pass: `mvn test` exits 0 on JDK 21
- ✅ No HIGH severity dependency compatibility issues remain OPEN
- ✅ Before/after artifacts captured in findings directory
