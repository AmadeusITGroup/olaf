#!/usr/bin/env bash
set -euo pipefail

VERSION="${VERSION:-8.10.1}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/migration-toolkit/gradle}"
SYMLINK_BIN_DIR="${SYMLINK_BIN_DIR:-$HOME/migration-toolkit/bin}"
FORCE="${FORCE:-false}"

log(){ echo "[gradle-install] $*"; }
warn(){ echo "[gradle-install][WARN] $*" >&2; }

if [[ "$VERSION" == "latest" ]]; then
  if command -v curl >/dev/null 2>&1; then
    log "Resolving latest version (stable)"
    VERSION=$(curl -s https://services.gradle.org/versions/current | grep '"version"' | sed -E 's/.*"version" *: *"([^"]+)".*/\1/')
  fi
  [[ -z "$VERSION" ]] && VERSION=8.10.1
fi

DIST_NAME="gradle-${VERSION}"
ZIP_NAME="${DIST_NAME}-bin.zip"
BASE_URL="https://services.gradle.org/distributions"
URL="${BASE_URL}/${ZIP_NAME}"
TARGET_DIR="${INSTALL_DIR}/${DIST_NAME}"

if [[ -d "$TARGET_DIR" && "$FORCE" != "true" ]]; then
  log "Gradle ${VERSION} already installed (use FORCE=true to reinstall)."
else
  [[ -d "$TARGET_DIR" && "$FORCE" == "true" ]] && { log "Removing existing $TARGET_DIR"; rm -rf "$TARGET_DIR"; }
  mkdir -p "$INSTALL_DIR" "$SYMLINK_BIN_DIR"
  TMP_ZIP=$(mktemp /tmp/gradle.XXXXXX.zip)
  log "Downloading $URL"
  curl -fsSL "$URL" -o "$TMP_ZIP"
  log "Extracting"
  unzip -q "$TMP_ZIP" -d "$INSTALL_DIR"
  rm -f "$TMP_ZIP"
fi

mkdir -p "$SYMLINK_BIN_DIR"
SHIM="$SYMLINK_BIN_DIR/gradle"
TARGET_BIN="$TARGET_DIR/bin/gradle"
cat > "$SHIM" <<EOF
#!/usr/bin/env bash
"$TARGET_BIN" "$@"
EOF
chmod +x "$SHIM"

# PATH guidance (can't persistently modify here portably)
if ! command -v gradle >/dev/null 2>&1; then
  warn "gradle not yet on PATH; add ${SYMLINK_BIN_DIR} to your PATH."
fi

log "Installed Gradle version:"
"$TARGET_BIN" --version | head -n 5
log "Done"
