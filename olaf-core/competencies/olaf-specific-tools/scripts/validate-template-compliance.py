#!/usr/bin/env python3
"""
Template Compliance Validator for OLAF Framework

Validates that OLAF artifacts (competency descriptions, tutorials, README files)
comply with their respective templates.

Usage:
    python validate-template-compliance.py [options]

Options:
    --all                   Validate all competency pack documentation
    --competency PATH       Validate specific competency pack
    --report PATH           Output validation report to file (default: stdout)
    --strict                Fail on warnings as well as errors
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional
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
    section: str
    message: str
    suggestion: str = ""


@dataclass
class ValidationResult:
    competency_path: Path
    is_valid: bool
    issues: List[ValidationIssue] = field(default_factory=list)
    
    def add_error(self, file: str, section: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.ERROR, file, section, message, suggestion))
        self.is_valid = False
    
    def add_warning(self, file: str, section: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.WARNING, file, section, message, suggestion))
    
    def add_info(self, file: str, section: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.INFO, file, section, message, suggestion))


class TemplateValidator:
    """Validates OLAF documentation against templates"""
    
    # Expected sections in competency description
    DESCRIPTION_SECTIONS = [
        "# ",  # Title
        "## Overview",
        "## Purpose",
        "## Usage",
        "## Parameters",
        "## Output",
        "## Examples",
        "## Related Competencies"
    ]
    
    # Expected sections in tutorial
    TUTORIAL_SECTIONS = [
        "# ",  # Title
        "## Prerequisites",
        "## Step-by-Step Instructions",
        "### Step 1:",
        "## Verification Checklist",
        "## Troubleshooting",
        "## Key Learning Points",
        "## Next Steps to Try",
        "## Expected Timeline"
    ]
    
    # Expected sections in competency pack README
    README_SECTIONS = [
        "# ",  # Title
        "## Overview",
        "## Entry Points"
    ]
    
    def __init__(self, strict: bool = False):
        self.strict = strict
    
    def validate_competency_pack(self, competency_path: Path) -> ValidationResult:
        """Validate all documentation in a competency pack"""
        result = ValidationResult(competency_path=competency_path, is_valid=True)
        
        docs_path = competency_path / "docs"
        
        if not docs_path.exists():
            result.add_info(
                "docs/",
                "structure",
                "No docs folder found",
                "Create docs/ folder if this competency has entry points"
            )
            return result
        
        # Validate README.md
        readme_path = docs_path / "README.md"
        if readme_path.exists():
            self._validate_readme(readme_path, result)
        else:
            result.add_warning(
                "docs/README.md",
                "missing",
                "README.md not found in docs folder",
                "Create README.md to index entry points"
            )
        
        # Validate entry point documentation
        for entry_dir in docs_path.iterdir():
            if entry_dir.is_dir():
                self._validate_entry_point_docs(entry_dir, result)
        
        return result
    
    def _validate_readme(self, readme_path: Path, result: ValidationResult):
        """Validate competency pack README structure"""
        try:
            content = readme_path.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(
                str(readme_path.relative_to(result.competency_path)),
                "file",
                f"Cannot read file: {e}",
                "Check file permissions and encoding"
            )
            return
        
        # Check for required sections
        missing_sections = []
        for section in self.README_SECTIONS:
            if section not in content:
                missing_sections.append(section.strip())
        
        if missing_sections:
            result.add_warning(
                str(readme_path.relative_to(result.competency_path)),
                "structure",
                f"Missing sections: {', '.join(missing_sections)}",
                "Add missing sections following README template"
            )
        
        # Check for entry point links
        if "## Entry Points" in content:
            entry_points_section = content.split("## Entry Points")[1].split("##")[0]
            if not re.search(r'\[.*?\]\(.*?description\.md\)', entry_points_section):
                result.add_warning(
                    str(readme_path.relative_to(result.competency_path)),
                    "entry_points",
                    "No links to description.md found in Entry Points section",
                    "Add links to entry point descriptions"
                )
            if not re.search(r'\[.*?\]\(.*?tutorial\.md\)', entry_points_section):
                result.add_warning(
                    str(readme_path.relative_to(result.competency_path)),
                    "entry_points",
                    "No links to tutorial.md found in Entry Points section",
                    "Add links to entry point tutorials"
                )
    
    def _validate_entry_point_docs(self, entry_dir: Path, result: ValidationResult):
        """Validate entry point description and tutorial"""
        entry_name = entry_dir.name
        
        # Check for description.md
        description_path = entry_dir / "description.md"
        if description_path.exists():
            self._validate_description(description_path, result)
        else:
            result.add_warning(
                f"docs/{entry_name}/description.md",
                "missing",
                f"description.md not found for entry point '{entry_name}'",
                "Create description.md following description template"
            )
        
        # Check for tutorial.md
        tutorial_path = entry_dir / "tutorial.md"
        if tutorial_path.exists():
            self._validate_tutorial(tutorial_path, result)
        else:
            result.add_warning(
                f"docs/{entry_name}/tutorial.md",
                "missing",
                f"tutorial.md not found for entry point '{entry_name}'",
                "Create tutorial.md following tutorial template"
            )
    
    def _validate_description(self, description_path: Path, result: ValidationResult):
        """Validate competency description structure"""
        try:
            content = description_path.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(
                str(description_path.relative_to(result.competency_path)),
                "file",
                f"Cannot read file: {e}",
                "Check file permissions and encoding"
            )
            return
        
        # Check for required sections
        missing_sections = []
        for section in self.DESCRIPTION_SECTIONS:
            if section not in content:
                missing_sections.append(section.strip())
        
        if missing_sections:
            result.add_warning(
                str(description_path.relative_to(result.competency_path)),
                "structure",
                f"Missing sections: {', '.join(missing_sections)}",
                "Add missing sections following description template"
            )
        
        # Check document length (should be ~500-750 words, max 2 pages)
        word_count = len(content.split())
        if word_count > 1000:
            result.add_warning(
                str(description_path.relative_to(result.competency_path)),
                "length",
                f"Document is {word_count} words (recommended max: 750 words)",
                "Consider condensing content or splitting into multiple documents"
            )
        
        # Check for usage section with command and protocol
        if "## Usage" in content:
            usage_section = content.split("## Usage")[1].split("##")[0]
            if "**Command**:" not in usage_section:
                result.add_warning(
                    str(description_path.relative_to(result.competency_path)),
                    "usage",
                    "Usage section missing **Command:** field",
                    "Add command invocation example"
                )
            if "**Protocol**:" not in usage_section:
                result.add_warning(
                    str(description_path.relative_to(result.competency_path)),
                    "usage",
                    "Usage section missing **Protocol:** field",
                    "Add protocol specification (Act/Propose-Act/Propose-Confirm-Act)"
                )
    
    def _validate_tutorial(self, tutorial_path: Path, result: ValidationResult):
        """Validate tutorial structure"""
        try:
            content = tutorial_path.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(
                str(tutorial_path.relative_to(result.competency_path)),
                "file",
                f"Cannot read file: {e}",
                "Check file permissions and encoding"
            )
            return
        
        # Check for required sections
        missing_sections = []
        for section in self.TUTORIAL_SECTIONS:
            # For "### Step 1:", just check if there's at least one step
            if section == "### Step 1:":
                if not re.search(r'### Step \d+:', content):
                    missing_sections.append("### Step X: (at least one step)")
            elif section not in content:
                missing_sections.append(section.strip())
        
        if missing_sections:
            result.add_warning(
                str(tutorial_path.relative_to(result.competency_path)),
                "structure",
                f"Missing sections: {', '.join(missing_sections)}",
                "Add missing sections following tutorial template"
            )
        
        # Check for verification checklist items
        if "## Verification Checklist" in content:
            checklist_section = content.split("## Verification Checklist")[1].split("##")[0]
            if not re.search(r'✅', checklist_section):
                result.add_warning(
                    str(tutorial_path.relative_to(result.competency_path)),
                    "verification",
                    "Verification Checklist has no checkmark items (✅)",
                    "Add verification items with ✅ checkmarks"
                )


def find_all_competency_packs(base_path: Path) -> List[Path]:
    """Find all competency pack directories"""
    competency_packs = []
    for item in base_path.iterdir():
        if item.is_dir() and (item / "competency-manifest.json").exists():
            competency_packs.append(item)
    return competency_packs


def format_report(results: List[ValidationResult], strict: bool = False) -> str:
    """Format validation results as a report"""
    lines = []
    lines.append("=" * 80)
    lines.append("OLAF Template Compliance Validation Report")
    lines.append("=" * 80)
    lines.append("")
    
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    invalid = total - valid
    
    # Summary
    lines.append(f"Total competency packs: {total}")
    lines.append(f"Compliant: {valid}")
    lines.append(f"Non-compliant: {invalid}")
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
            lines.append(f"✓ {result.competency_path.name}")
            lines.append("")
            continue
        
        status = "✓" if result.is_valid else "✗"
        lines.append(f"{status} {result.competency_path.name}")
        lines.append("-" * 80)
        
        if not result.issues:
            lines.append("  No issues found")
        else:
            for issue in result.issues:
                icon = "✗" if issue.severity == Severity.ERROR else "⚠" if issue.severity == Severity.WARNING else "ℹ"
                lines.append(f"  {icon} [{issue.severity.value}] {issue.file} ({issue.section})")
                lines.append(f"     {issue.message}")
                if issue.suggestion:
                    lines.append(f"     → {issue.suggestion}")
                lines.append("")
        
        lines.append("")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate OLAF documentation against templates"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all competency pack documentation"
    )
    parser.add_argument(
        "--competency",
        type=Path,
        help="Validate specific competency pack"
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
    
    if not args.all and not args.competency:
        parser.error("Must specify either --all or --competency")
    
    validator = TemplateValidator(strict=args.strict)
    results = []
    
    if args.all:
        # Find workspace root
        current = Path.cwd()
        workspace_root = current
        while workspace_root != workspace_root.parent:
            if (workspace_root / "olaf-core").exists():
                break
            workspace_root = workspace_root.parent
        
        competencies_path = workspace_root / "olaf-core" / "competencies"
        if not competencies_path.exists():
            print(f"Error: Cannot find olaf-core/competencies at {competencies_path}", file=sys.stderr)
            sys.exit(1)
        
        competency_packs = find_all_competency_packs(competencies_path)
        print(f"Found {len(competency_packs)} competency packs")
        
        for pack in competency_packs:
            result = validator.validate_competency_pack(pack)
            results.append(result)
    
    elif args.competency:
        if not args.competency.exists():
            print(f"Error: Competency pack not found: {args.competency}", file=sys.stderr)
            sys.exit(1)
        
        result = validator.validate_competency_pack(args.competency)
        results.append(result)
    
    # Generate report
    report = format_report(results, strict=args.strict)
    
    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to {args.report}")
    else:
        print(report)
    
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
