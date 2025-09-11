#!/usr/bin/env python3
"""
Internal Tool Error Analysis Script
Processes massive log files using structured error documentation for pattern matching
"""

import re
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging
from dataclasses import dataclass, asdict

@dataclass
class ErrorPattern:
    """Represents a single error pattern from documentation"""
    error_id: str
    description: str
    criticality: str  # CRITICAL, HIGH, MEDIUM, LOW
    impact: str
    regex_patterns: List[str]
    keywords: List[str]
    resolution: str
    escalation: str = ""
    compiled_patterns: List[re.Pattern] = None

@dataclass
class ErrorMatch:
    """Represents a matched error in the log"""
    error_id: str
    line_number: int
    matched_text: str
    context_lines: List[str]
    confidence: str  # High/Medium/Low
    timestamp: Optional[str] = None

class InternalToolErrorAnalyzer:
    """Main analyzer class for processing logs against error documentation"""
    
    def __init__(self, log_file: Path, doc_file: Path, tool_name: str):
        self.log_file = Path(log_file)
        self.doc_file = Path(doc_file)
        self.tool_name = tool_name
        self.error_patterns: Dict[str, ErrorPattern] = {}
        self.matches: List[ErrorMatch] = []
        self.unknown_errors: List[str] = []
        
        # Setup logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
    
    def parse_error_documentation(self) -> bool:
        """Parse structured MD documentation into error patterns"""
        try:
            with open(self.doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split by error ID sections
            error_sections = re.split(r'## Error ID:\s*([A-Z]+-\d+)', content)[1:]  # Skip first empty element
            
            for i in range(0, len(error_sections), 2):
                if i + 1 >= len(error_sections):
                    break
                    
                error_id = error_sections[i].strip()
                section_content = error_sections[i + 1]
                
                # Extract components using regex
                description_match = re.search(r'\*\*Description\*\*:\s*(.+?)(?=\n\*\*|\n##|$)', section_content, re.DOTALL)
                criticality_match = re.search(r'\*\*Criticality\*\*:\s*(.+?)(?=\n\*\*|\n##|$)', section_content)
                impact_match = re.search(r'\*\*Impact\*\*:\s*(.+?)(?=\n\*\*|\n##|$)', section_content, re.DOTALL)
                regex_match = re.search(r'- Regex:\s*`(.+?)`', section_content)
                keywords_match = re.search(r'- Keywords:\s*\[(.+?)\]', section_content)
                resolution_match = re.search(r'\*\*Proposed Resolution\*\*:\s*(.+?)(?=\n\*\*|\n##|$)', section_content, re.DOTALL)
                escalation_match = re.search(r'\*\*Escalation\*\*:\s*(.+?)(?=\n\*\*|\n##|$)', section_content, re.DOTALL)
                
                if not all([description_match, criticality_match, resolution_match]):
                    self.logger.warning(f"Incomplete error definition for {error_id}")
                    continue
                
                # Parse regex patterns
                regex_patterns = []
                if regex_match:
                    # Split multiple patterns by |
                    patterns = regex_match.group(1).split('|')
                    regex_patterns = [p.strip() for p in patterns]
                
                # Parse keywords
                keywords = []
                if keywords_match:
                    keywords_str = keywords_match.group(1)
                    keywords = [k.strip().strip('"\'') for k in keywords_str.split(',')]
                
                # Create error pattern
                pattern = ErrorPattern(
                    error_id=error_id,
                    description=description_match.group(1).strip(),
                    criticality=criticality_match.group(1).strip(),
                    impact=impact_match.group(1).strip() if impact_match else "",
                    regex_patterns=regex_patterns,
                    keywords=keywords,
                    resolution=resolution_match.group(1).strip(),
                    escalation=escalation_match.group(1).strip() if escalation_match else ""
                )
                
                self.error_patterns[error_id] = pattern
                self.logger.info(f"Loaded error pattern: {error_id}")
            
            return len(self.error_patterns) > 0
            
        except Exception as e:
            self.logger.error(f"Failed to parse error documentation: {e}")
            return False
    
    def compile_patterns(self) -> bool:
        """Compile regex patterns for efficient matching"""
        try:
            for error_id, pattern in self.error_patterns.items():
                compiled = []
                for regex_str in pattern.regex_patterns:
                    try:
                        compiled_pattern = re.compile(regex_str, re.IGNORECASE | re.MULTILINE)
                        compiled.append(compiled_pattern)
                    except re.error as e:
                        self.logger.warning(f"Invalid regex in {error_id}: {regex_str} - {e}")
                
                pattern.compiled_patterns = compiled
                
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to compile patterns: {e}")
            return False
    
    def analyze_log_chunk(self, lines: List[str], start_line: int) -> List[ErrorMatch]:
        """Analyze a chunk of log lines against error patterns"""
        chunk_matches = []
        
        # Track matches per error type for reporting
        error_type_counts = {error_id: 0 for error_id in self.error_patterns.keys()}
        
        # Track matched line numbers to prevent duplicates
        matched_lines = set()
        
        for i, line in enumerate(lines):
            line_number = start_line + i
            
            # Skip if this line was already matched
            if line_number in matched_lines:
                continue
            
            # Create multi-line context for better matching (current + next 2 lines)
            context_window = " ".join(lines[i:min(len(lines), i + 3)])
            
            # Check each error pattern
            for error_id, pattern in self.error_patterns.items():
                match_found = False
                confidence = "Low"
                matched_text = line.strip()
                
                # Try regex patterns first (highest confidence) - check both single line and context
                if pattern.compiled_patterns:
                    for compiled_regex in pattern.compiled_patterns:
                        if compiled_regex.search(line) or compiled_regex.search(context_window):
                            match_found = True
                            confidence = "High"
                            break
                
                # Much stricter keyword matching - only for lines with actual error indicators AND strong keyword correlation
                if not match_found and pattern.keywords:
                    # Only apply to lines that look like real errors (not just DEBUG/INFO/TRACE with error keywords)
                    error_indicators = ['ERROR', 'FATAL', 'WARN', 'EXCEPTION', 'FAILED', 'TIMEOUT', 'OUTOFMEMORY']
                    has_error_indicator = any(indicator in line.upper() for indicator in error_indicators)
                    
                    # Additional check: avoid matching lines that are clearly just status messages
                    status_indicators = ['DEBUG', 'INFO', 'TRACE']
                    is_status_line = any(status in line.upper() for status in status_indicators)
                    
                    if has_error_indicator and not is_status_line:
                        # Check keywords in both single line and context window
                        line_keyword_matches = sum(1 for keyword in pattern.keywords 
                                                 if keyword.lower() in line.lower())
                        context_keyword_matches = sum(1 for keyword in pattern.keywords 
                                                    if keyword.lower() in context_window.lower())
                        
                        # Use the better of the two scores
                        keyword_matches = max(line_keyword_matches, context_keyword_matches)
                        
                        # Much stricter threshold: need at least 3 keywords OR 70% coverage (whichever is higher)
                        min_keywords = max(3, int(len(pattern.keywords) * 0.7))
                        if keyword_matches >= min_keywords:
                            match_found = True
                            confidence = "Medium" if keyword_matches >= len(pattern.keywords) * 0.8 else "Low"
                            # If context window had better match, include it in matched text
                            if context_keyword_matches > line_keyword_matches:
                                matched_text = context_window[:200] + "..." if len(context_window) > 200 else context_window
                
                if match_found:
                    # Extract context lines (2 before, 2 after)
                    context_start = max(0, i - 2)
                    context_end = min(len(lines), i + 3)
                    context_lines = lines[context_start:context_end]
                    
                    # Extract timestamp if present
                    timestamp = self._extract_timestamp(line)
                    
                    error_match = ErrorMatch(
                        error_id=error_id,
                        line_number=line_number,
                        matched_text=matched_text,
                        context_lines=context_lines,
                        confidence=confidence,
                        timestamp=timestamp
                    )
                    
                    chunk_matches.append(error_match)
                    error_type_counts[error_id] += 1
                    matched_lines.add(line_number)
                    
                    # Also mark nearby lines as matched to avoid clustering
                    for nearby_line in range(max(start_line, line_number - 1), 
                                           min(start_line + len(lines), line_number + 2)):
                        matched_lines.add(nearby_line)
                    
                    break  # Don't match multiple patterns for same line
        
        return chunk_matches
    
    def _extract_timestamp(self, line: str) -> Optional[str]:
        """Extract timestamp from log line using common patterns"""
        timestamp_patterns = [
            r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}',
            r'\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}',
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
        ]
        
        for pattern in timestamp_patterns:
            match = re.search(pattern, line)
            if match:
                return match.group(0)
        
        return None
    
    def process_log_file(self, chunk_size: int = 10000) -> bool:
        """Process the entire log file in chunks"""
        try:
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
                chunk = []
                line_number = 1
                
                for line in f:
                    chunk.append(line.rstrip('\n\r'))
                    
                    if len(chunk) >= chunk_size:
                        # Process chunk
                        chunk_matches = self.analyze_log_chunk(chunk, line_number)
                        self.matches.extend(chunk_matches)
                        
                        # Update progress
                        self.logger.info(f"Processed lines {line_number}-{line_number + len(chunk) - 1}, found {len(chunk_matches)} matches")
                        
                        # Reset for next chunk
                        line_number += len(chunk)
                        chunk = []
                
                # Process remaining lines
                if chunk:
                    chunk_matches = self.analyze_log_chunk(chunk, line_number)
                    self.matches.extend(chunk_matches)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to process log file: {e}")
            return False
    
    def generate_analysis_report(self, output_dir: Path) -> bool:
        """Generate comprehensive analysis report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M")
            
            # Group matches by error ID
            error_summary = {}
            for match in self.matches:
                if match.error_id not in error_summary:
                    error_summary[match.error_id] = []
                error_summary[match.error_id].append(match)
            
            # Generate markdown report
            report_path = output_dir / f"internal-tool-error-analysis-{timestamp}.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(f"# Internal Tool Error Analysis Report\n")
                f.write(f"**Tool**: {self.tool_name}\n")
                f.write(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M CEDT')}\n")
                f.write(f"**Log File**: {self.log_file.name}\n")
                f.write(f"**Total Log Lines**: {sum(1 for _ in open(self.log_file, 'r'))}\n\n")
                
                f.write(f"## Executive Summary\n")
                f.write(f"- **Total Errors Identified**: {len(self.matches)}\n")
                f.write(f"- **Known Error Types**: {len(error_summary)}\n")
                f.write(f"- **Error Documentation Patterns**: {len(self.error_patterns)}\n\n")
                
                f.write(f"## Known Error Analysis\n")
                # Sort errors by criticality for prioritized reporting
                criticality_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
                sorted_errors = sorted(error_summary.items(), 
                                     key=lambda x: criticality_order.get(self.error_patterns[x[0]].criticality, 4))
                
                for error_id, matches in sorted_errors:
                    pattern = self.error_patterns[error_id]
                    f.write(f"### Error ID: {error_id} [{pattern.criticality}]\n")
                    f.write(f"**Description**: {pattern.description}\n")
                    f.write(f"**Criticality**: {pattern.criticality}\n")
                    f.write(f"**Impact**: {pattern.impact}\n")
                    f.write(f"**Frequency**: {len(matches)} occurrences\n")
                    f.write(f"**Confidence Distribution**: {self._get_confidence_stats(matches)}\n")
                    f.write(f"**Sample Entry**:\n```\n{matches[0].matched_text}\n```\n")
                    f.write(f"**Resolution Steps**:\n{pattern.resolution}\n")
                    if pattern.escalation:
                        f.write(f"**Escalation**: {pattern.escalation}\n")
                    f.write(f"\n")
            
            # Generate JSON details
            json_path = output_dir / f"error-details-{timestamp}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json_data = {
                    'analysis_metadata': {
                        'tool_name': self.tool_name,
                        'log_file': str(self.log_file),
                        'analysis_date': datetime.now().isoformat(),
                        'total_matches': len(self.matches)
                    },
                    'error_patterns': {eid: asdict(pattern) for eid, pattern in self.error_patterns.items()},
                    'matches': [asdict(match) for match in self.matches]
                }
                json.dump(json_data, f, indent=2, default=str)
            
            self.logger.info(f"Analysis report generated: {report_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to generate report: {e}")
            return False
    
    def _get_confidence_stats(self, matches: List[ErrorMatch]) -> str:
        """Generate confidence statistics for matches"""
        high = sum(1 for m in matches if m.confidence == "High")
        medium = sum(1 for m in matches if m.confidence == "Medium")
        low = sum(1 for m in matches if m.confidence == "Low")
        return f"High: {high}, Medium: {medium}, Low: {low}"

def main():
    parser = argparse.ArgumentParser(description="Analyze internal tool errors using structured documentation")
    parser.add_argument("--log-file", required=True, help="Path to log file")
    parser.add_argument("--doc-file", required=True, help="Path to error documentation")
    parser.add_argument("--tool-name", required=True, help="Name of the internal tool")
    parser.add_argument("--output-dir", default=".", help="Output directory for results")
    parser.add_argument("--chunk-size", type=int, default=10000, help="Log processing chunk size")
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = InternalToolErrorAnalyzer(args.log_file, args.doc_file, args.tool_name)
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Execute analysis pipeline
    print("Parsing error documentation...")
    if not analyzer.parse_error_documentation():
        print("Failed to parse error documentation")
        return 1
    
    print("Compiling regex patterns...")
    if not analyzer.compile_patterns():
        print("Failed to compile patterns")
        return 1
    
    print("Processing log file...")
    if not analyzer.process_log_file(args.chunk_size):
        print("Failed to process log file")
        return 1
    
    print("Generating analysis report...")
    if not analyzer.generate_analysis_report(output_dir):
        print("Failed to generate report")
        return 1
    
    print(f"Analysis complete! Found {len(analyzer.matches)} error matches.")
    return 0

if __name__ == "__main__":
    exit(main())
