# Remediation and Tests — JDK 21 Migration

## Preferred approach
1. Clean build with tests to surface issues:
   - Maven: `mvn clean verify`
   - Gradle: `./gradlew clean build`
2. Triage failures by category:
   - Removed/changed APIs, stricter checks, reflective access, security manager removal
3. Remediate iteratively:
   - Fix source issues; prefer minimal code changes first
   - Update plugins if build fails due to toolchain
4. Re-run tests until green.

## Backup option
- If tests can’t run yet, aim for `mvn -q -DskipTests compile` or Gradle `classes` to validate compilation
  and defer integration tests to a later step.

## Verify
- `mvn clean verify` (or Gradle equivalent) passes.
- No warnings indicating deprecated/removed APIs in core paths.
