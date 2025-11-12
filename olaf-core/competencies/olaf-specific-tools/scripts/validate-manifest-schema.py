#!/usr/bin/env python3
"""
Manifest Schema Validator for OLAF Framework

Validates competency manifest files against the standard schema defined in
competency-creation/templates/competency-manifest-template.json

Usage:
    python validate-manifest-schema.py [options]

Options:
    --all                   Validate all manifests in olaf-core/competencies
    --manifest PATH         Validate specific manifest file
    --report PATH           Output validation report to file (default: stdout)
    --strict                Fail on warnings as well as errors
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationIssue:
    severity: Severity
    field: str
    message: str
    suggestion: str = ""


@dataclass
class ValidationResult:
    manifest_path: Path
    is_valid: bool
    issues: List[ValidationIssue] = field(default_factory=list)
    
    def add_error(self, field: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.ERROR, field, message, suggestion))
        self.is_valid = False
    
    def add_warning(self, field: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.WARNING, field, message, suggestion))
    
    def add_info(self, field: str, message: str, suggestion: str = ""):
        self.issues.append(ValidationIssue(Severity.INFO, field, message, suggestion))


class ManifestValidator:
    """Validates OLAF competency manifests against standard schema"""
    
    REQUIRED_FIELDS = {
        "name": str,
        "version": str,
        "description": str,
        "category": str,
    }
    
    RECOMMENDED_FIELDS = {
        "id": str,
        "author": str,
        "created": str,
        "updated": str,
        "tags": list,
        "classification": dict,
        "target_users": dict,
        "maintenance": dict,
        "status": str,
        "technical_requirements": dict,
        "entry_points": list,
        "compatibility": dict,
    }
    
    VALID_STATUSES = {
        "experimental", "alpha", "beta", "public-beta", 
        "production", "active", "deprecated", "archived"
    }
    
    VALID_PROTOCOLS = {"Act", "Propose-Act", "Propose-Confirm-Act"}
    
    def __init__(self, strict: bool = False):
        self.strict = strict
    
    def validate_manifest(self, manifest_path: Path) -> ValidationResult:
        """Validate a single manifest file"""
        result = ValidationResult(manifest_path=manifest_path, is_valid=True)
        
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            result.add_error("_file", f"Invalid JSON: {e}", "Fix JSON syntax errors")
            return result
        except Exception as e:
            result.add_error("_file", f"Cannot read file: {e}", "Check file permissions and encoding")
            return result
        
        # Validate required fields
        self._validate_required_fields(data, result)
        
        # Validate recommended fields
        self._validate_recommended_fields(data, result)
        
        # Validate field types and values
        self._validate_field_types(data, result)
        
        # Validate entry_points structure
        self._validate_entry_points(data, result)
        
        # Validate classification structure
        self._validate_classification(data, result)
        
        # Validate target_users structure
        self._validate_target_users(data, result)
        
        # Validate compatibility structure
        self._validate_compatibility(data, result)
        
        return result
    
    def _validate_required_fields(self, data: Dict, result: ValidationResult):
        """Check for required fields"""
        for field, expected_type in self.REQUIRED_FIELDS.items():
            if field not in data:
                result.add_error(
                    field, 
                    f"Required field '{field}' is missing",
                    f"Add '{field}' field with type {expected_type.__name__}"
                )
            elif not isinstance(data[field], expected_type):
                result.add_error(
                    field,
                    f"Field '{field}' has wrong type: expected {expected_type.__name__}, got {type(data[field]).__name__}",
                    f"Change '{field}' to {expected_type.__name__} type"
                )
    
    def _validate_recommended_fields(self, data: Dict, result: ValidationResult):
        """Check for recommended fields"""
        for field, expected_type in self.RECOMMENDED_FIELDS.items():
            if field not in data:
                result.add_warning(
                    field,
                    f"Recommended field '{field}' is missing",
                    f"Consider adding '{field}' field with type {expected_type.__name__}"
                )
    
    def _validate_field_types(self, data: Dict, result: ValidationResult):
        """Validate field types and values"""
        # Validate status
        if "status" in data:
            if data["status"] not in self.VALID_STATUSES:
                result.add_warning(
                    "status",
                    f"Status '{data['status']}' is not a standard value",
                    f"Use one of: {', '.join(sorted(self.VALID_STATUSES))}"
                )
        
        # Validate version format
        if "version" in data:
            version = data["version"]
            if not self._is_valid_version(version):
                result.add_warning(
                    "version",
                    f"Version '{version}' doesn't follow semantic versioning",
                    "Use format: MAJOR.MINOR.PATCH (e.g., 1.0.0)"
                )
    
    def _validate_entry_points(self, data: Dict, result: ValidationResult):
        """Validate entry_points structure"""
        if "entry_points" not in data:
            return
        
        entry_points = data["entry_points"]
        
        if not isinstance(entry_points, list):
            result.add_error(
                "entry_points",
                "entry_points must be a list",
                "Convert entry_points to list format"
            )
            return
        
        for idx, entry in enumerate(entry_points):
            if not isinstance(entry, dict):
                result.add_error(
                    f"entry_points[{idx}]",
                    "Entry point must be an object",
                    "Use object format with id, file, protocol, description, aliases"
                )
                continue
            
            # Check required entry point fields (developer format)
            required_ep_fields = ["id", "file", "protocol", "description"]
            for field in required_ep_fields:
                if field not in entry:
                    result.add_error(
                        f"entry_points[{idx}].{field}",
                        f"Entry point missing required field '{field}'",
                        f"Add '{field}' to entry point definition"
                    )
            
            # Validate protocol
            if "protocol" in entry:
                protocol = entry["protocol"]
                if protocol not in self.VALID_PROTOCOLS:
                    result.add_error(
                        f"entry_points[{idx}].protocol",
                        f"Invalid protocol '{protocol}'",
                        f"Use one of: {', '.join(sorted(self.VALID_PROTOCOLS))}"
                    )
            
            # Check for aliases (recommended)
            if "aliases" not in entry:
                result.add_warning(
                    f"entry_points[{idx}].aliases",
                    "Entry point missing recommended field 'aliases'",
                    "Add 'aliases' array to define command variations"
                )
    
    def _validate_classification(self, data: Dict, result: ValidationResult):
        """Validate classification structure"""
        if "classification" not in data:
            return
        
        classification = data["classification"]
        if not isinstance(classification, dict):
            result.add_error(
                "classification",
                "classification must be an object",
                "Use object format with 'type' and 'reason' fields"
            )
            return
        
        if "type" not in classification:
            result.add_warning(
                "classification.type",
                "classification missing 'type' field",
                "Add 'type' field (e.g., 'core', 'kernel', 'specialized')"
            )
        
        if "reason" not in classification:
            result.add_warning(
                "classification.reason",
                "classification missing 'reason' field",
                "Add 'reason' field explaining the classification"
            )
    
    def _validate_target_users(self, data: Dict, result: ValidationResult):
        """Validate target_users structure"""
        if "target_users" not in data:
            return
        
        target_users = data["target_users"]
        if not isinstance(target_users, dict):
            result.add_error(
                "target_users",
                "target_users must be an object",
                "Use object format with 'primary', 'secondary', 'description' fields"
            )
            return
        
        if "primary" not in target_users:
            result.add_warning(
                "target_users.primary",
                "target_users missing 'primary' field",
                "Add 'primary' field specifying primary user type"
            )
    
    def _validate_compatibility(self, data: Dict, result: ValidationResult):
        """Validate compatibility structure"""
        if "compatibility" not in data:
            return
        
        compatibility = data["compatibility"]
        if not isinstance(compatibility, dict):
            result.add_error(
                "compatibility",
                "compatibility must be an object",
                "Use object format with 'olaf_version', 'platforms', 'shells' fields"
            )
    
    @staticmethod
    def _is_valid_version(version: str) -> bool:
        """Check if version follows semantic versioning"""
        parts = version.split('.')
        if len(parts) != 3:
            return False
        return all(part.isdigit() for part in parts)


def find_all_manifests(base_path: Path) -> List[Path]:
    """Find all competency-manifest.json files"""
    return list(base_path.rglob("competency-manifest.json"))


def format_report(results: List[ValidationResult], strict: bool = False) -> str:
    """Format validation results as a report"""
    lines = []
    lines.append("=" * 80)
    lines.append("OLAF Manifest Validation Report")
    lines.append("=" * 80)
    lines.append("")
    
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    invalid = total - valid
    
    # Summary
    lines.append(f"Total manifests: {total}")
    lines.append(f"Valid: {valid}")
    lines.append(f"Invalid: {invalid}")
    lines.append("")
    
    # Count issues by severity
    all_issues = [issue for result in results for issue in result.issues]
    errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    
    lines.append(f"Total errors: {errors}")
    lines.append(f"Total warnings: {warnings}")
    lines.append("")
    lines.append("=" * 80)
    lines.append("")
    
    # Detailed results
    for result in results:
        if result.is_valid and not result.issues:
            lines.append(f"✓ {result.manifest_path}")
            lines.append("")
            continue
        
        status = "✓" if result.is_valid else "✗"
        lines.append(f"{status} {result.manifest_path}")
        lines.append("-" * 80)
        
        if not result.issues:
            lines.append("  No issues found")
        else:
            for issue in result.issues:
                icon = "✗" if issue.severity == Severity.ERROR else "⚠" if issue.severity == Severity.WARNING else "ℹ"
                lines.append(f"  {icon} [{issue.severity.value}] {issue.field}")
                lines.append(f"     {issue.message}")
                if issue.suggestion:
                    lines.append(f"     → {issue.suggestion}")
                lines.append("")
        
        lines.append("")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate OLAF competency manifests against standard schema"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all manifests in olaf-core/competencies"
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Validate specific manifest file"
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
    
    if not args.all and not args.manifest:
        parser.error("Must specify either --all or --manifest")
    
    validator = ManifestValidator(strict=args.strict)
    results = []
    
    if args.all:
        # Find workspace root (look for olaf-core directory)
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
        
        manifests = find_all_manifests(competencies_path)
        print(f"Found {len(manifests)} manifest files")
        
        for manifest in manifests:
            result = validator.validate_manifest(manifest)
            results.append(result)
    
    elif args.manifest:
        if not args.manifest.exists():
            print(f"Error: Manifest file not found: {args.manifest}", file=sys.stderr)
            sys.exit(1)
        
        result = validator.validate_manifest(args.manifest)
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
