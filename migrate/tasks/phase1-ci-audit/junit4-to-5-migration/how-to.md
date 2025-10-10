# JUnit 4 → 5 Migration — Phase 1

## Preferred approach
1. Add JUnit Jupiter dependencies; ensure vintage where needed temporarily.
2. Migrate annotations and assertions; update Surefire plugin if Maven.
3. Run tests, remove vintage when clean.

## Backup option
- Keep vintage engine longer for slow-moving modules; plan gradual migration.

## Verify
- Tests pass on JUnit 5 only; no vintage dependencies remain.
