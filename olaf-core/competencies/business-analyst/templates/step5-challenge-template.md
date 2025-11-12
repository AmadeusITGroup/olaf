# Step 5: Challenge, Simplify, Amplify

Date: <YYYY-MM-DD HH:MM>
Sources: <steps 1–4 files>
Process: Web-informed challenge and refinement with decisions

## Challenge Catalog

### CLI UX & Safety
- Challenge: Inconsistent flag forms and interactive defaults can surprise users.
- Simplification: Standardize short `-x`, long `--flag`; make interactive opt-in.
- Amplification: Add `--yes` and `--plan` to preview actions.
- Decisions:
  1. Default interactive OFF with explicit confirm for multi-repo.
  2. Provide `--multi` and `--yes` for non-interactive pipelines.

### Error Taxonomy & Exit Codes
- Challenge: Mixed patterns (warn/continue vs fail-fast).
- Simplification: Define critical vs optional classes.
- Amplification: Granular exit codes (config/network/auth/lock/etc.).
- Decisions:
  1. Single non-zero vs granular codes.
  2. Strict vs permissive modes.

### Integrity & Supply Chain
- Challenge: No integrity verification on downloads.
- Simplification: Optional SHA256 checks in registry metadata.
- Amplification: Future signature support.
- Decisions:
  1. Enable hash checks for critical artifacts (Y/N).

### Structured Logging & Redaction
- Challenge: Human-readable only; risk of secret leaks.
- Simplification: Dual-mode (text + JSON), stable schema.
- Amplification: Full redaction (S2-2); DEBUG toggles (no partial token reveal if S2-2).
- Decisions:
  1. Adopt JSON alongside text (Y/N).

### Retries & Idempotency
- Challenge: Limited retries; copy operations not configurable.
- Simplification: Defaults with sane limits.
- Amplification: `--copy-retries`, `--copy-retry-wait` options.
- Decisions:
  1. Keep fixed retry vs configurable.

### Multi-Repo Discovery Safety
- Challenge: Overreach across repos.
- Simplification: Interactive plan + confirm; excludes (.venv, node_modules, hidden).
- Amplification: Global cache `~/.olaf-global` for reuse.
- Decisions:
  1. Interactive vs subcommand vs defer feature.

### Proxy/CA Patterns (MVP policy-dependent)
- Challenge: Corporate environments.
- Simplification: Warn if detected when out of scope.
- Amplification: Document env vars (HTTP_PROXY/HTTPS_PROXY/NO_PROXY) and CA hooks for later.

### Security Hardening
- Challenge: Temp dirs, path traversal, privilege scope.
- Simplification: Use `OLAF_TMPDIR`/`--tmp-dir`; validate paths.
- Amplification: Defense in depth checks.

## MoSCoW Prioritization
- <Item>: M/S/C/W

## Decisions (Recorded)
- <Decision key>: <option>

Examples to emulate
- Breadth: spec-github-sonnet4/step5-<timestamp>.md
- Decision capture: spec-windsurf-gpt5lr/step5-<timestamp>.md (A2-1, P7-M, S2-2, etc.)
