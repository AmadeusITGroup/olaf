#!/usr/bin/env python3
"""
Run both Spring Boot upgrade risk detectors (2.7 and 3) and write JSON reports
under olaf-data/findings/migrations/<timestamp>/.

Usage:
  python run-upgrade-detectors.py --project <path-to-maven-project> [--timestamp YYYYMMDD-HHmm] [--out-dir <dir>] [--no-scan-sources] [--quiet]

Outputs:
  - olaf-data/findings/migrations/<ts>/boot-2.7-report.json
  - olaf-data/findings/migrations/<ts>/boot-3-report.json
  - olaf-data/findings/migrations/<ts>/index.json (summary)
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
REPO_ROOT = HERE.parents[3]  # .../olaf
DEFAULT_FINDINGS_DIR = REPO_ROOT / "olaf-data" / "findings" / "migrations"
DETECTOR_CLI = HERE / "detect-risk-upgrade.py"

def _now_ts() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M")


def run_detector(project: Path, target: str, out_dir: Path, scan_sources: bool = True, quiet: bool = False) -> Path:
    out_file = out_dir / ("boot-" + ("2.7" if target == "2.7" else "3") + "-report.json")
    cmd = [
        sys.executable,
        str(DETECTOR_CLI),
        "--target", target,
        "--output", "json",
        "--out-file", str(out_file),
        str(project),
    ]
    if scan_sources:
        cmd.insert(4, "--scan-sources")
    if quiet:
        cmd.insert(4, "--quiet")
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True)
    return out_file


def summarize(boot27: dict, boot3: dict) -> dict:
    def _counts(payload: dict) -> dict:
        res = payload.get("results", {})
        summary = res.get("summary", {})
        return {
            "parent": summary.get("parent"),
            "java": summary.get("java"),
            "counts": summary.get("counts", {}),
        }
    return {
        "boot_2_7": _counts(boot27),
        "boot_3": _counts(boot3),
    }


def main():
    p = argparse.ArgumentParser(description="Run both Spring Boot upgrade detectors and write JSON reports")
    p.add_argument("--project", required=True, help="Path to Maven project root (contains pom.xml)")
    p.add_argument("--timestamp", help="Timestamp in YYYYMMDD-HHmm (default: now)")
    p.add_argument("--out-dir", help="Override output base directory (default: olaf-data/findings/migrations)")
    p.add_argument("--no-scan-sources", action="store_true", help="Disable source/config scans")
    p.add_argument("--quiet", action="store_true", help="Suppress stdout index printing")
    args = p.parse_args()

    project = Path(args.project).resolve()
    if not (project / "pom.xml").exists():
        print(f"Error: pom.xml not found under {project}", file=sys.stderr)
        sys.exit(2)

    ts = args.timestamp or _now_ts()
    base_dir = Path(args.out_dir).resolve() if args.out_dir else DEFAULT_FINDINGS_DIR
    out_dir = base_dir / ts

    scan = not args.no_scan_sources

    f27 = run_detector(project, "2.7", out_dir, scan_sources=scan, quiet=args.quiet)
    f3 = run_detector(project, "3", out_dir, scan_sources=scan, quiet=args.quiet)

    boot27 = json.loads(f27.read_text(encoding="utf-8"))
    boot3 = json.loads(f3.read_text(encoding="utf-8"))

    index = {
        "project": str(project),
        "timestamp": ts,
        "output_dir": str(out_dir),
        "summary": summarize(boot27, boot3),
        "artifacts": {
            "boot_2_7": str(f27),
            "boot_3": str(f3),
        },
    }
    (out_dir / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    if not args.quiet:
        print(json.dumps(index, indent=2))


if __name__ == "__main__":
    main()
