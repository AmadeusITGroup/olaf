# Install Podman — Toolkit

## Preferred approach (Windows/macOS/Linux)
1. Install Podman using your OS package manager.
   - Windows: `winget install -e --id RedHat.Podman`
   - macOS: `brew install podman`
   - Linux (Fedora/RHEL): `sudo dnf install podman`
   - Linux (Debian/Ubuntu): `sudo apt-get install podman`
2. Initialize user-level containers environment if needed.
3. Ensure Podman is on PATH in the current shell.

## Backup option
- If package manager not available, download from official releases and install manually.

## Verify
- `podman --version` prints a valid version.
- `podman info` succeeds.
