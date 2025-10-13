# Java Migration Plan: <project-name>

## Executive Summary

### Migration Overview

| Aspect | Current | Target | Strategy |
|--------|---------|--------|----------|
| **Java** | <detected-java-version> | <target-java-version> | Incremental: <detected-java-version> → <target-java-version> |
| **Spring Boot** | <detected-boot-version> | <target-boot-version> | Incremental: <detected-boot-version> → <target-boot-version> |
| **Jakarta EE** | javax.* | jakarta.* | Phase 2 migration (<javax-import-count> imports) |
| **Test Framework** | <detected-junit-version> | JUnit 5 | <junit-migration-strategy> |
| **Build Tool** | <detected-build-tool> | <detected-build-tool> | No change |
| **Modules** | <module-count> (<module-type>) | <module-count> | No change |

### Risk Assessment

**Overall Risk Level:** **<overall-risk-level>**

<risk-factors>


---

## Phase Overview

| Phase | Dependencies | Key Risks | Rollback Point | Estimated Effort |
|-------|--------------|-----------|----------------|------------------|
| **Phase 1** | None (baseline) | JDK compatibility, Spring Boot incremental upgrades | `backup/pre-migration` | <phase1-effort> |
| **Phase 2** | Phase 1 complete | javax→jakarta namespace changes, API breaking changes | `checkpoint-phase1` | <phase2-effort> |
| **Phase 3** | Phase 2 complete | JDK 21 compatibility, dependency alignment | `checkpoint-phase2` | <phase3-effort> |

---

## Detailed Task List

### Prerequisites
- Set both `JAVA_HOME` and `MAVEN_JAVA_HOME` to the JDK version currently used by the project (detected: <detected-java-version>)

- [ ] **0.0 - Branch and Tag Before Migration**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** Create git branch `<branch-name>` from `<current-branch-name>` and git tag `olaf-starts-java-migration`

### Phase 1: JDK 17 + Spring Boot 2.x Incremental Upgrades

**Goal:** Modernize to JDK 17 and incrementally upgrade Spring Boot through 2.4, 2.5, 2.6, 2.7 releases and upgrade JUnit 4 to 5.

#### Phase 1 Tasks

- [ ] **1.0 - Start Phase 1 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-starts-phase1-migration`

- [ ] **1.1 - CI Pipeline Inventory**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/ci-pipeline-inventory/`
  - **Action:** Document existing CI/CD configuration
  - **Commit:** `docs(ci): inventory existing pipelines (1.1)`

- [ ] **1.2 - OpenRewrite Configuration**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/rewrite-config/`
  - **Action:** Create `rewrite.yml` with upgrade recipes
  - **Commit:** `chore(rewrite): add OpenRewrite configuration (1.2)`

- [ ] **1.3 - OpenRewrite Dry Run**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/rewrite-dry-run/`
  - **Action:** Test OpenRewrite recipes without applying
  - **Commit:** `chore(rewrite): add Maven plugin and dry run assessment (1.3)`

- [ ] **1.4 - Apply JDK 17 Upgrade**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/apply-jdk17-upgrade/`
  - **Action:** Update pom.xml `<java.version>` to 17, fix compilation issues
  - **Commit:** `feat(java): upgrade to JDK 17 (1.4)`

- [ ] **1.5 - Upgrade Spring Boot 2.3 → 2.4**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/upgrade-sb-2.3-to-2.4/`
  - **Action:** Update parent POM to Spring Boot 2.4.13
  - **Commit:** `feat(spring-boot): upgrade to 2.4.13 (1.5)`

- [ ] **1.6 - JUnit 4 → JUnit 5 Migration**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/junit4-to-5-migration/`
  - **Action:** Migrate all test files from JUnit 4 to JUnit 5 syntax
  - **Commit:** `test(junit): migrate from JUnit 4 to JUnit 5 (1.6)`

- [ ] **1.7 - Upgrade Spring Boot 2.4 → 2.5**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/upgrade-sb-2.4-to-2.5/`
  - **Action:** Update parent POM to Spring Boot 2.5.15
  - **Commit:** `feat(spring-boot): upgrade to 2.5.15 (1.7)`

- [ ] **1.8 - Upgrade Spring Boot 2.5 → 2.6**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/upgrade-sb-2.5-to-2.6/`
  - **Action:** Update parent POM to Spring Boot 2.6.15
  - **Commit:** `feat(spring-boot): upgrade to 2.6.15 (1.8)`

- [ ] **1.9 - Upgrade Spring Boot 2.6 → 2.7**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/upgrade-sb-2.6-to-2.7/`
  - **Action:** Update parent POM to Spring Boot 2.7.18 (last 2.x release)
  - **Commit:** `feat(spring-boot): upgrade to 2.7.18 (1.9)`

- [ ] **1.10 - Phase 1 Checkpoint**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/checkpoint/`
  - **Action:** Verify that all tasks are completed and exit criteria are met
  - **Exit Criteria:**
    - JDK 17 compilation successful
    - Spring Boot 2.7.18 active
    - All tests passing with JUnit 5
    - `mvn clean verify` succeeds

- [ ] **1.11 - End Phase 1 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-end-phase1-migration`

---

### Phase 2: Spring Boot 3.x + Jakarta EE Migration

**Goal:** Upgrade to Spring Boot 3.4.0 and migrate from javax.* to jakarta.* packages.

**Prerequisites:** 
- Phase 1 completed successfully - check through last git tag
- Spring Boot 2.7.x is configured
- JDK 17 is configured

**Environment Setup:** Set both `JAVA_HOME` and `MAVEN_JAVA_HOME` to JDK 17 installation path for the current shell/session before executing any Phase 2 tasks. (See Appendix B for examples)

#### Phase 2 Tasks

- [ ] **2.0 - Start Phase 2 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-starts-phase2-migration`

- [ ] **2.1 - Boot 3 Readiness Assessment**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/boot3-readiness/`
  - **Action:** Assess codebase for Spring Boot 3 + Jakarta migration
  - **Commit:** `docs(boot3): readiness assessment (2.1)`

- [ ] **2.2 - Upgrade Spring Boot 2.7 → 3.4**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/upgrade-boot3/`
  - **Action:** Switch project from Boot 2.7.x to target Boot 3.x version
  - **Commit:** `feat(spring-boot): upgrade to 3.4.0 (2.2)`

- [ ] **2.3 - Jakarta EE Migration (javax → jakarta)**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/jakarta-migration/`
  - **Action:** Eliminate all javax.* usages by migrating to jakarta.* packages
  - **Commit:** `refactor(jakarta): migrate javax to jakarta packages (2.3)`

- [ ] **2.4 - Update Dependencies**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/update-dependencies/`
  - **Action:** Update dependencies to Boot 3 compatible versions
  - **Commit:** `build(deps): update dependencies for Boot 3 compatibility (2.4)`

- [ ] **2.5 - Fix Servlet API Changes**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/servlet-changes/`
  - **Action:** Address Servlet 6.0 breaking changes
  - **Commit:** `fix(servlet): address Servlet 6.0 API changes (2.5)`

- [ ] **2.6 - Fix Validation API Changes**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/validation-changes/`
  - **Action:** Address Jakarta Validation 3.0 changes
  - **Commit:** `fix(validation): address Jakarta Validation 3.0 changes (2.6)`

- [ ] **2.7 - Update Actuator Configuration**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/actuator-updates/`
  - **Action:** Review and update Actuator endpoints for Boot 3
  - **Commit:** `feat(actuator): update configuration for Boot 3 (2.7)`

- [ ] **2.8 - Full Integration Test**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/integration-test/`
  - **Action:** Run full test suite and manual smoke tests
  - **Commit:** `test(phase2): complete integration testing (2.8)`

- [ ] **2.9 - Phase 2 Checkpoint**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/checkpoint/`
  - **Action:** Verify Phase 2 completion and exit criteria
  - **Exit Criteria:**
    - Spring Boot 3.4.0 active
    - All javax → jakarta migrations complete
    - All tests passing
    - Application starts and runs on JDK 17
    - No compilation warnings

- [ ] **2.10 - End Phase 2 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-end-phase2-migration`

---

### Phase 3: JDK 21 + Modernization

**Goal:** Upgrade to JDK 21 and adopt modern Java features.

**Prerequisites:** Phase 2 complete, Spring Boot 3.4.0, JDK 17
**Environment Setup:** Set both `JAVA_HOME` and `MAVEN_JAVA_HOME` to JDK 21 installation path for the current shell/session before executing any Phase 3 tasks. (See Appendix B for examples)

#### Phase 3 Tasks

- [ ] **3.0 - Start Phase 3 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-starts-phase3-migration`

- [ ] **3.1 - Set JAVA_HOME and MAVEN_JAVA_HOME to JDK 21**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/jdk-switch/`
  - **Action:** Update JAVA_HOME and MAVEN_JAVA_HOME environment variables to JDK 21
  - **Commit:** `chore(jdk21): configure environment for JDK 21 (3.1)`

- [ ] **3.2 - Update pom.xml for JDK 21**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/dependency-alignment/`
  - **Action:** Update Java version in pom.xml
  - **Commit:** `feat(java): upgrade to JDK 21 (3.2)`

- [ ] **3.3 - Fix JDK 21 Compilation Issues**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/remediation-and-tests/`
  - **Action:** Resolve any JDK 21 specific compilation issues
  - **Commit:** `fix(jdk21): resolve compilation issues (3.3)`

- [ ] **3.4 - Update Dependencies for JDK 21**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/dependency-alignment/`
  - **Action:** Ensure all dependencies are compatible with JDK 21
  - **Commit:** `build(deps): update dependencies for JDK 21 compatibility (3.4)`

- [ ] **3.5 - Run Full Test Suite on JDK 21**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/remediation-and-tests/`
  - **Action:** Execute complete test suite
  - **Commit:** `test(jdk21): validate full test suite on JDK 21 (3.5)`

- [ ] **3.6 - Performance Validation**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/performance-and-gc-profiling/`
  - **Action:** Validate performance characteristics on JDK 21
  - **Commit:** `docs(perf): add JDK 21 performance baseline (3.6)`

- [ ] **3.7 - Virtual Threads Assessment** (Optional)
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/language-feature-adoption/`
  - **Action:** Evaluate virtual threads (Project Loom) for I/O-bound operations
  - **Commit:** `docs(modernization): assess virtual threads opportunities (3.7)`

- [ ] **3.8 - Modernization Opportunities Catalog** (Optional)
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/modernization-opportunities/`
  - **Action:** Document modern Java features applicable to codebase
  - **Commit:** `docs(modernization): catalog JDK 21 feature opportunities (3.8)`

- [ ] **3.9 - Phase 3 Checkpoint**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/checkpoint/`
  - **Action:** Verify Phase 3 completion and exit criteria
  - **Exit Criteria:**
    - JDK 21 compilation successful
    - All tests passing on JDK 21
    - Application runs successfully
    - Performance metrics acceptable
    - No regression in functionality

- [ ] **3.10 - End Phase 3 Git Tag**
  - **Task Ref:** `olaf-core/prompts/java-migration/tasks/git-branch-tag/`
  - **Action:** git tag `olaf-end-phase3-migration`

---

## Final Migration Checkpoint

- [ ] **Final Verification**
  - **Action:** Complete end-to-end verification
  - **Checks:**
    - ✅ Java 21 active
    - ✅ Spring Boot 3.4.0 active
    - ✅ All tests passing
    - ✅ Application starts and serves requests
    - ✅ Actuator endpoints functional
    - ✅ Database connectivity verified
    - ✅ Logging working correctly
    - ✅ Metrics publishing to Prometheus

- [ ] **Create Pull Request**
  - **Branch:** `<branch-name>` → `<current-branch-name>`
  - **Title:** `feat: migrate to Java 21 and Spring Boot 3.4`
  - **Description:** Include migration summary, breaking changes, testing notes

- [ ] **Final Tag**
  - **Tag:** `migration-complete-java21-boot3.4`
  - **Message:** "Completed migration to Java 21 and Spring Boot 3.4.0"

---

## Git Strategy

### Rollback Points
- **Phase 1 Issues:** `git checkout olaf-end-phase1-migration`
- **Phase 2 Issues:** `git checkout olaf-end-phase2-migration`
- **Phase 3 Issues:** `git checkout olaf-end-phase3-migration`
- **Complete Rollback:** `git checkout olaf-starts-java-migration`

---

## Success Criteria

### Phase 1: JDK 17 + Boot 2.7
- Compiles with JDK 17
- Spring Boot 2.7.18 active
- JUnit 5 tests passing
- `mvn clean verify` succeeds

### Phase 2: Boot 3 + Jakarta
- Spring Boot 3.4.0 active
- All javax imports migrated to jakarta
- Oracle JDBC compatible
- Application starts and runs
- All tests passing

### Phase 3: JDK 21
- Compiles with JDK 21
- All tests passing on JDK 21
- Performance acceptable
- No regressions

### Final
- Production-ready state on JDK 21 + Spring Boot 3.4.0
- Documentation updated
- Team trained on new versions

---

**End of Migration Plan**

Generated by: bootstrap-java-migration v1.0  
Plan ID: java-migration-plan-yyyymmdd-hhmm  
Context: migration-bootstrap-context.yaml
