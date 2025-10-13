# Remediation and Tests — JDK 21 Migration

## Goal
Systematically identify and resolve JDK 21 related build/test failures to achieve a stable green build on JDK 21.

## Prerequisites
- Dependency alignment completed for JDK 21
- JDK 21 environment configured
- Project partially compiles on JDK 21

## Preferred Approach (Automated)
1. **Full Build Analysis**:
   ```bash
   # Attempt full build on JDK 21
   mvn clean verify > jdk21-build.log 2>&1 || true
   
   # Extract compilation errors
   grep -E "(error|ERROR)" jdk21-build.log > jdk21-compilation-errors.txt
   
   # Extract test failures
   grep -E "(FAILED|Failed)" jdk21-build.log > jdk21-test-failures.txt
   ```

2. **Issue Categorization**:
   ```bash
   # Find removed API usage
   grep -r "sun\." src/ > removed-api-usage.txt
   
   # Find reflective access warnings
   grep "illegal reflective access" jdk21-build.log > reflective-access-issues.txt
   
   # Find module warnings
   grep "module" jdk21-build.log | grep -i "warning" > module-warnings.txt
   ```

3. **Systematic Remediation**:
   ```bash
   # Compile-only first to isolate compilation issues
   mvn clean compile -DskipTests
   
   # Run tests after compilation fixes
   mvn test
   
   # Full verification
   mvn clean verify
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually review compilation errors one by one
2. Replace removed APIs with public alternatives
3. Add JVM arguments for reflective access if needed
4. Update test frameworks for JDK 21 compatibility

## Verification Commands
```bash
# Verify clean compilation on JDK 21
mvn clean compile -q && echo "PASS: Compilation successful" || echo "FAIL: Compilation failed"

# Verify tests pass on JDK 21
mvn test -q && echo "PASS: Tests successful" || echo "FAIL: Tests failed"

# Full verification
mvn clean verify -q && echo "PASS: Full build successful" || echo "FAIL: Build failed"

# Check for reflective access warnings
grep -i "illegal.*access" jdk21-build.log || echo "No reflective access warnings"
```

## Issue Detection & Remediation

### Removed API Usage (Severity: high)
**Detection Pattern**: Compilation errors for removed sun.* or internal APIs
**Remediation**:
1. Replace sun.misc.Unsafe with VarHandle or MethodHandle APIs
2. Replace removed security manager APIs with modern alternatives
3. Update deprecated javax.xml.bind usage to jakarta.xml.bind
**Validation**: Code compiles without removed API references

### Illegal Reflective Access (Severity: medium)
**Detection Pattern**: "illegal reflective access" warnings in logs
**Remediation**:
1. Add --add-opens JVM arguments as temporary fix
2. Update libraries to versions that don't use internal APIs
3. Replace reflective access with public API alternatives where possible
**Validation**: No illegal reflective access warnings in build logs

### Library JDK 21 Incompatibility (Severity: high)
**Detection Pattern**: ClassNotFoundException or NoSuchMethodError at runtime
**Remediation**:
1. Update libraries to JDK 21 compatible versions
2. Replace incompatible libraries with alternatives
3. Check vendor documentation for JDK 21 support timeline
**Validation**: All libraries work correctly with JDK 21

### Module System Issues (Severity: low)
**Detection Pattern**: Module warnings or JPMS-related errors
**Remediation**:
1. Add automatic module names to dependencies if needed
2. Use --add-modules for required modules
3. Document module system warnings for future resolution
**Validation**: Application runs without module system errors

### Test Framework Compatibility (Severity: medium)
**Detection Pattern**: Test execution failures specific to JDK 21
**Remediation**:
1. Update test frameworks (JUnit, Mockito, etc.) to JDK 21 compatible versions
2. Fix test code using removed or changed APIs
3. Update test JVM arguments for JDK 21
**Validation**: All tests pass on JDK 21

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `remediation-and-tests-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, runtime, reflection, module, library
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (temporary workarounds)

## Success Criteria
- ✅ Clean compilation: `mvn clean compile` exits 0 on JDK 21
- ✅ Tests pass: `mvn test` exits 0 on JDK 21
- ✅ Full build succeeds: `mvn clean verify` exits 0 on JDK 21
- ✅ No HIGH severity JDK 21 compatibility issues remain OPEN
- ✅ Remediation artifacts stored in findings directory
