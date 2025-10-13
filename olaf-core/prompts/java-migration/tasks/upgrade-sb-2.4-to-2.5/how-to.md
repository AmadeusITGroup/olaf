# Upgrade Spring Boot 2.4 → 2.5 — Phase 1

## Goal
Upgrade from Spring Boot 2.4.x to 2.5.15 with stable compile + unit tests, addressing layering, dependency and config adjustments.

## Prerequisites
- Spring Boot 2.4.x active and functional
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
   mvn versions:update-parent -DparentVersion=2.5.15 -DgenerateBackupPoms=false
   
   # Remove explicit versions managed by new BOM
   mvn versions:use-dep-version -DdepVersion=RELEASE -DforceVersion=false
   ```

3. **Build and Test**:
   ```bash
   # Rebuild with new version
   mvn clean compile -q
   
   # Run unit tests
   mvn test -q
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually edit pom.xml parent version to 2.5.15
2. Remove explicit dependency versions managed by BOM
3. Address Docker layering configuration if using spring-boot:build-image
4. Update any deprecated properties manually

## Verification Commands
```bash
# Confirm Spring Boot 2.5.15 active
mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout | grep "2.5.15"

# Validate compilation
mvn clean compile -q

# Validate tests
mvn test -q

# Check for layered jar configuration (if using Docker)
grep -r "spring.boot.build-image" src/main/resources/ || echo "No layered jar config found"
```

## Issue Detection & Remediation

### Docker Layered Jar Configuration (Severity: medium)
**Detection Pattern**: Docker build failures or layer optimization issues
**Remediation**:
1. Update Docker build configuration for layered jar changes
2. Adjust build-image plugin configuration if needed
3. Update Dockerfile COPY commands for new layer structure
**Validation**: Docker build succeeds with optimized layers

### Reactive Timing Changes (Severity: medium)
**Detection Pattern**: Test failures in reactive/async code due to timing changes
**Remediation**:
1. Update test timeouts for reactive streams
2. Adjust StepVerifier expectations for new timing behavior
3. Update WebTestClient timeout configurations
**Validation**: Reactive tests pass consistently

### Configuration Property Changes (Severity: low)
**Detection Pattern**: Deprecated property warnings in logs
**Remediation**:
1. Update deprecated properties per Spring Boot 2.5 migration guide
2. Replace removed property aliases with new names
3. Update actuator configuration properties
**Validation**: No deprecated property warnings in application startup

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `upgrade-sb-2.4-to-2.5-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, config, dependency, docker
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-critical warnings)

## Success Criteria
- ✅ Spring Boot 2.5.15 parent version active
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0
- ✅ No HIGH severity configuration issues remain OPEN
- ✅ Docker layering works correctly (if applicable)
