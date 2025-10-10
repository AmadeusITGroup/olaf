# OpenRewrite Dry Run — Phase 1

## Preferred approach
1. Ensure project compiles: `mvn -q -DskipTests compile`.
2. Run dry run: `mvn rewrite:dryRun` (or Gradle plugin equivalent).
3. Review generated diffs/reports without applying.

## Backup option
- If compilation fails, fix build blockers first (dependency alignment, source errors), then retry dry run.

## Verify
- Dry-run report produced; no code changes applied.
