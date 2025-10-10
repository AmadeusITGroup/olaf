# Upgrade Spring Boot 2.3 → 2.4 — Phase 1

## Preferred approach
1. Use Boot BOM to manage versions; remove explicit overrides where possible.
2. Upgrade parent or dependency management to 2.4.x.
3. Build and fix deprecations.

## Backup option
- Pin only conflicting artifacts explicitly.

## Verify
- Build passes with Boot 2.4.x; no major regressions.
