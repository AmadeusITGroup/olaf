# Upgrade Spring Boot 2.5 → 2.6 — Phase 1

## Preferred approach
1. Update to 2.6.x and address configuration changes (e.g., path matching strategy).
2. Run integration tests focusing on web endpoints.

## Backup option
- Use compatibility flags temporarily while refactoring configs.

## Verify
- All tests pass; configuration aligns with Boot 2.6 defaults.
