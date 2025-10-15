---
key: test-failure-junit4-annotations
triggers:
  - regex: 'Failed to load ApplicationContext'
  - regex: 'org.junit.runner.RunWith'
  - regex: 'NoClassDefFoundError: org/junit/platform'
severity: medium
priority: 3
---

## Problem
Tests still depend on JUnit 4 constructs while running under JDK 17 with JUnit 5 engine expectations.

## Recommended Actions
1. Ensure JUnit 5 (jupiter + platform launcher) dependencies present.
2. Remove `@RunWith(SpringRunner.class)` -> use `@SpringBootTest` / `@ExtendWith(SpringExtension.class)` if needed.
3. Convert JUnit 4 annotations: `@Before`->`@BeforeEach`, `@After`->`@AfterEach`, etc.
4. Replace expected exceptions with `assertThrows`.
5. Run `mvn -q test` again.

## Validation
Unit tests pass without JUnit 4 annotation errors.

## Rollback
If widespread failures, branch for migration and merge after stabilization.
