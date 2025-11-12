#!/usr/bin/env python3
"""
Code Hotspot Analyzer for Project Onboarding

Identifies complexity hotspots by analyzing Git history and code complexity,
combining change frequency with complexity metrics to find problematic areas.

Based on PowerShell identify-complexity-hotspots.ps1 from OLAF toolkit.
"""

import os
import re
import subprocess
import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, NamedTuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileHotspot(NamedTuple):
    """Represents a code hotspot with change frequency and complexity metrics."""
    file_path: str
    change_frequency: int
    line_count: int
    conditional_count: int
    conditional_density: float
    complexity_score: float


class HotspotAnalyzer:
    """Analyzes code hotspots by combining Git history and complexity metrics."""
    
    def __init__(self, repo_path: str, output_file: str = None, months_to_analyze: int = 12):
        self.repo_path = Path(repo_path).resolve()
        self.output_file = output_file or self.repo_path / "complexity-hotspots.md"
        self.months_to_analyze = months_to_analyze
        self.file_extensions = [
            '.cs', '.java', '.js', '.jsx', '.ts', '.tsx', '.py', '.rb', 
            '.php', '.go', '.rs', '.cpp', '.c', '.h', '.hpp'
        ]
        self.exclude_patterns = [
            'node_modules', 'dist', 'bin', 'obj', 'build', 'target', 
            'vendor', 'packages', '.git', '__pycache__', '.pytest_cache'
        ]
        
    def is_git_repository(self) -> bool:
        """Check if the path is a Git repository."""
        git_dir = self.repo_path / '.git'
        return git_dir.exists()
    
    def should_exclude_file(self, file_path: str) -> bool:
        """Check if file should be excluded from analysis."""
        return any(pattern in file_path for pattern in self.exclude_patterns)
    
    def get_file_extension(self, file_path: str) -> str:
        """Get file extension in lowercase."""
        return Path(file_path).suffix.lower()
    
    def is_source_file(self, file_path: str) -> bool:
        """Check if file is a source code file we want to analyze."""
        if self.should_exclude_file(file_path):
            return False
        
        extension = self.get_file_extension(file_path)
        return extension in self.file_extensions
    
    def get_git_changed_files(self) -> Dict[str, int]:
        """Get frequently changed files from Git history."""
        if not self.is_git_repository():
            logger.warning("Not a Git repository, will analyze all source files")
            return self._get_all_source_files()
        
        # Calculate date for git log
        since_date = datetime.now() - timedelta(days=30 * self.months_to_analyze)
        since_str = since_date.strftime('%Y-%m-%d')
        
        logger.info(f"Analyzing Git history since {since_str}")
        
        try:
            # Get changed files from git log
            cmd = [
                'git', 'log', f'--since={since_str}', 
                '--name-only', '--pretty=format:'
            ]
            
            result = subprocess.run(
                cmd, 
                cwd=self.repo_path, 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            # Process git log output
            changed_files = {}
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line and self.is_source_file(line):
                    changed_files[line] = changed_files.get(line, 0) + 1
            
            if not changed_files:
                logger.warning("No Git history found, analyzing all source files")
                return self._get_all_source_files()
            
            logger.info(f"Found {len(changed_files)} changed files in Git history")
            return changed_files
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Git command failed: {e}")
            return self._get_all_source_files()
        except FileNotFoundError:
            logger.error("Git not found in PATH")
            return self._get_all_source_files()
    
    def _get_all_source_files(self) -> Dict[str, int]:
        """Get all source files as fallback when Git history is unavailable."""
        all_files = {}
        
        for ext in self.file_extensions:
            pattern = f"**/*{ext}"
            files = self.repo_path.glob(pattern)
            
            for file_path in files:
                if not self.should_exclude_file(str(file_path)):
                    relative_path = file_path.relative_to(self.repo_path)
                    all_files[str(relative_path)] = 1  # Assign weight of 1
        
        logger.info(f"Found {len(all_files)} source files")
        return all_files
    
    def analyze_file_complexity(self, file_path: Path) -> Tuple[int, int]:
        """Analyze complexity metrics for a single file."""
        if not file_path.exists():
            return 0, 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()
        except (IOError, UnicodeDecodeError) as e:
            logger.warning(f"Could not read {file_path}: {e}")
            return 0, 0
        
        if not content:
            return 0, 0
        
        line_count = len(content)
        conditional_count = 0
        
        # Complexity patterns (simplified cyclomatic complexity indicators)
        complexity_patterns = [
            r'if\s*\(',           # if statements
            r'else\s*{',          # else blocks
            r'else\s+if',         # else if
            r'switch\s*\(',       # switch statements
            r'case\s+[^:]*:',     # case statements
            r'for\s*\(',          # for loops
            r'while\s*\(',        # while loops
            r'do\s*{',            # do-while loops
            r'\?\s*.*\s*:',       # ternary operators
            r'&&',                # logical AND
            r'\|\|',              # logical OR
            r'catch\s*\(',        # exception handling
            r'except\s*:',        # Python exception handling
            r'finally\s*:',       # finally blocks
        ]
        
        for line in content:
            for pattern in complexity_patterns:
                matches = len(re.findall(pattern, line, re.IGNORECASE))
                conditional_count += matches
        
        return line_count, conditional_count
    
    def analyze_hotspots(self) -> List[FileHotspot]:
        """Analyze code hotspots combining change frequency and complexity."""
        changed_files = self.get_git_changed_files()
        hotspots = []
        
        # Analyze top changed files (limit to avoid excessive processing)
        top_files = sorted(changed_files.items(), key=lambda x: x[1], reverse=True)[:50]
        
        logger.info(f"Analyzing complexity for {len(top_files)} files")
        
        for file_path, change_frequency in top_files:
            full_path = self.repo_path / file_path
            
            if not full_path.exists():
                continue
            
            line_count, conditional_count = self.analyze_file_complexity(full_path)
            
            if line_count == 0:
                continue
            
            # Calculate metrics
            conditional_density = conditional_count / line_count if line_count > 0 else 0
            complexity_score = change_frequency * conditional_density * 100
            
            hotspot = FileHotspot(
                file_path=file_path,
                change_frequency=change_frequency,
                line_count=line_count,
                conditional_count=conditional_count,
                conditional_density=round(conditional_density, 3),
                complexity_score=round(complexity_score, 1)
            )
            
            hotspots.append(hotspot)
        
        # Sort by complexity score (highest first)
        return sorted(hotspots, key=lambda x: x.complexity_score, reverse=True)
    
    def generate_report(self, hotspots: List[FileHotspot]) -> str:
        """Generate comprehensive hotspot analysis report."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        since_date = (datetime.now() - timedelta(days=30 * self.months_to_analyze)).strftime('%Y-%m-%d')
        
        report = f"""# Complexity Hotspots Analysis

Analysis performed on: {timestamp}  
Repository: {self.repo_path}  
Period analyzed: {self.months_to_analyze} months (since {since_date})

## Executive Summary

This analysis identified {len(hotspots)} potential complexity hotspots by combining:
- **Change Frequency**: How often files have been modified
- **Complexity Metrics**: Density of conditional statements and control flow
- **Risk Score**: Combined metric indicating maintenance risk

## Top Complexity Hotspots

Files with high change frequency and complexity (top 20):

| File | Change Frequency | Lines | Conditionals | Conditional Density | Complexity Score |
|------|-----------------|-------|-------------|-------------------|----------------|
"""
        
        for hotspot in hotspots[:20]:
            report += f"| {hotspot.file_path} | {hotspot.change_frequency} | {hotspot.line_count} | {hotspot.conditional_count} | {hotspot.conditional_density} | {hotspot.complexity_score} |\n"
        
        # Calculate statistics
        if hotspots:
            avg_score = sum(h.complexity_score for h in hotspots) / len(hotspots)
            max_score = max(h.complexity_score for h in hotspots)
            high_risk_count = len([h for h in hotspots if h.complexity_score > avg_score * 1.5])
            
            report += f"""
## Analysis Statistics

- **Total Files Analyzed**: {len(hotspots)}
- **Average Complexity Score**: {round(avg_score, 1)}
- **Maximum Complexity Score**: {max_score}
- **High-Risk Files** (>1.5x average): {high_risk_count}

## Risk Categories

Based on complexity scores, files are categorized as:

| Risk Level | Score Range | Count | Recommendation |
|------------|-------------|-------|----------------|
"""
            
            # Define risk categories
            categories = [
                ("Low", 0, avg_score * 0.5, "Monitor during regular maintenance"),
                ("Medium", avg_score * 0.5, avg_score, "Include in code review focus"),
                ("High", avg_score, avg_score * 1.5, "Priority for refactoring"),
                ("Critical", avg_score * 1.5, float('inf'), "Immediate attention required")
            ]
            
            for risk_level, min_score, max_score, recommendation in categories:
                count = len([h for h in hotspots if min_score <= h.complexity_score < max_score])
                score_range = f"{round(min_score, 1)}-{round(max_score, 1) if max_score != float('inf') else '∞'}"
                report += f"| {risk_level} | {score_range} | {count} | {recommendation} |\n"
        
        report += f"""
## Analysis Methodology

This report identifies potential complexity hotspots by combining:

1. **Change Frequency**: How often a file has been modified in the last {self.months_to_analyze} months
2. **Conditional Density**: The ratio of conditional statements to total lines of code
3. **Complexity Score**: Change frequency × conditional density × 100

Higher scores indicate files that are both frequently changed and complex, which may benefit from refactoring.

### Complexity Indicators

The analysis counts the following complexity indicators:
- Conditional statements (if, else, switch)
- Loop constructs (for, while, do-while)
- Logical operators (&&, ||)
- Exception handling (try, catch, finally)
- Ternary operators

## Recommendations

### Immediate Actions

For files with **Critical** risk scores:
1. **Code Review**: Conduct thorough review of high-scoring files
2. **Refactoring**: Break down complex functions into smaller units
3. **Testing**: Ensure comprehensive test coverage
4. **Documentation**: Add detailed comments for complex logic

### Medium-term Improvements

1. **Extract Methods**: Break large functions into smaller, focused methods
2. **Reduce Nesting**: Simplify nested conditional statements
3. **Design Patterns**: Apply appropriate design patterns to reduce complexity
4. **Monitoring**: Set up alerts for files that frequently change

### Long-term Strategy

1. **Architecture Review**: Consider architectural changes for consistently problematic areas
2. **Team Training**: Provide training on complexity management techniques
3. **Code Standards**: Establish and enforce complexity thresholds
4. **Automated Analysis**: Integrate complexity analysis into CI/CD pipeline

## Hotspot Details

### Files Requiring Immediate Attention
"""
        
        critical_hotspots = [h for h in hotspots if h.complexity_score > (sum(h.complexity_score for h in hotspots) / len(hotspots) * 1.5)] if hotspots else []
        
        if critical_hotspots:
            for hotspot in critical_hotspots[:10]:  # Top 10 critical
                report += f"""
**{hotspot.file_path}**
- Complexity Score: {hotspot.complexity_score}
- Changed {hotspot.change_frequency} times in {self.months_to_analyze} months
- {hotspot.line_count} lines with {hotspot.conditional_count} conditional statements
- Conditional density: {hotspot.conditional_density}
"""
        else:
            report += "\nNo files identified as critical risk based on current thresholds.\n"
        
        report += """
## Next Steps

1. **Prioritize Refactoring**: Focus on files with highest complexity scores
2. **Increase Test Coverage**: Ensure high-risk files have comprehensive tests
3. **Code Review Process**: Implement stricter review for high-risk files
4. **Monitor Changes**: Track complexity trends over time
5. **Team Discussion**: Review findings with development team

---
*Generated by OLAF Hotspot Analyzer*
"""
        
        return report
    
    def run_analysis(self) -> None:
        """Run complete hotspot analysis."""
        logger.info(f"Starting hotspot analysis of: {self.repo_path}")
        
        hotspots = self.analyze_hotspots()
        report = self.generate_report(hotspots)
        
        # Save report
        output_path = Path(self.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Analysis complete. Report saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Analyze code complexity hotspots')
    parser.add_argument('repo_path', help='Path to Git repository')
    parser.add_argument('-o', '--output', help='Output file path', default=None)
    parser.add_argument('-m', '--months', type=int, default=12, help='Months of history to analyze')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not os.path.exists(args.repo_path):
        logger.error(f"Repository path does not exist: {args.repo_path}")
        sys.exit(1)
    
    analyzer = HotspotAnalyzer(args.repo_path, args.output, args.months)
    analyzer.run_analysis()


if __name__ == '__main__':
    main()
