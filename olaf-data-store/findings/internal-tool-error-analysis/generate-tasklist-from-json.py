#!/usr/bin/env python3
"""
Generate individual error fix tasklist from JSON error details.
Creates one task per error occurrence with simplified format.
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

def load_json_data(json_file):
    """Load and parse JSON error details."""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_priority_level(criticality):
    """Map criticality to priority level."""
    priority_map = {
        'CRITICAL': 'P0',
        'HIGH': 'P1', 
        'MEDIUM': 'P2',
        'LOW': 'P3'
    }
    return priority_map.get(criticality.upper(), 'P3')

def generate_tasklist(json_data, output_file):
    """Generate simplified tasklist from JSON data."""
    
    # Extract metadata
    timestamp = json_data.get('analysis_timestamp', datetime.now().strftime('%Y-%m-%d %H:%M CEDT'))
    total_matches = len(json_data.get('matches', []))
    
    # Count by priority
    priority_counts = {'P0': 0, 'P1': 0, 'P2': 0, 'P3': 0}
    
    # Sort matches by priority and timestamp
    matches = json_data.get('matches', [])
    for match in matches:
        error_id = match.get('error_id', '')
        # Get criticality from error patterns
        criticality = 'MEDIUM'  # default
        for pattern_id, pattern_data in json_data.get('error_patterns', {}).items():
            if pattern_id == error_id:
                criticality = pattern_data.get('criticality', 'MEDIUM')
                break
        
        priority = get_priority_level(criticality)
        priority_counts[priority] += 1
    
    # Sort matches for output
    def sort_key(match):
        error_id = match.get('error_id', '')
        criticality = 'MEDIUM'
        for pattern_id, pattern_data in json_data.get('error_patterns', {}).items():
            if pattern_id == error_id:
                criticality = pattern_data.get('criticality', 'MEDIUM')
                break
        
        priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        return (priority_order.get(criticality, 3), match.get('line_number', 0))
    
    sorted_matches = sorted(matches, key=sort_key)
    
    # Generate markdown content
    content = f"""# Individual Error Fix Task List
**Generated**: {timestamp}
**Total Tasks**: {total_matches} (one per error occurrence)

## Task Summary by Priority
- P0 (Critical): {priority_counts['P0']} tasks
- P1 (High): {priority_counts['P1']} tasks 
- P2 (Medium): {priority_counts['P2']} tasks
- P3 (Low): {priority_counts['P3']} tasks

## Individual Tasks (Priority Order)

"""
    
    # Generate individual tasks
    for i, match in enumerate(sorted_matches, 1):
        error_id = match.get('error_id', 'UNKNOWN')
        line_number = match.get('line_number', 0)
        timestamp_str = match.get('timestamp', 'Unknown')
        
        # Get priority
        criticality = 'MEDIUM'
        for pattern_id, pattern_data in json_data.get('error_patterns', {}).items():
            if pattern_id == error_id:
                criticality = pattern_data.get('criticality', 'MEDIUM')
                break
        
        priority = get_priority_level(criticality)
        
        content += f"""### Task {i}: [{priority}] {error_id} - Line {line_number}
**Status**: PENDING
**Timestamp**: {timestamp_str}

"""
    
    content += """---

**Usage**: 
- Reference JSON file for full error details and context
- Reference template for resolution steps
- Mark tasks as COMPLETED/BLOCKED/FAILED as processed

**Files**:
- Analysis: internal-tool-error-analysis-{timestamp}.md
- Details: error-details-{timestamp}.json"""
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated tasklist with {total_matches} individual tasks")
    print(f"Priority breakdown: P0: {priority_counts['P0']}, P1: {priority_counts['P1']}, P2: {priority_counts['P2']}, P3: {priority_counts['P3']}")
    print(f"Output: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate individual error fix tasklist from JSON')
    parser.add_argument('--json-file', required=True, help='JSON error details file')
    parser.add_argument('--output', required=True, help='Output tasklist markdown file')
    
    args = parser.parse_args()
    
    # Load JSON data
    json_data = load_json_data(args.json_file)
    
    # Generate tasklist
    generate_tasklist(json_data, args.output)

if __name__ == '__main__':
    main()
