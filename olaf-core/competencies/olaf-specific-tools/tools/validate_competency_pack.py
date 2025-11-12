import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ALLOWED_PROTOCOLS = {
    "Act",
    "Propose-Act",
    "Propose-Confirm-Act",
}

KebabPromptRegex = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){2,3}\.md$")


@dataclass
class RuleResult:
    id: str
    title: str
    passed: bool
    details: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


@dataclass
class PackScan:
    root: Path
    readme: Optional[Path]
    prompts_dir: Optional[Path]
    templates_dir: Optional[Path]
    tools_dir: Optional[Path]
    docs_dir: Optional[Path]
    manifest_path: Optional[Path]
    prompt_files: List[Path]
    template_files: List[Path]
    tool_files: List[Path]
    docs_required: Dict[str, bool]
    entry_points: List[Dict]


def find_manifest(root: Path) -> Optional[Path]:
    candidates = [
        root / "manifest.json",
        root / "competency.json",
        root / "pack.json",
        root / "competency-manifest.json",
    ]
    for c in candidates:
        if c.is_file():
            return c
    # Fallback: any json with entry_points at root
    for p in root.glob("*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("entry_points"), list):
                return p
        except Exception:
            continue
    return None


def load_manifest(path: Path) -> Tuple[Optional[dict], Optional[str]]:
    if not path:
        return None, "No manifest found"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data, None
    except Exception as e:
        return None, f"Manifest parse error: {e}"


def scan_pack(root: Path) -> PackScan:
    prompts_dir = (root / "prompts") if (root / "prompts").is_dir() else None
    templates_dir = (root / "templates") if (root / "templates").is_dir() else None
    tools_dir = (root / "tools") if (root / "tools").is_dir() else None
    docs_dir = (root / "docs") if (root / "docs").is_dir() else None
    readme = root / "README.md" if (root / "README.md").is_file() else None

    prompt_files: List[Path] = []
    if prompts_dir:
        prompt_files = [p for p in prompts_dir.rglob("*.md") if p.is_file()]

    template_files: List[Path] = []
    if templates_dir:
        template_files = [p for p in templates_dir.rglob("*") if p.is_file()]

    tool_files: List[Path] = []
    if tools_dir:
        tool_files = [p for p in tools_dir.rglob("*") if p.is_file()]

    # docs validation is performed against README.md at docs/ and per-entry folders; no precomputed flags here
    docs_required = {}

    manifest_path = find_manifest(root)
    manifest, _ = load_manifest(manifest_path) if manifest_path else (None, None)

    entry_points = manifest.get("entry_points", []) if isinstance(manifest, dict) else []

    return PackScan(
        root=root,
        readme=readme,
        prompts_dir=prompts_dir,
        templates_dir=templates_dir,
        tools_dir=tools_dir,
        docs_dir=docs_dir,
        manifest_path=manifest_path,
        prompt_files=prompt_files,
        template_files=template_files,
        tool_files=tool_files,
        docs_required=docs_required,
        entry_points=entry_points,
    )


def classify_prompts(prompt_files: List[Path], root: Path) -> Dict[str, List[Path]]:
    """Classify prompts using explicit frontmatter role/tags first, then heuristics.
    Roles: orchestrator, workflow, else typical.
    """
    cats = {"orchestrator": [], "workflow": [], "typical": []}
    for p in prompt_files:
        text = read_file_text(p)
        meta = parse_frontmatter(text)
        role = str(meta.get("role", "")).lower()
        tags_text = str(meta.get("tags", "")).lower()

        name = p.stem.lower()
        parts_lower = [pp.lower() for pp in p.parts]

        is_orch = False
        is_wf = False

        # 1) Explicit role
        if role == "orchestrator":
            is_orch = True
        elif role == "workflow":
            is_wf = True

        # 2) Tags hint
        if not (is_orch or is_wf):
            if "orchestrator" in tags_text:
                is_orch = True
            elif "workflow" in tags_text:
                is_wf = True

        # 3) Filename/folder heuristic
        if not (is_orch or is_wf):
            if "orchestrator" in name or any("orchestrator" in seg for seg in parts_lower):
                is_orch = True
            elif name.endswith("-workflow") or "workflow" in name or any("workflow" in seg for seg in parts_lower):
                is_wf = True

        if is_orch:
            cats["orchestrator"].append(p)
        elif is_wf:
            cats["workflow"].append(p)
        else:
            cats["typical"].append(p)
    return cats


def check_r01_structure(scan: PackScan) -> RuleResult:
    missing: List[str] = []
    if not scan.readme:
        missing.append("README.md at root")
    if not scan.prompts_dir:
        missing.append("prompts/")
    if not scan.templates_dir:
        missing.append("templates/")
    if not scan.tools_dir:
        missing.append("tools/")
    if not scan.docs_dir:
        missing.append("docs/")
    rr = RuleResult(id="R01", title="Required Structure", passed=len(missing) == 0)
    if missing:
        rr.details.append("Missing: " + ", ".join(missing))
        rr.recommendations.append("Create required folders/files and add a root README.md")
    return rr


def check_r02_prompt_filenames(scan: PackScan) -> RuleResult:
    bad: List[str] = []
    for p in scan.prompt_files:
        if not KebabPromptRegex.match(p.name):
            bad.append(str(p.relative_to(scan.root)))
    rr = RuleResult(id="R02", title="Prompt Filenames (kebab, 3-4 words)", passed=len(bad) == 0)
    if bad:
        rr.details.extend([f"Non-compliant filename: {b}" for b in bad])
        rr.recommendations.append("Rename to verb-entity(-complement)(-extra).md with 3-4 tokens, lowercase")
    return rr


def check_r03_docs(scan: PackScan) -> RuleResult:
    title = "Docs Structure"
    details: List[str] = []
    # Require docs/README.md
    if not scan.docs_dir or not (scan.docs_dir / "README.md").is_file():
        details.append("Missing docs/README.md for the competency pack")

    # For each manifest entry, require docs/<prompt-stem>/{description.md,tutorial.md}
    missing_per_entry: List[str] = []
    for ep in scan.entry_points:
        f = ep.get("file")
        if not isinstance(f, str) or not f.endswith(".md"):
            # skip invalid or non-md
            continue
        stem = Path(f).stem
        entry_dir = (scan.docs_dir / stem) if scan.docs_dir else None
        if not entry_dir or not entry_dir.is_dir():
            missing_per_entry.append(f"docs/{stem}/ (folder missing)")
            continue
        if not (entry_dir / "description.md").is_file():
            missing_per_entry.append(f"docs/{stem}/description.md")
        if not (entry_dir / "tutorial.md").is_file():
            missing_per_entry.append(f"docs/{stem}/tutorial.md")

    if missing_per_entry:
        details.extend([f"Missing: {m}" for m in missing_per_entry])

    passed = len(details) == 0
    rr = RuleResult(id="R03", title=title, passed=passed)
    rr.details.extend(details)
    if not passed:
        rr.recommendations.append("Add docs/README.md and per-entry docs/<prompt-stem>/{description.md,tutorial.md}")
    return rr


def check_r04_manifest(scan: PackScan) -> RuleResult:
    if not scan.manifest_path:
        return RuleResult(id="R04", title="Manifest Presence & Format", passed=False, details=["No manifest found"], recommendations=["Add manifest.json with required fields"]) 
    manifest, err = load_manifest(scan.manifest_path)
    if err:
        return RuleResult(id="R04", title="Manifest Presence & Format", passed=False, details=[err], recommendations=["Fix JSON syntax"]) 
    required_fields = ["id", "name", "version", "description", "entry_points"]
    missing = [f for f in required_fields if f not in manifest]
    ep_ok = isinstance(manifest.get("entry_points"), list)
    passed = (len(missing) == 0) and ep_ok
    rr = RuleResult(id="R04", title="Manifest Presence & Format", passed=passed)
    if missing:
        rr.details.append("Missing fields: " + ", ".join(missing))
    if not ep_ok:
        rr.details.append("entry_points must be a list")
    if not passed:
        rr.recommendations.append("Align manifest with competency-manifest-template.json")
    return rr


def manifest_entry_paths(scan: PackScan) -> Set[Path]:
    eps: Set[Path] = set()
    for ep in scan.entry_points:
        f = ep.get("file")
        if isinstance(f, str):
            p = (scan.root / f).resolve()
            try:
                eps.add(p)
            except Exception:
                continue
    return eps


def check_r05_entry_points_coverage(scan: PackScan) -> RuleResult:
    cats = classify_prompts(scan.prompt_files, scan.root)
    ep_paths = manifest_entry_paths(scan)
    missing: List[str] = []

    def rel(p: Path) -> str:
        try:
            return str(p.relative_to(scan.root))
        except Exception:
            return str(p)

    if cats["orchestrator"] or cats["workflow"]:
        for p in cats["orchestrator"] + cats["workflow"]:
            if p.resolve() not in ep_paths:
                missing.append(rel(p))
    else:
        for p in scan.prompt_files:
            if p.resolve() not in ep_paths:
                missing.append(rel(p))

    rr = RuleResult(id="R05", title="Entry Points Coverage", passed=len(missing) == 0)
    if missing:
        rr.details.extend([f"Not in manifest.entry_points: {m}" for m in missing])
        rr.recommendations.append("Add missing files to manifest.entry_points or adjust classification")
    return rr


def read_file_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def check_r06_templates_referenced(scan: PackScan) -> RuleResult:
    # If there is no templates dir/files, pass this rule (no templates to enforce)
    if not scan.templates_dir:
        return RuleResult(id="R06", title="Templates Referenced", passed=True)

    text_cache: Dict[Path, str] = {p: read_file_text(p) for p in scan.prompt_files}

    # 1) Unreferenced templates in templates/
    unreferenced: List[str] = []
    template_rel_paths = []
    template_names = set()
    for tf in scan.template_files:
        rel = str(tf.relative_to(scan.root))
        template_rel_paths.append(rel)
        template_names.add(tf.name)
        found = any(tf.name in txt for txt in text_cache.values())
        if not found:
            unreferenced.append(rel)

    # 2) Referenced templates in prompts must exist under templates/
    missing_refs: List[str] = []
    templates_dir = scan.templates_dir
    ref_pattern = re.compile(r"templates/([A-Za-z0-9_\-./]+\.md)")
    for p, txt in text_cache.items():
        for m in ref_pattern.finditer(txt):
            ref_rel = m.group(1)  # may contain subfolders relative to templates/
            candidate = (templates_dir / ref_rel).resolve()
            if not candidate.is_file():
                # report relative to pack root for clarity
                missing_refs.append(f"Missing referenced template in prompt {p.relative_to(scan.root)}: templates/{ref_rel}")

    passed = (len(unreferenced) == 0) and (len(missing_refs) == 0)
    rr = RuleResult(id="R06", title="Templates Referenced", passed=passed)
    if unreferenced:
        rr.details.extend([f"Unreferenced template: {m}" for m in unreferenced])
    if missing_refs:
        rr.details.extend(missing_refs)
    if not passed:
        rr.recommendations.append("Ensure templates referenced in prompts exist under templates/, and reference all templates from prompts")
    return rr


def parse_frontmatter(text: str) -> Dict[str, object]:
    # very simple YAML-ish frontmatter parser for keys we care about
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    header = text[3:end]
    meta: Dict[str, object] = {}
    for line in header.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def check_r07_prompt_template_compliance(scan: PackScan) -> RuleResult:
    missing: List[str] = []
    for p in scan.prompt_files:
        meta = parse_frontmatter(read_file_text(p))
        required = ["name", "description", "tags"]
        miss = [k for k in required if k not in meta or not meta.get(k)]
        if miss:
            missing.append(f"{p.relative_to(scan.root)} missing: {', '.join(miss)}")
    rr = RuleResult(id="R07", title="Prompt Template Compliance (basic)", passed=len(missing) == 0)
    if missing:
        rr.details.extend(missing)
        rr.recommendations.append("Ensure YAML frontmatter includes at least name, description, tags")
    return rr


def check_r08_tools_referenced(scan: PackScan) -> RuleResult:
    if not scan.tool_files:
        return RuleResult(id="R08", title="Tools Referenced", passed=True)
    text_cache: Dict[Path, str] = {p: read_file_text(p) for p in scan.prompt_files}
    missing: List[str] = []
    for tf in scan.tool_files:
        if tf.suffix.lower() == ".md":
            continue  # ignore markdown files in tools/
        fname = tf.name
        found = any(fname in txt for txt in text_cache.values())
        if not found:
            missing.append(str(tf.relative_to(scan.root)))
    rr = RuleResult(id="R08", title="Tools Referenced", passed=len(missing) == 0)
    if missing:
        rr.details.extend([f"Unreferenced tool: {m}" for m in missing])
        rr.recommendations.append("Reference tools in prompts by filename/path where used")
    return rr


def check_r09_entry_paths_exist(scan: PackScan) -> RuleResult:
    missing: List[str] = []
    for ep in scan.entry_points:
        f = ep.get("file")
        if not isinstance(f, str):
            missing.append("entry point missing 'file' string")
            continue
        p = scan.root / f
        if not p.is_file():
            missing.append(f"Missing prompt file for entry point: {f}")
    rr = RuleResult(id="R09", title="Entry Points Valid Paths", passed=len(missing) == 0)
    if missing:
        rr.details.extend(missing)
        rr.recommendations.append("Fix entry_points file paths to point to existing prompts/*.md")
    return rr


def check_r10_alias_protocol_sanity(scan: PackScan) -> RuleResult:
    problems: List[str] = []
    for ep in scan.entry_points:
        if not ep.get("id"):
            problems.append("entry_point missing id")
        if not ep.get("description"):
            problems.append(f"entry_point '{ep.get('id','<no id>')}' missing description")
        proto = ep.get("protocol")
        if proto not in ALLOWED_PROTOCOLS:
            problems.append(f"entry_point '{ep.get('id','<no id>')}' invalid protocol: {proto}")
    rr = RuleResult(id="R10", title="Aliases & Protocol Sanity", passed=len(problems) == 0)
    if problems:
        rr.details.extend(problems)
        rr.recommendations.append("Provide id, description and a valid protocol for each entry point")
    return rr


def build_result(scan: PackScan, rules: List[RuleResult], cats: Dict[str, List[Path]]):
    total_prompts = len(scan.prompt_files)
    n_orch = len(cats["orchestrator"]) 
    n_wf = len(cats["workflow"]) 
    n_typ = len(cats["typical"]) 
    n_entry = len(scan.entry_points)
    return {
        "pack": scan.root.name,
        "root": str(scan.root),
        "counts": {
            "prompts": total_prompts,
            "orchestrator": n_orch,
            "workflows": n_wf,
            "typical": n_typ,
            "entry_points": n_entry,
        },
        "rules": [
            {
                "id": r.id,
                "title": r.title,
                "passed": r.passed,
                "details": r.details,
                "recommendations": r.recommendations,
            } for r in rules
        ]
    }


def print_markdown(result: dict):
    print(f"# Competency Pack Validation Report: {result['pack']}")
    print()
    print(f"Root: {result['root']}")
    c = result["counts"]
    print(f"Prompts: {c['prompts']} (orchestrator={c['orchestrator']}, workflows={c['workflows']}, typical={c['typical']})")
    print(f"Manifest entry_points: {c['entry_points']}")
    print()
    print("## Results")
    for r in result["rules"]:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"- [{status}] {r['id']} - {r['title']}")
        for d in r["details"]:
            print(f"  - {d}")
        if r["recommendations"]:
            print("  - Recommendation(s):")
            for rec in r["recommendations"]:
                print(f"    - {rec}")
    print()
    passed = sum(1 for r in result["rules"] if r["passed"]) 
    print(f"Overall: {passed}/{len(result['rules'])} rules passed")


def main():
    parser = argparse.ArgumentParser(description="Validate an OLAF competency pack against structural and manifest rules")
    parser.add_argument("path", help="Path to competency pack root")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON report")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"Error: path is not a directory: {root}", file=sys.stderr)
        sys.exit(2)

    scan = scan_pack(root)
    cats = classify_prompts(scan.prompt_files, root)

    rules = [
        check_r01_structure(scan),
        check_r02_prompt_filenames(scan),
        check_r03_docs(scan),
        check_r04_manifest(scan),
        check_r05_entry_points_coverage(scan),
        check_r06_templates_referenced(scan),
        check_r07_prompt_template_compliance(scan),
        check_r08_tools_referenced(scan),
        check_r09_entry_paths_exist(scan),
        check_r10_alias_protocol_sanity(scan),
    ]

    result = build_result(scan, rules, cats)

    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print_markdown(result)

    # exit code 1 if any rule failed
    if any(not r.passed for r in rules):
        sys.exit(1)


if __name__ == "__main__":
    main()
