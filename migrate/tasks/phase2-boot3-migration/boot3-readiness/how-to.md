# Boot 3 Readiness — Phase 2

## Preferred approach
1. Scan for `javax.*` imports, servlet API usage, validation API usage.
2. Inventory security, actuator, and configuration features.
3. Produce `boot3_readiness.md` with findings and risks.

## Backup option
- If scanning tools are unavailable, grep for `javax` and known migration hotspots manually.

## Verify
- Readiness report exists with clear risk classification (LOW/MEDIUM/HIGH).
