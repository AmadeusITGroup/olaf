#!/usr/bin/env python3
"""
Halstead Complexity Metrics Analyzer

Analyzes Halstead complexity metrics for source code files.
Halstead metrics measure software complexity based on the number of operators 
and operands in the code, providing insights into program effort, difficulty, 
and maintainability.
"""

import argparse
import os
import re
import sys
import math
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Any

def show_banner():
    """Display ASCII art banner"""
    banner = r"""
 _   _       _     _                 _ 
| | | |     | |   | |               | |
| |_| | __ _| |___| |_ ___  __ _  __| |
|  _  |/ _` | / __| __/ _ \/ _` |/ _` |
| | | | (_| | \__ \ ||  __/ (_| | (_| |
\_| |_/\__,_|_|___/\__\___|\__,_|\__,_|
                                       
"""
    print(f"\033[96m{banner}\033[0m")
    print("\033[96mHalstead Metrics Analyzer\033[0m")
    print("\033[96m=========================\033[0m")

def get_project_root(path: str) -> str:
    """Find project root by looking for .git directory"""
    current_path = Path(path).resolve()
    
    while current_path != current_path.parent:
        if (current_path / ".git").exists():
            return str(current_path)
        current_path = current_path.parent
    
    return path  # Return original path if .git not found

def get_language_patterns() -> Dict[str, Dict[str, List[str]]]:
    """Define language-specific patterns for operators and operands"""
    return {
        "cs": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'%',           # Arithmetic operators
                r'==', r'!=', r'>', r'<', r'>=', r'<=',    # Comparison operators
                r'&&', r'\|\|', r'!',                     # Logical operators
                r'\+=', r'-=', r'\*=', r'/=', r'%=',      # Assignment operators
                r'=', r'\+\+', r'--',                     # Other assignment/increment
                r'\?', r':', r'\|\|', r'&&',              # Ternary and logical
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',   # Bitwise operators
                r'is', r'as', r'new', r'typeof'           # C# specific keywords
            ],
            "operands": [
                r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',           # Identifiers
                r'\b\d+\.?\d*[fFdDmM]?\b',               # Numeric literals
                r'"[^"]*"', r"'[^']*'",                  # String literals
                r'\btrue\b', r'\bfalse\b', r'\bnull\b'   # Boolean and null literals
            ]
        },
        "java": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'%',
                r'==', r'!=', r'>', r'<', r'>=', r'<=',
                r'&&', r'\|\|', r'!',
                r'\+=', r'-=', r'\*=', r'/=', r'%=',
                r'=', r'\+\+', r'--',
                r'\?', r':',
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',
                r'instanceof', r'new'
            ],
            "operands": [
                r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
                r'\b\d+\.?\d*[lLfFdD]?\b',
                r'"[^"]*"', r"'[^']*'",
                r'\btrue\b', r'\bfalse\b', r'\bnull\b'
            ]
        },
        "js": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'%',
                r'===', r'!==', r'==', r'!=', r'>', r'<', r'>=', r'<=',
                r'&&', r'\|\|', r'!',
                r'\+=', r'-=', r'\*=', r'/=', r'%=',
                r'=', r'\+\+', r'--',
                r'\?', r':',
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',
                r'typeof', r'instanceof', r'new', r'delete'
            ],
            "operands": [
                r'\b[a-zA-Z_$][a-zA-Z0-9_$]*\b',
                r'\b\d+\.?\d*\b',
                r'"[^"]*"', r"'[^']*'", r'`[^`]*`',
                r'\btrue\b', r'\bfalse\b', r'\bnull\b', r'\bundefined\b'
            ]
        },
        "ts": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'%',
                r'===', r'!==', r'==', r'!=', r'>', r'<', r'>=', r'<=',
                r'&&', r'\|\|', r'!',
                r'\+=', r'-=', r'\*=', r'/=', r'%=',
                r'=', r'\+\+', r'--',
                r'\?', r':',
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',
                r'typeof', r'instanceof', r'new', r'delete', r'as'
            ],
            "operands": [
                r'\b[a-zA-Z_$][a-zA-Z0-9_$]*\b',
                r'\b\d+\.?\d*\b',
                r'"[^"]*"', r"'[^']*'", r'`[^`]*`',
                r'\btrue\b', r'\bfalse\b', r'\bnull\b', r'\bundefined\b'
            ]
        },
        "py": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'//', r'%', r'\*\*',
                r'==', r'!=', r'>', r'<', r'>=', r'<=',
                r'and', r'or', r'not',
                r'\+=', r'-=', r'\*=', r'/=', r'//=', r'%=', r'\*\*=',
                r'=',
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',
                r'is', r'in', r'lambda'
            ],
            "operands": [
                r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
                r'\b\d+\.?\d*\b',
                r'"[^"]*"', r"'[^']*'", r'"""[^"]*"""', r"'''[^']*'''",
                r'\bTrue\b', r'\bFalse\b', r'\bNone\b'
            ]
        },
        "rb": {
            "operators": [
                r'\+', r'-', r'\*', r'/', r'%', r'\*\*',
                r'==', r'!=', r'>', r'<', r'>=', r'<=', r'<=>',
                r'&&', r'\|\|', r'!', r'and', r'or', r'not',
                r'\+=', r'-=', r'\*=', r'/=', r'%=', r'\*\*=',
                r'=', r'=>',
                r'&', r'\|', r'\^', r'~', r'<<', r'>>',
                r'=~', r'!~'
            ],
            "operands": [
                r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
                r'\b\d+\.?\d*\b',
                r'"[^"]*"', r"'[^']*'",
                r'\btrue\b', r'\bfalse\b', r'\bnil\b'
            ]
        }
    }

def get_halstead_metrics(file_path: str, language: str) -> Dict[str, float]:
    """Calculate Halstead metrics for a file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read file {file_path} as text. It might be a binary file: {e}")
        return {
            'vocabulary': 0, 'length': 0, 'volume': 0,
            'difficulty': 0, 'effort': 0, 'time': 0, 'bugs': 0
        }
    
    if not content.strip():
        print(f"Warning: File {file_path} is empty or could not be read.")
        return {
            'vocabulary': 0, 'length': 0, 'volume': 0,
            'difficulty': 0, 'effort': 0, 'time': 0, 'bugs': 0
        }
    
    # Get language patterns
    patterns = get_language_patterns()
    lang_patterns = patterns.get(language, patterns.get('py', {}))  # Default to Python
    
    unique_operators = defaultdict(int)
    unique_operands = defaultdict(int)
    total_operators = 0
    total_operands = 0
    
    # Count operators
    for pattern in lang_patterns.get('operators', []):
        try:
            matches = re.findall(pattern, content)
            for match in matches:
                unique_operators[match] += 1
                total_operators += 1
        except Exception as e:
            print(f"Warning: Error matching operator pattern '{pattern}': {e}")
    
    # Count operands
    for pattern in lang_patterns.get('operands', []):
        try:
            matches = re.findall(pattern, content)
            for match in matches:
                unique_operands[match] += 1
                total_operands += 1
        except Exception as e:
            print(f"Warning: Error matching operand pattern '{pattern}': {e}")
    
    # Calculate Halstead metrics
    n1 = len(unique_operators)    # Number of unique operators
    n2 = len(unique_operands)     # Number of unique operands
    N1 = total_operators          # Total number of operators
    N2 = total_operands           # Total number of operands
    
    # Avoid division by zero
    if n1 == 0 or n2 == 0:
        return {
            'vocabulary': 0, 'length': 0, 'volume': 0,
            'difficulty': 0, 'effort': 0, 'time': 0, 'bugs': 0
        }
    
    vocabulary = n1 + n2                      # Program vocabulary
    length = N1 + N2                          # Program length
    volume = length * math.log2(vocabulary)   # Program volume
    difficulty = (n1 / 2) * (N2 / n2)        # Program difficulty
    effort = volume * difficulty              # Programming effort
    time = effort / 18                        # Time to implement (in seconds)
    bugs = volume / 3000                      # Estimated number of bugs
    
    return {
        'vocabulary': round(vocabulary, 2),
        'length': length,
        'volume': round(volume, 2),
        'difficulty': round(difficulty, 2),
        'effort': round(effort, 2),
        'time': round(time, 2),
        'bugs': round(bugs, 3)
    }

def get_language_from_extension(file_path: str) -> str:
    """Determine language from file extension"""
    ext = Path(file_path).suffix.lower().lstrip('.')
    language_map = {
        'cs': 'cs',
        'java': 'java',
        'js': 'js',
        'ts': 'ts',
        'py': 'py',
        'rb': 'rb',
        'php': 'php',
        'go': 'go',
        'cpp': 'cpp',
        'c': 'c',
        'h': 'c',
        'hpp': 'cpp'
    }
    return language_map.get(ext, 'unknown')

def find_files_to_analyze(repo_path: str, file_extensions: List[str], 
                         exclude_patterns: List[str], max_files: int,
                         files_to_analyze_file: str = None) -> List[Path]:
    """Find files to analyze based on criteria"""
    files_to_analyze = []
    
    # Check for files-to-be-analyzed.txt if no specific file provided
    if not files_to_analyze_file:
        default_files_list = Path(repo_path) / "files-to-be-analyzed.txt"
        if default_files_list.exists():
            files_to_analyze_file = str(default_files_list)
            print(f"\033[92mFound default files list: {default_files_list}\033[0m")
    
    if files_to_analyze_file and Path(files_to_analyze_file).exists():
        print(f"\033[93mReading files from: {files_to_analyze_file}\033[0m")
        
        try:
            with open(files_to_analyze_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue  # Skip empty lines and comments
                    
                    # Convert relative paths to absolute paths
                    if not Path(line).is_absolute():
                        file_path = Path(repo_path) / line
                    else:
                        file_path = Path(line)
                    
                    if file_path.exists() and file_path.is_file():
                        files_to_analyze.append(file_path)
                    else:
                        print(f"Warning: File not found: {file_path}")
            
            print(f"\033[92mLoaded {len(files_to_analyze)} files from the provided list.\033[0m")
            
        except Exception as e:
            print(f"Error reading files list: {e}")
            sys.exit(1)
    else:
        # Default behavior: scan repository for files matching extensions
        print(f"\033[93mNo files list provided. Scanning repository for files matching extensions...\033[0m")
        
        repo_path_obj = Path(repo_path)
        for ext in file_extensions:
            for file_path in repo_path_obj.rglob(f"*.{ext}"):
                # Check exclusion patterns
                should_exclude = any(pattern in str(file_path) for pattern in exclude_patterns)
                
                if not should_exclude:
                    files_to_analyze.append(file_path)
                
                # Limit the number of files if MaxFiles is set
                if max_files > 0 and len(files_to_analyze) >= max_files:
                    print(f"\033[93mReached maximum file limit ({max_files}). Use --max-files parameter to adjust.\033[0m")
                    break
            
            if max_files > 0 and len(files_to_analyze) >= max_files:
                break
    
    return files_to_analyze

def generate_report(results: List[Dict[str, Any]], output_file: str, repo_path: str):
    """Generate markdown report"""
    if not results:
        print("No files were analyzed. Cannot generate report.")
        return
    
    # Sort results by effort (descending)
    sorted_results = sorted(results, key=lambda x: x['effort'], reverse=True)
    
    # Calculate summary statistics
    total_files = len(results)
    avg_volume = sum(r['volume'] for r in results) / total_files
    avg_difficulty = sum(r['difficulty'] for r in results) / total_files
    avg_effort = sum(r['effort'] for r in results) / total_files
    total_effort = sum(r['effort'] for r in results)
    total_bugs = sum(r['bugs'] for r in results)
    
    # High complexity files (effort > 100000)
    high_complexity_files = [r for r in sorted_results if r['effort'] > 100000]
    
    report = f"""# Halstead Complexity Metrics Analysis

## Summary

- **Repository**: {repo_path}
- **Files Analyzed**: {total_files}
- **Average Volume**: {avg_volume:.2f}
- **Average Difficulty**: {avg_difficulty:.2f}
- **Average Effort**: {avg_effort:.2f}
- **Total Effort**: {total_effort:.2f}
- **Total Estimated Bugs**: {total_bugs:.3f}

## High-Complexity Files Requiring Attention

Files with **Effort > 100,000** should be prioritized for refactoring:

"""
    
    if high_complexity_files:
        report += "| File | Volume | Difficulty | Effort | Est. Time (min) | Est. Bugs |\n"
        report += "|------|--------|------------|--------|-----------------|----------|\n"
        
        for item in high_complexity_files:
            time_in_minutes = round(item['time'] / 60, 1)
            report += f"| {item['file']} | {item['volume']} | {item['difficulty']} | {item['effort']} | {time_in_minutes} | {item['bugs']} |\n"
        
        report += "\n\n**These files should be prioritized for refactoring, simplification, and documentation.**\n"
    else:
        report += "\n\n_No files exceeded high-complexity thresholds for refactoring._\n"
    
    report += """

## Files Ranked by Effort

The following files require the most effort to understand and maintain:

| File | Volume | Difficulty | Effort | Est. Time (min) | Est. Bugs |
|------|--------|------------|--------|----------------|-----------|
"""
    
    for item in sorted_results[:20]:  # Top 20 files
        time_in_minutes = round(item['time'] / 60, 1)
        report += f"| {item['file']} | {item['volume']} | {item['difficulty']} | {item['effort']} | {time_in_minutes} | {item['bugs']} |\n"
    
    report += "\n\n## Files Grouped by Language\n"
    
    # Group by language
    language_groups = defaultdict(list)
    for result in results:
        language_groups[result['language']].append(result)
    
    for language, group in language_groups.items():
        lang_avg_volume = sum(r['volume'] for r in group) / len(group)
        lang_avg_difficulty = sum(r['difficulty'] for r in group) / len(group)
        lang_avg_effort = sum(r['effort'] for r in group) / len(group)
        
        report += f"""
### {language} Files ({len(group)} files)

- **Average Volume**: {lang_avg_volume:.2f}
- **Average Difficulty**: {lang_avg_difficulty:.2f}
- **Average Effort**: {lang_avg_effort:.2f}

"""
    
    report += """

## Recommendations

Based on the Halstead metrics analysis:

1. **Focus Refactoring Efforts**: Files with high Effort values should be prioritized for refactoring.
2. **Documentation**: Files with high Difficulty should be well-documented.
3. **Code Reviews**: High Volume files should receive thorough code reviews.
4. **Testing**: Files with higher estimated bug counts should have comprehensive test coverage.

## Interpretation Guide

- **Volume < 1000**: Simple, straightforward code
- **Volume 1000-10000**: Moderate complexity
- **Volume > 10000**: High complexity, consider refactoring

- **Difficulty < 10**: Easy to understand
- **Difficulty 10-20**: Moderate difficulty
- **Difficulty > 20**: Difficult to understand, may need simplification

- **Effort < 10000**: Low effort required
- **Effort 10000-100000**: Moderate effort required
- **Effort > 100000**: High effort required, consider refactoring

## Notes on Accuracy

This analysis provides approximate Halstead metrics. For more accurate results, consider using language-specific static analysis tools.

"""
    
    # Write report to file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\033[92mAnalysis complete. Report saved to {output_file}\033[0m")

def main():
    parser = argparse.ArgumentParser(description='Analyze Halstead complexity metrics for source code files')
    parser.add_argument('--repo-path', default='.', help='Path to the repository to analyze')
    parser.add_argument('--output-file', help='Path to the output markdown file')
    parser.add_argument('--file-extensions', nargs='+', 
                       default=['cs', 'java', 'js', 'ts', 'py', 'rb', 'php', 'go', 'cpp', 'c', 'h', 'hpp'],
                       help='File extensions to analyze (without the dot)')
    parser.add_argument('--exclude-patterns', nargs='+',
                       default=['node_modules', 'dist', 'bin', 'obj', 'build', 'target', 'vendor', 'packages'],
                       help='Patterns to exclude from analysis')
    parser.add_argument('--max-files', type=int, default=500,
                       help='Maximum number of files to analyze (0 for unlimited)')
    parser.add_argument('--files-to-analyze-file',
                       help='Path to a text file containing a list of files to analyze')
    
    args = parser.parse_args()
    
    try:
        show_banner()
        
        # Determine project root and output file
        project_root = get_project_root(args.repo_path)
        if project_root == args.repo_path:
            print(f"Warning: Could not find .git directory, using specified path as project root: {args.repo_path}")
        else:
            print(f"Project root found: {project_root}")
        
        # Set default output file if not provided
        if not args.output_file:
            findings_dir = Path(project_root) / "olaf-data" / "findings"
            findings_dir.mkdir(parents=True, exist_ok=True)
            args.output_file = str(findings_dir / "halstead-metrics.md")
            print(f"Created findings directory: {findings_dir}")
        
        # Get all files to analyze
        print("\033[92mFinding files to analyze...\033[0m")
        
        files_to_analyze = find_files_to_analyze(
            project_root, args.file_extensions, args.exclude_patterns,
            args.max_files, args.files_to_analyze_file
        )
        
        if not files_to_analyze:
            print("No files found to analyze.")
            sys.exit(1)
        
        print(f"Found {len(files_to_analyze)} files to analyze.")
        
        # Analyze files
        results = []
        for i, file_path in enumerate(files_to_analyze, 1):
            print(f"Analyzing {i}/{len(files_to_analyze)}: {file_path.name}")
            
            language = get_language_from_extension(str(file_path))
            metrics = get_halstead_metrics(str(file_path), language)
            
            relative_path = file_path.relative_to(project_root)
            
            result = {
                'file': str(relative_path),
                'language': language,
                **metrics
            }
            results.append(result)
        
        # Generate report
        generate_report(results, args.output_file, project_root)
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()