# JUnit 4 → 5 Migration — Phase 1

## Goal
Eliminate JUnit 4 dependencies and constructs; run all unit tests on JUnit Jupiter only (no vintage engine) with green results.

## Prerequisites
- Baseline JDK compile + unit tests green
- JDK 17 upgrade completed or in progress

## Preferred Approach (Automated)
1. **Detection and Inventory**:
   ```bash
   # Count JUnit 4 patterns
   grep -r "import org.junit.Assert" src/test/ | wc -l
   grep -r "@RunWith" src/test/ | wc -l
   grep -r "@Test(expected" src/test/ | wc -l
   
   # Generate migration inventory
   grep -r "org.junit\." src/test/ > junit4-inventory-before.txt
   ```

2. **Dependency Updates**:
   ```bash
   # Add JUnit 5 dependencies (if not managed by Spring Boot BOM)
   mvn versions:use-dep-version -Dincludes=org.junit.jupiter:junit-jupiter -DdepVersion=5.10.1
   
   # Remove JUnit 4 dependency
   mvn versions:use-dep-version -Dincludes=junit:junit -DdepVersion=RELEASE
   ```

3. **Automated Migration** (if OpenRewrite available):
   ```bash
   # Apply JUnit 5 migration recipes
   mvn rewrite:run -Drewrite.activeRecipes=org.openrewrite.java.testing.junit5.JUnit4to5Migration
   ```

4. **Manual Cleanup**:
   ```bash
   # Find remaining JUnit 4 imports
   grep -r "import org.junit\." src/test/ | grep -v jupiter
   
   # Run tests to identify failures
   mvn test -q
   ```

## Fallback Approach (Manual)
If automated migration fails:
1. **Annotation Migration**:
   - `@Before` → `@BeforeEach`
   - `@After` → `@AfterEach`
   - `@BeforeClass` → `@BeforeAll`
   - `@AfterClass` → `@AfterAll`
   - `@Ignore` → `@Disabled`

2. **Assertion Migration**:
   - `Assert.assertEquals` → `Assertions.assertEquals`
   - `@Test(expected=X.class)` → `assertThrows(X.class, () -> { ... })`

3. **Runner Migration**:
   - `@RunWith(SpringRunner.class)` → Remove (implicit in Spring Boot)
   - `@RunWith(MockitoJUnitRunner.class)` → `@ExtendWith(MockitoExtension.class)`

## Verification Commands
```bash
# Verify no JUnit 4 imports remain
grep -r "import org.junit\." src/test/ | grep -v jupiter && echo "FAIL: JUnit 4 imports found" || echo "PASS: No JUnit 4 imports"

# Check for @RunWith usage
grep -r "@RunWith" src/test/ && echo "FAIL: @RunWith found" || echo "PASS: No @RunWith usage"

# Verify no vintage engine dependency
mvn dependency:tree | grep vintage && echo "FAIL: Vintage engine present" || echo "PASS: No vintage engine"

# Run all tests
mvn test -q

# Generate post-migration inventory
grep -r "org.junit.jupiter" src/test/ > junit5-inventory-after.txt
```

## Issue Detection & Remediation

### JUnit 4 Annotations (Severity: medium)
**Detection Pattern**: `@Before\|@After\|@BeforeClass\|@AfterClass\|@Ignore` in test files
**Remediation**:
1. Replace `@Before` with `@BeforeEach`
2. Replace `@After` with `@AfterEach`  
3. Replace `@BeforeClass` with `@BeforeAll` (make methods static)
4. Replace `@AfterClass` with `@AfterAll` (make methods static)
5. Replace `@Ignore` with `@Disabled`
**Validation**: No JUnit 4 annotations remain: `grep -r "@Before\|@After\|@Ignore" src/test/`

### Missing Jupiter Engine (Severity: high)
**Detection Pattern**: Tests not discovered or executed
**Remediation**:
1. Add `junit-jupiter-engine` dependency to pom.xml
2. Update maven-surefire-plugin to ≥ 3.0.0
3. Remove `junit-vintage-engine` if present
**Validation**: `mvn test` discovers and runs Jupiter tests

### JUnit 4 Assertions (Severity: medium)
**Detection Pattern**: `import org.junit.Assert\|Assert\.assertEquals`
**Remediation**:
1. Replace `org.junit.Assert.*` with `org.junit.jupiter.api.Assertions.*`
2. Convert `@Test(expected=X.class)` to `assertThrows(X.class, () -> { ... })`
3. Update static imports for assertions
**Validation**: No JUnit 4 assertion imports: `grep -r "import org.junit.Assert" src/test/`

### Runner Migration (Severity: medium)
**Detection Pattern**: `@RunWith\(.*\.class\)`
**Remediation**:
1. Replace `@RunWith(SpringRunner.class)` with removal (implicit in Spring Boot)
2. Replace `@RunWith(MockitoJUnitRunner.class)` with `@ExtendWith(MockitoExtension.class)`
3. Convert parameterized runners to `@ParameterizedTest`
**Validation**: No `@RunWith` usage: `grep -r "@RunWith" src/test/`

### Rule Migration (Severity: medium)
**Detection Pattern**: `@Rule\|ExpectedException\|TemporaryFolder`
**Remediation**:
1. Replace `ExpectedException` rule with `assertThrows`
2. Replace `TemporaryFolder` rule with `@TempDir` annotation
3. Convert custom rules to extensions where possible
**Validation**: No JUnit 4 rules remain: `grep -r "@Rule\|ExpectedException" src/test/`

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `junit4-to-5-migration-<YYYYMMDD-HHmm>.json`
- **Categories**: import, runwith, rule, expected-exception, parameterized
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (vintage engine temporarily allowed)

## Defer Rules
- Vintage engine allowed temporarily if >20% tests failing (must include removal plan)
- Parameterized test refactors may defer if flaky (document rationale and timeline)
- Complex rule migrations may defer to separate task if blocking

## Success Criteria
- ✅ No JUnit 4 imports: `grep -r "import org.junit\." src/test/ | grep -v jupiter` returns empty
- ✅ No @RunWith usage: `grep -r "@RunWith" src/test/` returns empty
- ✅ No vintage engine dependency in `mvn dependency:tree`
- ✅ All unit tests pass: `mvn test` exits 0
- ✅ JUnit 5 inventory generated showing successful migration
