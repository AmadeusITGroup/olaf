# Java Migration Prerequisites

**Role**: Quick prerequisite checker - Verifies essential tools are available before migration.

**Mission**: Check for required tools and provide simple installation guidance if missing.

---

## Essential Requirements

Only 4 tools are absolutely required:

### 1. Java Development Kits
- **JDK 11, 17, 21** installed at `~/.olaf/jdk/{version}/`
- **Verification**: `~/.olaf/jdk/17/bin/java -version` works
- **If missing**: Use provided JDK installation scripts

### 2. Build Tool
- **Maven ≥ 3.9** OR **Gradle ≥ 8.0**
- **Verification**: `mvn --version` or `gradle --version`
- **If missing**: Install from official websites

### 3. Git
- **Any recent version**
- **Verification**: `git --version`
- **If missing**: Install from git-scm.com

### 4. Python 3
- **Python 3.8+** for migration scripts
- **Verification**: `python --version` shows 3.x
- **If missing**: Install from python.org

---

## Quick Check Commands

Run these to verify your setup:

```bash
# Check JDKs
~/.olaf/jdk/11/bin/java -version
~/.olaf/jdk/17/bin/java -version  
~/.olaf/jdk/21/bin/java -version

# Check build tool
mvn --version
# OR
gradle --version

# Check Git and Python
git --version
python --version
```

---

## Installation Help

### JDK Setup
1. Download JDK 11, 17, 21 from Eclipse Temurin
2. Extract to `~/.olaf/jdk/{version}/`
3. Use provided switching scripts in `olaf-core/prompts/java-migration/`

### Build Tools
- **Maven**: Download from maven.apache.org
- **Gradle**: Download from gradle.org or use wrapper

### Git & Python
- **Git**: Download from git-scm.com
- **Python**: Download from python.org

---

## Usage

```
User: Check prerequisites

Agent: 
🔍 Checking Java migration prerequisites...

✅ JDK 11: Found at ~/.olaf/jdk/11/
✅ JDK 17: Found at ~/.olaf/jdk/17/
✅ JDK 21: Found at ~/.olaf/jdk/21/
✅ Maven: 3.9.9
✅ Git: 2.45.2
✅ Python: 3.13.2

All prerequisites satisfied! Ready for migration.
```

If tools are missing, the agent provides simple installation guidance and offers to help set up the JDK switching scripts.
