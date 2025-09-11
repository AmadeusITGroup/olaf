#!/usr/bin/env python3
"""
Enhanced BMS Build Log Error Extractor with LLM-Optimized Migration Guide Integration
Uses structured migration guides for comprehensive error pattern matching and resolution mapping.
"""

import re
import sys
import yaml
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class BuildError:
    file_path: str
    line_number: int
    error_type: str
    error_message: str
    context_lines: List[str]
    component: str = ""
    severity: str = "UNKNOWN"
    resolution: Optional[str] = None

class LLMOptimizedBMSParser:
    def __init__(self, structured_guide_path: str):
        self.guide_path = Path(structured_guide_path)
        self.error_patterns = {}
        self.resolution_mappings = {}
        self.component_changes = {}
        self.load_structured_guide()
        
    def load_structured_guide(self):
        """Load LLM-optimized structured migration guide."""
        if not self.guide_path.exists():
            print(f"Warning: Structured guide not found at {self.guide_path}")
            return
            
        with open(self.guide_path, 'r') as f:
            content = f.read()
            
        # Extract YAML blocks from markdown
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
        
        for block in yaml_blocks:
            try:
                data = yaml.safe_load(block)
                if isinstance(data, list):
                    for item in data:
                        if 'pattern' in item:
                            self.error_patterns[item['pattern']] = item
                elif isinstance(data, dict):
                    if 'error_patterns' in data:
                        for pattern in data['error_patterns']:
                            self.resolution_mappings[pattern] = data['resolution']
                    elif 'component' in data and 'old_name' in data:
                        self.component_changes[data['old_name']] = data
            except yaml.YAMLError:
                continue
    
    def extract_errors_with_resolution(self, log_file: Path) -> List[BuildError]:
        """Extract errors and map them to structured resolutions."""
        errors = []
        current_component = ""
        
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Track current component
            component_match = re.match(r'^(.+?)\s+\d+\.\d+\.\d+\.\d+\s*-\s*\(\d+/\d+\)$', line)
            if component_match:
                current_component = component_match.group(1)
                continue
            
            # Check for errors with pattern matching
            error = self._match_error_patterns(line, i, lines, current_component)
            if error:
                errors.append(error)
        
        return errors
    
    def _match_error_patterns(self, line: str, line_idx: int, all_lines: List[str], component: str) -> Optional[BuildError]:
        """Match line against structured error patterns."""
        
        # Standard compilation error patterns
        fatal_match = re.match(r'^(.+?):(\d+):(\d+):\s*fatal error:\s*(.+)$', line)
        if fatal_match:
            error_msg = fatal_match.group(4)
            resolution = self._find_resolution(error_msg, line)
            return BuildError(
                file_path=fatal_match.group(1),
                line_number=int(fatal_match.group(2)),
                error_type="fatal_error",
                error_message=error_msg,
                context_lines=self._get_context_lines(all_lines, line_idx),
                component=component,
                severity="FATAL",
                resolution=resolution
            )
        
        error_match = re.match(r'^(.+?):(\d+):(\d+):\s*error:\s*(.+)$', line)
        if error_match:
            error_msg = error_match.group(4)
            resolution = self._find_resolution(error_msg, line)
            return BuildError(
                file_path=error_match.group(1),
                line_number=int(error_match.group(2)),
                error_type="compilation_error",
                error_message=error_msg,
                context_lines=self._get_context_lines(all_lines, line_idx),
                component=component,
                severity="FATAL",
                resolution=resolution
            )
        
        warning_match = re.match(r'^(.+?):(\d+):(\d+):\s*warning:\s*(.+)$', line)
        if warning_match:
            error_msg = warning_match.group(4)
            resolution = self._find_resolution(error_msg, line)
            return BuildError(
                file_path=warning_match.group(1),
                line_number=int(warning_match.group(2)),
                error_type="warning",
                error_message=error_msg,
                context_lines=self._get_context_lines(all_lines, line_idx),
                component=component,
                severity="WARNING",
                resolution=resolution
            )
        
        return None
    
    def _find_resolution(self, error_msg: str, full_line: str) -> Optional[str]:
        """Find resolution using structured patterns."""
        
        # Check against loaded error patterns
        for pattern, pattern_data in self.error_patterns.items():
            if re.search(pattern, error_msg) or re.search(pattern, full_line):
                return f"Component: {pattern_data.get('component', 'Unknown')}, Keywords: {pattern_data.get('keywords', [])}"
        
        # Check resolution mappings
        for pattern, resolution in self.resolution_mappings.items():
            if re.search(pattern, error_msg) or re.search(pattern, full_line):
                if isinstance(resolution, list):
                    return "; ".join([f"Action: {action}" for action in resolution])
                elif isinstance(resolution, dict) and 'action' in resolution:
                    return f"Action: {resolution['action']}"
        
        return None
    
    def _get_context_lines(self, lines: List[str], error_line_idx: int, context_size: int = 2) -> List[str]:
        """Get context lines around an error."""
        start = max(0, error_line_idx - context_size)
        end = min(len(lines), error_line_idx + context_size + 1)
        return [line.strip() for line in lines[start:end]]
    
    def generate_enhanced_report(self, errors: List[BuildError], output_file: Path):
        """Generate enhanced report with structured resolutions."""
        
        # Categorize by severity and component
        by_severity = {"FATAL": [], "WARNING": [], "UNKNOWN": []}
        by_component = {}
        
        for error in errors:
            by_severity[error.severity].append(error)
            if error.component not in by_component:
                by_component[error.component] = []
            by_component[error.component].append(error)
        
        with open(output_file, 'w') as f:
            f.write("# Enhanced BMS Build Error Analysis Report\n\n")
            f.write(f"**Total Errors:** {len(errors)}\n")
            f.write(f"**Fatal:** {len(by_severity['FATAL'])}, **Warnings:** {len(by_severity['WARNING'])}\n\n")
            
            # Summary by severity
            for severity in ["FATAL", "WARNING", "UNKNOWN"]:
                if not by_severity[severity]:
                    continue
                    
                f.write(f"## {severity} Errors ({len(by_severity[severity])})\n\n")
                
                # Group by error message pattern
                error_groups = {}
                for error in by_severity[severity]:
                    key = error.error_message[:80]
                    if key not in error_groups:
                        error_groups[key] = []
                    error_groups[key].append(error)
                
                for error_pattern, error_list in error_groups.items():
                    f.write(f"### {error_pattern}{'...' if len(error_pattern) == 80 else ''}\n")
                    f.write(f"**Occurrences:** {len(error_list)}\n")
                    
                    # Show resolution if available
                    if error_list[0].resolution:
                        f.write(f"**Resolution:** {error_list[0].resolution}\n")
                    
                    f.write(f"**Files affected:**\n")
                    for error in error_list[:3]:  # Show first 3
                        f.write(f"- `{error.file_path}:{error.line_number}` (Component: {error.component})\n")
                    
                    if len(error_list) > 3:
                        f.write(f"- ... and {len(error_list) - 3} more files\n")
                    f.write("\n")
            
            # Component summary
            f.write("## Summary by Component\n\n")
            for component, comp_errors in by_component.items():
                if component:
                    f.write(f"- **{component}**: {len(comp_errors)} errors\n")

def main():
    parser = argparse.ArgumentParser(description='Enhanced BMS build error extraction with structured migration guides')
    parser.add_argument('log_file', help='Path to BMS build log file')
    parser.add_argument('-g', '--guide', help='Path to structured migration guide', 
                       default='18-to-19-structured.md')
    parser.add_argument('-o', '--output', help='Output report file', 
                       default='enhanced_build_error_analysis.md')
    
    args = parser.parse_args()
    
    log_file = Path(args.log_file)
    if not log_file.exists():
        print(f"Error: Log file {log_file} not found")
        sys.exit(1)
    
    parser = LLMOptimizedBMSParser(args.guide)
    
    print(f"Extracting errors from {log_file} using structured guide {args.guide}...")
    errors = parser.extract_errors_with_resolution(log_file)
    print(f"Found {len(errors)} errors")
    
    output_file = Path(args.output)
    print(f"Generating enhanced report: {output_file}")
    parser.generate_enhanced_report(errors, output_file)
    
    print("Enhanced analysis complete!")

if __name__ == "__main__":
    main()
