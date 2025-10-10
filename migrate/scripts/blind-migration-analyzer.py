#!/usr/bin/env python3
"""
Blind Migration Compatibility Analyzer - No Prior Knowledge Version

This version tests what we can actually detect without knowing specific issues.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re
import subprocess
from typing import Dict, List, Optional

class BlindMigrationAnalyzer:
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.pom_path = self.project_path / "pom.xml"
        
        # Generic rules - no specific library knowledge
        self.generic_risk_patterns = {
            "javax_packages": [
                "javax.servlet",
                "javax.persistence", 
                "javax.annotation",
                "javax.validation",
                "javax.xml.bind"
            ],
            "version_gap_threshold": 0.5,  # Major version gaps
            "pre_jakarta_indicators": [
                "1.4.", "4.0.", "2.7.", "5.6."  # Common pre-Jakarta versions
            ]
        }

    def analyze_blind(self) -> Dict:
        """Analyze without specific library knowledge"""
        print(f"🔍 BLIND ANALYSIS (No Prior Knowledge): {self.project_path}")
        
        results = {
            "detected_issues": [],
            "version_gaps": [],
            "javax_usage": [],
            "web_research_needed": []
        }
        
        if not self.pom_path.exists():
            return results
        
        try:
            tree = ET.parse(self.pom_path)
            root = tree.getroot()
            
            # Generic analysis
            results.update(self._analyze_generic_risks(root))
            
        except Exception as e:
            results["error"] = str(e)
        
        return results
    
    def _analyze_generic_risks(self, root: ET.Element) -> Dict:
        """Find generic risk patterns"""
        detected_issues = []
        version_gaps = []
        javax_usage = []
        web_research_needed = []
        
        ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}
        
        dependencies = root.findall('.//maven:dependency', ns)
        
        for dep in dependencies:
            group_id = self._get_text(dep.find('maven:groupId', ns)) or ""
            artifact_id = self._get_text(dep.find('maven:artifactId', ns)) or ""
            version = self._get_text(dep.find('maven:version', ns)) or ""
            
            # Check for javax packages
            if any(javax_pkg in group_id for javax_pkg in self.generic_risk_patterns["javax_packages"]):
                javax_usage.append({
                    "dependency": f"{group_id}:{artifact_id}:{version}",
                    "risk": "javax package in Spring Boot 3.x migration",
                    "action": "Research Jakarta EE equivalent"
                })
            
            # Check for suspicious version patterns
            if version:
                for pre_jakarta_version in self.generic_risk_patterns["pre_jakarta_indicators"]:
                    if version.startswith(pre_jakarta_version):
                        web_research_needed.append({
                            "dependency": f"{group_id}:{artifact_id}:{version}",
                            "reason": f"Version {version} might be pre-Jakarta EE",
                            "search_query": f'"{artifact_id}" "{version}" "spring boot 3" compatibility'
                        })
            
            # Flag anything with "access" in name for web research
            if "access" in artifact_id.lower():
                web_research_needed.append({
                    "dependency": f"{group_id}:{artifact_id}:{version}",
                    "reason": "Access-related libraries often have servlet dependencies",
                    "search_query": f'"{artifact_id}" "spring boot 3" "jakarta ee" compatibility'
                })
        
        return {
            "detected_issues": detected_issues,
            "version_gaps": version_gaps,
            "javax_usage": javax_usage,
            "web_research_needed": web_research_needed
        }
    
    def _get_text(self, element) -> Optional[str]:
        """Safely get text from XML element"""
        return element.text.strip() if element is not None and element.text else None
    
    def generate_blind_report(self, results: Dict):
        """Generate report showing what we can detect blindly"""
        print("\n" + "="*80)
        print("🔍 BLIND MIGRATION ANALYSIS RESULTS")
        print("="*80)
        
        javax_count = len(results.get('javax_usage', []))
        research_count = len(results.get('web_research_needed', []))
        
        print(f"\n📊 GENERIC DETECTION SUMMARY:")
        print(f"   ⚠️  javax Dependencies: {javax_count}")
        print(f"   🔍 Needs Web Research: {research_count}")
        
        if javax_count > 0:
            print(f"\n⚠️  JAVAX DEPENDENCIES FOUND:")
            for javax_dep in results['javax_usage'][:3]:  # Show first 3
                print(f"   📦 {javax_dep['dependency']}")
                print(f"      Risk: {javax_dep['risk']}")
        
        if research_count > 0:
            print(f"\n🔍 REQUIRES WEB RESEARCH:")
            for research_item in results['web_research_needed'][:3]:  # Show first 3
                print(f"   📦 {research_item['dependency']}")
                print(f"      Reason: {research_item['reason']}")
                print(f"      Search: {research_item['search_query']}")
                print()
        
        print(f"\n💡 HONEST ASSESSMENT:")
        print("   ✅ Can detect javax dependencies automatically")
        print("   ✅ Can flag suspicious version patterns")  
        print("   ❓ Cannot know specific incompatibilities without research")
        print("   🔍 Must perform web research for each flagged dependency")
        
        print("\n" + "="*80)

def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    analyzer = BlindMigrationAnalyzer(project_path)
    results = analyzer.analyze_blind()
    analyzer.generate_blind_report(results)

if __name__ == "__main__":
    main()