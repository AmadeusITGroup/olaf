#!/usr/bin/env python3
"""
Task 0.0.1: Verify JDK Installation
Checks that JDK 11, 17, 21 are installed correctly
"""

import os
import sys
import subprocess
import platform

def verify_jdk(version, jdk_home_var):
    """Verify a single JDK installation"""
    print(f"\nVerifying JDK {version}...")
    
    # Check environment variable
    jdk_home = os.environ.get(jdk_home_var)
    if not jdk_home:
        print(f"  ❌ Environment variable {jdk_home_var} not set")
        return False
    
    print(f"  ✓ {jdk_home_var} = {jdk_home}")
    
    # Check directory exists
    if not os.path.exists(jdk_home):
        print(f"  ❌ Directory does not exist: {jdk_home}")
        return False
    
    print(f"  ✓ Directory exists")
    
    # Check java executable
    java_exe = os.path.join(jdk_home, "bin", "java")
    if platform.system() == "Windows":
        java_exe += ".exe"
    
    if not os.path.exists(java_exe):
        print(f"  ❌ Java executable not found: {java_exe}")
        return False
    
    print(f"  ✓ Java executable found")
    
    # Check java version
    try:
        result = subprocess.run(
            [java_exe, "-version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        version_output = result.stderr  # java -version outputs to stderr
        
        # Check if version matches
        if f'version "{version}.' in version_output or f'version "{version}"' in version_output:
            print(f"  ✓ Version confirmed: JDK {version}")
            return True
        else:
            print(f"  ❌ Version mismatch. Expected {version}, got:")
            print(f"     {version_output.split(chr(10))[0]}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ❌ Java command timed out")
        return False
    except Exception as e:
        print(f"  ❌ Failed to run java -version: {e}")
        return False

def verify_java_home():
    """Verify JAVA_HOME is set"""
    print("\nVerifying JAVA_HOME...")
    
    java_home = os.environ.get("JAVA_HOME")
    if not java_home:
        print("  ❌ JAVA_HOME not set")
        return False
    
    print(f"  ✓ JAVA_HOME = {java_home}")
    
    # Check it points to a valid JDK
    java_exe = os.path.join(java_home, "bin", "java")
    if platform.system() == "Windows":
        java_exe += ".exe"
    
    if not os.path.exists(java_exe):
        print(f"  ❌ JAVA_HOME does not point to valid JDK")
        return False
    
    print(f"  ✓ JAVA_HOME points to valid JDK")
    return True

def main():
    print("=" * 50)
    print("Task 0.0.1: Verify JDK Installation")
    print("=" * 50)
    
    results = []
    
    # Verify each JDK
    results.append(verify_jdk("11", "JDK11_HOME"))
    results.append(verify_jdk("17", "JDK17_HOME"))
    results.append(verify_jdk("21", "JDK21_HOME"))
    
    # Verify JAVA_HOME
    results.append(verify_java_home())
    
    # Summary
    print("\n" + "=" * 50)
    if all(results):
        print("✅ All verifications passed")
        print("=" * 50)
        return 0
    else:
        print("❌ Some verifications failed")
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
