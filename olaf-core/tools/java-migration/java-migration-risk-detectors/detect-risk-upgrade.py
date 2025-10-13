#!/usr/bin/env python3
"""
Unified Spring Boot upgrade risk detector.

Usage:
  python detect-risk-upgrade.py --target {2.7,3} [/path/to/maven-project]
Optional flags:
  --scan-sources           Enable source/config scans when supported
  --output json            Output results as JSON (printed to stdout unless --out-file is set)
  --out-file <path>        File path to write JSON results
  --quiet                  Suppress console report output
"""
import argparse
import json
import importlib.util
import sys
from pathlib import Path

# Ensure local imports
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))


def _load_detector(module_path: Path, class_name: str):
    spec = importlib.util.spec_from_file_location(class_name, str(module_path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cls = getattr(module, class_name)
    return cls


def main():
    parser = argparse.ArgumentParser(description="Unified Spring Boot upgrade risk detector")
    parser.add_argument("project", nargs="?", default=".", help="Path to Maven project root (contains pom.xml)")
    parser.add_argument("--target", choices=["2.7", "3"], required=True, help="Target Spring Boot version track")
    parser.add_argument("--scan-sources", action="store_true", help="Enable source/config scans when supported")
    parser.add_argument("--output", choices=["json"], help="Output format (json)")
    parser.add_argument("--out-file", help="Path to write JSON output")
    parser.add_argument("--quiet", action="store_true", help="Suppress console report output")
    args = parser.parse_args()

    if args.target == "2.7":
        module_path = _HERE / "detect-risk-upgrade-to-spring-boot-2-7.py"
        Detector = _load_detector(module_path, "Boot27UpgradeRiskDetector")
    else:
        module_path = _HERE / "detect-risk-upgrade-to-spring-boot-3.py"
        Detector = _load_detector(module_path, "Boot3UpgradeRiskDetector")

    det = Detector(args.project, scan_sources=bool(args.scan_sources))
    results = det.analyze()

    # Emit console report always unless JSON-only requested with out-file
    if args.output == "json":
        payload = {
            "tool": "detect-risk-upgrade",
            "target": args.target,
            "project": str(Path(args.project).resolve()),
            "scan_sources": bool(args.scan_sources),
            "results": results,
        }
        text = json.dumps(payload, indent=2)
        if args.out_file:
            out_path = Path(args.out_file)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(text, encoding="utf-8")
        else:
            print(text)
    else:
        if not args.quiet:
            det.report(results)


if __name__ == "__main__":
    main()
