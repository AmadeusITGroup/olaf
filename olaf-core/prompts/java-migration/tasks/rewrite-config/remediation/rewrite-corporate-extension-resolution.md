---
key: rewrite-corporate-extension-resolution
triggers:
  - regex: '(Could not find artifact .*develocity-maven-extension.*|develocity-maven-extension:RELEASE.*not resolvable)'
severity: high
priority: 1
---

## Problem
Maven fails before plugin goals due to an enterprise extension in `.mvn/extensions.xml` that cannot be resolved (e.g. `com.amadeus.develocity.extension:develocity-maven-extension:RELEASE`).

## Recommended Actions
1. Configure Maven `settings.xml` with corporate mirrors/servers:
   - Place at `%USERPROFILE%/.m2/settings.xml` (Windows) or `~/.m2/settings.xml` (Unix).
   - Include `<mirrors>` for corporate Artifactory/Nexus and `<servers>` credentials if needed.
   - See the `settings.xml.example` provided in findings for a template.
2. If immediate validation is needed, temporarily disable the extension:
   - Edit `.mvn/extensions.xml` and comment out the enterprise extension block.
   - Run the validation command (e.g. `mvn -q rewrite:help`).
   - Restore the extension after validation and proceed with a long-term fix.

## Validation
- `mvn -q rewrite:help` runs successfully (no failures) with the rewrite plugin configured and no active recipes.

## Rollback
- Re-enable the extension by restoring `.mvn/extensions.xml` to its original content.
- Keep `settings.xml` in place for future builds.
