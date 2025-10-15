# Validation API Changes — Phase 2

## Goal
Migrate Bean Validation from javax.validation to jakarta.validation (Jakarta Validation 3.0) while preserving validation behavior and test coverage.

## Prerequisites
- Spring Boot 3.x upgrade completed
- Unit tests passing pre-migration
- Jakarta migration in progress or planned

## Preferred Approach (Automated)
1. **Current Inventory**:
   ```bash
   # Count current javax.validation imports
   grep -r "import javax\.validation" src/ | wc -l > validation-count-before.txt
   
   # Generate detailed inventory
   grep -r "import javax\.validation" src/ > validation-inventory-before.txt
   ```

2. **Dependency Verification**:
   ```bash
   # Check for Jakarta validation dependency
   mvn dependency:tree | grep jakarta.validation || echo "Jakarta validation not found"
   
   # Verify Spring Boot starter includes validation
   mvn dependency:tree | grep spring-boot-starter-validation
   ```

3. **Namespace Migration**:
   ```bash
   # Use OpenRewrite for automated migration (if available)
   mvn rewrite:run -Drewrite.activeRecipes=org.openrewrite.java.migrate.jakarta.ValidationMigration
   
   # Manual approach: bulk replace imports
   find src/ -name "*.java" -exec sed -i 's/import javax\.validation/import jakarta.validation/g' {} \;
   ```

4. **Compilation and Testing**:
   ```bash
   # Compile to identify remaining issues
   mvn clean compile -q
   
   # Run validation-focused tests
   mvn test -Dtest="*ValidationTest,*ValidatorTest" -q
   ```

5. **Post-Migration Verification**:
   ```bash
   # Verify no javax.validation imports remain
   grep -r "import javax\.validation" src/ > validation-inventory-after.txt || echo "No javax.validation imports found"
   
   # Count remaining imports (should be 0)
   grep -r "import javax\.validation" src/ | wc -l
   ```

## Fallback Approach (Manual)
If automated migration fails:
1. Manually update imports in IDE using find/replace
2. Update custom constraint annotations and validators
3. Fix ConstraintValidator implementations
4. Update test assertions for validation messages

## Verification Commands
```bash
# Verify no javax.validation imports remain
grep -r "import javax\.validation" src/ && echo "FAIL: javax.validation imports found" || echo "PASS: No javax.validation imports"

# Validate compilation
mvn clean compile -q

# Run validation-related tests
mvn test -Dtest="*ValidationTest,*ValidatorTest" -q

# Check validation inventory files
test -f validation-inventory-before.txt && test -f validation-inventory-after.txt && echo "PASS: Inventory files created"
```

## Issue Detection & Remediation

### Missing Jakarta Validation Dependency (Severity: high)
**Detection Pattern**: `ClassNotFoundException` for jakarta.validation classes
**Remediation**:
1. Ensure Spring Boot starter-validation includes jakarta.validation-api
2. Add explicit jakarta.validation-api dependency if needed
3. Remove any explicit javax.validation-api dependencies
**Validation**: Jakarta validation classes resolve correctly in compilation

### Custom Constraint Migration (Severity: medium)
**Detection Pattern**: Compilation errors in custom constraint annotations or validators
**Remediation**:
1. Update custom constraint annotation packages to jakarta.validation
2. Update ConstraintValidator implementations to use jakarta imports
3. Fix any custom validation message interpolation
**Validation**: Custom constraints compile and function correctly

### Third-Party Library Conflicts (Severity: medium)
**Detection Pattern**: Transitive javax.validation dependencies from third-party libraries
**Remediation**:
1. Upgrade third-party libraries to Jakarta-compatible versions
2. Add dependency exclusions for javax.validation if needed
3. Use dependency management to force jakarta.validation versions
**Validation**: No javax.validation in dependency tree

### Validation Message Changes (Severity: low)
**Detection Pattern**: Test failures due to changed validation messages
**Remediation**:
1. Update test assertions for new Jakarta validation messages
2. Check for message interpolation differences
3. Update custom message properties if needed
**Validation**: All validation tests pass with correct messages

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `validation-changes-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, constraint, dependency, message
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (third-party library dependencies)

## Success Criteria
- ✅ Zero javax.validation imports: `grep -r "import javax\.validation" src/` returns empty
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Validation tests pass: validation-focused test suite passes
- ✅ No HIGH severity validation issues remain OPEN
- ✅ Before/after inventory files document successful migration
