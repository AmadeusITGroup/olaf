# CI Pipeline Inventory — Phase 1

## Goal
Document all CI/CD pipelines and their Java configuration to identify migration impact points.

## Preferred Approach (Automated)
1. **Repository Scan**:
   ```bash
   # Scan for CI configuration files
   find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | grep -E "(\.github|\.gitlab|jenkins|ci)"
   
   # Extract Java version references
   grep -r "java.*version\|JAVA_HOME\|setup-java" .github/ .gitlab-ci.yml Jenkinsfile 2>/dev/null || true
   ```

2. **Automated Analysis**: Run scan script if available:
   ```bash
   # Windows
   powershell -ExecutionPolicy Bypass -File scan-ci.ps1
   
   # Unix/Linux/macOS  
   bash scan-ci.sh
   ```

3. **Generate Report**: Create structured inventory in findings directory

## Fallback Approach (Manual)
If automated scanning fails:
1. Manually identify CI files in `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`
2. Document Java version matrices, setup actions, and build tool configurations
3. Note hardcoded JAVA_HOME paths and version constraints
4. Create inventory manually using template format

## Verification Commands
```bash
# Verify inventory files exist
ls -la olaf-data/findings/migrations/migration_*/ci/ci_inventory.*

# Check for missed CI files
find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | wc -l

# Validate no hardcoded Java versions remain undetected
grep -r "JAVA_HOME.*[=/].*[0-9]" .github/ .gitlab-ci.yml Jenkinsfile 2>/dev/null || echo "No hardcoded JAVA_HOME found"
```

## Outputs
- **Primary**: `olaf-data/findings/migrations/migration_<ts>/ci/ci_inventory.md`
- **Optional**: `olaf-data/findings/migrations/migration_<ts>/ci/ci_inventory.json`

## Issue Detection & Remediation

### Hard-coded JAVA_HOME (Severity: high)
**Detection Pattern**: `JAVA_HOME\s*=.*(8|11)`
**Remediation**: 
1. Replace hard-coded path with matrix/managed tool installer (actions/setup-java, Jenkins tool)
2. Parameterize JDK via variable (JAVA_VERSION) 
3. Remove legacy export lines from shell steps
**Validation**: Re-run scan - no lines matching regex; pipeline picks JAVA_VERSION variable

### Outdated JDK References (Severity: medium)  
**Detection Pattern**: `java.*version.*['"](8|11)['"]\|matrix.*java.*['"](8|11)['"']`
**Remediation**:
1. Update CI matrices to include JDK 17 and 21
2. Replace hardcoded version references with variables
3. Update Docker base images to use newer JDK versions
**Validation**: CI configuration references JDK 17+ versions

### Container Image JDK Upgrade (Severity: medium)
**Detection Pattern**: `FROM.*openjdk:(8|11)\|FROM.*java:(8|11)`
**Remediation**:
1. Update base images to openjdk:17 or openjdk:21
2. Update any JDK installation scripts in Dockerfiles
3. Test container builds with new JDK versions
**Validation**: No container definitions using JDK 8/11 base images

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `ci-pipeline-inventory-<YYYYMMDD-HHmm>.json`
- **Categories**: hardcoded-java-home, outdated-jdk-reference, container-image-jdk
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (manual review needed)

## Success Criteria
- ✅ CI inventory files created in findings directory
- ✅ All active pipelines documented with Java configuration details
- ✅ High severity issues remediated or documented as DEFERRED
- ✅ No CI files missed in repository scan
- ✅ All detection patterns validated - no matches for problematic configurations

