#!/usr/bin/env python3
"""
Detect Risks for Upgrading to Spring Boot 2.7.x

Refactored to reuse common utilities from migration_common to avoid duplication.

Usage:
  python detect-risk-upgrade-to-spring-boot-2-7.py [/path/to/maven-project]
"""
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Ensure we can import sibling module when run as a script
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from migration_common import (
    ReportPrinter,
    get_effective_java,
    get_parent_version,
    iter_dependencies,
    parse_pom,
    is_version_lt,
    apply_rule_junit,
    apply_rule_cloud,
    apply_rule_servlet_scope,
    apply_rule_flyway_liquibase,
    apply_rule_pinned_core_libs,
)


class Boot27UpgradeRiskDetector:
    def __init__(self, project_path: str = ".", scan_sources: bool = False):
        self.project_path = project_path
        self.scan_sources = scan_sources

    def analyze(self) -> Dict:
        results: Dict = {
            "errors": [],
            "summary": {},
            "java_version_risks": [],
            "parent_version": None,
            "cloud_compat_risks": [],
            "doc_api_risks": [],
            "testing_risks": [],
            "security_risks": [],
            "version_alignment_risks": [],
            "server_risks": [],
        }

        root = parse_pom(self.project_path)
        if root is None:
            results["errors"].append("pom.xml not found")
            return results

        # Parent Spring Boot version
        parent_version = get_parent_version(root)
        results["parent_version"] = parent_version
        if parent_version:
            if parent_version.startswith("2."):
                # Warn if far behind 2.7 (use semver compare)
                lt_26 = is_version_lt(parent_version, "2.6.0")
                if lt_26 is True:
                    results["version_alignment_risks"].append({
                        "risk": "Old Spring Boot parent",
                        "detail": f"Current parent {parent_version}. Consider stepping to 2.7.x first.",
                        "action": "Plan intermediate upgrades and review release notes for 2.6 and 2.7",
                    })
            else:
                results["version_alignment_risks"].append({
                    "risk": "Non-2.x parent when targeting 2.7",
                    "detail": f"Parent is {parent_version}",
                    "action": "Align parent to Spring Boot 2.7.x for this step",
                })

        # Java version checks
        raw_java, java_major = get_effective_java(root)
        if java_major is None:
            results["java_version_risks"].append({
                "risk": "Java version not specified or unrecognized",
                "detail": f"Value: {raw_java}",
                "action": "Specify java.version or compiler source/target",
            })
        else:
            if java_major < 8:
                results["java_version_risks"].append({
                    "risk": "Java < 8 not supported",
                    "detail": f"Detected Java {raw_java}",
                    "action": "Upgrade to Java 11 or 17",
                })
            elif java_major in (8, 11):
                results["java_version_risks"].append({
                    "risk": "Using older Java",
                    "detail": f"Detected Java {raw_java}",
                    "action": "Consider Java 17 to ease later Boot 3 upgrade",
                })

        # Apply shared rules
        apply_rule_cloud(root, results, expected_prefix="2021.")
        apply_rule_junit(root, results, min_surefire="2.22.0")
        apply_rule_servlet_scope(root, results)
        apply_rule_flyway_liquibase(root, results, min_flyway="8.0.0", min_liquibase=None)
        apply_rule_pinned_core_libs(
            root,
            results,
            gids=(
                "com.fasterxml.jackson.core",
                "io.projectreactor",
                "io.netty",
                "org.hibernate.validator",
                "org.hibernate",
            ),
        )

        # Springfox breaks with Boot 2.6/2.7 default path matching
        has_springfox = False
        for gid, aid, ver, _dep in iter_dependencies(root):
            if gid == "io.springfox":
                results["doc_api_risks"].append({
                    "risk": "Springfox compatibility issues with Boot 2.6/2.7",
                    "detail": f"Detected {gid}:{aid}:{ver}",
                    "action": "Migrate to org.springdoc starters or set spring.mvc.pathmatch.matching-strategy=ant_path_matcher as workaround",
                })
                has_springfox = True

        # Optional source/config scans
        if self.scan_sources:
            from migration_common import grep_sources_count, read_app_config_texts

            # JUnit 4 imports
            j4_count = grep_sources_count(self.project_path, r"\bimport\s+org\.junit\.Test\b")
            if j4_count:
                results["testing_risks"].append({
                    "risk": "JUnit 4 imports in source",
                    "detail": f"Occurrences: {j4_count}",
                    "action": "Replace with JUnit 5 (Jupiter) to ease later Boot 3 upgrade",
                })

            # MockitoExtension usage hint when migrating tests to JUnit 5
            # Determine presence of junit-jupiter, mockito-core, mockito-junit-jupiter
            has_junit_jupiter = False
            has_mockito_core = False
            has_mockito_junit_jupiter = False
            for gid, aid, ver, _dep in iter_dependencies(root):
                if gid.startswith("org.junit.jupiter"):
                    has_junit_jupiter = True
                if gid == "org.mockito" and aid == "mockito-core":
                    has_mockito_core = True
                if gid == "org.mockito" and aid == "mockito-junit-jupiter":
                    has_mockito_junit_jupiter = True
            mock_ext = grep_sources_count(self.project_path, r"@ExtendWith\(\s*MockitoExtension\.class\s*\)")
            if has_mockito_core and has_junit_jupiter and not has_mockito_junit_jupiter and mock_ext == 0:
                results["testing_risks"].append({
                    "risk": "MockitoExtension not found in tests",
                    "detail": "No @ExtendWith(MockitoExtension.class) detected",
                    "action": "Add mockito-junit-jupiter and annotate tests (for JUnit 5)",
                })

            # WebSecurityConfigurerAdapter usage (deprecated in 5.7, removed in 6)
            wsca = grep_sources_count(self.project_path, r"\bWebSecurityConfigurerAdapter\b")
            if wsca:
                results["security_risks"].append({
                    "risk": "WebSecurityConfigurerAdapter deprecated (5.7) and removed in Spring Security 6",
                    "detail": f"Occurrences: {wsca}",
                    "action": "Consider migrating to SecurityFilterChain bean to reduce Boot 3 friction",
                })

            # Springfox path-match property presence
            if has_springfox:
                texts = read_app_config_texts(self.project_path)
                has_prop = any("spring.mvc.pathmatch.matching-strategy" in t for t in texts)
                if not has_prop:
                    results["doc_api_risks"].append({
                        "risk": "Springfox present without pathmatch workaround",
                        "detail": "spring.mvc.pathmatch.matching-strategy not found in application config",
                        "action": "Add spring.mvc.pathmatch.matching-strategy=ant_path_matcher (temporary)",
                    })

        # Summary
        results["summary"] = {
            "parent": parent_version or "unknown",
            "java": raw_java or "unspecified",
            "counts": {
                "java_version_risks": len(results["java_version_risks"]),
                "cloud_compat_risks": len(results["cloud_compat_risks"]),
                "doc_api_risks": len(results["doc_api_risks"]),
                "testing_risks": len(results["testing_risks"]),
                "version_alignment_risks": len(results["version_alignment_risks"]),
                "server_risks": len(results["server_risks"]),
            },
        }
        return results

    def report(self, r: Dict) -> None:
        printer = ReportPrinter("🔍 Spring Boot 2.7 Upgrade Risk Report")
        printer.header()
        if r.get("errors"):
            for e in r["errors"]:
                print(f"❌ {e}")
            return
        summary = r.get("summary", {})
        print(f"Parent: {summary.get('parent')}  |  Java: {summary.get('java')}")
        printer.counts(summary.get("counts", {}))
        printer.dump("Java Version Risks", r["java_version_risks"], limit=5)
        printer.dump("Spring Cloud Compatibility", r["cloud_compat_risks"], limit=5)
        printer.dump("API Documentation (Swagger) Risks", r["doc_api_risks"], limit=5)
        printer.dump("Testing Risks", r["testing_risks"], limit=5)
        printer.dump("Version Alignment Risks", r["version_alignment_risks"], limit=5)
        printer.dump("Servlet Container Risks", r["server_risks"], limit=5)
        print("\n" + "=" * 80)


def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    detector = Boot27UpgradeRiskDetector(project_path)
    results = detector.analyze()
    detector.report(results)


if __name__ == "__main__":
    main()
