#!/usr/bin/env python3
"""
Common utilities for Spring Boot migration analyzers.
Provides POM parsing helpers, semantic version comparison, and report printing.
"""
from __future__ import annotations
import os
import re
from pathlib import Path
from typing import Dict, Iterable, Iterator, Optional, Tuple, List
import xml.etree.ElementTree as ET

# Maven POM namespace
NS: Dict[str, str] = {"maven": "http://maven.apache.org/POM/4.0.0"}


# -----------------------------
# Internal helpers
# -----------------------------
def _text(el: Optional[ET.Element]) -> Optional[str]:
    return el.text.strip() if el is not None and el.text else None


# -----------------------------
# POM helpers
# -----------------------------

def parse_pom(project_path: str | Path) -> Optional[ET.Element]:
    path = Path(project_path) / "pom.xml"
    if not path.exists():
        return None
    tree = ET.parse(path)
    return tree.getroot()


def get_parent_version(root: ET.Element) -> Optional[str]:
    el = root.find("./maven:parent/maven:version", NS)
    return el.text.strip() if el is not None and el.text else None


# -----------------------------
# Source/config scanning helpers
# -----------------------------
def iter_source_files(project_path: str | Path, exts: Tuple[str, ...] = (".java",)) -> Iterator[Path]:
    root = Path(project_path)
    src_dir = root / "src"
    if not src_dir.exists():
        return iter(())
    for dirpath, _dirnames, filenames in os.walk(src_dir):
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in exts:
                yield p


def grep_sources_count(project_path: str | Path, pattern: str) -> int:
    """Return count of lines matching regex pattern across Java sources."""
    rx = re.compile(pattern)
    count = 0
    for fp in iter_source_files(project_path):
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        count += len(rx.findall(text))
    return count


def read_app_config_texts(project_path: str | Path) -> List[str]:
    root = Path(project_path)
    patterns = [
        root / "src" / "main" / "resources" / "application.properties",
        root / "src" / "main" / "resources" / "application.yaml",
        root / "src" / "main" / "resources" / "application.yml",
    ]
    texts: List[str] = []
    for p in patterns:
        if p.exists():
            try:
                texts.append(p.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                pass
    return texts


def get_properties(root: ET.Element) -> ET.Element:
    props = root.find("./maven:properties", NS)
    return props if props is not None else ET.Element("properties")


def get_property(root: ET.Element, name: str) -> Optional[str]:
    props = get_properties(root)
    # names in POM use the same namespace prefix
    el = props.find(f"maven:{name}", NS)
    return el.text.strip() if el is not None and el.text else None


def iter_dependencies(root: ET.Element) -> Iterator[Tuple[str, str, str, ET.Element]]:
    for dep in root.findall(".//maven:dependency", NS):
        gid = _text(dep.find("maven:groupId", NS)) or ""
        aid = _text(dep.find("maven:artifactId", NS)) or ""
        ver = _text(dep.find("maven:version", NS)) or ""
        yield gid.strip(), aid.strip(), ver.strip(), dep


def iter_plugins(root: ET.Element) -> Iterator[Tuple[str, str, ET.Element]]:
    for plugin in root.findall(".//maven:plugin", NS):
        aid = _text(plugin.find("maven:artifactId", NS)) or ""
        ver = _text(plugin.find("maven:version", NS)) or ""
        yield aid.strip(), ver.strip(), plugin


def get_effective_java(root: ET.Element) -> Tuple[Optional[str], Optional[int]]:
    """Return (raw_string, numeric_major) for Java version if detectable."""
    java_version = get_property(root, "java.version")
    source = target = None
    for aid, _ver, plugin in iter_plugins(root):
        if aid == "maven-compiler-plugin":
            conf = plugin.find("maven:configuration", NS)
            if conf is not None:
                source = _text(conf.find("maven:source", NS))
                target = _text(conf.find("maven:target", NS))
    raw = java_version or source or target
    if raw is None:
        return None, None
    try:
        if raw.startswith("1."):
            num = int(raw.replace("1.", ""))
        else:
            num = int(raw)
        return raw, num
    except Exception:
        return raw, None


# -----------------------------
# SemVer helpers
# -----------------------------

def parse_semver(v: str) -> Optional[Tuple[int, int, int]]:
    if not v:
        return None
    # Strip qualifiers like -RELEASE, -SNAPSHOT, etc.
    core = v.split("-")[0]
    parts = core.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0
        return (major, minor, patch)
    except ValueError:
        return None


def is_version_lt(v: str, threshold: str) -> Optional[bool]:
    a = parse_semver(v)
    b = parse_semver(threshold)
    if a is None or b is None:
        return None
    return a < b


# -----------------------------
# Report helpers
# -----------------------------
class ReportPrinter:
    def __init__(self, title: str):
        self.title = title

    def header(self) -> None:
        print("\n" + "=" * 80)
        print(self.title)
        print("=" * 80)

    @staticmethod
    def counts(summary_counts: Dict[str, int]) -> None:
        print("\nCounts:")
        for k, v in summary_counts.items():
            print(f" - {k}: {v}")

    @staticmethod
    def dump(title: str, items: Iterable[Dict], limit: int = 6) -> None:
        items = list(items)
        if not items:
            return
        print(f"\n▶ {title}:")
        for it in items[:limit]:
            risk = it.get("risk") or ""
            print(f" - Risk: {risk}")
            for key in ("dependency", "detail", "action", "reason", "search"):
                if it.get(key):
                    label = key.capitalize()
                    print(f"   {label}: {it[key]}")


# -----------------------------
# Reusable rules
# -----------------------------

def apply_rule_junit(root: ET.Element, results: Dict, min_surefire: str) -> None:
    """Populate results['testing_risks'] with JUnit 4, Vintage, and surefire/failsafe checks.
    Also add Mockito Jupiter hint when applicable.
    """
    testing = results.setdefault("testing_risks", [])

    has_junit_jupiter = False
    has_mockito_core = False
    has_mockito_junit_jupiter = False

    for gid, aid, ver, _dep in iter_dependencies(root):
        if gid == "junit" and aid == "junit":
            testing.append({
                "risk": "Using JUnit 4",
                "detail": "junit:junit present",
                "action": "Migrate to JUnit 5 (org.junit.jupiter) and ensure surefire supports JUnit Platform",
            })
        if gid.startswith("org.junit.jupiter"):
            has_junit_jupiter = True
        if gid == "org.junit.vintage" and aid == "junit-vintage-engine":
            testing.append({
                "risk": "Vintage engine present",
                "detail": "org.junit.vintage:junit-vintage-engine",
                "action": "Remove vintage engine once migrated to JUnit 5",
            })
        if gid == "org.mockito" and aid == "mockito-core":
            has_mockito_core = True
        if gid == "org.mockito" and aid == "mockito-junit-jupiter":
            has_mockito_junit_jupiter = True

    for aid, ver, _plugin in iter_plugins(root):
        if aid in ("maven-surefire-plugin", "maven-failsafe-plugin") and ver:
            too_old = is_version_lt(ver, min_surefire)
            if too_old is True:
                testing.append({
                    "risk": f"{aid} too old for JUnit Platform",
                    "detail": f"Detected {aid}:{ver}",
                    "action": f"Upgrade to >= {min_surefire} (recommend 3.0.0+) for stable JUnit 5 support",
                })

    if has_mockito_core and has_junit_jupiter and not has_mockito_junit_jupiter:
        testing.append({
            "risk": "Mockito with JUnit 5 missing mockito-junit-jupiter",
            "detail": "org.mockito:mockito-core present without mockito-junit-jupiter",
            "action": "Add org.mockito:mockito-junit-jupiter and use @ExtendWith(MockitoExtension.class)",
        })


def apply_rule_cloud(root: ET.Element, results: Dict, expected_prefix: str) -> None:
    cloud = results.setdefault("cloud_compat_risks", [])
    for gid, aid, ver, _dep in iter_dependencies(root):
        if gid == "org.springframework.cloud":
            if ver and not ver.startswith(expected_prefix):
                cloud.append({
                    "risk": "Spring Cloud train incompatible with target Boot",
                    "detail": f"Detected {aid}:{ver}",
                    "action": f"Use Spring Cloud {expected_prefix}x aligned with target Spring Boot",
                })


def apply_rule_servlet_scope(root: ET.Element, results: Dict) -> None:
    server = results.setdefault("server_risks", [])
    for dep_el in root.findall(".//maven:dependency", NS):
        gid = _text(dep_el.find("maven:groupId", NS)) or ""
        aid = _text(dep_el.find("maven:artifactId", NS)) or ""
        ver = _text(dep_el.find("maven:version", NS)) or ""
        if gid in ("javax.servlet", "jakarta.servlet"):
            scope_el = dep_el.find("maven:scope", NS)
            scope = scope_el.text.strip() if scope_el is not None and scope_el.text else "compile"
            if scope not in ("provided", "test"):
                server.append({
                    "risk": "Servlet API should not be on compile/runtime scope",
                    "detail": f"{gid}:{aid}:{ver} scope={scope}",
                    "action": "Remove explicit servlet API or set scope to provided if needed",
                })


def apply_rule_flyway_liquibase(root: ET.Element, results: Dict, min_flyway: Optional[str], min_liquibase: Optional[str]) -> None:
    va = results.setdefault("version_alignment_risks", [])
    for gid, aid, ver, _dep in iter_dependencies(root):
        if gid == "org.flywaydb" and aid == "flyway-core" and ver and min_flyway:
            if is_version_lt(ver, min_flyway) is True:
                va.append({
                    "risk": f"Flyway < {min_flyway} may not align with target Boot",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": f"Upgrade Flyway to >= {min_flyway}",
                })
        if gid == "org.liquibase" and aid == "liquibase-core" and ver:
            if min_liquibase and is_version_lt(ver, min_liquibase) is True:
                va.append({
                    "risk": f"Liquibase < {min_liquibase} may be too old for target Boot",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": f"Upgrade Liquibase to a version aligned with target Boot BOM",
                })
            elif not min_liquibase:
                va.append({
                    "risk": "Pinned Liquibase version",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Align Liquibase with Boot-managed version to avoid conflicts",
                })


def apply_rule_pinned_core_libs(root: ET.Element, results: Dict, gids: Tuple[str, ...]) -> None:
    va = results.setdefault("version_alignment_risks", [])
    for gid, aid, ver, _dep in iter_dependencies(root):
        if gid in gids and ver:
            va.append({
                "risk": "Pinned dependency version may conflict with BOM",
                "detail": f"{gid}:{aid}:{ver}",
                "action": "Prefer versions managed by Spring Boot or align to its BOM",
            })
