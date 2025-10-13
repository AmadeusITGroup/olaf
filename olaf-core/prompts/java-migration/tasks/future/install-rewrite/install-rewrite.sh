#!/usr/bin/env bash
set -euo pipefail
VERSION="${VERSION:-latest}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/migration-toolkit/bin}"
FORCE="${FORCE:-false}"

log(){ echo "[rewrite-install] $*"; }
warn(){ echo "[rewrite-install][WARN] $*" >&2; }

if [[ "$VERSION" == "latest" ]]; then
  if command -v curl >/dev/null 2>&1; then
    VERSION=$(curl -s https://api.github.com/repos/openrewrite/rewrite/releases/latest | grep '"tag_name"' | sed -E 's/.*"v?([^"}]+)".*/\1/')
  fi
  [[ -z "$VERSION" ]] && VERSION=5.37.0
fi

mkdir -p "$INSTALL_DIR"
TARGET="$INSTALL_DIR/rewrite"
if [[ -x "$TARGET" && "$FORCE" != "true" ]]; then
  if "$TARGET" --version 2>/dev/null | grep -q "$VERSION"; then
    log "rewrite $VERSION already installed (FORCE=true to reinstall)"
    exit 0
  fi
fi

ASSET="rewrite-linux-amd64"
UNAME=$(uname -s | tr '[:upper:]' '[:lower:]')
if [[ "$UNAME" == *"darwin"* ]]; then ASSET="rewrite-darwin-amd64"; fi
URL="https://github.com/openrewrite/rewrite/releases/download/v${VERSION}/${ASSET}"
TMP=$(mktemp /tmp/rewrite.XXXXXX)
log "Downloading $URL"
curl -fsSL "$URL" -o "$TMP"
install -m 0755 "$TMP" "$TARGET"
rm -f "$TMP"

if ! command -v rewrite >/dev/null 2>&1; then
  warn "rewrite not on PATH. Add $INSTALL_DIR to your PATH."
fi

log "Installed version:"
"$TARGET" --version
log "Done"
