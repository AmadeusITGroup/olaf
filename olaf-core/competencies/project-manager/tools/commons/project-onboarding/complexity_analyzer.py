#!/usr/bin/env python3
"""
Cyclomatic Complexity Analyzer for Project Onboarding

Analyzes cyclomatic complexity across multiple programming languages,
providing detailed function-level and file-level complexity metrics.

Based on PowerShell analyze-cyclomatic-complexity.ps1 from OLAF toolkit.
"""

import os
import re
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, NamedTuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FunctionComplexity(NamedTuple):
    """Represents complexity metrics for a function."""
    name: str
    start_line: int
    end_line: int
    line_count: int
    complexity: int
    complexity_density: float


class ComplexityAnalyzer:
    """Analyzes cyclomatic complexity for source code files."""
    
    # Language-specific function patterns
    FUNCTION_PATTERNS = {
        'cs': r'(?:public|private|protected|internal|static)?\s+\w+\s+(\w+)\s*\([^)]*\)\s*(?:{|\n*{)',
        'java': r'(?:public|private|protected|static|final)?\s+\w+\s+(\w+)\s*\([^)]*\)\s*(?:{|\n*{)',
        'js': r'(?:function\s+(\w+)|(\w+)\s*[:=]\s*function|\(.*\)\s*=>\s*{|(\w+)\s*\(.*\)\s*{)',
        'ts': r'(?:(?:public|private|protected|static|async|export)\s+)*(?:\w+\s+)?(\w+)\s*\([^)]*\)(?:\s*:\s*[\w<>|\[\]\s]+)?\s*\{',
        'py': r'def\s+(\w+)\s*\(',
        'go': r'func\s+(?:\([^)]*\)\s+)?(\w+)\s*\([^)]*\)(?:\s*\([^)]*\))?\s*{',
        'rs': r'fn\s+(\w+)\s*\([^)]*\)(?:\s*->\s*[^{]+)?\s*{',
        'php': r'(?:public|private|protected)?\s*function\s+(\w+)\s*\([^)]*\)\s*{',
        'rb': r'def\s+(\w+)(?:\([^)]*\))?\s*$',
        'cpp': r'(?:\w+\s+)*(\w+)\s*\([^)]*\)\s*(?:const\s*)?{',
        'c': r'(?:\w+\s+)*(\w+)\s*\([^)]*\)\s*{',
        'default': r'(?:function\s+)?(\w+)\s*\([^)]*\)\s*\{'
    }
    
    # Complexity-increasing patterns (language-agnostic)
    COMPLEXITY_PATTERNS = [
        r'if\s*\(',
        r'else\s+if',
        r'else\b',
        r'switch\s*\(',
        r'case\s+',
        r'for\s*\(',
        r'foreach\s*\(',
        r'while\s*\(',
        r'do\s*{',
        r'\?\s*',
        r'\|\|',
        r'&&',
        r'except\b',
        r'catch\b',
        r'finally\b'
    ]
    
    # File extensions to language mapping
    LANGUAGE_MAP = {
        '.cs': 'cs',
        '.java': 'java',
        '.js': 'js',
        '.jsx': 'js',
        '.ts': 'ts',
        '.tsx': 'ts',
        '.py': 'py',
        '.go': 'go',
        '.rs': 'rs',
        '.php': 'php',
        '.rb': 'rb',
        '.cpp': 'cpp',
        '.cc': 'cpp',
        '.cxx': 'cpp',
        '.c': 'c',
        '.h': 'c',
        '.hpp': 'cpp'
    }
    
    def __init__(self, repo_path: str, output_file: str = None, complexity_threshold: int = 10):
        self.repo_path = Path(repo_path).resolve()
        self.output_file = output_file or self.repo_path / "cyclomatic-complexity.md"
        self.complexity_threshold = complexity_threshold
        self.exclude_patterns = [
            'node_modules', 'dist', 'bin', 'obj', 'build', 'target', 
            'vendor', 'packages', '.git', '__pycache__', '.pytest_cache'
        ]
        
    def should_exclude_file(self, file_path: Path) -> bool:
        """Check if file should be excluded from analysis."""
        path_str = str(file_path)
        return any(pattern in path_str for pattern in self.exclude_patterns)
    
    def get_source_files(self) -> List[Path]:
        """Get all source files to analyze."""
        source_files = []
        
        for ext in self.LANGUAGE_MAP.keys():
            pattern = f"**/*{ext}"
            files = self.repo_path.glob(pattern)
            for file_path in files:
                if not self.should_exclude_file(file_path):
                    source_files.append(file_path)
        
        return sorted(source_files)
    
    def analyze_file_complexity(self, file_path: Path) -> List[FunctionComplexity]:
        """Analyze cyclomatic complexity for a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()
        except (IOError, UnicodeDecodeError) as e:
            logger.warning(f"Could not read {file_path}: {e}")
            return []
        
        if not content:
            return []
        
        language = self.LANGUAGE_MAP.get(file_path.suffix.lower(), 'default')
        
        if language == 'py':
            return self._analyze_python_complexity(content)
        else:
            return self._analyze_brace_language_complexity(content, language)
    
    def _analyze_python_complexity(self, content: List[str]) -> List[FunctionComplexity]:
        """Analyze Python files using indentation-based parsing."""
        functions = []
        current_function = None
        indent_stack = []
        
        for i, line in enumerate(content):
            stripped = line.strip()
            
            # Skip empty lines and comments
            if not stripped or stripped.startswith('#'):
                continue
            
            # Calculate indentation level
            indent = len(line) - len(line.lstrip())
            
            # Check for function definition
            func_match = re.match(r'def\s+(\w+)\s*\(', stripped)
            if func_match:
                function_name = func_match.group(1)
                
                current_function = {
                    'name': function_name,
                    'start_line': i + 1,
                    'end_line': 0,
                    'lines': [],
                    'complexity': 1,  # Base complexity
                    'indent_level': indent
                }
                
                indent_stack.append(current_function)
            
            # Process lines within functions
            if indent_stack:
                current_function = indent_stack[-1]
                current_function['lines'].append(line)
                
                # Count complexity-increasing constructs
                if re.search(r'^\s*(?:if|elif|else|for|while|except|finally)\b', line):
                    current_function['complexity'] += 1
                
                # Count logical operators
                and_count = len(re.findall(r'\band\b', line))
                or_count = len(re.findall(r'\bor\b', line))
                current_function['complexity'] += and_count + or_count
                
                # Check if function has ended
                if i + 1 < len(content):
                    next_line = content[i + 1]
                    next_stripped = next_line.strip()
                    
                    if next_stripped and not next_stripped.startswith('#'):
                        next_indent = len(next_line) - len(next_line.lstrip())
                        
                        if next_indent <= current_function['indent_level']:
                            current_function['end_line'] = i + 1
                            line_count = current_function['end_line'] - current_function['start_line'] + 1
                            complexity_density = round(current_function['complexity'] / line_count, 3)
                            
                            functions.append(FunctionComplexity(
                                name=current_function['name'],
                                start_line=current_function['start_line'],
                                end_line=current_function['end_line'],
                                line_count=line_count,
                                complexity=current_function['complexity'],
                                complexity_density=complexity_density
                            ))
                            
                            indent_stack.pop()
                else:
                    # End of file
                    current_function['end_line'] = i + 1
                    line_count = current_function['end_line'] - current_function['start_line'] + 1
                    complexity_density = round(current_function['complexity'] / line_count, 3)
                    
                    functions.append(FunctionComplexity(
                        name=current_function['name'],
                        start_line=current_function['start_line'],
                        end_line=current_function['end_line'],
                        line_count=line_count,
                        complexity=current_function['complexity'],
                        complexity_density=complexity_density
                    ))
        
        return functions
    
    def _analyze_brace_language_complexity(self, content: List[str], language: str) -> List[FunctionComplexity]:
        """Analyze brace-based languages (C, Java, JavaScript, etc.)."""
        functions = []
        current_function = None
        brace_count = 0
        in_function = False
        
        function_pattern = self.FUNCTION_PATTERNS.get(language, self.FUNCTION_PATTERNS['default'])
        
        for i, line in enumerate(content):
            # Check for function declaration
            if not in_function:
                func_match = re.search(function_pattern, line)
                if func_match:
                    # Extract function name from capture groups
                    function_name = None
                    for group in func_match.groups():
                        if group and group.strip() and not re.match(r'^(public|private|protected|internal|static|final|function|def|async|export)$', group.strip()):
                            function_name = group.strip()
                            break
                    
                    if not function_name:
                        function_name = f"Anonymous_Function_Line_{i+1}"
                    
                    current_function = {
                        'name': function_name,
                        'start_line': i + 1,
                        'end_line': 0,
                        'lines': [],
                        'complexity': 1  # Base complexity
                    }
                    
                    in_function = True
                    brace_count = 0
            
            if in_function:
                current_function['lines'].append(line)
                
                # Count braces
                open_braces = line.count('{')
                close_braces = line.count('}')
                brace_count += open_braces - close_braces
                
                # Count complexity patterns
                for pattern in self.COMPLEXITY_PATTERNS:
                    matches = len(re.findall(pattern, line))
                    current_function['complexity'] += matches
                
                # Check if function has ended
                if brace_count == 0 and '}' in line:
                    current_function['end_line'] = i + 1
                    line_count = current_function['end_line'] - current_function['start_line'] + 1
                    complexity_density = round(current_function['complexity'] / line_count, 3)
                    
                    functions.append(FunctionComplexity(
                        name=current_function['name'],
                        start_line=current_function['start_line'],
                        end_line=current_function['end_line'],
                        line_count=line_count,
                        complexity=current_function['complexity'],
                        complexity_density=complexity_density
                    ))
                    
                    in_function = False
                    current_function = None
        
        return functions
    
    def calculate_file_level_complexity(self, file_path: Path) -> FunctionComplexity:
        """Calculate file-level complexity if no functions found."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()
        except (IOError, UnicodeDecodeError):
            return FunctionComplexity("File_Level", 1, 1, 0, 0, 0.0)
        
        if not content:
            return FunctionComplexity("File_Level", 1, 1, 0, 0, 0.0)
        
        file_complexity = 1  # Base complexity
        
        for line in content:
            for pattern in self.COMPLEXITY_PATTERNS:
                matches = len(re.findall(pattern, line))
                file_complexity += matches
        
        line_count = len(content)
        complexity_density = round(file_complexity / line_count, 3) if line_count > 0 else 0.0
        
        return FunctionComplexity(
            name="File_Level",
            start_line=1,
            end_line=line_count,
            line_count=line_count,
            complexity=file_complexity,
            complexity_density=complexity_density
        )
    
    def analyze_repository(self) -> Dict:
        """Analyze entire repository for complexity."""
        logger.info(f"Analyzing repository: {self.repo_path}")
        
        source_files = self.get_source_files()
        logger.info(f"Found {len(source_files)} source files")
        
        all_results = []
        files_analyzed = 0
        
        for file_path in source_files:
            files_analyzed += 1
            if files_analyzed % 50 == 0:
                logger.info(f"Analyzed {files_analyzed}/{len(source_files)} files")
            
            relative_path = file_path.relative_to(self.repo_path)
            functions = self.analyze_file_complexity(file_path)
            
            if not functions:
                # No functions found, use file-level complexity
                file_complexity = self.calculate_file_level_complexity(file_path)
                functions = [file_complexity]
            
            for func in functions:
                all_results.append({
                    'file': str(relative_path),
                    'function': func.name,
                    'start_line': func.start_line,
                    'end_line': func.end_line,
                    'line_count': func.line_count,
                    'complexity': func.complexity,
                    'complexity_density': func.complexity_density
                })
        
        return {
            'results': all_results,
            'files_analyzed': len(source_files),
            'total_functions': len(all_results)
        }
    
    def generate_report(self, analysis_data: Dict) -> str:
        """Generate comprehensive complexity analysis report."""
        results = analysis_data['results']
        files_analyzed = analysis_data['files_analyzed']
        total_functions = analysis_data['total_functions']
        
        # Sort by complexity (highest first)
        sorted_results = sorted(results, key=lambda x: x['complexity'], reverse=True)
        
        # Calculate statistics
        complexities = [r['complexity'] for r in results]
        avg_complexity = sum(complexities) / len(complexities) if complexities else 0
        max_complexity = max(complexities) if complexities else 0
        complex_functions = len([r for r in results if r['complexity'] > self.complexity_threshold])
        percent_complex = round((complex_functions / total_functions) * 100, 1) if total_functions > 0 else 0
        
        # Complexity distribution
        ranges = [
            {'name': 'Low (1-5)', 'min': 1, 'max': 5},
            {'name': 'Moderate (6-10)', 'min': 6, 'max': 10},
            {'name': 'High (11-20)', 'min': 11, 'max': 20},
            {'name': 'Very High (21-50)', 'min': 21, 'max': 50},
            {'name': 'Extremely High (50+)', 'min': 51, 'max': float('inf')}
        ]
        
        distribution = []
        for range_info in ranges:
            count = len([r for r in results if range_info['min'] <= r['complexity'] <= range_info['max']])
            percent = round((count / total_functions) * 100, 1) if total_functions > 0 else 0
            distribution.append({'range': range_info['name'], 'count': count, 'percent': percent})
        
        # Generate report
        timestamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
        
        report = f"""# Cyclomatic Complexity Analysis Report

Analysis performed on: {timestamp}  
Repository: {self.repo_path}  
Files analyzed: {files_analyzed}  
Functions/methods analyzed: {total_functions}

## Overview

Cyclomatic Complexity (CC) measures the number of linearly independent paths through a program's source code.
It directly corresponds to the number of test cases needed to achieve complete branch coverage.

## Summary Statistics

- **Average Complexity**: {round(avg_complexity, 2)}
- **Maximum Complexity**: {max_complexity}
- **Functions with CC > {self.complexity_threshold}**: {complex_functions} ({percent_complex}%)

## Complexity Distribution

| Complexity Range | Function Count | Percentage |
|------------------|---------------|-----------|
"""
        
        for dist in distribution:
            report += f"| {dist['range']} | {dist['count']} | {dist['percent']}% |\n"
        
        report += """
## Most Complex Functions

The following functions have the highest cyclomatic complexity (ordered from most to least complex):

| File | Function | Line | Line Count | Complexity | Density |
|------|----------|------|-----------|------------|---------|
"""
        
        for item in sorted_results[:20]:
            report += f"| {item['file']} | {item['function']} | {item['start_line']} | {item['line_count']} | {item['complexity']} | {item['complexity_density']} |\n"
        
        report += f"""
## Functions Exceeding Threshold (CC > {self.complexity_threshold})

The following functions exceed the complexity threshold and should be prioritized for refactoring:

| File | Function | Line | Line Count | Complexity | Density |
|------|----------|------|-----------|------------|---------|
"""
        
        high_complexity = [r for r in sorted_results if r['complexity'] > self.complexity_threshold]
        for item in high_complexity:
            report += f"| {item['file']} | {item['function']} | {item['start_line']} | {item['line_count']} | {item['complexity']} | {item['complexity_density']} |\n"
        
        report += """
## Recommendations

Based on the cyclomatic complexity analysis:

1. **Refactor High-Complexity Functions**: Functions with CC > 10 should be refactored into smaller, more focused units.
   - Consider extracting complex conditions into separate functions
   - Break large functions into smaller, more manageable pieces
   - Simplify nested conditionals with early returns or guard clauses

2. **Increase Test Coverage**: Functions with high complexity need more thorough testing.
   - Each decision point (if, loop, etc.) represents a path that should be tested
   - High-complexity functions may need specific focus in your test suite

3. **Code Review Focus**: Direct extra attention to high-complexity areas during code reviews.

4. **Documentation**: Ensure complex logic is well-documented to aid understanding.

## Complexity Risk Categories

| Complexity | Risk | Recommendation |
|------------|------|---------------|
| 1-5 | Low | Simple, well-structured code. Generally easy to maintain. |
| 6-10 | Moderate | Reasonably complex. May need minor refactoring. |
| 11-20 | High | Complex code. Should be refactored and well-tested. |
| 21-50 | Very High | Excessively complex. High priority for refactoring. |
| 50+ | Extremely High | Unmaintainable code. Critical priority for refactoring. |

## Notes on Accuracy

This analysis provides approximate cyclomatic complexity. For more accurate results, consider using language-specific static analysis tools.

---
*Generated by OLAF Complexity Analyzer*
"""
        
        return report
    
    def run_analysis(self) -> None:
        """Run complete complexity analysis."""
        analysis_data = self.analyze_repository()
        report = self.generate_report(analysis_data)
        
        # Save report
        output_path = Path(self.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Analysis complete. Report saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Analyze cyclomatic complexity')
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('-o', '--output', help='Output file path', default=None)
    parser.add_argument('-t', '--threshold', type=int, default=10, help='Complexity threshold')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not os.path.exists(args.repo_path):
        logger.error(f"Repository path does not exist: {args.repo_path}")
        sys.exit(1)
    
    analyzer = ComplexityAnalyzer(args.repo_path, args.output, args.threshold)
    analyzer.run_analysis()


if __name__ == '__main__':
    main()
