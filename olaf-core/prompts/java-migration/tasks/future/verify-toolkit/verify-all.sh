#!/bin/bash
# Task 0.2: Verify Toolkit (Linux/Mac/WSL)
# Verifies all migration tools are installed and configured correctly
# Usage: ./verify-all.sh

set +e  # Don't exit on first error

echo "=== Task 0.2: Verify Toolkit ==="
echo ""

ALL_CHECKS_PASSED=true
JDK_DIR="/opt/migration-toolkit/jdk"

# Detect WSL (use Windows paths if in WSL)
if grep -qi microsoft /proc/version 2>/dev/null; then
    JDK_DIR="/mnt/c/migration-toolkit/jdk"
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to extract Java version
get_java_version() {
    local output="$1"
    if echo "$output" | grep -oP 'version\s+"\K\d+' 2>/dev/null | head -1; then
        return
    elif echo "$output" | grep -oP 'version\s+"1\.\K\d+' 2>/dev/null | head -1; then
        return
    fi
    echo "unknown"
}

# Check JDK Installations
echo "Checking JDK Installations..."

for version in 11 17 21; do
    jdk_path="$JDK_DIR/$version"
    
    # Determine java executable path (WSL uses .exe)
    if [ -f "$jdk_path/bin/java.exe" ]; then
        java_exe="$jdk_path/bin/java.exe"
    else
        java_exe="$jdk_path/bin/java"
    fi
    
    if [ ! -d "$jdk_path" ]; then
        echo "  ✗ JDK $version: Not found at $jdk_path"
        ALL_CHECKS_PASSED=false
    elif [ ! -f "$java_exe" ]; then
        echo "  ✗ JDK $version: Directory exists but java executable missing"
        ALL_CHECKS_PASSED=false
    else
        if java_version_output=$("$java_exe" -version 2>&1 | head -1); then
            version_num=$(get_java_version "$java_version_output")
            echo "  ✓ JDK $version: $jdk_path (version $version_num)"
        else
            echo "  ✗ JDK $version: Found but java executable doesn't work"
            ALL_CHECKS_PASSED=false
        fi
    fi
done

# Check Maven
echo ""
echo "Checking Maven..."

if ! command_exists mvn; then
    echo "  ✗ Maven: Not found in PATH"
    ALL_CHECKS_PASSED=false
else
    if maven_version=$(mvn --version 2>&1 | head -1); then
        if echo "$maven_version" | grep -oP 'Apache Maven \K[\d.]+' > /dev/null 2>&1; then
            version=$(echo "$maven_version" | grep -oP 'Apache Maven \K[\d.]+')
            
            # Parse version
            IFS='.' read -r major minor patch <<< "$version"
            
            # Check if version >= 3.9.5
            if [ "$major" -gt 3 ] || \
               ([ "$major" -eq 3 ] && [ "$minor" -gt 9 ]) || \
               ([ "$major" -eq 3 ] && [ "$minor" -eq 9 ] && [ "$patch" -ge 5 ]); then
                echo "  ✓ Maven: $version (in PATH)"
            else
                echo "  ✗ Maven: $version is too old (need 3.9.5+)"
                ALL_CHECKS_PASSED=false
            fi
        else
            echo "  ✗ Maven: Found but couldn't parse version"
            ALL_CHECKS_PASSED=false
        fi
    else
        echo "  ✗ Maven: Found but 'mvn --version' failed"
        ALL_CHECKS_PASSED=false
    fi
fi

# Check Git
echo ""
echo "Checking Git..."

if ! command_exists git; then
    echo "  ✗ Git: Not found in PATH"
    ALL_CHECKS_PASSED=false
else
    if git_version=$(git --version 2>&1); then
        if echo "$git_version" | grep -oP 'git version \K.+' > /dev/null 2>&1; then
            version=$(echo "$git_version" | grep -oP 'git version \K.+')
            echo "  ✓ Git: $version (in PATH)"
        else
            echo "  ✓ Git: Found in PATH"
        fi
    else
        echo "  ✗ Git: Found but 'git --version' failed"
        ALL_CHECKS_PASSED=false
    fi
fi

# Check Environment Variables
echo ""
echo "Checking Environment Variables..."

declare -A env_vars
env_vars["JDK11_HOME"]="$JDK_DIR/11"
env_vars["JDK17_HOME"]="$JDK_DIR/17"
env_vars["JDK21_HOME"]="$JDK_DIR/21"
env_vars["JAVA_HOME"]="$JDK_DIR/17"

for var_name in JDK8_HOME JDK11_HOME JDK17_HOME JDK21_HOME JAVA_HOME; do
    expected_value="${env_vars[$var_name]}"
    actual_value="${!var_name}"
    
    if [ -z "$actual_value" ]; then
        echo "  ✗ $var_name: Not set"
        ALL_CHECKS_PASSED=false
    elif [ "$actual_value" = "$expected_value" ]; then
        echo "  ✓ $var_name = $actual_value"
    else
        echo "  ⚠ $var_name = $actual_value (expected: $expected_value)"
        # Not failing for this, just warning
    fi
done

# Summary
echo ""
if [ "$ALL_CHECKS_PASSED" = true ]; then
    echo "=== All Checks Passed ==="
    echo "Toolkit is ready for migration!"
    echo ""
    exit 0
else
    echo "=== Some Checks Failed ==="
    echo ""
    echo "Troubleshooting:"
    echo "  - Missing JDK: Run Task 0.0.1 (Install JDKs) again"
    echo "  - Missing Maven: Install Maven 3.9.5+ (apt install maven / brew install maven)"
    echo "  - Missing Git: Install Git (apt install git / brew install git)"
    echo "  - Environment variables: Run 'source ~/.bashrc' or 'source ~/.zshrc'"
    echo ""
    exit 1
fi
