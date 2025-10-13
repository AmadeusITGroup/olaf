# JDK Switch — Set Environment to JDK 21

## Goal
Switch current shell environment to use JDK 21 for compilation and execution.

## Prerequisites
- JDK 21 installed and available on system
- Current project running on JDK 17
- Spring Boot 3.x and Jakarta migration completed

## Preferred Approach (OLAF JDK Structure)
1. **Verify JDK 21 in OLAF Structure**:
   ```bash
   # Check OLAF JDK installation
   ~/.olaf/jdk/21/bin/java -version
   
   # Verify all required JDKs present
   ls ~/.olaf/jdk/
   ```

2. **Set Environment Variables**:
   ```bash
   # Windows (PowerShell)
   $env:JAVA_HOME = "$env:USERPROFILE\.olaf\jdk\21"
   $env:MAVEN_JAVA_HOME = $env:JAVA_HOME
   $env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
   
   # Linux/macOS (Bash)
   export JAVA_HOME=~/.olaf/jdk/21
   export MAVEN_JAVA_HOME=$JAVA_HOME
   export PATH=$JAVA_HOME/bin:$PATH
   ```

3. **Verification**:
   ```bash
   # Verify JDK 21 is active
   java -version
   javac -version
   mvn -version
   
   # Check Maven uses correct JDK
   mvn help:evaluate -Dexpression=java.version -q -DforceStdout
   ```

## Fallback Approach (System JDK)
If OLAF JDK structure not available, fall back to system JDK:
1. **Detect System JDK 21**:
   ```bash
   # Windows
   where java
   dir "C:\Program Files\Java" | findstr "jdk-21"
   
   # Linux/macOS
   which java
   ls /usr/lib/jvm/ | grep 21
   /usr/libexec/java_home -V | grep 21
   ```

2. **Set Environment Variables**:
   ```bash
   # Windows (PowerShell)
   $env:JAVA_HOME = "C:\Program Files\Java\jdk-21"
   $env:MAVEN_JAVA_HOME = $env:JAVA_HOME
   $env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
   
   # Linux/macOS (Bash)
   export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
   export MAVEN_JAVA_HOME=$JAVA_HOME
   export PATH=$JAVA_HOME/bin:$PATH
   ```
## Verification Commands
```bash
# Verify JDK 21 is active
java -version | grep "21\." && echo "PASS: JDK 21 active" || echo "FAIL: JDK 21 not active"

# Verify Maven uses JDK 21
mvn -version | grep "Java version: 21" && echo "PASS: Maven uses JDK 21" || echo "FAIL: Maven not using JDK 21"

# Check Java compiler version
javac -version | grep "21\." && echo "PASS: Compiler JDK 21" || echo "FAIL: Compiler not JDK 21"

# Verify environment variables
echo "JAVA_HOME: $JAVA_HOME"
echo "MAVEN_JAVA_HOME: $MAVEN_JAVA_HOME"
```

## Issue Detection & Remediation

### JDK 21 Not Found (Severity: high)
**Detection Pattern**: JDK 21 not found at `~/.olaf/jdk/21/` or system locations
**Remediation**:
1. Check OLAF JDK structure: `~/.olaf/jdk/21/bin/java -version`
2. If missing, install JDK 21 to OLAF structure or system location
3. Verify installation with `java -version`
**Validation**: JDK 21 accessible via OLAF structure or system PATH

### Environment Variables Not Set (Severity: high)
**Detection Pattern**: JAVA_HOME or MAVEN_JAVA_HOME pointing to wrong JDK
**Remediation**:
1. Set JAVA_HOME to JDK 21 installation directory
2. Set MAVEN_JAVA_HOME to same value as JAVA_HOME
3. Update PATH to include JDK 21 bin directory first
**Validation**: Environment variables point to JDK 21 installation

### Maven Still Using Old JDK (Severity: medium)
**Detection Pattern**: `mvn -version` shows JDK version other than 21
**Remediation**:
1. Ensure MAVEN_JAVA_HOME is set correctly
2. Check for Maven toolchain configuration overriding JDK
3. Restart shell session to pick up new environment variables
**Validation**: `mvn -version` reports JDK 21

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `jdk-switch-<YYYYMMDD-HHmm>.json`
- **Categories**: installation, environment, maven, toolchain
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (toolchain conflicts)

## Success Criteria
- ✅ JDK 21 active: `java -version` shows 21.x
- ✅ Maven uses JDK 21: `mvn -version` shows Java version 21
- ✅ Compiler uses JDK 21: `javac -version` shows 21.x
- ✅ Environment variables set correctly: JAVA_HOME and MAVEN_JAVA_HOME point to JDK 21
- ✅ Session-scoped change documented (new shells need re-configuration)