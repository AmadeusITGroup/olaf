#!/bin/bash
# Switch JDK - Quickly change JAVA_HOME to a different JDK version
# Usage: ./switch-jdk.sh <version>
# Example: ./switch-jdk.sh 17

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

JDK_DIR="/opt/migration-toolkit/jdk"
TARGET_JDK="$JDK_DIR/$VERSION"

# Check if JDK exists
if [ ! -d "$TARGET_JDK" ]; then
    echo "ERROR: JDK $VERSION not found at $TARGET_JDK"
    echo "Run install-linux.sh first to install JDKs"
    exit 1
fi

if [ ! -f "$TARGET_JDK/bin/java" ]; then
    echo "ERROR: JDK $VERSION installation appears incomplete"
    echo "Missing: $TARGET_JDK/bin/java"
    exit 1
fi

# Determine profile file
PROFILE_FILE="$HOME/.bashrc"
if [[ "$OSTYPE" == "darwin"* ]]; then
    PROFILE_FILE="$HOME/.zshrc"
fi

# Update profile file
echo "Switching to JDK $VERSION..."

# Remove old JAVA_HOME entry
sed -i.bak '/^export JAVA_HOME=/d' "$PROFILE_FILE" 2>/dev/null || true

# Add new JAVA_HOME entry
echo "export JAVA_HOME=\"\$JDK${VERSION}_HOME\"" >> "$PROFILE_FILE"

# Set for current session
export JAVA_HOME="$TARGET_JDK"
export PATH="$JAVA_HOME/bin:$PATH"

echo ""
echo "SUCCESS: JAVA_HOME set to JDK $VERSION"
echo "  Path: $TARGET_JDK"
echo ""

# Show version
echo "Java version:"
"$TARGET_JDK/bin/java" -version

echo ""
echo "NOTE: Current session updated. New terminals will use JDK $VERSION automatically."
echo "      To apply in THIS terminal, run: source $PROFILE_FILE"

exit 0
