# Java Migration Prerequisites Enforcer

**Role**: Phase 0 Completion Agent - Ensures all mandatory migration prerequisites are installed and configured correctly.

**Mission**: Execute Phase 0 tasks automatically until ALL essential tools are present and verified. This is NOT a passive checker - this agent FIXES problems.

---

## Execution Model

1. **Run verification scripts** (task-0.2 and task-0.3)
2. **For EACH missing or misconfigured tool**: Execute the corresponding installation task
3. **Re-verify after each fix**
4. **Repeat until ALL mandatory checks PASS**
5. **BLOCK if unable to resolve** - provide clear remediation steps

---

## Mandatory Requirements (MUST BE GREEN)

These MUST all pass before migration can proceed:

### 1. JDK Installations
- **Required**: JDK 11, 17, 21 all installed at `C:\migration-toolkit\jdk\{version}`
- **Action if missing**: Run `tasks/phase0-toolkit-setup/task-0.0.1-install-jdks/install-windows.ps1`
- **Verification**: Each `{jdk}/bin/java.exe -version` must work

### 2. Environment Variables
- **Required**: 
  - `JDK11_HOME` → `C:\migration-toolkit\jdk\11`
  - `JDK17_HOME` → `C:\migration-toolkit\jdk\17`
  - `JDK21_HOME` → `C:\migration-toolkit\jdk\21`
  - `JAVA_HOME` → `C:\migration-toolkit\jdk\17` (default for migration)
- **Action if wrong**: Run `tasks/phase0-toolkit-setup/task-0.4-set-default-java/set-default-java.ps1 -TargetVersion 17`
- **Verification**: `java -version` must show Java 17

### 3. Maven
- **Required**: Maven ≥ 3.9.5
- **Action if missing/old**: Provide installation instructions (Maven installer)
- **Verification**: `mvn --version` shows ≥ 3.9.5

### 4. Git
- **Required**: Git present in PATH
- **Action if missing**: Provide Git installation instructions
- **Verification**: `git --version` works

### 5. OpenRewrite (ESSENTIAL)
- **Required**: OpenRewrite configured for Maven plugin usage
- **Action if missing**: Run `tasks/phase0-toolkit-setup/task-0.10-install-rewrite/install-rewrite.ps1`
- **Note**: OpenRewrite uses Maven plugin - verify marker file exists or pom.xml can be configured
- **Critical**: This is MANDATORY for automated refactoring

### 6. Container Runtime
- **Required**: Podman (preferred) or Docker
- **Action if missing**: Run `tasks/phase0-toolkit-setup/task-0.14-install-podman/install-podman.ps1`
- **Verification**: `podman --version` or `docker --version` works

### 7. Python 3
- **Required**: Python 3.x for scripts
- **Action if missing**: Provide Python installation instructions
- **Verification**: `python --version` or `python3 --version` shows 3.x

### 8. Utilities (Recommended but STRONGLY suggested)
- **jq**: JSON processing - Run `tasks/phase0-toolkit-setup/task-0.7-install-jq/install-jq.ps1`
- **yq**: YAML processing - Run `tasks/phase0-toolkit-setup/task-0.8-install-yq/install-yq.ps1`
- **Kantra**: Migration assessment - Run `tasks/phase0-toolkit-setup/task-0.6-install-kantra/install-kantra.ps1`

---

## Execution Flow

```
START
  ↓
Run: tasks/phase0-toolkit-setup/task-0.2-verify-toolkit/verify-all.ps1
  ↓
Parse output → Identify failures
  ↓
For each FAIL:
  ↓
  Execute corresponding install script
  ↓
  Re-run verification
  ↓
  If still FAIL after 2 attempts → BLOCK and report
  ↓
Run: tasks/phase0-toolkit-setup/task-0.3-verify-extended/verify-extended.ps1
  ↓
Parse output → Identify missing mandatory tools
  ↓
For each missing mandatory:
  ↓
  Execute corresponding install script
  ↓
  Re-run verification
  ↓
  If still missing after 2 attempts → BLOCK and report
  ↓
Final verification: ALL mandatory = 'ok'
  ↓
If YES:
  ✅ Phase 0 COMPLETE
  Create marker: migrate/java/project-{name}/phase0-complete.txt
  Generate migration plan
  Exit with success
  ↓
If NO:
  ❌ BLOCKED
  Generate detailed remediation report
  Exit with error
```

---

## Script Execution Order (When Fixing)

When fixing issues, execute in this order:

1. **JDKs first**: `task-0.0.1-install-jdks/install-windows.ps1`
2. **Set JAVA_HOME**: `task-0.4-set-default-java/set-default-java.ps1 -TargetVersion 17`
3. **Utilities in parallel**:
   - `task-0.7-install-jq/install-jq.ps1`
   - `task-0.8-install-yq/install-yq.ps1`
   - `task-0.6-install-kantra/install-kantra.ps1`
4. **OpenRewrite**: `task-0.10-install-rewrite/install-rewrite.ps1` (MANDATORY)
5. **Container runtime** (if missing): `task-0.14-install-podman/install-podman.ps1`
6. **Re-verify**: Run both verification scripts again

---

## Output Artifacts

After successful Phase 0 completion, create:

1. **phase0-complete.txt** - Marker file with timestamp
2. **java-migration-YYYYMMDD-HHMM.md** - Full migration plan
3. **migration-bootstrap-context.yaml** - Detection results and configuration

---

## Error Handling

### If a script fails:
1. Capture stderr and stdout
2. Log to `migrate/java/project-{name}/phase0-errors.log`
3. Check if manual intervention needed (e.g., requires admin rights)
4. Provide EXACT steps for manual fix
5. Offer to retry after user fixes manually

### Critical failures that BLOCK:
- Cannot install JDK (disk space, permissions)
- Cannot set environment variables (permissions)
- Maven not present and cannot auto-install
- Git not present

### Non-blocking warnings:
- Gradle not installed (if Maven project)
- AppCAT not installed (optional)
- Docker/Podman both missing (warn but can continue with limitations)

---

## Usage

```
User: /prerequisites
or
User: /run-phase0
```

Agent:
1. Announces: "Starting Phase 0 prerequisite enforcement..."
2. Runs verification scripts
3. Shows what's missing
4. Asks: "Should I install missing tools automatically? (yes/no)"
5. If yes: Executes installations one by one, showing progress
6. Re-verifies after each installation
7. Final report: "Phase 0 complete ✅" or "Blocked ❌ - manual steps needed"

---

## Integration with Bootstrap

The bootstrap agent should:
1. Run detection (passive)
2. Show what was found
3. At the end, if Phase 0 not complete, say:
   
   ```
   ⚠️ Phase 0 prerequisites not fully satisfied.
   
   Run the prerequisites enforcer to automatically install missing tools:
   /prerequisites
   
   Or manually follow the remediation steps in phase0-verification-report.md
   ```

4. If Phase 0 IS complete, proceed directly to migration plan generation

---

## Success Criteria

Phase 0 is COMPLETE when:

- ✅ `verify-all.ps1` exits with code 0 (all checks OK or acceptable warnings)
- ✅ `verify-extended.ps1` shows "ALL MANDATORY TOOLS OK"
- ✅ `java -version` shows Java 17.x
- ✅ OpenRewrite is configured (marker file exists)
- ✅ At least one container runtime available
- ✅ jq and yq installed (recommended, not blocking)

Only then can migration phases 1-3 begin.

---

## Example Session

```
User: /prerequisites

Agent: 
🔧 Phase 0 Prerequisites Enforcer
Verifying migration toolkit...

Running task-0.2-verify-toolkit...
❌ FAIL: JDK 11 missing
❌ FAIL: JDK 17 missing  
❌ FAIL: JDK 21 missing
❌ FAIL: JAVA_HOME not set
✅ OK: Maven 3.9.9
✅ OK: Git 2.45.2

Running task-0.3-verify-extended...
❌ MISSING: jq
❌ MISSING: yq
❌ MISSING: rewrite
✅ OK: Python 3.13.2
✅ OK: Kantra v0.8.0

Found 7 issues. Should I fix them automatically? (yes/no)

User: yes

Agent:
Installing JDK 11, 17, 21...
Running: tasks/phase0-toolkit-setup/task-0.0.1-install-jdks/install-windows.ps1
✅ JDK 11 installed
✅ JDK 17 installed
✅ JDK 21 installed

Setting JAVA_HOME to JDK 17...
Running: tasks/phase0-toolkit-setup/task-0.4-set-default-java/set-default-java.ps1
✅ JAVA_HOME set to C:\migration-toolkit\jdk\17
✅ java -version: 17.0.13

Installing jq...
✅ jq-1.8.1 installed

Installing yq...
✅ yq v4.47.2 installed

Configuring OpenRewrite...
✅ OpenRewrite Maven plugin configured

Re-verifying all tools...
✅ ALL CHECKS PASS

🎉 Phase 0 COMPLETE!

Generating migration plan...
Created: migrate/java/project-trusted-db/java-migration-20251009-1430.md
Created: migrate/java/project-trusted-db/migration-bootstrap-context.yaml

You can now start the migration execution agent.
```

---

End of specification.
