# Update Dependencies for Boot 3 — Phase 2

## Preferred approach
1. Use Boot 3 BOM; remove explicit versions.
2. Upgrade incompatible libs (e.g., Oracle JDBC, validation, servlet-related libs) to Boot 3/Jakarta compatible versions.
3. Run full build.

## Backup option
- Pin only conflicting artifacts while migrating code; remove pins later.

## Verify
- Build passes with no convergence errors.
