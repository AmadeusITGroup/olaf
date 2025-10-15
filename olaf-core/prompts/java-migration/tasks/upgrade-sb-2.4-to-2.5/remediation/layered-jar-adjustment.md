---
key: layered-jar-adjustment
triggers:
  - regex: 'layered jar'
  - regex: 'Unable to create image'
severity: medium
priority: 1
---
## Problem
Jar layering/build-image differences after upgrading to 2.5.x cause Docker build issues or cache misses.
## Recommended Actions
1. Regenerate layers: run `mvn spring-boot:build-image` (or Gradle equivalent) and inspect output.
2. Add/adjust `spring-boot.build-image.layered` config if custom.
3. Update Dockerfile to reference new layer ordering if relying on exploded layers.
## Validation
Image builds successfully; layers reflect expected ordering; no errors.
## Rollback
Revert to previous layering config; document deferral.
