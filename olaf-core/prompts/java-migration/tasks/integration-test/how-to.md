# Full Integration Test — Phase 2

## Goal
Validate end-to-end functionality post Boot 3 / Jakarta refactors with a reliable integration test suite; surface regressions early before proceeding to deeper modernization tasks.

## Prerequisites
- Unit tests passing on current branch
- Spring Boot 3 upgrade completed with successful compilation
- Test environment services available (DB, message broker, etc.)

## Preferred Approach (Automated)
1. **Environment Preparation**:
   ```bash
   # Start required services (if using Docker Compose)
   docker-compose -f docker-compose.test.yml up -d
   
   # Verify services are ready
   docker-compose -f docker-compose.test.yml ps
   
   # Set required environment variables
   export TEST_DB_URL=jdbc:h2:mem:testdb
   export TEST_PROFILE=integration
   ```

2. **Integration Test Execution**:
   ```bash
   # Run full integration test suite
   mvn clean verify -Pintegration-test
   
   # Alternative: Gradle
   ./gradlew clean integrationTest
   
   # Capture exit code for analysis
   echo $? > integration-test-exit-code.txt
   ```

3. **Results Collection**:
   ```bash
   # Copy test reports to findings
   mkdir -p olaf-data/findings/migrations/migration_*/integration-test-reports-*/
   cp -r target/surefire-reports/* olaf-data/findings/migrations/migration_*/integration-test-reports-*/
   cp -r target/failsafe-reports/* olaf-data/findings/migrations/migration_*/integration-test-reports-*/
   
   # Generate summary
   mvn surefire-report:report-only failsafe-report:report-only
   ```

## Fallback Approach (Manual)
If full suite fails or is unstable:
1. Run smoke tests first: `mvn test -Dgroups=smoke`
2. Run tests by category: `mvn test -Dtest="*ControllerTest"`
3. Identify and isolate flaky tests
4. Run stable subset until issues are resolved

## Verification Commands
```bash
# Check integration test results
mvn verify -Pintegration-test -q && echo "PASS: Integration tests successful" || echo "FAIL: Integration tests failed"

# Count test results
grep -r "Tests run:" target/surefire-reports/ target/failsafe-reports/ | tail -1

# Verify application startup in test context
mvn spring-boot:run -Dspring-boot.run.profiles=test -Dspring-boot.run.arguments="--server.port=0" &
sleep 10 && kill %1

# Check for flaky tests (run twice)
mvn verify -Pintegration-test && mvn verify -Pintegration-test
```

## Issue Detection & Remediation

### Application Startup Failure (Severity: critical)
**Detection Pattern**: Application fails to start in test context
**Remediation**:
1. Check for missing Jakarta dependencies in test classpath
2. Update test configuration properties for Spring Boot 3
3. Fix autowiring issues with new component scanning rules
4. Update security configuration for test profiles
**Validation**: Application starts successfully: `mvn spring-boot:run -Dspring-boot.run.profiles=test`

### Endpoint Mismatch (Severity: high)
**Detection Pattern**: 404 errors or unexpected endpoint responses in tests
**Remediation**:
1. Update controller mappings for Spring Boot 3 changes
2. Fix path variable and request parameter binding issues
3. Update content negotiation configuration
4. Check for actuator endpoint path changes
**Validation**: All endpoint tests pass, no 404 errors

### Serialization Issues (Severity: medium)
**Detection Pattern**: JSON serialization/deserialization failures
**Remediation**:
1. Update Jackson configuration for Spring Boot 3
2. Fix date/time serialization format changes
3. Update custom serializers for Jakarta namespace
4. Check for removed Jackson modules
**Validation**: JSON serialization tests pass, API responses correct

### Security Configuration Failure (Severity: high)
**Detection Pattern**: Authentication/authorization failures in tests
**Remediation**:
1. Update security test configuration for new SecurityFilterChain approach
2. Fix test security context setup
3. Update mock authentication for Spring Security 6
4. Check for removed security auto-configuration
**Validation**: Security tests pass, authentication works correctly

### Database Migration Issues (Severity: high)
**Detection Pattern**: Database schema or migration failures
**Remediation**:
1. Update Hibernate configuration for Jakarta persistence
2. Fix entity mapping issues with new JPA version
3. Update database migration scripts for schema changes
4. Check for removed Hibernate properties
**Validation**: Database tests pass, schema migrations successful

### Async Timing Issues (Severity: medium)
**Detection Pattern**: Intermittent failures in async/concurrent tests
**Remediation**:
1. Update async configuration for Spring Boot 3
2. Fix thread pool configuration changes
3. Add proper test synchronization for async operations
4. Update timeout configurations
**Validation**: Async tests pass consistently across multiple runs

### Flaky Tests (Severity: low)
**Detection Pattern**: Tests that pass/fail intermittently without code changes
**Remediation**:
1. Identify root cause of flakiness (timing, state, environment)
2. Add proper test isolation and cleanup
3. Fix shared state issues between tests
4. Consider marking as `@Disabled` with issue tracking
**Validation**: Tests pass consistently or are properly disabled with rationale

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `integration-test-<YYYYMMDD-HHmm>.json`
- **Categories**: startup, web-endpoint, security, data, serialization, async, flaky
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (flaky tests with stabilization plan)

## Defer Rules
- Flaky non-critical tests may defer with stabilization plan and timeline
- Low-impact endpoint tests may defer if due to pending jakarta migration
- Performance tests may defer to dedicated performance validation phase

## Success Criteria
- ✅ Integration test suite passes: `mvn verify -Pintegration-test` exits 0
- ✅ Application starts successfully in test context
- ✅ No CRITICAL or HIGH severity OPEN issues
- ✅ Test reports and summary stored in findings directory
- ✅ Flaky tests identified and documented with remediation plan
