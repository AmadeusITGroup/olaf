# Apply JDK 17 Upgrade — Phase 1

## Goal
Green baseline (compile + unit tests) on current JDK, then upgrade to JDK 17 and re‑establish green status.

## ⚠️ BLOCKING Prerequisites (EXECUTION WILL FAIL WITHOUT THESE)
**CRITICAL: These steps are MANDATORY. Task execution WILL ABORT if skipped.**

### STEP 0: Baseline Validation (EXECUTION BLOCKER)
**This is NOT optional. You MUST execute and verify SUCCESS before proceeding.**

```bash
# Detect current JDK (REQUIRED)
java -version
mvn help:evaluate -Dexpression=java.version -q -DforceStdout

# Validate baseline (BLOCKING - MUST succeed)
mvn clean compile test -q
# IF EXIT CODE != 0: ABORT task execution immediately
```

**BLOCKING CONDITION**: If baseline validation fails, you MUST:
1. **STOP task execution** immediately  
2. Report: "TASK BLOCKED: Baseline validation failed - cannot proceed with JDK upgrade"
3. **DO NOT attempt** JDK 17 upgrade under any circumstances
4. Create issue collection JSON documenting baseline failure

## Preferred Approach (Automated)
**Prerequisites: STEP 0 baseline validation MUST be completed successfully**

1. **JDK 17 Upgrade** (Only after baseline SUCCESS):

2. **JDK 17 Upgrade**:
   ```bash
   # Switch to JDK 17 (platform-specific)
   export JAVA_HOME=/path/to/jdk17  # Linux/Mac
   # or set JAVA_HOME=C:\path\to\jdk17  # Windows
   
   # Update pom.xml
   mvn versions:set-property -Dproperty=java.version -DnewVersion=17
   
   # Compile and test
   mvn clean compile test -q
   ```

3. **Issue Resolution**: Address compilation/test failures using remediation guidance

4. **Verification**: Confirm green status before commit

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit `pom.xml` to set `<java.version>17</java.version>`
2. Update plugin versions individually if needed:
   - maven-compiler-plugin ≥ 3.8.0
   - maven-surefire-plugin ≥ 3.0.0
3. Address compilation errors one by one using IDE guidance
4. Run tests in smaller batches to isolate failures

## Verification Commands
```bash
# Confirm JDK 17 active
java -version | grep "17\."

# Validate compilation
mvn clean compile -q

# Validate tests  
mvn test -q

# Full verification
mvn clean verify -DskipITs=true
```

## Issue Detection & Remediation

### JDK 17 Compilation Errors
**Detection Pattern**: Compilation failures after JDK 17 upgrade
**Remediation**:
1. Update Maven compiler plugin to ≥ 3.8.0: `<maven.compiler.source>17</maven.compiler.source>`
2. Add `--add-opens` JVM arguments for reflective access warnings
3. Update deprecated API usage (e.g., `SecurityManager`, `Applet`)
**Validation**: `mvn clean compile` exits 0

### Plugin Version Incompatibility  
**Detection Pattern**: Plugin execution failures with JDK 17
**Remediation**:
1. Update maven-surefire-plugin to ≥ 3.0.0
2. Update maven-failsafe-plugin to ≥ 3.0.0  
3. Update jacoco-maven-plugin to ≥ 0.8.7
**Validation**: `mvn clean verify` completes without plugin errors

### JDK 17 API Removals
**Detection Pattern**: `ClassNotFoundException` or `NoSuchMethodError` for removed APIs
**Remediation**:
1. Replace removed `sun.*` internal APIs with public alternatives
2. Update security provider configurations
3. Replace deprecated `javax.xml.bind` with `jakarta.xml.bind`
**Validation**: Application starts and runs without `ClassNotFoundException`

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `apply-jdk17-upgrade-<YYYYMMDD-HHmm>.json`
- **Categories**: baseline-compile, baseline-test, upgrade-compile, upgrade-test
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (integration-only failures)

## Defer Rules
- Integration-only failures may be deferred until integration-test task
- Reflective access warnings can be deferred unless blocking compilation
- Performance test failures can be deferred until performance validation phase

## Success Criteria
- ✅ JDK 17 active: `java -version` shows 17.x
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0  
- ✅ No HIGH severity OPEN issues in collected-issues/
