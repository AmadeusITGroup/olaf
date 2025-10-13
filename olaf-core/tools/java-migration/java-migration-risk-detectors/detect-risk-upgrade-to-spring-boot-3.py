#!/usr/bin/env python3
"""
Detect Risks for Upgrading to Spring Boot 3.x

Refactored to reuse common utilities from migration_common to avoid duplication.

Usage:
  python detect-risk-upgrade-to-spring-boot-3.py [/path/to/maven-project]
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
    # Shared reusable rules
    apply_rule_junit,
    apply_rule_cloud,
    apply_rule_servlet_scope,
    apply_rule_flyway_liquibase,
    apply_rule_pinned_core_libs,
)


class Boot3UpgradeRiskDetector:
    def __init__(self, project_path: str = ".", scan_sources: bool = False):
        self.project_path = project_path
        self.scan_sources = scan_sources

        # javax groups frequently needing Jakarta migration
        self.javax_groups = (
            "javax.servlet",
            "javax.persistence",
            "javax.annotation",
            "javax.validation",
            "javax.xml.bind",
            "javax.activation",
            "javax.mail",
            "javax.transaction",
            "javax.ws.rs",
            "javax.faces",
            "javax.enterprise",
            "javax.jws",
            "javax.json",
        )

    def analyze(self) -> Dict:
        results: Dict = {
            "errors": [],
            "summary": {},
            "parent_version": None,
            "java_version_risks": [],
            "javax_usage": [],
            "jakarta_migration_risks": [],
            "security_risks": [],
            "testing_risks": [],
            "cloud_compat_risks": [],
            "orm_risks": [],
            "doc_api_risks": [],
            "server_risks": [],
            "version_alignment_risks": [],
            "web_research": [],
            "logging_risks": [],
            "source_scan": [],
            "api_changes": [],
        }

        root = parse_pom(self.project_path)
        if root is None:
            results["errors"].append("pom.xml not found")
            return results

        # Parent Spring Boot version should be 3.x
        parent_version = get_parent_version(root)
        results["parent_version"] = parent_version
        if parent_version and not parent_version.startswith("3."):
            results["version_alignment_risks"].append({
                "risk": "Parent not aligned to Boot 3.x",
                "detail": f"Parent is {parent_version}",
                "action": "Align parent to Spring Boot 3.x (and Framework 6.x)",
            })

        # Java version checks: Boot 3 requires Java 17+
        raw_java, java_major = get_effective_java(root)
        if java_major is None:
            results["java_version_risks"].append({
                "risk": "Java version not specified or unrecognized",
                "detail": f"Value: {raw_java}",
                "action": "Specify Java 17+ in properties or compiler plugin",
            })
        else:
            if java_major < 17:
                results["java_version_risks"].append({
                    "risk": "Java < 17 not supported by Boot 3",
                    "detail": f"Detected Java {raw_java}",
                    "action": "Upgrade to Java 17 or higher",
                })

        # Dependencies scan
        # Track testing libs presence for optional source-scan hints
        has_junit_jupiter = False
        has_mockito_core = False
        has_mockito_junit_jupiter = False

        has_springfox = False
        has_javax_servlet_dep = False
        has_jakarta_servlet_dep = False
        for gid, aid, ver, dep_el in iter_dependencies(root):
            # javax usage
            if any(gid.startswith(jx) for jx in self.javax_groups):
                results["javax_usage"].append({
                    "dependency": f"{gid}:{aid}:{ver}",
                    "risk": "javax dependency incompatible with Jakarta (Boot 3)",
                    "action": "Find Jakarta EE replacement (jakarta.* group or equivalent)",
                })
                if aid:
                    results["web_research"].append({
                        "dependency": f"{gid}:{aid}:{ver}",
                        "reason": "Likely Jakarta namespace migration required",
                        "search": f'"{aid}" "jakarta" "spring boot 3" compatibility',
                    })

            # Spring Cloud compatibility handled by shared rule later

            # Springfox incompatible; suggest SpringDoc starter
            if gid == "io.springfox":
                results["doc_api_risks"].append({
                    "risk": "Springfox incompatible with Spring Boot 3",
                    "detail": f"Detected {gid}:{aid}:{ver}",
                    "action": "Migrate to org.springdoc:springdoc-openapi-starter-webmvc-ui (or webflux)",
                })
                has_springfox = True

            # Testing libs presence (detailed checks via shared rule later)
            if gid.startswith("org.junit.jupiter"):
                has_junit_jupiter = True
            if gid == "org.mockito" and aid == "mockito-core":
                has_mockito_core = True
            if gid == "org.mockito" and aid == "mockito-junit-jupiter":
                has_mockito_junit_jupiter = True

            # ORM / Validation compatibility
            if gid == "org.hibernate" and aid == "hibernate-core" and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (6, 0, 0):
                    results["orm_risks"].append({
                        "risk": "Hibernate < 6 incompatible with Jakarta Persistence 3",
                        "detail": f"Detected {gid}:{aid}:{ver}",
                        "action": "Upgrade to Hibernate 6.x and adjust APIs/mappings as needed",
                    })
            if gid == "org.hibernate.validator" and aid == "hibernate-validator" and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (7, 0, 0):
                    results["orm_risks"].append({
                        "risk": "Hibernate Validator < 7 uses javax.validation",
                        "detail": f"Detected {gid}:{aid}:{ver}",
                        "action": "Upgrade to 7.x+ for jakarta.validation",
                    })
            if gid == "javax.validation" and aid == "validation-api":
                results["orm_risks"].append({
                    "risk": "javax.validation API present",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Replace with jakarta.validation:jakarta.validation-api",
                })
            if gid == "javax.xml.bind" and aid == "jaxb-api":
                results["version_alignment_risks"].append({
                    "risk": "JAXB javax API present",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Use jakarta.xml.bind:jakarta.xml.bind-api",
                })
            if gid == "com.fasterxml.jackson.module" and aid == "jackson-module-jaxb-annotations":
                results["version_alignment_risks"].append({
                    "risk": "Jackson JAXB module depends on javax",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Remove or replace with Jakarta-friendly approach",
                })

            # Explicit servlet container versions must be Jakarta-ready
            if gid == "org.apache.tomcat":
                if ver:
                    from migration_common import parse_semver
                    sv = parse_semver(ver)
                    if sv and sv < (10, 1, 0):
                        results["server_risks"].append({
                            "risk": "Tomcat < 10.1 not Jakarta ready",
                            "detail": f"{gid}:{aid}:{ver}",
                            "action": "Use Tomcat 10.1+ (Servlet 6)",
                        })
            if gid == "org.eclipse.jetty":
                if ver:
                    from migration_common import parse_semver
                    sv = parse_semver(ver)
                    if sv and sv < (11, 0, 0):
                        results["server_risks"].append({
                            "risk": "Jetty < 11 not Jakarta ready",
                            "detail": f"{gid}:{aid}:{ver}",
                            "action": "Use Jetty 11+",
                        })

            # Track servlet API type to detect mixed javax/jakarta
            if gid.startswith("javax.servlet"):
                has_javax_servlet_dep = True
            if gid.startswith("jakarta.servlet"):
                has_jakarta_servlet_dep = True

            # Pinned core libs may conflict with Boot 3 managed versions
            if gid in ("com.fasterxml.jackson.core", "io.projectreactor", "io.netty") and ver:
                results["version_alignment_risks"].append({
                    "risk": "Pinned dependency version may conflict with Boot 3 BOM",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Prefer versions managed by Spring Boot 3 or align to its BOM",
                })

            # Logging: Log4j 1.x
            if gid == "log4j" and aid == "log4j" and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (2, 0, 0):
                    results["logging_risks"].append({
                        "risk": "Log4j 1.x detected",
                        "detail": f"{gid}:{aid}:{ver}",
                        "action": "Remove/migrate to Boot default (Logback) or Log4j2",
                    })

            # Flyway/Liquibase versions
            if gid == "org.flywaydb" and aid == "flyway-core" and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (9, 0, 0):
                    results["version_alignment_risks"].append({
                        "risk": "Flyway < 9 may not align with Boot 3",
                        "detail": f"{gid}:{aid}:{ver}",
                        "action": "Upgrade Flyway to 9.x+",
                    })
            if gid == "org.liquibase" and aid == "liquibase-core" and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (4, 15, 0):
                    results["version_alignment_risks"].append({
                        "risk": "Liquibase version may be too old for Boot 3",
                        "detail": f"{gid}:{aid}:{ver}",
                        "action": "Upgrade Liquibase to a version aligned with Boot 3 BOM",
                    })

            # Legacy Spring Security OAuth artifacts
            if gid.startswith("org.springframework.security.oauth"):
                results["security_risks"].append({
                    "risk": "Legacy Spring Security OAuth detected",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Migrate to spring-security-oauth2-* (client/resource-server) or Spring Authorization Server",
                })

            # Jersey / JAX-RS Jakarta migration
            if gid.startswith("org.glassfish.jersey") and ver:
                from migration_common import parse_semver
                sv = parse_semver(ver)
                if sv and sv < (3, 0, 0):
                    results["version_alignment_risks"].append({
                        "risk": "Jersey < 3 uses javax.ws.rs",
                        "detail": f"{gid}:{aid}:{ver}",
                        "action": "Upgrade to Jersey 3.x (Jakarta)",
                    })
            if gid == "javax.ws.rs":
                results["version_alignment_risks"].append({
                    "risk": "javax.ws.rs API present",
                    "detail": f"{gid}:{aid}:{ver}",
                    "action": "Move to jakarta.ws.rs API and Jersey 3.x",
                })

            # Servlet API scope handled by shared rule later

        # Apply shared reusable rules (no behavior change intended)
        apply_rule_cloud(root, results, expected_prefix="2022.")
        apply_rule_junit(root, results, min_surefire="3.0.0")
        apply_rule_servlet_scope(root, results)
        apply_rule_flyway_liquibase(root, results, min_flyway="9.0.0", min_liquibase="4.15.0")
        apply_rule_pinned_core_libs(
            root,
            results,
            gids=(
                "com.fasterxml.jackson.core",
                "io.projectreactor",
                "io.netty",
            ),
        )

        # Surefire/Failsafe plugin checks handled by apply_rule_junit

        # Optional source/config scans
        if self.scan_sources:
            from migration_common import grep_sources_count, read_app_config_texts
            # javax imports count
            javax_count = grep_sources_count(self.project_path, r"\bimport\s+javax\.")
            if javax_count:
                results["source_scan"].append({
                    "risk": "Source imports javax.*",
                    "detail": f"Occurrences: {javax_count}",
                    "action": "Migrate imports to jakarta.*",
                })
            # CronSequenceGenerator removal -> use CronExpression
            cron_seq = grep_sources_count(self.project_path, r"\bCronSequenceGenerator\b")
            if cron_seq:
                results["api_changes"].append({
                    "risk": "CronSequenceGenerator removed in Spring Boot 3.x",
                    "detail": f"Occurrences in code: {cron_seq}",
                    "action": "Replace with org.springframework.scheduling.support.CronExpression",
                })
            # JUnit 4 imports
            j4_count = grep_sources_count(self.project_path, r"\bimport\s+org\.junit\.Test\b")
            if j4_count:
                results["testing_risks"].append({
                    "risk": "JUnit 4 imports in source",
                    "detail": f"Occurrences: {j4_count}",
                    "action": "Replace with JUnit 5 and Jupiter annotations",
                })
            # MockitoExtension usage
            mock_ext = grep_sources_count(self.project_path, r"@ExtendWith\(\s*MockitoExtension\.class\s*\)")
            if has_mockito_core and has_junit_jupiter and not has_mockito_junit_jupiter and mock_ext == 0:
                results["testing_risks"].append({
                    "risk": "MockitoExtension not found in tests",
                    "detail": "No @ExtendWith(MockitoExtension.class) detected",
                    "action": "Add mockito-junit-jupiter and annotate tests",
                })
            # WebSecurityConfigurerAdapter usage
            wsca = grep_sources_count(self.project_path, r"\bWebSecurityConfigurerAdapter\b")
            if wsca:
                results["security_risks"].append({
                    "risk": "WebSecurityConfigurerAdapter removed in Spring Security 6",
                    "detail": f"Occurrences: {wsca}",
                    "action": "Migrate to SecurityFilterChain bean configuration",
                })
            # Config property for path matching (mostly for Springfox context)
            if has_springfox:
                texts = read_app_config_texts(self.project_path)
                has_prop = any("spring.mvc.pathmatch.matching-strategy" in t for t in texts)
                if not has_prop:
                    results["doc_api_risks"].append({
                        "risk": "Springfox present without pathmatch workaround",
                        "detail": "spring.mvc.pathmatch.matching-strategy not found in application config",
                        "action": "Add spring.mvc.pathmatch.matching-strategy=ant_path_matcher (temporary)",
                    })
            # HttpStatus vs HttpStatusCode signal (informational)
            hs_count = grep_sources_count(self.project_path, r"\bHttpStatus\b")
            hsc_count = grep_sources_count(self.project_path, r"\bHttpStatusCode\b")
            if hsc_count > 0 and hs_count > 0:
                results["api_changes"].append({
                    "risk": "Mixed HttpStatus and HttpStatusCode usages",
                    "detail": f"HttpStatus: {hs_count}, HttpStatusCode: {hsc_count}",
                    "action": "Review method signatures in Spring Framework 6 for HttpStatusCode returns",
                })

        # Summary
        results["summary"] = {
            "parent": parent_version or "unknown",
            "java": raw_java or "unspecified",
            "counts": {
                "java_version_risks": len(results["java_version_risks"]),
                "javax_usage": len(results["javax_usage"]),
                "cloud_compat_risks": len(results["cloud_compat_risks"]),
                "doc_api_risks": len(results["doc_api_risks"]),
                "testing_risks": len(results["testing_risks"]),
                "orm_risks": len(results["orm_risks"]),
                "server_risks": len(results["server_risks"]),
                "version_alignment_risks": len(results["version_alignment_risks"]),
                "web_research": len(results["web_research"]),
                "logging_risks": len(results["logging_risks"]),
                "source_scan": len(results["source_scan"]),
                "api_changes": len(results["api_changes"]),
            },
        }
        # Mixed servlet API detection (pom-level)
        if has_javax_servlet_dep and has_jakarta_servlet_dep:
            results["logging_risks"].append({
                "risk": "Both javax.servlet and jakarta.servlet dependencies present",
                "detail": "Mixed servlet APIs can cause linkage errors",
                "action": "Remove javax.servlet artifacts; ensure all libraries are Jakarta-compatible",
            })
        return results

    def report(self, r: Dict) -> None:
        printer = ReportPrinter("🔍 Spring Boot 3.x Upgrade Risk Report")
        printer.header()
        if r.get("errors"):
            for e in r["errors"]:
                print(f"❌ {e}")
            return
        summary = r.get("summary", {})
        print(f"Parent: {summary.get('parent')}  |  Java: {summary.get('java')}")
        printer.counts(summary.get("counts", {}))

        def dump(title: str, items: List[Dict]):
            printer.dump(title, items, limit=6)

        dump("Java Version Risks", r["java_version_risks"])
        dump("javax Usage (Jakarta Migration)", r["javax_usage"])
        dump("Spring Cloud Compatibility", r["cloud_compat_risks"])
        dump("API Documentation (Swagger) Risks", r["doc_api_risks"])
        dump("Testing Risks", r["testing_risks"])
        dump("ORM / Validation Risks", r["orm_risks"])
        dump("Servlet Container Risks", r["server_risks"])
        dump("Version Alignment Risks", r["version_alignment_risks"])

        printer.dump("Suggested Web Research", r["web_research"], limit=6)
        dump("Logging Risks", r["logging_risks"])
        dump("API Changes (source)", r["api_changes"]) 
        dump("Source Scan Findings", r["source_scan"]) 
        print("\n" + "=" * 80)


def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    detector = Boot3UpgradeRiskDetector(project_path)
    results = detector.analyze()
    detector.report(results)


if __name__ == "__main__":
    main()
