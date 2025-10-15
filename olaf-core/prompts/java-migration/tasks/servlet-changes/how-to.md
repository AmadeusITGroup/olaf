# Servlet API Changes — Phase 2

## Goal
Migrate servlet-layer code from javax.servlet to jakarta.servlet (Servlet 6.0) ensuring filters, listeners, and custom components function correctly.

## Prerequisites
- Spring Boot 3.x upgrade completed
- Boot 3 readiness assessment completed with servlet inventory
- Jakarta migration in progress or planned

## Preferred Approach (Automated)
1. **Current Inventory**:
   ```bash
   # Count current javax.servlet imports
   grep -r "import javax\.servlet" src/ | wc -l > servlet-count-before.txt
   
   # Generate detailed inventory
   grep -r "import javax\.servlet" src/ > servlet-inventory-before.txt
   ```

2. **Namespace Migration**:
   ```bash
   # Use OpenRewrite for automated migration (if available)
   mvn rewrite:run -Drewrite.activeRecipes=org.openrewrite.java.migrate.jakarta.ServletMigration
   
   # Manual approach: bulk replace imports
   find src/ -name "*.java" -exec sed -i 's/import javax\.servlet/import jakarta.servlet/g' {} \;
   ```

3. **Compilation and Testing**:
   ```bash
   # Compile to identify remaining issues
   mvn clean compile -q
   
   # Run web-focused tests
   mvn test -Dtest="*ControllerTest,*FilterTest,*ServletTest" -q
   ```

4. **Post-Migration Verification**:
   ```bash
   # Verify no javax.servlet imports remain
   grep -r "import javax\.servlet" src/ > servlet-inventory-after.txt || echo "No javax.servlet imports found"
   
   # Count remaining imports (should be 0)
   grep -r "import javax\.servlet" src/ | wc -l
   ```

## Fallback Approach (Manual)
If automated migration fails:
1. Manually update imports in IDE using find/replace
2. Update FilterRegistrationBean and ServletRegistrationBean types
3. Fix method signature changes for Servlet 6.0 API
4. Update custom error page configurations

## Verification Commands
```bash
# Verify no javax.servlet imports remain
grep -r "import javax\.servlet" src/ && echo "FAIL: javax.servlet imports found" || echo "PASS: No javax.servlet imports"

# Validate compilation
mvn clean compile -q

# Run servlet-related tests
mvn test -Dtest="*ControllerTest,*FilterTest,*ServletTest" -q

# Check servlet inventory files
test -f servlet-inventory-before.txt && test -f servlet-inventory-after.txt && echo "PASS: Inventory files created"
```

## Issue Detection & Remediation

### Missing Jakarta Servlet Dependency (Severity: high)
**Detection Pattern**: `ClassNotFoundException` for jakarta.servlet classes
**Remediation**:
1. Ensure Spring Boot web starter includes jakarta.servlet-api
2. Add explicit jakarta.servlet-api dependency if needed
3. Remove any explicit javax.servlet-api dependencies
**Validation**: Jakarta servlet classes resolve correctly in compilation

### Filter Registration Issues (Severity: medium)
**Detection Pattern**: Filters not invoked after migration
**Remediation**:
1. Update FilterRegistrationBean generic types to jakarta.servlet
2. Verify @WebFilter annotations use jakarta imports
3. Check Spring Boot auto-configuration for filter registration
**Validation**: Filters execute correctly in integration tests

### Servlet API Method Changes (Severity: medium)
**Detection Pattern**: Method signature compilation errors
**Remediation**:
1. Update method signatures for Servlet 6.0 API changes
2. Fix deprecated method usage in custom servlets
3. Update ServletContext and HttpServletRequest method calls
**Validation**: All servlet code compiles without signature errors

### Endpoint Mapping Issues (Severity: medium)
**Detection Pattern**: 404 errors or mapping failures after migration
**Remediation**:
1. Verify servlet mappings in web.xml or annotations
2. Check Spring MVC controller mappings still work
3. Update custom servlet path configurations
**Validation**: All web endpoints respond correctly

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `servlet-changes-<YYYYMMDD-HHmm>.json`
- **Categories**: compile, test, mapping, api, dependency
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-critical legacy components)

## Success Criteria
- ✅ Zero javax.servlet imports: `grep -r "import javax\.servlet" src/` returns empty
- ✅ Clean compilation: `mvn clean compile` exits 0
- ✅ Servlet tests pass: web-focused test suite passes
- ✅ No HIGH severity servlet issues remain OPEN
- ✅ Before/after inventory files document successful migration
