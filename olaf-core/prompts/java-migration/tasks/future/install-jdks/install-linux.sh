#!/bin/bash
# Task 0.0.1: Install JDKs (Linux/Mac)
# Installs JDK 11, 17, 21 to /opt/migration-toolkit/jdk/
# Usage: ./install-linux.sh [-f|--force]
# Note: JDK 8 is excluded as it's EOL and most migrations start from JDK 11+

set -e

# Parse arguments
FORCE=false
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--force)
            FORCE=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [-f|--force]"
            exit 1
            ;;
    esac
done

echo "=== Task 0.0.1: Install JDKs ==="
if [ "$FORCE" = true ]; then
    echo "Force reinstall enabled"
fi

TOOLKIT_DIR="/opt/migration-toolkit"
JDK_DIR="$TOOLKIT_DIR/jdk"

# Detect OS
OS="linux"
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="mac"
fi

# JDK download URLs (Eclipse Temurin - latest stable versions)
if [ "$OS" = "linux" ]; then
    JDK_11_URL="https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.25%2B9/OpenJDK11U-jdk_x64_linux_hotspot_11.0.25_9.tar.gz"
    JDK_17_URL="https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.13%2B11/OpenJDK17U-jdk_x64_linux_hotspot_17.0.13_11.tar.gz"
    JDK_21_URL="https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.5%2B11/OpenJDK21U-jdk_x64_linux_hotspot_21.0.5_11.tar.gz"
else
    JDK_11_URL="https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.25%2B9/OpenJDK11U-jdk_x64_mac_hotspot_11.0.25_9.tar.gz"
    JDK_17_URL="https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.13%2B11/OpenJDK17U-jdk_x64_mac_hotspot_17.0.13_11.tar.gz"
    JDK_21_URL="https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.5%2B11/OpenJDK21U-jdk_x64_mac_hotspot_21.0.5_11.tar.gz"
fi

# Function to install a JDK
install_jdk() {
    local version=$1
    local url=$2
    local target_dir="$JDK_DIR/$version"
    
    echo ""
    echo "Installing JDK $version..."
    
    # Check if already installed
    if [ -d "$target_dir" ] && [ -f "$target_dir/bin/java" ] && [ "$FORCE" = false ]; then
        echo "  SKIP: JDK $version already installed (use -f to reinstall)"
        return 0
    fi
    
    # Remove existing if force reinstall
    if [ "$FORCE" = true ] && [ -d "$target_dir" ]; then
        echo "  Removing existing installation..."
        sudo rm -rf "$target_dir"
    fi
    
    # Download
    echo "  Downloading..."
    cd /tmp
    curl -L -o "jdk-$version.tar.gz" "$url" || {
        echo "  ERROR: Failed to download JDK $version"
        return 1
    }
    
    # Extract
    echo "  Extracting to $target_dir"
    sudo mkdir -p "$target_dir"
    sudo tar -xzf "jdk-$version.tar.gz" -C "$target_dir" --strip-components=1 || {
        echo "  ERROR: Failed to extract JDK $version"
        rm "jdk-$version.tar.gz"
        return 1
    }
    
    # Cleanup
    rm "jdk-$version.tar.gz"
    echo "  SUCCESS: JDK $version installed"
}

# Create directories
echo "Creating directories..."
sudo mkdir -p "$JDK_DIR"

# Install each JDK
install_jdk "11" "$JDK_11_URL"
install_jdk "17" "$JDK_17_URL"
install_jdk "21" "$JDK_21_URL"

# Set permissions
sudo chmod -R 755 "$JDK_DIR"

# Add to shell profile
PROFILE_FILE="$HOME/.bashrc"
if [[ "$OSTYPE" == "darwin"* ]]; then
    PROFILE_FILE="$HOME/.zshrc"
fi

echo ""
echo "Setting environment variables..."

# Remove old entries if they exist
sed -i.bak '/# Migration Toolkit JDKs/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/JDK8_HOME/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/JDK11_HOME/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/JDK17_HOME/d' "$PROFILE_FILE" 2>/dev/null || true
sed -i.bak '/JDK21_HOME/d' "$PROFILE_FILE" 2>/dev/null || true

# Add new entries
cat >> "$PROFILE_FILE" << EOF

# Migration Toolkit JDKs
export JDK11_HOME="$JDK_DIR/11"
export JDK17_HOME="$JDK_DIR/17"
export JDK21_HOME="$JDK_DIR/21"
export JAVA_HOME="\$JDK17_HOME"
export PATH="\$JAVA_HOME/bin:\$PATH"
EOF

# Set for current session
export JDK11_HOME="$JDK_DIR/11"
export JDK17_HOME="$JDK_DIR/17"
export JDK21_HOME="$JDK_DIR/21"
export JAVA_HOME="$JDK17_HOME"
export PATH="$JAVA_HOME/bin:$PATH"

echo "  JDK11_HOME = $JDK_DIR/11"
echo "  JDK17_HOME = $JDK_DIR/17"
echo "  JDK21_HOME = $JDK_DIR/21"
echo "  JAVA_HOME  = $JDK_DIR/17 (default)"

echo ""
echo "=== Installation Complete ==="
echo "JDKs installed to: $JDK_DIR"
echo "Run 'source $PROFILE_FILE' or restart terminal to apply environment variables"
echo "Run verify.py to confirm installation"

exit 0
