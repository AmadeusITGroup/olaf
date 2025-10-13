# Phase Checkpoint Verification

## Goal
Verify that all phase exit criteria are met before proceeding to the next phase.

## Sequence
1. **Review Phase Tasks**: Confirm all tasks in current phase are marked `[x]` or `[-]` with valid rationale
2. **Validate Exit Criteria**: Check each criterion listed in the migration plan for this phase
3. **Issue Resolution**: Ensure no HIGH severity OPEN issues remain in collected-issues/
4. **Compilation Test**: Run `mvn clean compile` (or gradle equivalent) - must succeed
5. **Unit Test Validation**: Run `mvn test` - must pass or have documented deferrals
6. **Environment Verification**: Confirm expected JDK/Spring Boot versions are active
7. **Documentation**: Update checkpoint status in findings directory

## Verification Commands
- `java -version` (confirm expected JDK)
- `mvn help:evaluate -Dexpression=project.parent.version -q -DforceStdout` (Spring Boot version)
- `mvn clean compile test` (full validation)

## Issue Collection
- File: `checkpoint-phase<N>-<YYYYMMDD-HHmm>.json`
- Fields: id, detected_at, category (exit-criteria|compilation|test|environment), severity, status, rationale_for_deferral

## Exit Criteria Validation
The checkpoint task validates phase-specific criteria defined in the migration plan:

### Phase 1 Criteria
- JDK 17 compilation successful
- Spring Boot 2.7.18 active
- All tests passing with JUnit 5
- `mvn clean verify` succeeds

### Phase 2 Criteria  
- Spring Boot 3.4.0 active
- All javax → jakarta migrations complete
- All tests passing
- Application starts and runs on JDK 17
- No compilation warnings

### Phase 3 Criteria
- JDK 21 compilation successful
- All tests passing on JDK 21
- Application runs successfully
- Performance metrics acceptable
- No regression in functionality

## Defer Rules
- Minor test failures may be deferred with documented rationale and remediation plan
- Performance regressions <10% may be deferred for optimization phase
- Non-critical warnings may be deferred if they don't block functionality

## Backup Option
If checkpoint fails:
1. Review collected issues for resolution guidance
2. Roll back to previous phase end tag if needed
3. Address blocking issues before proceeding