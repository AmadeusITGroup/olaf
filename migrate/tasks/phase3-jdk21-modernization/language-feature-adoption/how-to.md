# Language Feature Adoption — JDK 21

## Preferred approach
1. Identify candidate areas (I/O-bound or concurrency hot paths) for virtual threads; evaluate behind a feature flag.
2. Consider modern features where safe:
   - Pattern matching, records, sealed classes, text blocks, switch expressions.
3. Apply incrementally with small PRs; add unit tests to cover changes.

## Backup option
- If runtime risks are unclear, document opportunities without code changes and revisit after performance validation.

## Verify
- All tests pass; no performance regressions.
- Code readability and maintainability improved (code reviews).
