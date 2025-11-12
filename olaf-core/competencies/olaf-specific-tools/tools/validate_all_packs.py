import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parents[3]  # .../olaf-xdlc
DEFAULT_COMPETENCIES_DIR = REPO_ROOT / "olaf-core" / "competencies"
VALIDATOR = THIS_DIR / "validate_competency_pack.py"

EXCLUDE_DIRS = {
    "strands-exploration",
}


def is_pack_dir(d: Path) -> bool:
    if not d.is_dir():
        return False
    if d.name in EXCLUDE_DIRS:
        return False
    # consider a directory a pack if it has prompts/ or a manifest json
    if (d / "prompts").is_dir():
        return True
    for mf in ("manifest.json", "competency.json", "pack.json", "competency-manifest.json"):
        if (d / mf).is_file():
            return True
    return False


def validate_pack(pack_dir: Path) -> Dict:
    cmd = [sys.executable, str(VALIDATOR), str(pack_dir), "--json"]
    try:
        out = subprocess.check_output(cmd, cwd=str(REPO_ROOT), stderr=subprocess.STDOUT)
        data = json.loads(out.decode("utf-8", errors="ignore"))
        data["exit_code"] = 0
        return data
    except subprocess.CalledProcessError as e:
        # Even on failures the validator prints JSON then exits 1 if any rule failed; try to parse JSON first.
        text = e.output.decode("utf-8", errors="ignore")
        try:
            data = json.loads(text)
            data["exit_code"] = e.returncode
            return data
        except Exception:
            return {
                "pack": pack_dir.name,
                "root": str(pack_dir),
                "error": f"Validator failed: {e.returncode}",
                "output": text,
                "exit_code": e.returncode,
            }


def main():
    ap = argparse.ArgumentParser(description="Validate all OLAF competency packs and aggregate results")
    ap.add_argument("--packs-root", default=str(DEFAULT_COMPETENCIES_DIR), help="Path to competencies root")
    ap.add_argument("--json", action="store_true", help="Emit JSON aggregate report")
    args = ap.parse_args()

    root = Path(args.packs_root).resolve()
    if not root.is_dir():
        print(f"Error: packs root not found: {root}", file=sys.stderr)
        sys.exit(2)

    packs: List[Path] = [d for d in root.iterdir() if is_pack_dir(d)]
    packs.sort(key=lambda p: p.name.lower())

    results: List[Dict] = []
    for p in packs:
        results.append(validate_pack(p))

    if args.json:
        print(json.dumps({"root": str(root), "results": results}, ensure_ascii=False))
        return

    # Markdown summary
    print(f"# All Competency Packs Validation Summary")
    print()
    print(f"Root: {root}")
    total = len(results)
    print(f"Packs scanned: {total}")
    print()
    for r in results:
        if "error" in r:
            print(f"- [ERROR] {r.get('pack','<unknown>')}: {r['error']}")
            continue
        counts = r.get("counts", {})
        passed = sum(1 for x in r.get("rules", []) if x.get("passed"))
        total_rules = len(r.get("rules", []))
        print(f"- {r['pack']}: {passed}/{total_rules} rules passed; prompts={counts.get('prompts',0)}, entry_points={counts.get('entry_points',0)}")
    print()
    print("Note: Detailed rule breakdown available in JSON mode (--json)")


if __name__ == "__main__":
    main()
