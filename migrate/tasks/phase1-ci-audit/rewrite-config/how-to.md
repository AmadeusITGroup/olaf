# OpenRewrite Configuration — Phase 1

## Preferred approach
1. Add OpenRewrite plugin configuration (Maven or Gradle) with no active recipes yet.
2. Create a `rewrite.yml` file at project root for recipes management.
3. Validate plugin loads: `mvn -q rewrite:help` or Gradle equivalent.

## Backup option
- If plugin setup fails, run rewrite via CLI Docker image temporarily and migrate to build plugin later.

## Verify
- Build shows OpenRewrite plugin available; no recipes run yet.
