# How to Run Tests and Generate Coverage

## Prerequisites
- Java 17 installed and on PATH (`java -version`).
- Maven 3.9+ installed (`mvn -version`).

## Quick start (unit tests + coverage)
- Windows PowerShell:
```powershell
mvn clean test jacoco:report
```

## What this does
- Runs unit tests via Surefire (JUnit 4/Vintage + Kotlin tests).
- Generates JaCoCo coverage report.

## Where to find results
- Test reports (per-suite): `target/surefire-reports/`
- Coverage HTML report: `target/site/jacoco/index.html`

## Useful variations
- Run a single test class:
```powershell
mvn -Dtest=MainControllerTest clean test jacoco:report
```
- Run classes by pattern (glob):
```powershell
mvn -Dtest=*Controller*Test clean test jacoco:report
```
- Skip tests (build only):
```powershell
mvn -DskipTests clean package
```

## Notes
- Integration tests are not separated; most tests run as standard unit tests with Spring context.
- Active profiles in tests: `dev`, `test` as defined in test classes.
