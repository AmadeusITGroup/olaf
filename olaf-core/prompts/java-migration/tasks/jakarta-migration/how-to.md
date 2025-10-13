# Jakarta Migration (javax → jakarta) — Phase 2

## Goal
Eliminate all `javax.*` usages by migrating to `jakarta.*` packages and required API versions while preserving behavior.

## Prerequisites
- Spring Boot 3.x upgrade completed
- JDK 17 active
- Boot 3 readiness inventory available

## Preferred Approach (Automated)
1. **Pre-migration Inventory**:
   ```bash
   # Snapshot current javax usage
   grep -r "import javax\." src/ > javax-inventory-before.txt
   grep -r "javax\." src/ | wc -l  # Count total references
   ```

2. **OpenRewrite Migration** (if configured):
   ```bash
   # Dry run first
   mvn rewrite:dryRun -Drewrite.activeRecipes=org.openrewrite.java.migrate.jakarta.JavaxMigrationToJakarta
   
   # Apply if dry run successful
   mvn rewrite:run -Drewrite.activeRecipes=org.openrewrite.java.migrate.jakarta.JavaxMigrationToJakarta
   ```

3. **Manual Cleanup**:
   ```bash
   # Find remaining javax imports
   grep -r "import javax\." src/ || echo "No javax imports remaining"
   
   # Compile and fix remaining issues
   mvn clean compile
   ```

## Fallback Approach (Manual)
If OpenRewrite fails or unavailable:
1. Use IDE find/replace: `javax.servlet` → `jakarta.servlet`
2. Update imports systematically by package:
   - `javax.servlet.*` → `jakarta.servlet.*`
   - `javax.validation.*` → `jakarta.validation.*`
   - `javax.persistence.*` → `jakarta.persistence.*`
3. Address API signature changes manually

## Verification Commands
```bash
# Verify zero javax imports remain
grep -r "import javax\." src/ && echo "FAIL: javax imports found" || echo "PASS: No javax imports"

# Count javax references (should be 0)
grep -r "javax\." src/ | wc -l

# Validate compilation
mvn clean compile -q

# Validate tests
mvn test -q

# Generate post-migration inventory
grep -r "import jakarta\." src/ > jakarta-inventory-after.txt
```

## Issue Detection & Remediation

### Namespace Rewrite Missing (Severity: high)
**Detection Pattern**: `package javax.* does not exist`
**Remediation**:
1. Apply OpenRewrite Jakarta migration recipes
2. Manual find/replace: `javax.servlet` → `jakarta.servlet`
3. Update import statements systematically by package
**Validation**: Zero javax imports remain: `grep -r "import javax\." src/`

### Dependency Jakarta Version Missing (Severity: high)  
**Detection Pattern**: `ClassNotFoundException: javax.*` at runtime
**Remediation**:
1. Update dependencies to Jakarta-compatible versions
2. Add `jakarta.activation:jakarta.activation-api` if needed
3. Update XML binding dependencies to Jakarta variants
**Validation**: `mvn dependency:tree` shows jakarta.* dependencies, no javax.*

### Servlet API Changes (Severity: medium)
**Detection Pattern**: Method signature mismatches in servlet code
**Remediation**:
1. Update servlet method signatures for Servlet 6.0 API changes
2. Replace deprecated `HttpServletRequest.getSession(boolean)` usage
3. Update filter and listener configurations
**Validation**: Servlet code compiles without signature errors

### Validation Constraint Changes (Severity: medium)
**Detection Pattern**: Validation annotation import failures
**Remediation**:
1. Update `javax.validation.*` imports to `jakarta.validation.*`
2. Update custom validator implementations
3. Update validation configuration in `application.yml`
**Validation**: Validation annotations resolve correctly, tests pass

### Jakarta Activation Missing (Severity: medium)
**Detection Pattern**: `ClassNotFoundException` for activation classes
**Remediation**:
1. Add `jakarta.activation:jakarta.activation-api` dependency
2. Update mail configuration to use Jakarta activation
3. Replace `javax.activation.*` imports
**Validation**: Mail functionality works without activation class errors

## Issue Collection
**Only collect issues if remediation fails (no deferrals allowed)**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `jakarta-migration-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, api, dependency
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful)
- **Note**: No DEFERRED status allowed - all javax references must be eliminated

## Defer Rules
- **No deferrals allowed**: All javax references must be eliminated
- Exception: javax references in test data strings or comments (document as acceptable)

## Success Criteria
- ✅ Zero javax imports: `grep -r "import javax\." src/` returns empty
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Unit tests pass: `mvn test` exits 0
- ✅ All HIGH severity issues RESOLVED
- ✅ Jakarta inventory generated showing successful migration
