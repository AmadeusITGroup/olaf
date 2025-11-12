#!/usr/bin/env python3
"""
Documentation Structure Validator for OLAF Framework

Validates documentation integrity including:
- Link validity (internal and cross-references)
- Orphaned files
- Missing documentation
- Naming conventions (kebab-case)
- Document length guidelines

Usage:
    python validate-docs-structure.py [options]

Options:
    --all                   Validate all documentation
    --docs-path PATH        Validate specific docs folder
    --report PATH           Output validation report to file (default: stdout)
    --strict                Fail on warnings as well as errors
"""

import sys
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass, field
from enum import Enum
import re


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationIssue:
    severity: Severity
    file: str
    issue_type: str
    message: str
    suggestion: str = ""


@dataclass
class ValidationResult:
    docs_path: Path
    is_valid: bool
    issues: List[ValidationIssue] = field(default_factory=list)
    
    def add_error(self, file: str, issue_type: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.ERROR, file, issue_type, message, suggestion))
        self.is_valid = False
    
    def add_warning(self, file: str, issue_type: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.WARNING, file, issue_type, message, suggestion))
    
    def add_info(self, file: str, issue_type: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.INFO, file, issue_type, message, suggestion))


class DocsStructureValidator:
    """Validates OLAF documentation structure and integrity"""
    
    def __init__(self, strict: bool = False):
        self.strict = strict
        self.all_files: Set[Path] = set()
        self.referenced_files: Set[Path] = set()
    
    def validate_docs(self, docs_path: Path) -> ValidationResult:
        """Validate documentation structure and integrity"""
        result = ValidationResult(docs_path=docs_path, is_valid=True)
        
        if not docs_path.exists():
            result.add_error(
                str(docs_path),
                "missing",
                "Documentation folder does not exist",
                "Create docs folder"
            )
            return result
        
        # Collect all markdown files
        self.all_files = set(docs_path.rglob("*.md"))
        self.referenced_files = set()
        
        # Validate each markdown file
        for md_file in self.all_files:
            self._validate_markdown_file(md_file, docs_path, result)
        
        # Check for orphaned files
        self._check_orphaned_files(docs_path, result)
        
        # Validate naming conventions
        self._validate_naming_conventions(docs_path, result)
        
        return result
    
    def _validate_markdown_file(self, md_file: Path, docs_path: Path, result: ValidationResult):
        """Validate a single markdown file"""
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(
                str(md_file.relative_to(docs_path)),
                "file_read",
                f"Cannot read file: {e}",
                "Check file permissions and encoding"
            )
            return
        
        # Validate links
        self._validate_links(md_file, content, docs_path, result)
        
        # Check document length (5-minute read ~500-750 words)
        self._check_document_length(md_file, content, docs_path, result)
        
        # Check for proper markdown structure
        self._check_markdown_structure(md_file, content, docs_path, result)
    
    def _validate_links(self, md_file: Path, content: str, docs_path: Path, result: ValidationResult):
        """Validate all links in a markdown file"""
        # Find all markdown links: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_url in links:
            # Skip external links (http/https)
            if link_url.startswith(('http://', 'https://', 'mailto:')):
                continue
            
            # Skip anchors
            if link_url.startswith('#'):
                continue
            
            # Handle relative links
            if link_url.startswith('./') or link_url.startswith('../'):
                # Resolve relative path
                target_path = (md_file.parent / link_url).resolve()
            else:
                # Assume relative to docs_path
                target_path = (docs_path / link_url).resolve()
            
            # Track referenced file
            if target_path.suffix == '.md':
                self.referenced_files.add(target_path)
            
            # Check if target exists
            if not target_path.exists():
                result.add_error(
                    str(md_file.relative_to(docs_path)),
                    "broken_link",
                    f"Broken link to '{link_url}' (target not found)",
                    f"Fix link or create target file: {target_path.name}"
                )
        
        # Find file references in format #[[file:path]]
        file_ref_pattern = r'#\[\[file:([^\]]+)\]\]'
        file_refs = re.findall(file_ref_pattern, content)
        
        for file_ref in file_refs:
            # Resolve file reference relative to workspace root
            workspace_root = self._find_workspace_root(docs_path)
            target_path = (workspace_root / file_ref).resolve()
            
            if not target_path.exists():
                result.add_error(
                    str(md_file.relative_to(docs_path)),
                    "broken_file_ref",
                    f"Broken file reference: #[[file:{file_ref}]]",
                    f"Fix reference or create file: {file_ref}"
                )
    
    def _check_document_length(self, md_file: Path, content: str, docs_path: Path, result: ValidationResult):
        """Check if document meets length guidelines"""
        word_count = len(content.split())
        
        # Guideline: 5-minute read time (~500-750 words)
        if word_count > 1000:
            result.add_warning(
                str(md_file.relative_to(docs_path)),
                "length",
                f"Document is {word_count} words (recommended max: 750 words for 5-minute read)",
                "Consider splitting into smaller focused documents"
            )
        elif word_count < 100 and md_file.name != "README.md":
            result.add_info(
                str(md_file.relative_to(docs_path)),
                "length",
                f"Document is very short ({word_count} words)",
                "Consider adding more detail or examples"
            )
    
    def _check_markdown_structure(self, md_file: Path, content: str, docs_path: Path, result: ValidationResult):
        """Check for proper markdown structure"""
        # Check for title (# heading)
        if not re.search(r'^# .+', content, re.MULTILINE):
            result.add_warning(
                str(md_file.relative_to(docs_path)),
                "structure",
                "Document missing top-level heading (# Title)",
                "Add a title heading at the top of the document"
            )
        
        # Check for multiple top-level headings (should typically have only one)
        top_level_headings = re.findall(r'^# .+', content, re.MULTILINE)
        if len(top_level_headings) > 1:
            result.add_warning(
                str(md_file.relative_to(docs_path)),
                "structure",
                f"Document has {len(top_level_headings)} top-level headings (# Title)",
                "Consider using ## for section headings"
            )
    
    def _check_orphaned_files(self, docs_path: Path, result: ValidationResult):
        """Check for orphaned files (not referenced by any other file)"""
        # README files and index files are entry points, not orphans
        entry_points = {f for f in self.all_files if f.name in ['README.md', 'index.md']}
        
        # Files that are not referenced and not entry points
        orphaned = self.all_files - self.referenced_files - entry_points
        
        for orphan in orphaned:
            # Skip if it's in a docs root (likely an entry point)
            if orphan.parent.name == 'docs' and orphan.parent.parent.name != 'docs':
                continue
            
            result.add_info(
                str(orphan.relative_to(docs_path)),
                "orphaned",
                "File is not referenced by any other documentation",
                "Add links to this file from relevant documentation or remove if obsolete"
            )
    
    def _validate_naming_conventions(self, docs_path: Path, result: ValidationResult):
        """Validate that files follow kebab-case naming convention"""
        for md_file in self.all_files:
            filename = md_file.stem  # filename without extension
            
            # Skip special files
            if filename in ['README', 'CHANGELOG', 'LICENSE']:
                continue
            
            # Check for kebab-case (lowercase with hyphens)
            if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', filename):
                result.add_warning(
                    str(md_file.relative_to(docs_path)),
                    "naming",
                    f"Filename '{filename}' does not follow kebab-case convention",
                    f"Rename to kebab-case: {self._to_kebab_case(filename)}"
                )
    
    @staticmethod
    def _to_kebab_case(text: str) -> str:
        """Convert text to kebab-case"""
        # Replace underscores and spaces with hyphens
        text = text.replace('_', '-').replace(' ', '-')
        # Convert to lowercase
        text = text.lower()
        # Remove any non-alphanumeric characters except hyphens
        text = re.sub(r'[^a-z0-9-]', '', text)
        # Remove multiple consecutive hyphens
        text = re.sub(r'-+', '-', text)
        return text
    
    @staticmethod
    def _find_workspace_root(start_path: Path) -> Path:
        """Find workspace root by looking for olaf-core directory"""
        current = start_path.resolve()
        while current != current.parent:
            if (current / "olaf-core").exists():
                return current
            current = current.parent
        return start_path


def find_all_docs_folders(base_path: Path) -> List[Path]:
    """Find all docs folders in the workspace"""
    docs_folders = []
    
    # Root docs folder
    root_docs = base_path / "docs"
    if root_docs.exists():
        docs_folders.append(root_docs)
    
    # Competency pack docs folders
    competencies_path = base_path / "olaf-core" / "competencies"
    if competencies_path.exists():
        for item in competencies_path.iterdir():
            if item.is_dir():
                pack_docs = item / "docs"
                if pack_docs.exists():
                    docs_folders.append(pack_docs)
    
    return docs_folders


def format_report(results: List[ValidationResult], strict: bool = False) -> str:
    """Format validation results as a report"""
    lines = []
    lines.append("=" * 80)
    lines.append("OLAF Documentation Structure Validation Report")
    lines.append("=" * 80)
    lines.append("")
    
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    invalid = total - valid
    
    # Summary
    lines.append(f"Total documentation folders: {total}")
    lines.append(f"Valid: {valid}")
    lines.append(f"Invalid: {invalid}")
    lines.append("")
    
    # Count issues by severity
    all_issues = [issue for result in results for issue in result.issues]
    errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    info = sum(1 for i in all_issues if i.severity == Severity.INFO)
    
    lines.append(f"Total errors: {errors}")
    lines.append(f"Total warnings: {warnings}")
    lines.append(f"Total info: {info}")
    lines.append("")
    lines.append("=" * 80)
    lines.append("")
    
    # Detailed results
    for result in results:
        if result.is_valid and not result.issues:
            lines.append(f"✓ {result.docs_path}")
            lines.append("")
            continue
        
        status = "✓" if result.is_valid else "✗"
        lines.append(f"{status} {result.docs_path}")
        lines.append("-" * 80)
        
        if not result.issues:
            lines.append("  No issues found")
        else:
            # Group issues by type
            issues_by_type: Dict[str, List[ValidationIssue]] = {}
            for issue in result.issues:
                if issue.issue_type not in issues_by_type:
                    issues_by_type[issue.issue_type] = []
                issues_by_type[issue.issue_type].append(issue)
            
            for issue_type, issues in sorted(issues_by_type.items()):
                lines.append(f"\n  {issue_type.upper().replace('_', ' ')}:")
                for issue in issues:
                    icon = "✗" if issue.severity == Severity.ERROR else "⚠" if issue.severity == Severity.WARNING else "ℹ"
                    lines.append(f"    {icon} [{issue.severity.value}] {issue.file}")
                    lines.append(f"       {issue.message}")
                    if issue.suggestion:
                        lines.append(f"       → {issue.suggestion}")
        
        lines.append("")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate OLAF documentation structure and integrity"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all documentation folders"
    )
    parser.add_argument(
        "--docs-path",
        type=Path,
        help="Validate specific docs folder"
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Output validation report to file (default: stdout)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on warnings as well as errors"
    )
    
    args = parser.parse_args()
    
    if not args.all and not args.docs_path:
        parser.error("Must specify either --all or --docs-path")
    
    validator = DocsStructureValidator(strict=args.strict)
    results = []
    
    if args.all:
        # Find workspace root
        current = Path.cwd()
        workspace_root = current
        while workspace_root != workspace_root.parent:
            if (workspace_root / "olaf-core").exists():
                break
            workspace_root = workspace_root.parent
        
        docs_folders = find_all_docs_folders(workspace_root)
        print(f"Found {len(docs_folders)} documentation folders")
        
        for docs_path in docs_folders:
            result = validator.validate_docs(docs_path)
            results.append(result)
    
    elif args.docs_path:
        if not args.docs_path.exists():
            print(f"Error: Documentation folder not found: {args.docs_path}", file=sys.stderr)
            sys.exit(1)
        
        result = validator.validate_docs(args.docs_path)
        results.append(result)
    
    # Generate report
    report = format_report(results, strict=args.strict)
    
    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to {args.report}")
    else:
        # Handle Windows console encoding issues by replacing Unicode symbols
        try:
            print(report)
        except UnicodeEncodeError:
            # Replace Unicode symbols with ASCII equivalents for Windows console
            ascii_report = (report
                .replace('✓', '[OK]')
                .replace('✗', '[X]')
                .replace('⚠', '[!]')
                .replace('ℹ', '[i]')
                .replace('→', '->')
                .replace('—', '--')
                .replace(''', "'")
                .replace(''', "'")
                .replace('"', '"')
                .replace('"', '"'))
            print(ascii_report)
    
    # Exit code
    has_errors = any(not r.is_valid for r in results)
    has_warnings = any(
        any(i.severity == Severity.WARNING for i in r.issues)
        for r in results
    )
    
    if has_errors or (args.strict and has_warnings):
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()