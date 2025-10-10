# Java Migration Plan: cytric.mobile.certifiedscanning.trusted_db


---

## Executive Summary

### Migration Overview

| Aspect | Current | Target | Strategy |
|--------|---------|--------|----------|
| **Java** | 11 | 21 (LTS) | Incremental: 11â†’17â†’21 |
| **Spring Boot** | 2.3.12.RELEASE | 3.4.0 (latest GA) | Incremental: 2.3â†’2.4â†’2.5â†’2.6â†’2.7â†’3.4 |
| **Jakarta EE** | javax.* | jakarta.* | Phase 2 migration (12 imports) |
| **Test Framework** | JUnit 4 | JUnit 5 | Included in Phase 1 |
| **Build Tool** | Maven | Maven | No change |
| **Modules** | 1 (single) | 1 | Simple topology |

### Risk Assessment

**Overall Risk Level:** ðŸŸ¡ **MEDIUM**

**Key Risk Factors:**
- âœ… **LOW:** Small javax import footprint (12 occurrences)
- âš ï¸ **MEDIUM:** JUnit 4â†’5 migration required
- âš ï¸ **MEDIUM:** Servlet API changes (javax.servlet â†’ jakarta.servlet)
- âš ï¸ **MEDIUM:** Validation API changes (javax.validation â†’ jakarta.validation)
- âš ï¸ **MEDIUM:** Oracle JDBC driver compatibility (requires version check for JDK 21)
- âœ… **LOW:** No Spring Security complexity
- âœ… **LOW:** Single module (no inter-module dependencies)


---

## Phase Overview

| Phase | Goal | Key Milestones | Exit Criteria |
|-------|------|----------------|---------------|
| **Phase 1** | Java 17 + Boot 2.7 | JDK 17 upgrade, Spring Boot 2.3â†’2.7 ladder, JUnit 4â†’5 | Builds & tests pass on JDK 17 + Boot 2.7 |
| **Phase 2** | Boot 3 + Jakarta | Spring Boot 2.7â†’3.4, javaxâ†’jakarta migration | Builds & tests pass on Boot 3.4 |
| **Phase 3** | Java 21 + Modernization | JDK 21 upgrade, modern API adoption | Builds & tests pass on JDK 21 + Boot 3.4 |

---

## Detailed Task List


### Phase 1: JDK 17 + Spring Boot 2.x Incremental Upgrades

**Goal:** Modernize to JDK 17 and incrementally upgrade Spring Boot through 2.4, 2.5, 2.6, 2.7 releases and upgrade JUnit 4 to 5.

**Prerequisites:** JAVA_HOME=JDK17
Create a branch `migration/springboot-3.4-jdk21` from `<current-one>`

#### Phase 1 Tasks

-  [ ] **1.0 - CI Pipeline Inventory**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/ci-pipeline-inventory/`
  - **Action:** Document existing CI/CD configuration
  - **Commit:**  `phase0.1.0: inventory existing pipelines`
  - **Evidence:** Found 1 Java 11 reference in Dockerfile (eclipse-temurin:11-jre-alpine)

-  [ ] **1.1 - OpenRewrite Configuration**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/rewrite-config/`
  - **Action:** Create `rewrite.yml` with upgrade recipes
  - **Commit:**  `chore(rewrite): add OpenRewrite configuration (1.1)`
  - **Evidence:** Created rewrite/rewrite.yml with pinned recipe versions for JDK 17/21 and Spring Boot 2.xâ†’3.4 migration path

-  [ ] **1.2 - OpenRewrite Dry Run**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/rewrite-dry-run/`
  - **Action:** Test OpenRewrite recipes without applying
  - **Commit:**  `chore(rewrite): add Maven plugin and dry run assessment (1.2)`
  - **Evidence:** Created rewrite-results/initial/summary.txt with manual assessment (corporate Maven extension blocks automation)


-  [ ] **1.4 - JDK 17 Upgrade Plan**  - **Task Ref:** `migrate/tasks/phase1-ci-audit/jdk17-upgrade-plan/`
  - **Action:** Review JDK 17 compatibility and plan changes
  - **Commit:**  `docs(jdk17): add upgrade plan (1.4)`
  - **Evidence:** Created plans/jdk17-upgrade-pln.md with comprehensive migration strategy

-  [ ] **1.5 - Apply JDK 17 Upgrade**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/apply-jdk17-upgrade/`
  - **Action:** Update pom.xml `<java.version>` to 17, fix compilation issues
  - **Evidence:** 
    - Updated java.version: 11 â†’ 17 âœ…
    - Updated jacoco.plugin.version: 0.8.5 â†’ 0.8.12 (JDK 17 support) âœ…
    - Build test: `mvn clean compile` SUCCESS âœ…
    - Tests: Require Spring Boot upgrade for full ASM support (proceed to 1.6)
  


-  [ ] **1.6 - Upgrade Spring Boot 2.3 â†’ 2.4**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/upgrade-sb-2.3-to-2.4/` (adapt for 2.3â†’2.4)
  - **Action:** Update parent POM to Spring Boot 2.4.13
  - **Commit:**  `feat(spring-boot): upgrade to 2.4.13 (1.6)`
  - **Evidence:** Compilation succeeds, JUnit 4â†’5 migration pending in task 1.10

-  [ ] **1.10 - JUnit 4 â†’ JUnit 5 Migration**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/junit4-to-5-migration/` (includes JUnit migration)
  - **Action:** Migrate all test files from JUnit 4 to JUnit 5 syntax
  - **Method:** Automated using Python script `scripts/migrate-junit4-to-junit5.py`
  - **Changes:**
    - Removed `@RunWith(SpringRunner.class)` (not needed in Spring Boot 2.4+)
    - Updated imports: `org.junit.*` â†’ `org.junit.jupiter.api.*`
    - Updated annotations: `@Before` â†’ `@BeforeEach`, `@Ignore` â†’ `@Disabled`
    - Converted `@Test(expected=...)` â†’ `assertThrows()`
    - Removed `ExpectedException` rule pattern
    - Files modified: 10 out of 13 test files
    - Total automated transformations: 53
  - **Build Test:** `mvn clean test-compile` 

-  [ ] **1.7 - Upgrade Spring Boot 2.4 â†’ 2.5**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/upgrade-sb-2.4-to-2.5/` (adapt for 2.4â†’2.5)
  - **Action:** Update parent POM to Spring Boot 2.5.15
  - **OpenRewrite Recipe:** `org.openrewrite.java.spring.boot2.UpgradeSpringBoot_2_5`
  - **Build Test:** `mvn clean verify`


-  [ ] **1.8 - Upgrade Spring Boot 2.5 â†’ 2.6**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/upgrade-sb-2.5-to-2.6/` (adapt for 2.5â†’2.6)
  - **Action:** Update parent POM to Spring Boot 2.6.15
  - **OpenRewrite Recipe:** `org.openrewrite.java.spring.boot2.UpgradeSpringBoot_2_6`
  - **Build Test:** `mvn clean verify`

-  [ ] **1.9 - Upgrade Spring Boot 2.6 â†’ 2.7**
  - **Task Ref:** `migrate/tasks/phase1-ci-audit/upgrade-sb-2.6-to-2.7/` (adapt for 2.6â†’2.7)
  - **Action:** Update parent POM to Spring Boot 2.7.18 (last 2.x release)
  - **OpenRewrite Recipe:** `org.openrewrite.java.spring.boot2.UpgradeSpringBoot_2_7`
  - **Build Test:** `mvn clean verify`

**Phase 1 Checkpoint:**
- **Tag:** `checkpoint-phase1`
- **Exit Criteria:** 
  - âœ… JDK 17 compilation successful
  - âœ… Spring Boot 2.7.18 active
  - âœ… All tests passing with JUnit 5
  - âœ… `mvn clean verify` succeeds

---

### Phase 2: Spring Boot 3.x + Jakarta EE Migration

**Goal:** Upgrade to Spring Boot 3.4.0 and migrate from javax.* to jakarta.* packages.

**Prerequisites:** Phase 1 complete, Spring Boot 2.7.18, JDK 17

#### Phase 2 Tasks

-  [ ] **2.0 - Boot 3 Readiness Assessment**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/boot3-readiness/`
  - **Action:** Review breaking changes and prepare mitigation plan`
  - **Evidence:**
    - Report: boot3-readiness-report.md âœ… (comprehensive analysis with risk matrix)
    - Inventory: readiness-javax.txt âœ… (9 files, 12 javax imports)
    - Details: readiness-javax-details.txt âœ… (import-level breakdown)
    - Dependency tree: readiness-deps.txt âœ… (Maven analysis)
  - **Key Findings:**
    - Overall Risk: ðŸŸ¡ MEDIUM
    - javax.servlet: 4 files (MainController, filters, providers)
    - javax.sql: 4 files (config + tests)
    - javax.validation: 2 files (MainController, AuditTrailLog)
    - No WebSecurityConfigurerAdapter usage âœ…
    - Custom Amadeus libs need compatibility verification âš ï¸
    - Oracle JDBC upgrade required (19.3.0.0 â†’ 21.9.0.0+)

-  [ ] **2.1 - Upgrade Spring Boot 2.7 â†’ 3.4**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/upgrade-boot3/`
  - **Action:** Update parent POM to Spring Boot 3.4.0
  - **Status:** âœ… COMPLETED
  - **Changes:**
    ```xml
    <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>3.4.0</version>
    </parent>
    ```
  - **OpenRewrite Recipe:** `org.openrewrite.java.spring.boot3.UpgradeSpringBoot_3_4`
  - **Initial Build:** Expected to fail (javax imports) âœ… Confirmed - next task required
  - **Commit:** Already applied in pom.xml

- [ ] **2.2 - Jakarta EE Migration (javax â†’ jakarta)**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/jakarta-migration/`
  - **Action:** Migrate all javax.* imports to jakarta.*
  - **OpenRewrite Recipe:** `org.openrewrite.java.migrate.jakarta.JavaxMigrationToJakarta`
  - **Affected Imports (xx occurrences):**
    - `javax.servlet` â†’ `jakarta.servlet`
    - `javax.sql` â†’ `jakarta.sql`
    - `javax.validation` â†’ `jakarta.validation`
  - **Files to Update:**

    1. Test files (sql)
  - **Build Test:** `mvn clean verify`
  - **Commit:** `refactor(jakarta): migrate javax to jakarta packages (2.2)`

- [ ] **2.3 - Update Oracle JDBC Driver**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/update-dependencies/`
  - **Action:** Upgrade Oracle JDBC to version compatible with Jakarta EE 9+
  - **Changes:**
    ```xml
    <oracle.version>21.9.0.0</oracle.version>
    ```
  - **Verification:** Check compatibility matrix for JDK 17 + Jakarta
  - **Commit:** `build(deps): upgrade Oracle JDBC to 21.9.0.0 (2.3)`

- [ ] **2.4 - Update Other Dependencies**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/update-dependencies/`
  - **Action:** Update dependencies to Boot 3 compatible versions
  - **Changes:**
    - Logback: Update to version managed by Boot 3.4 (remove explicit version)
    - BouncyCastle: Update to `bcpkix-jdk18on` version 1.78+
    - PDFBox: Update to 2.0.30+
  - **Commit:** `build(deps): update dependencies for Boot 3 compatibility (2.4)`

- [ ] **2.5 - Fix Servlet API Changes**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/servlet-changes/`
  - **Action:** Address Servlet 6.0 breaking changes
  - **Key Changes:**
    - `HttpServletRequest` method signature changes
    - Filter registration updates
  - **Build Test:** `mvn clean verify`


- [ ] **2.6 - Fix Validation API Changes**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/validation-changes/`
  - **Action:** Address Jakarta Validation 3.0 changes
  - **Files:** `MainController.java`, `AuditTrailLog.java`
  - **Build Test:** `mvn clean verify`

- [ ] **2.7 - Update Actuator Configuration**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/actuator-updates/`
  - **Action:** Review and update Actuator endpoints for Boot 3
  - **Files:** `application.yml`, `OracleConnectionHealthIndicator.java`


- [ ] **2.8 - Full Integration Test**
  - **Task Ref:** `migrate/tasks/phase2-boot3-migration/integration-test/`
  - **Action:** Run full test suite and manual smoke tests
  - **Verification:**
    - `mvn clean verify` passes
    - All unit tests pass
    - All integration tests pass
    - Application starts successfully
    - Actuator endpoints respond

**Phase 2 Checkpoint:**
- **Tag:** `checkpoint-phase2`
- **Exit Criteria:**
  - âœ… Spring Boot 3.4.0 active
  - âœ… All javax â†’ jakarta migrations complete
  - âœ… All tests passing
  - âœ… Application starts and runs on JDK 17
  - âœ… No compilation warnings

---

### Phase 3: JDK 21 + Modernization

**Goal:** Upgrade to JDK 21 and adopt modern Java features.

**Prerequisites:** Phase 2 complete, Spring Boot 3.4.0, JDK 17
**Toolchain Alignment:** Ensure Maven runs on the same JDK as the target. Set both `JAVA_HOME` and `MAVEN_JAVA_HOME` to the JDK 21 installation for the current shell/session before building.

#### Phase 3 Tasks

- [ ] **3.0 - Set JAVA_HOME and MAVEN_JAVA_HOME to JDK 21**
  - **Task Ref:** `migrate/tasks/phase0-toolkit-setup/jdk-switch/`
  - **Action:** Update JAVA_HOME and MAVEN_JAVA_HOME environment variables to JDK 21 for the current shell/session
  - **Verification:** `java -version` and `mvn -v` both show JDK 21

- [ ] **3.1 - Update pom.xml for JDK 21**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/dependency-alignment/`
  - **Action:** Update Java version in pom.xml
  - **Changes:**
    ```xml
    <java.version>21</java.version>
    ```
  - **Build Test:** `mvn clean verify` with JDK 21
  - **Commit:** `feat(java): upgrade to JDK 21 (3.1)`

- [ ] **3.2 - Fix JDK 21 Compilation Issues**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/remediation-and-tests/`
  - **Action:** Resolve any JDK 21 specific compilation issues
  - **Common Issues:**
    - Deprecated API removals
    - Stricter null checks
    - Security manager removal impacts
  - **Build Test:** `mvn clean compile`
  - **Commit:** `fix(jdk21): resolve compilation issues (3.2)`

- [ ] **3.3 - Update Oracle Driver for JDK 21**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/dependency-alignment/`
  - **Action:** Verify/update Oracle JDBC driver for JDK 21 compatibility
  - **Verification:** Check Oracle compatibility matrix
  - **Recommended:** Oracle JDBC 21.x or 23.x
  - **Commit:** `build(deps): ensure Oracle JDBC compatible with JDK 21 (3.3)`

- [ ] **3.4 - Update BouncyCastle for JDK 21**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/dependency-alignment/`
  - **Action:** Ensure BouncyCastle library is JDK 21 compatible
  - **Changes:**
    ```xml
    <dependency>
      <groupId>org.bouncycastle</groupId>
      <artifactId>bcpkix-jdk18on</artifactId>
      <version>1.78</version>
    </dependency>
    ```
  - **Commit:** `build(deps): update BouncyCastle for JDK 21 (3.4)`

- [ ] **3.5 - Run Full Test Suite on JDK 21**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/remediation-and-tests/`
  - **Action:** Execute complete test suite
  - **Verification:**
    - `mvn clean verify` passes
    - No test failures
    - No warnings in logs
  - **Commit:** N/A (verification only)

- [ ] **3.6 - Performance Validation**
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/performance-and-gc-profiling/`
  - **Action:** Validate performance characteristics on JDK 21
  - **Checks:**
    - Application startup time
    - Memory footprint
    - Response times
  - **Commit:** `docs(perf): add JDK 21 performance baseline (3.6)`

- [ ] **3.7 - Virtual Threads Assessment** (Optional)
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/language-feature-adoption/`
  - **Action:** Evaluate virtual threads (Project Loom) for I/O-bound operations
  - **Scope:** Oracle DB connections, HTTP requests
  - **Status:** â„¹ï¸ OPTIONAL - Modern Java feature adoption
  - **Commit:** `docs(modernization): assess virtual threads opportunities (3.7)`

- [ ] **3.8 - Modernization Opportunities Catalog** (Optional)
  - **Task Ref:** `migrate/tasks/phase3-jdk21-modernization/modernization-opportunities/`
  - **Action:** Document modern Java features applicable to codebase
  - **Features to Consider:**
    - Pattern matching (JDK 21)
    - Record classes
    - Sealed classes
    - Text blocks
    - Switch expressions
    - Virtual threads
  - **Status:** â„¹ï¸ ADVISORY - Future improvement opportunities
  - **Commit:** `docs(modernization): catalog JDK 21 feature opportunities (3.8)`

**Phase 3 Checkpoint:**
- **Tag:** `checkpoint-phase3`
- **Exit Criteria:**
  - âœ… JDK 21 compilation successful
  - âœ… All tests passing on JDK 21
  - âœ… Application runs successfully
  - âœ… Performance metrics acceptable
  - âœ… No regression in functionality
- **Commit:** `chore(milestone): complete Phase 3 - JDK 21 + modernization (3.x)`

---

## Final Migration Checkpoint

- [ ] **Final Verification**
  - **Action:** Complete end-to-end verification
  - **Checks:**
    - âœ… Java 21 active
    - âœ… Spring Boot 3.4.0 active
    - âœ… All tests passing
    - âœ… Application starts and serves requests
    - âœ… Actuator endpoints functional
    - âœ… Database connectivity verified
    - âœ… Logging working correctly
    - âœ… Metrics publishing to Prometheus

- [ ] **Create Pull Request**
  - **Branch:** `migration/springboot-3.4-jdk21` â†’ `current develop`
  - **Title:** `feat: migrate to Java 21 and Spring Boot 3.4`
  - **Description:** Include migration summary, breaking changes, testing notes

- [ ] **Final Tag**
  - **Tag:** `migration-complete-java21-boot3.4`
  - **Message:** "Completed migration to Java 21 and Spring Boot 3.4.0"

---

## Commit Message Convention

All commits follow the Conventional Commits specification:

```
<type>(<scope>): <short description> (<phase.task>)

<optional body>

<optional footer>
```

**Types:** `feat`, `fix`, `docs`, `chore`, `test`, `refactor`, `build`  
**Scopes:** `java`, `spring-boot`, `jakarta`, `junit`, `deps`, `ci`, `toolkit`

**Examples:**
- `feat(java): upgrade to JDK 17 (1.5)`
- `feat(spring-boot): upgrade to 2.4.13 (1.6)`
- `refactor(jakarta): migrate javax to jakarta packages (2.2)`
- `test(junit): migrate from JUnit 4 to JUnit 5 (1.10)`
- `build(deps): upgrade Oracle JDBC to 21.9.0.0 (2.3)`

---

## Branch & Tag Strategy

### Branches
- **Main Migration Branch:** `migration/springboot-3.4-jdk21` (all work happens here)
- **Backup Branch:** `backup/pre-migration` (frozen snapshot of develop)
- **Base Branch:** `develop` (merge target)

### Tags
- `baseline-pre-migration` - Initial state before any changes
- `checkpoint-phase0` - Phase 0 complete (toolkit ready)
- `checkpoint-phase1` - Phase 1 complete (JDK 17 + Boot 2.7)
- `checkpoint-phase2` - Phase 2 complete (Boot 3.4 + Jakarta)
- `checkpoint-phase3` - Phase 3 complete (JDK 21)
- `migration-complete-java21-boot3.4` - Final successful state

---

## Risk Mitigation Strategies

### 1. JUnit 4â†’5 Migration Risks
**Risk:** Test failures due to assertion/annotation changes  
**Mitigation:**
- Use OpenRewrite automated migration
- Test after each module migration
- Keep test coverage metrics stable

### 2. Jakarta EE Migration Risks
**Risk:** Runtime issues with jakarta.* packages  
**Mitigation:**
- Thorough grep to find all javax imports (12 identified)
- Test thoroughly after migration
- Use OpenRewrite for consistency

### 3. Oracle JDBC Compatibility
**Risk:** Driver incompatibility with JDK 21  
**Mitigation:**
- Verify Oracle certification matrix
- Test database operations in Phase 3 early
- Have fallback driver versions ready

### 4. Servlet API Changes
**Risk:** Breaking changes in Servlet 6.0  
**Mitigation:**
- Review Servlet 6.0 migration guide
- Test filter registration thoroughly
- Validate request/response handling

### 5. Spring Boot 3 Breaking Changes
**Risk:** Configuration property changes, removed classes  
**Mitigation:**
- Review Spring Boot 3.0 migration guide
- Use OpenRewrite upgrade recipes
- Test incrementally with 2.7â†’3.0â†’3.4 path

---

## Rollback Strategy

If critical issues arise at any checkpoint:

1. **Immediate Rollback:**
   ```bash
   git checkout backup/pre-migration
   ```

2. **Partial Rollback to Checkpoint:**
   ```bash
   git checkout checkpoint-phase1  # or phase0, phase2
   git checkout -b migration/springboot-3.4-jdk21-retry
   ```

3. **Cherry-pick Successful Changes:**
   ```bash
   git cherry-pick <commit-hash>
   ```

---

## Testing Strategy

### Unit Tests
- Run after each Spring Boot version increment
- Command: `mvn clean test`
- Threshold: 100% must pass

### Integration Tests
- Run at each phase checkpoint
- Command: `mvn clean verify`
- Threshold: 100% must pass

### Manual Smoke Tests
- Application startup
- Actuator health endpoint: `/actuator/health`
- Database connectivity
- API endpoints (signing, validation)
- Logging output format

### Performance Tests (Phase 3)
- Baseline on JDK 17 vs JDK 21
- Memory usage comparison
- Startup time comparison
- Response time for key endpoints

---

## Dependencies Update Summary

| Dependency | Current | Target | Reason |
|------------|---------|--------|--------|
| Java | 11 | 21 | LTS upgrade path |
| Spring Boot | 2.3.12 | 3.4.0 | Latest GA, Jakarta EE 9+ |
| JUnit | 4 | 5 (Jupiter) | Modern testing framework |
| Oracle JDBC | 19.3.0.0 | 21.9.0.0+ | JDK 21 compatibility |
| BouncyCastle | bcpkix-jdk15on:1.61 | bcpkix-jdk18on:1.78 | JDK 21 compatibility |
| PDFBox | 2.0.14 | 2.0.30+ | Security updates |
| Logback | 1.2.3 | Boot-managed | Boot 3 dependency management |

---

## Known Issues & Limitations

### 1. Custom Amadeus Dependencies
- `com.amadeus.cytric.lab:spring-logging-id:1.0.0`
- `com.amadeus.cytric.lab:logback-formatter-bunyan:1.0.0`

**Action Required:** Verify these libraries are compatible with Spring Boot 3 and Jakarta EE 9. May require internal library updates.

### 2. Oracle UCP (Universal Connection Pool)
**Issue:** May have Jakarta namespace compatibility issues  
**Action:** Test thoroughly in Phase 2, consider upgrading to latest UCP version

### 3. Hamcrest Test Library
**Current:** 1.3 (old)  
**Recommendation:** Update to Hamcrest 2.2+ or migrate to AssertJ

---

## Success Criteria


### Phase 1: JDK 17 + Boot 2.7
âœ… Compiles with JDK 17  
âœ… Spring Boot 2.7.18 active  
âœ… JUnit 5 tests passing  
âœ… `mvn clean verify` succeeds  

### Phase 2: Boot 3 + Jakarta
âœ… Spring Boot 3.4.0 active  
âœ… All javax imports migrated to jakarta  
âœ… Oracle JDBC compatible  
âœ… Application starts and runs  
âœ… All tests passing  

### Phase 3: JDK 21
âœ… Compiles with JDK 21  
âœ… All tests passing on JDK 21  
âœ… Performance acceptable  
âœ… No regressions  

### Final
âœ… Production-ready state on JDK 21 + Spring Boot 3.4.0  
âœ… Documentation updated  
âœ… Team trained on new versions  

---


```
/exec-java-migration
```

---

## Appendix A: File Change Inventory

### Phase 1 Changes


### Phase 2 Changes


### Phase 3 Changes


**Total Estimated File Changes:** ~xxx files

---

## Appendix B: Useful Commands

### Build & Test
```bash
# Clean build with tests
mvn clean verify

# Skip tests (use sparingly)
mvn clean install -DskipTests

# Run tests only
mvn test

# Check for dependency updates
mvn versions:display-dependency-updates
```

### OpenRewrite
```bash
# Dry run (see changes without applying)
mvn rewrite:dryRun

# Apply changes
mvn rewrite:run

# Run specific recipe
mvn rewrite:run -Drewrite.activeRecipes=org.openrewrite.java.spring.boot3.UpgradeSpringBoot_3_4
```

### Git
```bash
# Check status
git status

# View changes
git diff

# Stage and commit
git add .
git commit -m "feat(java): upgrade to JDK 17 (1.5)"

# Create tag
git tag -a checkpoint-phase1 -m "Phase 1 complete: JDK 17 + Boot 2.7"

# Push with tags
git push origin migration/springboot-3.4-jdk21 --tags
```

### Toolchain Alignment (Maven on JDK 21)
PowerShell:
```powershell
$env:JAVA_HOME = "C:\\migration-toolkit\\jdk\\21"
$env:MAVEN_JAVA_HOME = $env:JAVA_HOME
$env:Path = "$($env:JAVA_HOME)\bin;$env:Path"
java -version
mvn -v
mvn -B clean verify
```

cmd:
```bat
set "JAVA_HOME=C:\\migration-toolkit\\jdk\\21"
set "MAVEN_JAVA_HOME=%JAVA_HOME%"
set "PATH=%JAVA_HOME%\bin;%PATH%"
java -version
mvn -v
mvn -B clean verify
```

---

**End of Migration Plan**

Generated by: java-migration-bootstrap v1.0  
Plan ID: java-migration-yyyymmdd-hhmm  
Context: migration-bootstrap-context.yaml

