# Upgrade to Spring Boot 3.x — Phase 2

## Preferred approach
1. Update parent/BOM to Boot 3.x target.
2. Align dependencies using Boot 3 BOM; remove redundant version overrides.
3. Build and fix breakages.

## Backup option
- Pin specific libraries temporarily if necessary; document for later cleanup.

## Verify
- Build + tests pass on Boot 3.x target.
