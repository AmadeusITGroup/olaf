#!/bin/bash
# Switch JDK - Quickly change JAVA_HOME to a different JDK version (WSL Version)
# This version works with JDKs installed on Windows, accessed via /mnt/c/
# Usage: ./switch-jdk-wsl.sh <version>
# Example: ./switch-jdk-wsl.sh 17

set -e

# Validate arguments
if [ $# -ne 1 ]; then
    echo "Usage: $0 <version>"
    echo "Available versions: 8, 11, 17, 21"
    exit 1
fi

VERSION=$1

# Validate version
case $VERSION in
    8|11|17|21)
        ;;
    *)
        echo "ERROR: Invalid version '$VERSION'"
        echo "Available versions: 8, 11, 17, 21"
        exit 1
        ;;
esac

# Use Windows JDK location via WSL mount
JDK_DIR="/mnt/c/migration-toolkit/jdk"
TARGET_JDK="$JDK_DIR/$VERSION"

# Check if JDK exists
if [ ! -d "$TARGET_JDK" ]; then
    echo "ERROR: JDK $VERSION not found at $TARGET_JDK"
    echo "Run install-windows.ps1 first to install JDKs"
    exit 1
fi

if [ ! -f "$TARGET_JDK/bin/java.exe" ]; then
    echo "ERROR: JDK $VERSION installation appears incomplete"
    echo "Missing: $TARGET_JDK/bin/java.exe"
    exit 1
fi

# Determine profile file
PROFILE_FILE="$HOME/.bashrc"
if [[ "$OSTYPE" == "darwin"* ]]; then
    PROFILE_FILE="$HOME/.zshrc"
fi

# Update profile file
echo "Switching to JDK $VERSION..."

# Remove old JDK environment variable entries
sed -i.bak '/^export JDK8_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/^export JDK11_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/^export JDK17_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/^export JDK21_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/^export JAVA_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/# Migration Toolkit JDKs (WSL)/d' "$PROFILE_FILE" 2>/dev/null || true

# Add new entries
cat >> "$PROFILE_FILE" << EOF

# Migration Toolkit JDKs (WSL)
export JDK8_HOME="$JDK_DIR/8"
export JDK11_HOME="$JDK_DIR/11"
export JDK17_HOME="$JDK_DIR/17"
export JDK21_HOME="$JDK_DIR/21"
export JAVA_HOME="\$JDK${VERSION}_HOME"
export PATH="\$JAVA_HOME/bin:\$PATH"
EOF

# Set for current session
export JDK8_HOME="$JDK_DIR/8"
export JDK11_HOME="$JDK_DIR/11"
export JDK17_HOME="$JDK_DIR/17"
export JDK21_HOME="$JDK_DIR/21"
export JAVA_HOME="$TARGET_JDK"
export PATH="$JAVA_HOME/bin:$PATH"

echo ""
echo "SUCCESS: JAVA_HOME set to JDK $VERSION"
echo "  Path: $TARGET_JDK"
echo ""

# Show version
echo "Java version:"
"$TARGET_JDK/bin/java.exe" -version

echo ""
echo "NOTE: Current session updated. New terminals will use JDK $VERSION automatically."
echo "      To apply in THIS terminal, run: source $PROFILE_FILE"

exit 0
