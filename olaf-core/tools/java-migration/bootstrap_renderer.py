#!/usr/bin/env python3
"""
Bootstrap Plan Renderer

- Copies the canonical migration plan template and writes it under the findings/migrations/<ts>/ directory.
- Optionally prepends a short dynamic summary block derived from detector JSONs and the bootstrap context.
- Keeps the canonical template content verbatim to remain parseable and consistent.

Usage:
  python bootstrap_renderer.py \
    --project <path-to-maven-project> \
    --timestamp <YYYYMMDD-HHmm> \
    --out-dir <findings/migrations base dir> \
    [--template <canonical-template-path>] \
    [--index-json <path to index.json>] \
    [--boot27-json <path to boot-2.7-report.json>] \
    [--boot3-json <path to boot-3-report.json>] \
    [--context <path to migration-bootstrap-context.yaml>] \
    [--quiet]

Outputs:
  - <out-dir>/<ts>/migration-plan-<ts>.md

Note: This is a minimal renderer that preserves the canonical template verbatim.
It adds a small preface header with dynamic values but does not attempt task-level
status token rewriting yet. That can be added incrementally while still preserving
canonical content.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # Optional; renderer works without context YAML

CORE_ROOT = Path(__file__).resolve().parents[2]  # .../olaf/olaf-core
REPO_ROOT = CORE_ROOT.parent                    # .../olaf
TEMPLATE_DEFAULT = CORE_ROOT / "templates" / "bootstrap-java-migration" / "java-migration-plan-yyyymmdd-hhmm.md"
FINDINGS_DEFAULT = REPO_ROOT / "olaf-data" / "findings" / "migrations"


def _load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8")) if p and p.exists() else {}


def _load_yaml(p: Path) -> dict:
    if yaml is None or not p or not p.exists():
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def _preface(index: dict, context: dict, boot27: dict, boot3: dict) -> str:
    # Best-effort dynamic summary; keep very short
    ts = index.get("timestamp") or ""
    summ = index.get("summary", {})
    b27 = summ.get("boot_2_7", {})
    b3 = summ.get("boot_3", {})
    detected_java = b3.get("java") or b27.get("java") or "unknown"
    detected_boot = b3.get("parent") or b27.get("parent") or "unknown"

    targets = (context.get("targets") or {}) if context else {}
    tgt_java = (targets.get("java") or "").__str__()
    tgt_boot_req = (targets.get("spring_boot") or {}).get("requested") or ""
    tgt_boot_res = (targets.get("spring_boot") or {}).get("resolved") or "(pending)"

    # Detector-driven annotations (non-destructive hints; template remains verbatim)
    boot3_res = (boot3 or {}).get("results", {})
    boot27_res = (boot27 or {}).get("results", {})
    junit4_count = 0
    javax_count = 0
    cron_occ = 0
    # Extract JUnit4
    for item in boot3_res.get("testing_risks", []) or []:
        if "JUnit 4" in (item.get("risk") or "") and "Occurrences:" in (item.get("detail") or ""):
            try:
                junit4_count = int((item.get("detail") or "").split("Occurrences:")[-1].strip())
            except Exception:
                pass
    # Extract javax imports
    for item in boot3_res.get("source_scan", []) or []:
        if "javax" in (item.get("detail") or "") and "Occurrences:" in (item.get("detail") or ""):
            try:
                javax_count = int((item.get("detail") or "").split("Occurrences:")[-1].strip())
            except Exception:
                pass
    # Extract CronSequenceGenerator occurrences
    for item in boot3_res.get("api_changes", []) or []:
        if "CronSequenceGenerator" in (item.get("risk") or "") and "Occurrences" in (item.get("detail") or ""):
            try:
                cron_occ = int((item.get("detail") or "").split(":")[-1].strip())
            except Exception:
                pass

    lines = [
        "# Migration Plan (Rendered Preface)",
        "",
        f"- Detected Java: {detected_java}",
        f"- Detected Spring Boot parent: {detected_boot}",
        f"- Target Java: {tgt_java or '(unspecified)'}",
        f"- Target Spring Boot: {tgt_boot_req} → {tgt_boot_res}",
        f"- Timestamp: {ts}",
        "",
        "## Detector-Driven Annotations",
        "- JUnit 4 imports detected: {} (Keep JUnit 5 migration tasks in Phase 1)".format(junit4_count),
        "- javax imports detected: {} (Keep Jakarta migration tasks in Phase 2)".format(javax_count),
        "- CronSequenceGenerator occurrences: {} (Address under API changes in Phase 2)".format(cron_occ),
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Render canonical migration plan from template")
    ap.add_argument("--project", required=True, help="Path to Maven project root (contains pom.xml)")
    ap.add_argument("--timestamp", required=True, help="Timestamp in YYYYMMDD-HHmm")
    ap.add_argument("--out-dir", default=str(FINDINGS_DEFAULT), help="Base findings/migrations directory")
    ap.add_argument("--template", default=str(TEMPLATE_DEFAULT), help="Canonical template path")
    ap.add_argument("--index-json", help="Path to detector index.json")
    ap.add_argument("--boot27-json", help="Path to boot-2.7-report.json (optional; inferred from index.json if omitted)")
    ap.add_argument("--boot3-json", help="Path to boot-3-report.json (optional; inferred from index.json if omitted)")
    ap.add_argument("--context", help="Path to migration-bootstrap-context.yaml")
    ap.add_argument("--quiet", action="store_true", help="Suppress stdout logs")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not (project / "pom.xml").exists():
        print(f"Error: pom.xml not found under {project}", file=sys.stderr)
        sys.exit(2)

    ts = args.timestamp
    out_base = Path(args.out_dir).resolve()
    out_dir = out_base / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    template_path = Path(args.template).resolve()
    if not template_path.exists():
        print(f"Error: template not found: {template_path}", file=sys.stderr)
        sys.exit(3)

    index = _load_json(Path(args.index_json)) if args.index_json else {}
    # Infer boot report paths from index if not provided
    boot27_path = Path(args.boot27_json) if args.boot27_json else Path(index.get("artifacts", {}).get("boot_2_7", ""))
    boot3_path = Path(args.boot3_json) if args.boot3_json else Path(index.get("artifacts", {}).get("boot_3", ""))
    boot27 = _load_json(boot27_path) if str(boot27_path) else {}
    boot3 = _load_json(boot3_path) if str(boot3_path) else {}
    context = _load_yaml(Path(args.context)) if args.context else {}

    preface = _preface(index, context, boot27, boot3)
    template_md = template_path.read_text(encoding="utf-8")

    out_path = out_dir / f"migration-plan-{ts}.md"
    # Write preface + canonical template verbatim
    out_path.write_text(preface + template_md, encoding="utf-8")

    if not args.quiet:
        print(f"Rendered plan to: {out_path}")


if __name__ == "__main__":
    main()
