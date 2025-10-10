# Upgrade Spring Boot 2.4 → 2.5 — Phase 1

## Preferred approach
1. Update BOM/parent to 2.5.x.
2. Fix breaking changes noted in release notes.
3. Rebuild and run tests.

## Backup option
- Pin conflicting transitive dependencies.

## Verify
- Build + tests pass on Boot 2.5.x.
