---
key: parameterized-conversion-needed
triggers:
  - regex: '@RunWith\(Parameterized.class\)'
severity: medium
priority: 3
---

## Problem
JUnit 4 parameterized tests still using `@RunWith(Parameterized.class)` preventing clean Jupiter-only run.

## Recommended Actions
1. Replace class with `@ParameterizedTest` methods.
2. Use appropriate sources: `@ValueSource`, `@CsvSource`, `@MethodSource`.
3. Move common setup into `@BeforeEach`.
4. Remove `@RunWith(Parameterized.class)`.

## Validation
Tests appear as multiple dynamic runs under Jupiter; no @RunWith usage remains.

## Rollback
Keep vintage engine temporarily if immediate conversion too large; mark DEFERRED entry.
