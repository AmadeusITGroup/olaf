# Full Integration Test — Phase 2

## Preferred approach
1. Run `mvn clean verify` (or Gradle equivalent) and capture reports.
2. Focus on areas impacted by Jakarta and Boot 3 changes.

## Backup option
- If integration tests are flaky, stabilize environment and re-run with logging and retries.

## Verify
- All integration tests pass; major endpoints function.
