---
name: detect-test-directives
description: Use this prompt to reproduce the workflow in any repository (any language/framework).
aliases: ["detect test directives", "discover test directives"]
protocol: Propose-Confirm-Act
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full .olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.

## Time Retrieval
You WILL always retrieve the current timestamp in CEDT format `YYYYMMDD-HHmm` for ephemeral artifacts and logging.

## Input Parameters
- repo_path (REQUIRED): absolute path to the repository root
- branch (OPTIONAL): branch to analyze; default is currently checked out
- os (OPTIONAL): assume Windows; produce PowerShell-friendly commands
- sample_limit (OPTIONAL): number of recent test commits/files to sample (default 30)

## User Interaction Protocol
You WILL follow Propose-Confirm-Act for this prompt due to repository scanning and optional coverage execution.

## Process

### 1. Validation Phase
- Verify `repo_path` exists and is a Git repository (`git rev-parse --is-inside-work-tree`).
- Detect dominant languages and test frameworks by scanning for well-known files:
  - Java/Kotlin: `pom.xml`, `build.gradle*`, `src/test/java`, `src/test/kotlin`
  - JS/TS: `package.json`, `jest.config.*`, `vitest.config.*`, `cypress.*`
  - Python: `pyproject.toml`, `pytest.ini`, `requirements.txt`
  - Go: `go.mod`, `*_test.go`
  - C/C++: `CMakeLists.txt`, `Makefile`, `meson.build`, `conanfile.*`, `vcpkg.json`, `tests/`, `**/*_test.(c|cc|cpp)`
  - .NET: `*.csproj`, `Directory.Build.props`, `test/*`
- Infer test runner/frameworks from dependency files and configs.

### 2. Execution Phase

#### 2.1 Git-based recent changes (Windows-safe)
- Current branch: `git rev-parse --abbrev-ref HEAD`
- Latest commit overview: `git log -1 --name-status --pretty=fuller`
- Recently changed tests (sample):
  - `git log -n {sample_limit} --name-status --date=short --pretty=format:"%h\t%ad\t%s" -- src/test`
  - If tests are elsewhere, adapt: `test`, `tests`, `__tests__`, `*.test.*`, `*.spec.*`, `**/*_test.go`, `**/*_test.cpp`
- You WILL write an ephemeral `RECENT_TESTS_REPORT.md` during the run ONLY to aid analysis.

#### 2.2 Sample tests for pattern analysis
Choose a representative small set:
- Controller/HTTP tests
- Service/component tests
- Utility/pure unit tests
- Integration tests (if present)
Identify patterns ("test directives"):
- Test runner annotations/markers
- Mocking libraries and techniques
- Assertion styles
- Test fixtures/resources
- Naming/structure conventions

#### 2.3 Generate documentation (persistent outputs)
You WILL create/update under `olaf-data/practices/` using kebab-case filenames:
- `how-to-run-tests.md`
  - Prerequisites (runtime, build tool)
  - Exact commands to run tests and coverage (Windows-friendly)
  - How to run single test/file/case
  - Report locations and useful variations
- `unit-test-patterns.md`
  - Recent change highlights
  - Frameworks/runners and directives
  - Web-layer/testing patterns
  - Mocking patterns, assertions, fixtures
  - Naming/structure and validated code snippets

#### 2.4 Optional: run tests with coverage (requires approval)
- Maven (JUnit): `mvn clean test jacoco:report`
- Gradle (JUnit): `gradlew clean test jacocoTestReport`
- Node.js (Jest): `npm test -- --coverage` or `npx jest --coverage`
- Python (pytest): `pytest --maxfail=1 --disable-warnings --cov --cov-report=html`
- Go: `go test ./... -coverprofile=coverage.out` then `go tool cover -html=coverage.out -o coverage.html`
- C/C++: configure/build/`ctest --output-on-failure`; coverage with `gcovr`/`lcov` (or platform alternatives)
- Artifacts: tool reports and coverage HTML paths should be recorded in the docs.

### 3. Validation Phase
- Confirm docs exist with required sections and stack-accurate commands/snippets.
- Verify `recent-tests-report.md` is deleted at end of run.

## Output Format
- Persistent:
  - `olaf-data/practices/how-to-run-tests.md`
  - `olaf-data/practices/unit-test-patterns.md`
- Ephemeral (deleted at end):
  - `recent-tests-report.md`

## User Communication
- Progress updates on detection, sampling, doc generation, and cleanup.
- Prompt for approval before any command that downloads deps or runs coverage.

## Domain-Specific Rules
- You MUST keep persistent practice docs under `olaf-data/practices/`.
- You MUST use kebab-case lowercase filenames for all generated artifacts.
- You MUST delete `recent-tests-report.md` after each run.
- If legacy files exist with uppercase or underscores (e.g., `HOW_TO_RUN_TESTS.md`, `UNIT_TEST_PATTERNS.md`, `RECENT_TESTS_REPORT.md`), you MUST rename them to kebab-case equivalents and update references:
  - `HOW_TO_RUN_TESTS.md` → `how-to-run-tests.md`
  - `UNIT_TEST_PATTERNS.md` → `unit-test-patterns.md`
  - `RECENT_TESTS_REPORT.md` → `recent-tests-report.md`
- You MUST use Windows-safe commands by default.

## Success Criteria
- Detected dominant test stack and summarized directives.
- Generated `HOW_TO_RUN_TESTS.md` with exact commands and report locations.
- Generated `UNIT_TEST_PATTERNS.md` with concrete, repo-specific patterns and snippets.
- Deleted `RECENT_TESTS_REPORT.md` at the end of the run.

## Error Handling
- Missing inputs or unknown test locations → request clarification.
- Unsupported stack or missing tools → propose alternatives or skips.
- Command failures → show stderr, propose remediation steps.
- Write failures → suggest alternate paths under `olaf-data/practices/`.
