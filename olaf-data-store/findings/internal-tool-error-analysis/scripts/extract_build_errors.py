#!/usr/bin/env python3
"""
BMS Build Log Error Extractor
Preprocesses large BMS build logs to extract and categorize compilation errors
for mapping to migration documentation.
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class BuildError:
    file_path: str
    line_number: int
    error_type: str
    error_message: str
    context_lines: List[str]
    component: str = ""

class BMSLogParser:
    def __init__(self):
        # Error patterns for different types of compilation errors
        self.error_patterns = {
            'fatal_error': re.compile(r'^(.+?):(\d+):(\d+):\s*fatal error:\s*(.+)$'),
            'error': re.compile(r'^(.+?):(\d+):(\d+):\s*error:\s*(.+)$'),
            'missing_header': re.compile(r"fatal error:\s*(.+?):\s*No such file or directory"),
            'incomplete_type': re.compile(r"error:\s*invalid use of incomplete type"),
            'not_member': re.compile(r"error:\s*'(.+?)' is not a member of '(.+?)'"),
            'undefined_reference': re.compile(r"undefined reference to"),
            'component_build': re.compile(r'^(.+?)\s+\d+\.\d+\.\d+\.\d+\s*-\s*\(\d+/\d+\)$')
        }
        
        # Migration-related patterns
        self.migration_patterns = {
            'otf_header': re.compile(r'otf/.*\.h'),
            'rest_service': re.compile(r'RESTService|ServiceInterface'),
            'iterator_inheritance': re.compile(r'std::iterator'),
            'cstdint_missing': re.compile(r'uint\d+_t|int\d+_t'),
            'const_correctness': re.compile(r'operator[<>=!]+.*const'),
            'kvclient': re.compile(r'KvClient|N1QLClient|Couchbase')
        }

    def extract_errors(self, log_file: Path) -> List[BuildError]:
        """Extract all compilation errors from a BMS build log."""
        errors = []
        current_component = ""
        
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Track current component being built
            component_match = self.error_patterns['component_build'].match(line)
            if component_match:
                current_component = component_match.group(1)
                continue
            
            # Check for fatal errors
            fatal_match = self.error_patterns['fatal_error'].match(line)
            if fatal_match:
                error = BuildError(
                    file_path=fatal_match.group(1),
                    line_number=int(fatal_match.group(2)),
                    error_type="fatal_error",
                    error_message=fatal_match.group(4),
                    context_lines=self._get_context_lines(lines, i),
                    component=current_component
                )
                errors.append(error)
                continue
            
            # Check for regular errors
            error_match = self.error_patterns['error'].match(line)
            if error_match:
                error = BuildError(
                    file_path=error_match.group(1),
                    line_number=int(error_match.group(2)),
                    error_type="compilation_error",
                    error_message=error_match.group(4),
                    context_lines=self._get_context_lines(lines, i),
                    component=current_component
                )
                errors.append(error)
        
        return errors

    def _get_context_lines(self, lines: List[str], error_line_idx: int, context_size: int = 3) -> List[str]:
        """Get context lines around an error for better understanding."""
        start = max(0, error_line_idx - context_size)
        end = min(len(lines), error_line_idx + context_size + 1)
        return [line.strip() for line in lines[start:end]]

    def categorize_errors(self, errors: List[BuildError]) -> Dict[str, List[BuildError]]:
        """Categorize errors by migration pattern."""
        categories = {
            'otf_migration': [],
            'missing_headers': [],
            'api_changes': [],
            'cpp_standard_issues': [],
            'kvclient_changes': [],
            'other': []
        }
        
        for error in errors:
            error_text = f"{error.error_message} {' '.join(error.context_lines)}"
            
            if self.migration_patterns['otf_header'].search(error_text):
                categories['otf_migration'].append(error)
            elif self.error_patterns['missing_header'].search(error.error_message):
                categories['missing_headers'].append(error)
            elif self.error_patterns['not_member'].search(error.error_message):
                categories['api_changes'].append(error)
            elif (self.migration_patterns['iterator_inheritance'].search(error_text) or 
                  self.migration_patterns['cstdint_missing'].search(error_text) or
                  self.migration_patterns['const_correctness'].search(error_text)):
                categories['cpp_standard_issues'].append(error)
            elif self.migration_patterns['kvclient'].search(error_text):
                categories['kvclient_changes'].append(error)
            else:
                categories['other'].append(error)
        
        return categories

    def generate_report(self, categories: Dict[str, List[BuildError]], output_file: Path):
        """Generate a structured error report with migration guidance."""
        with open(output_file, 'w') as f:
            f.write("# BMS Build Error Analysis Report\n\n")
            f.write(f"Generated: {Path.cwd()}\n\n")
            
            total_errors = sum(len(errors) for errors in categories.values())
            f.write(f"**Total Errors Found:** {total_errors}\n\n")
            
            for category, errors in categories.items():
                if not errors:
                    continue
                    
                f.write(f"## {category.replace('_', ' ').title()} ({len(errors)} errors)\n\n")
                
                # Add migration guidance
                guidance = self._get_migration_guidance(category)
                if guidance:
                    f.write(f"**Migration Guidance:** {guidance}\n\n")
                
                # Group by error message for summary
                error_groups = {}
                for error in errors:
                    key = error.error_message[:100]  # First 100 chars as key
                    if key not in error_groups:
                        error_groups[key] = []
                    error_groups[key].append(error)
                
                for error_msg, error_list in error_groups.items():
                    f.write(f"### {error_msg}{'...' if len(error_msg) == 100 else ''}\n")
                    f.write(f"**Occurrences:** {len(error_list)}\n")
                    f.write(f"**Files affected:**\n")
                    
                    for error in error_list[:5]:  # Show first 5 files
                        f.write(f"- `{error.file_path}:{error.line_number}` (Component: {error.component})\n")
                    
                    if len(error_list) > 5:
                        f.write(f"- ... and {len(error_list) - 5} more files\n")
                    
                    f.write("\n")

    def _get_migration_guidance(self, category: str) -> str:
        """Get migration guidance for each error category."""
        guidance_map = {
            'otf_migration': "Consult 18_to_19.md OTF Migration section. Update #include <otf/RESTServiceObject.h> to #include <otf/Service.h>",
            'missing_headers': "Check migration guides for header renames and new include paths",
            'api_changes': "Review API changes in migration guides. Methods may have been renamed or moved to different classes",
            'cpp_standard_issues': "C++17 to C++23 migration issues. Add const qualifiers, include <cstdint>, remove std::iterator inheritance",
            'kvclient_changes': "KvClient Pack 19+ changes. Check for header renames and class separations",
            'other': "Review detailed migration guides for component-specific changes"
        }
        return guidance_map.get(category, "")

def main():
    parser = argparse.ArgumentParser(description='Extract and categorize BMS build errors')
    parser.add_argument('log_file', help='Path to BMS build log file')
    parser.add_argument('-o', '--output', help='Output report file', 
                       default='build_error_analysis.md')
    
    args = parser.parse_args()
    
    log_file = Path(args.log_file)
    if not log_file.exists():
        print(f"Error: Log file {log_file} not found")
        sys.exit(1)
    
    parser = BMSLogParser()
    
    print(f"Extracting errors from {log_file}...")
    errors = parser.extract_errors(log_file)
    print(f"Found {len(errors)} errors")
    
    print("Categorizing errors...")
    categories = parser.categorize_errors(errors)
    
    output_file = Path(args.output)
    print(f"Generating report: {output_file}")
    parser.generate_report(categories, output_file)
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()
