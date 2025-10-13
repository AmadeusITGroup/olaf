#!/usr/bin/env bash
set -euo pipefail
VERSION="${VERSION:-distro}"  # distro | latest | explicit
INSTALL_DIR="${INSTALL_DIR:-$HOME/migration-toolkit/bin}"
CREATE_DOCKER_SHIM="${CREATE_DOCKER_SHIM:-true}"
FORCE="${FORCE:-false}"

log(){ echo "[podman-install] $*"; }
warn(){ echo "[podman-install][WARN] $*" >&2; }

have_cmd(){ command -v "$1" >/dev/null 2>&1; }

if have_cmd podman; then
  log "Podman already present: $(podman --version 2>/dev/null | head -n1)"
else
  if [[ "$VERSION" == "distro" ]]; then
    if have_cmd apt; then sudo apt update -y && sudo apt install -y podman
    elif have_cmd dnf; then sudo dnf install -y podman
    elif have_cmd yum; then sudo yum install -y podman
    elif have_cmd pacman; then sudo pacman -Sy --noconfirm podman
    else warn "No recognized package manager; install Podman manually."; fi
  else
    warn "Specific/latest version logic not implemented; attempting distro install"
    if have_cmd apt; then sudo apt update -y && sudo apt install -y podman; fi
  fi
fi

mkdir -p "$INSTALL_DIR"
if [[ "$CREATE_DOCKER_SHIM" == "true" ]]; then
  SHIM="$INSTALL_DIR/docker"
  if [[ ! -f "$SHIM" || "$FORCE" == "true" ]]; then
    log "Creating docker shim at $SHIM"
    cat > "$SHIM" <<'EOF'
#!/usr/bin/env bash
exec podman "$@"
EOF
    chmod +x "$SHIM"
  fi
fi

log "Smoke test:"
podman run --rm quay.io/podman/hello | head -n 5 || warn "Smoke test failed"
log "Done"
