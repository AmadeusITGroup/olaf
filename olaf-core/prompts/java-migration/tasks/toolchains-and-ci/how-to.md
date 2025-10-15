# Toolchains and CI — Enable JDK 21

## Goal
Introduce JDK 21 into local build toolchains and CI pipelines in parallel with JDK 17, validate stability, then promote 21 to primary once remediation complete.

## Preconditions
- Dependency alignment & initial JDK 21 remediation in progress.
- Build passes on JDK 17.

## Sequence (Preferred)
1. Local toolchain setup:
   - Maven: update `.mvn/toolchains.xml` to include JDK 17 & 21 definitions (vendor + version + path if needed).
   - Gradle: configure `java { toolchain { languageVersion = JavaLanguageVersion.of(17) } }` plus a conditional property to switch to 21 (`-PuseJdk21=true`).
2. CI matrix expansion:
   - Add JDK 21 to matrix (GitHub Actions: `[17,21]`; Jenkins: axis). Ensure cache keys include java version.
   - Install step uses setup action or tool installer supporting 21 GA build.
3. Conditional compilation level:
   - Keep target/release=17 initially while running tests on 21 to surface incompatibilities gradually.
4. Parallel verification runs:
   - Capture build + test results for both versions; store summaries (`ci-matrix-summary-<ts>.md`) under findings.
5. Promotion to 21:
   - After remediation-and-tests green on 21, raise release/target to 21; keep 17 as secondary (or remove if policy allows).
6. Observability:
   - Add basic telemetry comparing durations & test outcomes (optional) to detect regressions early.
7. Document workflow diff:
   - Create `ci_workflow_diff.md` with: previous jobs, new jobs, env var/property changes, cache key adjustments.
8. Commit: `ci(java): add JDK 21 toolchain + matrix` then later `ci(java): promote JDK 21 to primary`.

## Issue Collection
File: `toolchains-and-ci-<YYYYMMDD-HHmm>.json`.
Fields: id, detected_at, category (toolchain|ci-cache|config|build), file_path, snippet, severity, remediation_key, status, rationale_for_deferral.

## Common Problems → Remediation Keys
- Toolchain resolution failure → `ci-toolchain-resolution`
- CI job failing only on 21 → `ci-jdk21-failure`
- Cache mismatch (different JDK mixing caches) → `ci-cache-collision`
- Target release mismatch (compiles on 17 fails 21) → `ci-target-mismatch`
- Missing JDK 21 distribution in runner → `ci-missing-jdk21`

## Verification Criteria
- Matrix jobs succeed for both JDK versions (initial phase) then for JDK 21 alone (after promotion).
- ci_workflow_diff.md stored with clear before/after.
- No HIGH severity OPEN CI/toolchain issues.

## Backup Option
If toolchain plugin causes instability:
1. Revert to direct JAVA_HOME switching on runners.
2. Log issue `ci-toolchain-resolution` with details; attempt plugin upgrade or alternative distribution.
3. Retry integration after remediation tasks complete.

## Defer Rules
- Removal of JDK 17 lane may DEFER until post-release confidence window.
- Observability enhancements optional; may DEFER with rationale.

## Next Steps
Stable dual-version CI supports final performance profiling and language feature rollout before fully standardizing on JDK 21.
