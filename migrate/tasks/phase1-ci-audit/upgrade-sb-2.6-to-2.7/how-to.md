# Upgrade Spring Boot 2.6 → 2.7 — Phase 1

## Preferred approach
1. Update to 2.7.x; migrate any deprecated endpoints and config.
2. Ensure readiness for Boot 3 migration (actuator, metrics, security config).

## Backup option
- Temporarily pin problematic starters until migration phase.

## Verify
- Build green on 2.7.x; no Blockers for Boot 3.
