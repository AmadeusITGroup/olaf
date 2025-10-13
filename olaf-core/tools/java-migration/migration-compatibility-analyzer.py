#!/usr/bin/env python3
"""
Spring Boot 3.x Migration Compatibility Analyzer

This script analyzes a Maven project for potential compatibility issues
before migrating to Spring Boot 3.x, specifically focusing on Jakarta EE
compatibility and known problematic dependencies.

Usage:
    python migration-compatibility-analyzer.py [project-path]
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re
import subprocess
import json
from typing import Dict, List, Tuple, Optional

class SpringBootMigrationAnalyzer:
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.pom_path = self.project_path / "pom.xml"
        
        # Known compatibility issues database
        self.compatibility_matrix = {
            "logback-access": {
                "max_javax_version": "1.4.99",
                "min_jakarta_version": "2.0.0",
                "issue": "Logback Access 1.4.x only supports javax.servlet, incompatible with Tomcat 10.x (Jakarta EE 9+)",
                "solution": "Upgrade to logback-access 2.0+ or disable access logging"
            },
            "javax.servlet-api": {
                "max_version": "4.0.99",
                "issue": "javax.servlet replaced by jakarta.servlet in Spring Boot 3.x",
                "solution": "Remove explicit javax.servlet-api dependency, use spring-boot-starter-web"
            },
            "hibernate-core": {
                "max_javax_version": "5.6.99",
                "min_jakarta_version": "6.0.0",
                "issue": "Hibernate 5.x uses javax.persistence, incompatible with Spring Boot 3.x",
                "solution": "Upgrade to Hibernate 6.0+ (jakarta.persistence)"
            }
        }
        
        self.spring_boot_3_tomcat = "10.1"  # Spring Boot 3.x uses Tomcat 10.1.x

    def analyze_project(self) -> Dict:
        """Perform comprehensive compatibility analysis"""
        print(f"🔍 Analyzing Spring Boot migration compatibility for: {self.project_path}")
        
        results = {
            "project_path": str(self.project_path),
            "issues": [],
            "warnings": [],
            "recommendations": [],
            "maven_analysis": {}
        }
        
        # Check if Maven project
        if not self.pom_path.exists():
            results["issues"].append({
                "severity": "ERROR",
                "category": "PROJECT_STRUCTURE", 
                "message": f"No pom.xml found at {self.pom_path}"
            })
            return results
        
        # Parse POM
        try:
            tree = ET.parse(self.pom_path)
            root = tree.getroot()
            results.update(self._analyze_pom(root))
        except ET.ParseError as e:
            results["issues"].append({
                "severity": "ERROR",
                "category": "POM_PARSING",
                "message": f"Failed to parse pom.xml: {e}"
            })
            return results
        
        # Run Maven analysis
        results["maven_analysis"] = self._run_maven_analysis()
        
        # Generate report
        self._generate_report(results)
        
        return results
    
    def _analyze_pom(self, root: ET.Element) -> Dict:
        """Analyze pom.xml for compatibility issues"""
        issues = []
        warnings = []
        recommendations = []
        
        # Define namespace
        ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}
        
        # Check Spring Boot version
        spring_boot_version = self._get_spring_boot_version(root, ns)
        if spring_boot_version:
            if spring_boot_version.startswith("2."):
                warnings.append({
                    "severity": "INFO",
                    "category": "SPRING_BOOT_VERSION",
                    "message": f"Current Spring Boot version: {spring_boot_version}",
                    "action": "Will be upgraded to 3.x"
                })
            elif spring_boot_version.startswith("3."):
                recommendations.append({
                    "severity": "INFO", 
                    "category": "SPRING_BOOT_VERSION",
                    "message": f"Already using Spring Boot 3.x: {spring_boot_version}"
                })
        
        # Analyze dependencies
        dependencies = root.findall('.//maven:dependency', ns)
        for dep in dependencies:
            group_id = self._get_text(dep.find('maven:groupId', ns))
            artifact_id = self._get_text(dep.find('maven:artifactId', ns))
            version = self._get_text(dep.find('maven:version', ns))
            
            if artifact_id and group_id:
                issue = self._check_dependency_compatibility(group_id, artifact_id, version)
                if issue:
                    issues.append(issue)
        
        # Check for javax imports in source code
        javax_usage = self._scan_javax_imports()
        if javax_usage:
            warnings.extend(javax_usage)
        
        return {
            "issues": issues,
            "warnings": warnings, 
            "recommendations": recommendations
        }
    
    def _get_spring_boot_version(self, root: ET.Element, ns: Dict) -> Optional[str]:
        """Extract Spring Boot version from POM"""
        # Check parent
        parent = root.find('maven:parent', ns)
        if parent:
            parent_artifact = self._get_text(parent.find('maven:artifactId', ns))
            if parent_artifact == 'spring-boot-starter-parent':
                return self._get_text(parent.find('maven:version', ns))
        
        # Check properties
        properties = root.find('maven:properties', ns)
        if properties:
            for prop in properties:
                if 'spring.boot' in prop.tag or 'spring-boot' in prop.tag:
                    return prop.text
        
        return None
    
    def _check_dependency_compatibility(self, group_id: str, artifact_id: str, version: str) -> Optional[Dict]:
        """Check if dependency is compatible with Spring Boot 3.x"""
        
        # Check known incompatible dependencies
        if artifact_id in self.compatibility_matrix:
            compat_info = self.compatibility_matrix[artifact_id]
            
            if version and 'max_javax_version' in compat_info:
                if self._version_compare(version, compat_info['max_javax_version']) <= 0:
                    return {
                        "severity": "ERROR",
                        "category": "DEPENDENCY_COMPATIBILITY",
                        "dependency": f"{group_id}:{artifact_id}:{version}",
                        "message": compat_info['issue'],
                        "solution": compat_info['solution']
                    }
        
        # Check for javax.servlet dependencies
        if 'javax.servlet' in group_id:
            return {
                "severity": "ERROR", 
                "category": "JAVAX_DEPENDENCY",
                "dependency": f"{group_id}:{artifact_id}:{version}",
                "message": "javax.servlet dependencies are incompatible with Spring Boot 3.x",
                "solution": "Remove explicit javax.servlet dependencies, use Spring Boot starters"
            }
        
        return None
    
    def _scan_javax_imports(self) -> List[Dict]:
        """Scan source code for javax imports that need migration"""
        warnings = []
        src_paths = [
            self.project_path / "src" / "main" / "java",
            self.project_path / "src" / "test" / "java"
        ]
        
        javax_patterns = [
            r'import\s+javax\.servlet',
            r'import\s+javax\.persistence', 
            r'import\s+javax\.annotation',
            r'import\s+javax\.validation'
        ]
        
        for src_path in src_paths:
            if src_path.exists():
                for java_file in src_path.rglob("*.java"):
                    try:
                        content = java_file.read_text(encoding='utf-8')
                        for pattern in javax_patterns:
                            matches = re.findall(pattern, content)
                            if matches:
                                warnings.append({
                                    "severity": "WARNING",
                                    "category": "JAVAX_IMPORTS",
                                    "file": str(java_file.relative_to(self.project_path)),
                                    "message": f"Found javax import: {matches[0]}",
                                    "action": "Will need jakarta equivalent in Spring Boot 3.x"
                                })
                    except Exception as e:
                        continue  # Skip files that can't be read
        
        return warnings
    
    def _run_maven_analysis(self) -> Dict:
        """Run Maven commands to gather dependency information"""
        maven_results = {}
        
        commands = {
            "dependency_updates": ["mvn", "versions:display-dependency-updates", "-q"],
            "dependency_tree": ["mvn", "dependency:tree", "-q"],
            "outdated_logback": ["mvn", "dependency:tree", f"-Dincludes=*logback*", "-q"]
        }
        
        for name, cmd in commands.items():
            try:
                result = subprocess.run(cmd, 
                                      capture_output=True, 
                                      text=True, 
                                      cwd=self.project_path,
                                      timeout=60)
                maven_results[name] = {
                    "success": result.returncode == 0,
                    "output": result.stdout if result.returncode == 0 else result.stderr
                }
            except (subprocess.TimeoutExpired, FileNotFoundError) as e:
                maven_results[name] = {
                    "success": False,
                    "error": str(e)
                }
        
        return maven_results
    
    def _version_compare(self, version1: str, version2: str) -> int:
        """Compare semantic versions. Returns -1, 0, or 1"""
        def version_tuple(v):
            return tuple(map(int, (v.split("."))))
        
        try:
            v1_tuple = version_tuple(version1)
            v2_tuple = version_tuple(version2)
            
            if v1_tuple < v2_tuple:
                return -1
            elif v1_tuple > v2_tuple:
                return 1
            else:
                return 0
        except ValueError:
            # Fallback to string comparison
            return -1 if version1 < version2 else (1 if version1 > version2 else 0)
    
    def _get_text(self, element) -> Optional[str]:
        """Safely get text from XML element"""
        return element.text.strip() if element is not None and element.text else None
    
    def _generate_report(self, results: Dict):
        """Generate human-readable report"""
        print("\n" + "="*80)
        print("🚀 SPRING BOOT 3.x MIGRATION COMPATIBILITY REPORT")
        print("="*80)
        
        # Summary
        error_count = len([i for i in results['issues'] if i.get('severity') == 'ERROR'])
        warning_count = len(results['warnings'])
        
        print(f"\n📊 SUMMARY:")
        print(f"   ❌ Errors: {error_count}")
        print(f"   ⚠️  Warnings: {warning_count}")
        print(f"   ✅ Recommendations: {len(results['recommendations'])}")
        
        # Critical Issues
        if error_count > 0:
            print(f"\n🚨 CRITICAL ISSUES (Must Fix Before Migration):")
            for issue in results['issues']:
                if issue.get('severity') == 'ERROR':
                    print(f"   ❌ {issue.get('category', 'UNKNOWN')}: {issue.get('message', '')}")
                    if 'dependency' in issue:
                        print(f"      Dependency: {issue['dependency']}")
                    if 'solution' in issue:
                        print(f"      Solution: {issue['solution']}")
                    print()
        
        # Warnings
        if warning_count > 0:
            print(f"\n⚠️  WARNINGS (Review Required):")
            for warning in results['warnings'][:5]:  # Show first 5
                print(f"   ⚠️  {warning.get('category', 'UNKNOWN')}: {warning.get('message', '')}")
                if 'file' in warning:
                    print(f"      File: {warning['file']}")
                if 'action' in warning:
                    print(f"      Action: {warning['action']}")
                print()
            
            if len(results['warnings']) > 5:
                print(f"   ... and {len(results['warnings']) - 5} more warnings")
        
        # Maven Analysis Results
        maven_analysis = results.get('maven_analysis', {})
        if maven_analysis:
            print(f"\n🔧 MAVEN ANALYSIS:")
            for analysis_name, analysis_result in maven_analysis.items():
                status = "✅" if analysis_result.get('success') else "❌"
                print(f"   {status} {analysis_name.replace('_', ' ').title()}")
                
                if 'logback' in analysis_name and analysis_result.get('success'):
                    output = analysis_result.get('output', '')
                    if 'logback-access' in output and '1.4.' in output:
                        print(f"      🚨 DETECTED: Logback Access 1.4.x - INCOMPATIBLE with Spring Boot 3.x!")
        
        # Final Recommendation
        print(f"\n💡 MIGRATION READINESS:")
        if error_count == 0:
            print("   ✅ Project appears ready for Spring Boot 3.x migration")
            print("   📝 Review warnings and plan javax → jakarta refactoring")
        else:
            print("   ❌ Project NOT ready for migration")
            print("   🔧 Fix critical issues before proceeding")
        
        print("\n" + "="*80)

def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    analyzer = SpringBootMigrationAnalyzer(project_path)
    results = analyzer.analyze_project()
    
    # Exit with error code if critical issues found
    critical_issues = len([i for i in results['issues'] if i.get('severity') == 'ERROR'])
    sys.exit(1 if critical_issues > 0 else 0)

if __name__ == "__main__":
    main()