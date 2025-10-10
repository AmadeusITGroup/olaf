# Verify Podman Rootless — Toolkit

## Preferred approach (Windows/Linux/macOS)
1. Check rootless status:
   - `podman info --format '{{.Host.Security.Rootless}}'`
2. Run a simple container without elevation:
   - `podman run --rm docker.io/library/alpine:3.19 echo ok`
3. Inspect storage path is under user home (rootless):
   - `podman info --format '{{.Store.GraphRoot}}'`

## Backup option
- If rootless is disabled or fails, initialize user session for containers and retry:
  - On Windows/macOS: follow Podman machine init steps.
  - On Linux: ensure subuids/subgids configured for your user.

## Verify
- Rootless flag reports `true`.
- Test container prints `ok` and exits 0.
- Graph root points to a user-scoped directory.
