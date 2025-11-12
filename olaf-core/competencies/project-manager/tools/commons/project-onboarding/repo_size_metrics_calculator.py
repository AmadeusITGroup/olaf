#!/usr/bin/env python3
"""
Repository Size Metrics Calculator for Project Onboarding

Calculates comprehensive repository size metrics including file counts,
lines of code, binary file sizes, and Git repository statistics.

Built from scratch for OLAF toolkit project onboarding workflow.
"""

import os
import subprocess
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, NamedTuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileMetrics(NamedTuple):
    """Represents metrics for a single file."""
    path: str
    size_bytes: int
    line_count: int
    is_binary: bool
    file_type: str


class RepoSizeMetricsCalculator:
    """Calculates comprehensive repository size and complexity metrics."""
    
    # File type categories
    FILE_CATEGORIES = {
        'Source Code': [
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cs', '.go', '.rs', 
            '.cpp', '.c', '.h', '.hpp', '.php', '.rb', '.swift', '.kt', '.scala'
        ],
        'Web Assets': [
            '.html', '.css', '.scss', '.sass', '.less', '.vue', '.svelte'
        ],
        'Configuration': [
            '.json', '.yaml', '.yml', '.toml', '.ini', '.conf', '.config', 
            '.xml', '.plist', '.env'
        ],
        'Documentation': [
            '.md', '.rst', '.txt', '.adoc', '.tex'
        ],
        'Images': [
            '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.webp', '.bmp'
        ],
        'Media': [
            '.mp4', '.avi', '.mov', '.mp3', '.wav', '.ogg'
        ],
        'Archives': [
            '.zip', '.tar', '.gz', '.bz2', '.7z', '.rar'
        ],
        'Binaries': [
            '.exe', '.dll', '.so', '.dylib', '.bin', '.app'
        ],
        'Data': [
            '.csv', '.xlsx', '.xls', '.db', '.sqlite', '.json', '.parquet'
        ]
    }
    
    # Binary file extensions (files we shouldn't count lines for)
    BINARY_EXTENSIONS = {
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.webp', '.bmp', '.tiff',
        '.mp4', '.avi', '.mov', '.mp3', '.wav', '.ogg', '.flac',
        '.zip', '.tar', '.gz', '.bz2', '.7z', '.rar',
        '.exe', '.dll', '.so', '.dylib', '.bin', '.app',
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
        '.sqlite', '.db', '.parquet'
    }
    
    def __init__(self, repo_path: str, output_file: str = None):
        self.repo_path = Path(repo_path).resolve()
        self.output_file = output_file or self.repo_path / "repo-size-metrics.md"
        self.exclude_patterns = [
            'node_modules', 'dist', 'bin', 'obj', 'build', 'target', 
            'vendor', 'packages', '.git', '__pycache__', '.pytest_cache',
            '.next', '.turbo', '.cache', 'coverage', 'out', 'tmp'
        ]
        
    def should_exclude_path(self, path: Path) -> bool:
        """Check if path should be excluded from analysis."""
        path_str = str(path)
        return any(pattern in path_str for pattern in self.exclude_patterns)
    
    def is_binary_file(self, file_path: Path) -> bool:
        """Determine if a file is binary based on extension and content."""
        # Check extension first
        if file_path.suffix.lower() in self.BINARY_EXTENSIONS:
            return True
        
        # For unknown extensions, check content (sample first 1024 bytes)
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                if b'\0' in chunk:  # Null bytes indicate binary
                    return True
        except (IOError, OSError):
            return True  # Assume binary if can't read
        
        return False
    
    def get_file_category(self, file_path: Path) -> str:
        """Categorize file based on extension."""
        extension = file_path.suffix.lower()
        
        for category, extensions in self.FILE_CATEGORIES.items():
            if extension in extensions:
                return category
        
        return 'Other'
    
    def count_lines_in_file(self, file_path: Path) -> int:
        """Count lines in a text file."""
        if self.is_binary_file(file_path):
            return 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for _ in f)
        except (IOError, UnicodeDecodeError):
            return 0
    
    def analyze_file(self, file_path: Path) -> FileMetrics:
        """Analyze a single file and return its metrics."""
        try:
            size_bytes = file_path.stat().st_size
        except (OSError, IOError):
            size_bytes = 0
        
        is_binary = self.is_binary_file(file_path)
        line_count = 0 if is_binary else self.count_lines_in_file(file_path)
        file_type = self.get_file_category(file_path)
        
        relative_path = file_path.relative_to(self.repo_path)
        
        return FileMetrics(
            path=str(relative_path),
            size_bytes=size_bytes,
            line_count=line_count,
            is_binary=is_binary,
            file_type=file_type
        )
    
    def get_git_repository_size(self) -> Dict:
        """Get Git repository size information."""
        git_info = {
            'is_git_repo': False,
            'git_dir_size_bytes': 0,
            'commit_count': 0,
            'branch_count': 0,
            'tag_count': 0,
            'remote_count': 0
        }
        
        git_dir = self.repo_path / '.git'
        if not git_dir.exists():
            return git_info
        
        git_info['is_git_repo'] = True
        
        # Calculate .git directory size
        try:
            git_size = 0
            for root, dirs, files in os.walk(git_dir):
                for file in files:
                    file_path = Path(root) / file
                    try:
                        git_size += file_path.stat().st_size
                    except (OSError, IOError):
                        continue
            git_info['git_dir_size_bytes'] = git_size
        except (OSError, IOError):
            pass
        
        # Get Git statistics using git commands
        try:
            # Commit count
            result = subprocess.run(
                ['git', 'rev-list', '--all', '--count'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            git_info['commit_count'] = int(result.stdout.strip())
        except (subprocess.CalledProcessError, ValueError, FileNotFoundError):
            pass
        
        try:
            # Branch count
            result = subprocess.run(
                ['git', 'branch', '-a'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            branches = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            git_info['branch_count'] = len(branches)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        try:
            # Tag count
            result = subprocess.run(
                ['git', 'tag'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            tags = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            git_info['tag_count'] = len(tags)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        try:
            # Remote count
            result = subprocess.run(
                ['git', 'remote'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            remotes = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            git_info['remote_count'] = len(remotes)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        return git_info
    
    def analyze_repository(self) -> Dict:
        """Analyze entire repository for size metrics."""
        logger.info(f"Analyzing repository: {self.repo_path}")
        
        all_files = []
        file_metrics = []
        
        # Get all files
        for root, dirs, files in os.walk(self.repo_path):
            # Remove excluded directories from traversal
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in self.exclude_patterns)]
            
            for file in files:
                file_path = Path(root) / file
                if not self.should_exclude_path(file_path):
                    all_files.append(file_path)
        
        logger.info(f"Found {len(all_files)} files to analyze")
        
        # Analyze each file
        total_size_bytes = 0
        total_lines = 0
        category_stats = {}
        
        for i, file_path in enumerate(all_files):
            if i % 1000 == 0 and i > 0:
                logger.info(f"Analyzed {i}/{len(all_files)} files")
            
            metrics = self.analyze_file(file_path)
            file_metrics.append(metrics)
            
            total_size_bytes += metrics.size_bytes
            total_lines += metrics.line_count
            
            # Update category statistics
            category = metrics.file_type
            if category not in category_stats:
                category_stats[category] = {
                    'file_count': 0,
                    'total_size_bytes': 0,
                    'total_lines': 0,
                    'binary_files': 0
                }
            
            category_stats[category]['file_count'] += 1
            category_stats[category]['total_size_bytes'] += metrics.size_bytes
            category_stats[category]['total_lines'] += metrics.line_count
            if metrics.is_binary:
                category_stats[category]['binary_files'] += 1
        
        # Get Git repository information
        git_info = self.get_git_repository_size()
        
        return {
            'file_metrics': file_metrics,
            'total_files': len(all_files),
            'total_size_bytes': total_size_bytes,
            'total_lines': total_lines,
            'category_stats': category_stats,
            'git_info': git_info
        }
    
    def format_bytes(self, bytes_value: int) -> str:
        """Format bytes into human-readable string."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f} PB"
    
    def generate_report(self, analysis_data: Dict) -> str:
        """Generate comprehensive repository size metrics report."""
        file_metrics = analysis_data['file_metrics']
        total_files = analysis_data['total_files']
        total_size_bytes = analysis_data['total_size_bytes']
        total_lines = analysis_data['total_lines']
        category_stats = analysis_data['category_stats']
        git_info = analysis_data['git_info']
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""# Repository Size Metrics Report

**Analysis Date**: {timestamp}  
**Repository Path**: {self.repo_path}  
**Total Files**: {total_files:,}  
**Total Size**: {self.format_bytes(total_size_bytes)}  
**Total Lines of Code**: {total_lines:,}

## Overview Summary

| Metric | Value |
|--------|-------|
| Repository Size (excluding .git) | {self.format_bytes(total_size_bytes)} |
| Git Repository Size (.git directory) | {self.format_bytes(git_info['git_dir_size_bytes'])} |
| Total Repository Size | {self.format_bytes(total_size_bytes + git_info['git_dir_size_bytes'])} |
| File Count | {total_files:,} |
| Lines of Code | {total_lines:,} |
| Average File Size | {self.format_bytes(total_size_bytes // total_files) if total_files > 0 else '0 B'} |
| Average Lines per File | {total_lines // total_files if total_files > 0 else 0} |

## File Category Breakdown

| Category | Files | % of Files | Size | % of Size | Lines | Avg Size/File |
|----------|-------|------------|------|-----------|-------|---------------|
"""
        
        # Sort categories by size (descending)
        sorted_categories = sorted(category_stats.items(), key=lambda x: x[1]['total_size_bytes'], reverse=True)
        
        for category, stats in sorted_categories:
            file_count = stats['file_count']
            size_bytes = stats['total_size_bytes']
            lines = stats['total_lines']
            
            file_percent = round((file_count / total_files) * 100, 1) if total_files > 0 else 0
            size_percent = round((size_bytes / total_size_bytes) * 100, 1) if total_size_bytes > 0 else 0
            avg_size = self.format_bytes(size_bytes // file_count) if file_count > 0 else '0 B'
            
            report += f"| {category} | {file_count:,} | {file_percent}% | {self.format_bytes(size_bytes)} | {size_percent}% | {lines:,} | {avg_size} |\n"
        
        report += """
## Git Repository Statistics

"""
        
        if git_info['is_git_repo']:
            report += f"""| Metric | Value |
|--------|-------|
| Git Directory Size | {self.format_bytes(git_info['git_dir_size_bytes'])} |
| Total Commits | {git_info['commit_count']:,} |
| Branches | {git_info['branch_count']} |
| Tags | {git_info['tag_count']} |
| Remotes | {git_info['remote_count']} |
"""
        else:
            report += "This directory is not a Git repository.\n"
        
        report += """
## Largest Files

Top 20 largest files in the repository:

| File | Size | Type | Lines |
|------|------|------|-------|
"""
        
        # Sort files by size (descending) and show top 20
        largest_files = sorted(file_metrics, key=lambda x: x.size_bytes, reverse=True)[:20]
        
        for file_metric in largest_files:
            lines_str = f"{file_metric.line_count:,}" if not file_metric.is_binary else "Binary"
            report += f"| {file_metric.path} | {self.format_bytes(file_metric.size_bytes)} | {file_metric.file_type} | {lines_str} |\n"
        
        report += """
## Code Density Analysis

Analysis of lines of code per file type:

| File Type | Total Lines | Files | Avg Lines/File | Max Lines/File |
|-----------|-------------|-------|----------------|----------------|
"""
        
        # Analyze code density by category
        for category, stats in sorted_categories:
            if stats['total_lines'] > 0:  # Only show categories with code
                file_count = stats['file_count']
                total_lines_cat = stats['total_lines']
                avg_lines = total_lines_cat // file_count if file_count > 0 else 0
                
                # Find max lines for this category
                max_lines = 0
                for fm in file_metrics:
                    if fm.file_type == category and fm.line_count > max_lines:
                        max_lines = fm.line_count
                
                report += f"| {category} | {total_lines_cat:,} | {file_count:,} | {avg_lines} | {max_lines:,} |\n"
        
        # Repository size assessment
        total_repo_size = total_size_bytes + git_info['git_dir_size_bytes']
        
        report += """
## Repository Size Assessment

"""
        
        if total_repo_size < 10 * 1024 * 1024:  # < 10MB
            size_category = "Small"
            assessment = "Lightweight repository, easy to clone and work with."
        elif total_repo_size < 100 * 1024 * 1024:  # < 100MB
            size_category = "Medium"
            assessment = "Moderate size repository, reasonable for most development workflows."
        elif total_repo_size < 1024 * 1024 * 1024:  # < 1GB
            size_category = "Large"
            assessment = "Large repository, may impact clone times and storage requirements."
        else:
            size_category = "Very Large"
            assessment = "Very large repository, consider using Git LFS for large files."
        
        report += f"""**Size Category**: {size_category}  
**Assessment**: {assessment}

### Recommendations

"""
        
        if total_repo_size > 100 * 1024 * 1024:  # > 100MB
            report += """
**Size Optimization**:
- Consider using Git LFS for large binary files
- Review if all files in the repository are necessary
- Consider splitting large repositories into smaller modules

"""
        
        # Check for large files
        large_files = [fm for fm in file_metrics if fm.size_bytes > 10 * 1024 * 1024]  # > 10MB
        if large_files:
            report += f"""
**Large Files Detected**: {len(large_files)} files larger than 10MB
- Consider using Git LFS for these files
- Review if these files should be in version control

"""
        
        # Check for many small files
        small_files = [fm for fm in file_metrics if fm.size_bytes < 1024]  # < 1KB
        if len(small_files) > total_files * 0.3:  # > 30% small files
            report += """
**Many Small Files**: High proportion of very small files detected
- Consider consolidating configuration files
- Review if all small files are necessary

"""
        
        report += """
### Next Steps

1. **Storage Planning**: Plan storage requirements based on repository size
2. **Clone Optimization**: Consider shallow clones for large repositories  
3. **File Management**: Review large files for Git LFS candidates
4. **Cleanup**: Remove unnecessary files to reduce repository size
5. **Monitoring**: Track repository size growth over time

---
*Generated by OLAF Repository Size Metrics Calculator*
"""
        
        return report
    
    def run_analysis(self) -> None:
        """Run complete repository size analysis."""
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
    parser = argparse.ArgumentParser(description='Calculate repository size metrics')
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('-o', '--output', help='Output file path', default=None)
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not os.path.exists(args.repo_path):
        logger.error(f"Repository path does not exist: {args.repo_path}")
        sys.exit(1)
    
    calculator = RepoSizeMetricsCalculator(args.repo_path, args.output)
    calculator.run_analysis()


if __name__ == '__main__':
    main()
