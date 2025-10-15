# CI Pipeline Inventory — Angular Migration Phase 1

## Goal
Document all CI/CD pipelines and their Node.js/Angular configuration to identify migration impact points.

## Preferred Approach (Automated)
1. **Repository Scan**:
   ```bash
   # Scan for CI configuration files
   find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | grep -E "(\.github|\.gitlab|jenkins|ci)"
   
   # Extract Node.js and Angular version references
   grep -r "node.*version\|NODE_VERSION\|setup-node\|angular\|ng " .github/ .gitlab-ci.yml Jenkinsfile 2>/dev/null || true
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
2. Document Node.js version matrices, setup actions, and build configurations
3. Note hardcoded NODE_VERSION paths and Angular CLI versions
4. Create inventory manually using template format

## Verification Commands
```bash
# Verify inventory files exist
ls -la olaf-data/findings/migrations/migration_*/ci/ci_inventory.*

# Check for missed CI files
find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | wc -l

# Validate no hardcoded Node versions remain undetected
grep -r "NODE_VERSION.*[=/].*[0-9]" .github/ .gitlab-ci.yml Jenkinsfile 2>/dev/null || echo "No hardcoded NODE_VERSION found"
```

## Outputs
- **Primary**: `olaf-data/findings/migrations/migration_<ts>/ci/ci_inventory.md`
- **Optional**: `olaf-data/findings/migrations/migration_<ts>/ci/ci_inventory.json`

## Issue Detection & Remediation

### Hard-coded Node.js Version (Severity: high)
**Detection Pattern**: `NODE_VERSION\s*=.*(14|16|18)`
**Remediation**: 
1. Replace hard-coded version with matrix/managed tool installer (actions/setup-node)
2. Parameterize Node.js via variable (NODE_VERSION) 
3. Remove legacy export lines from shell steps
**Validation**: Re-run scan - no lines matching regex; pipeline picks NODE_VERSION variable

### Outdated Angular CLI References (Severity: medium)  
**Detection Pattern**: `@angular/cli@[0-9]+\|ng.*version.*['"](1[0-5])['"']`
**Remediation**:
1. Update CI to install latest Angular CLI
2. Replace hardcoded CLI version references with variables
3. Update Docker base images to use newer Node.js versions
**Validation**: CI configuration references Angular CLI 16+ versions

### Container Image Node.js Upgrade (Severity: medium)
**Detection Pattern**: `FROM.*node:(14|16)\|FROM.*node:.*-alpine.*1[4-6]`
**Remediation**:
1. Update base images to node:18 or node:20
2. Update any Node.js installation scripts in Dockerfiles
3. Test container builds with new Node.js versions
**Validation**: No container definitions using Node.js 14/16 base images

### Package Manager Lock Files (Severity: low)
**Detection Pattern**: Multiple lock files present (package-lock.json + yarn.lock)
**Remediation**:
1. Choose single package manager for CI
2. Remove conflicting lock files
3. Update CI scripts to use consistent package manager
**Validation**: Only one type of lock file present

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `ci-pipeline-inventory-<YYYYMMDD-HHmm>.json`
- **Categories**: hardcoded-node-version, outdated-angular-cli, container-image-node, package-manager-conflicts
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (manual review needed)

## Success Criteria
- ✅ CI inventory files created in findings directory
- ✅ All active pipelines documented with Node.js/Angular configuration details
- ✅ High severity issues remediated or documented as DEFERRED
- ✅ No CI files missed in repository scan
- ✅ All detection patterns validated - no matches for problematic configurations