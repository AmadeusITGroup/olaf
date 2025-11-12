#!/usr/bin/env python3
"""
File Reference Validator for OLAF

Validates file references in OLAF workspace by checking [id:xxx] patterns and direct file references.
Updated for current OLAF structure (olaf-core/ and olaf-data/).

Based on PowerShell validate-FileReferences.ps1 but updated for current OLAF architecture.
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class OLAFReferenceValidator:
    """Validates file references in OLAF workspace."""
    
    def __init__(self, workspace_root: Path):
        """
        Initialize validator with workspace root.
        
        Args:
            workspace_root: Root directory of OLAF workspace
        """
        self.workspace_root = workspace_root
        self.missing_references = []
        
        # Current OLAF ID mappings based on memory-map.md
        self.id_mappings = {
            # Core Framework (olaf-core)
            "ack_dir": "olaf-core",
            "prompts_dir": "olaf-core/prompts",
            "tools_dir": "olaf-core/tools",
            "templates_dir": "olaf-core/templates",
            "questionnaires_dir": "olaf-core/questionnaires",
            "reference_dir": "olaf-core/reference",
            "competency_index": "olaf-core/reference/query-competency-index.md",
            "llm_vs_ide_task_guide": "olaf-core/reference/llm-vs-ide-task-guide.md",
            
            # Work Environment (olaf-data)
            "ads_dir": "olaf-data",
            "peoples_dir": "olaf-data/peoples",
            "projects_dir": "olaf-data/projects",
            "changelog_register": "olaf-data/projects/changelog-register.md",
            "changelog_register_archive": "olaf-data/projects/changelog-register-archive.md",
            "jobs": "olaf-data/projects/jobs-register.md",
            "jobs_dir": "olaf-data/projects/Jobs",
            "product_dir": "olaf-data/product",
            "decision_records_dir": "olaf-data/product/decision-records",
            "decision_records_index": "olaf-data/product/decision-records/decision-records-register.md",
            "dr_naming_conventions": "olaf-data/product/decision-records/DR-2025-06-19-01-naming-conventions.md",
            "documentations_dir": "olaf-data/product/documentations",
            "product_docs_dir": "olaf-data/product/documentations",
            "conversation_records_dir": "olaf-data/product/documentations/conversations",
            "findings_dir": "olaf-data/findings",
            "code_reviews_dir": "olaf-data/findings/code-reviews",
            "practices_dir": "olaf-data/practices",
            "handover": "olaf-data/handover-conversation.md"
        }
        
        # File patterns for validation
        self.reference_patterns = [
            # [id:directory_name]filename references
            r'\[id:([^\]]+)\]([^\s\[\]]+\.(?:md|ps1|py|json|xml|txt|yml|yaml))',
            # Direct file operation commands
            r'(?:Read file:|Write file:|Load file:|Include file:|Import file:|Execute script:)\s*["`\']*([^\s"`\'\[\]]+\.(?:md|ps1|py|json|xml|txt|yml|yaml))["`\']*',
            # Script execution patterns
            r'(?:\.\s*[/\\]|python\s+|powershell\s+)\s*["`\']*([a-zA-Z0-9_-]+\.(?:ps1|py))["`\']*'
        ]
        
        # Template/placeholder patterns to skip
        self.template_patterns = [
            r'YYYY', r'MM', r'DD', r'NNN', r'SSS', r'XXX',  # Date/number placeholders
            r'\{[^}]+\}',  # {placeholder} patterns
            r'<[^>]+>',    # <placeholder> patterns
            r'example[_-]', r'sample[_-]', r'template[_-]',  # Example files
            r'your[_-]', r'my[_-]', r'user[_-]'  # User-specific placeholders
        ]
    
    def auto_detect_workspace(self) -> Optional[Path]:
        """
        Auto-detect OLAF workspace by looking for olaf-core and olaf-data folders.
        
        Returns:
            Path to workspace root or None if not found
        """
        current_dir = Path.cwd()
        search_dir = current_dir
        
        while search_dir != search_dir.parent:
            olaf_core_path = search_dir / "olaf-core"
            olaf_data_path = search_dir / "olaf-data"
            
            if olaf_core_path.exists() and olaf_data_path.exists():
                return search_dir
            
            search_dir = search_dir.parent
        
        return None
    
    def resolve_id_mapping(self, id_name: str) -> Optional[str]:
        """
        Resolve ID mapping to actual directory path.
        
        Args:
            id_name: ID name from [id:xxx] pattern
            
        Returns:
            Relative path or None if not found
        """
        return self.id_mappings.get(id_name)
    
    def is_template_reference(self, filename: str, context: str) -> bool:
        """
        Check if filename looks like a template/placeholder.
        
        Args:
            filename: Filename to check
            context: Surrounding context
            
        Returns:
            True if this appears to be a template/example
        """
        filename_lower = filename.lower()
        
        for pattern in self.template_patterns:
            if re.search(pattern, filename_lower, re.IGNORECASE):
                return True
        
        # Check for obvious template indicators in context
        context_lower = context.lower()
        template_indicators = ['example', 'template', 'placeholder', 'sample', 'your-']
        
        for indicator in template_indicators:
            if indicator in context_lower:
                return True
        
        return False
    
    def scan_file_for_references(self, file_path: Path) -> List[Dict]:
        """
        Scan a single file for file references.
        
        Args:
            file_path: Path to file to scan
            
        Returns:
            List of reference dictionaries
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except (IOError, UnicodeDecodeError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return []
        
        references = []
        
        for pattern in self.reference_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            
            for match in matches:
                if len(match.groups()) == 2:
                    # [id:directory]filename pattern
                    id_name = match.group(1)
                    filename = match.group(2)
                    resolved_dir = self.resolve_id_mapping(id_name)
                    
                    if resolved_dir:
                        # Skip if this looks like a template/example
                        if self.is_template_reference(filename, content[max(0, match.start()-100):match.end()+100]):
                            continue
                        
                        resolved_path = self.workspace_root / resolved_dir / filename
                        references.append({
                            'source_file': str(file_path),
                            'referenced_file': filename,
                            'resolved_path': str(resolved_path),
                            'full_match': match.group(0),
                            'id_name': id_name,
                            'exists': resolved_path.exists()
                        })
                
                elif len(match.groups()) == 1:
                    # Direct file reference
                    filename = match.group(1)
                    
                    # Skip template references
                    if self.is_template_reference(filename, content[max(0, match.start()-100):match.end()+100]):
                        continue
                    
                    # Resolve path (absolute or relative to current file)
                    if Path(filename).is_absolute():
                        resolved_path = Path(filename)
                    else:
                        resolved_path = file_path.parent / filename
                    
                    references.append({
                        'source_file': str(file_path),
                        'referenced_file': filename,
                        'resolved_path': str(resolved_path),
                        'full_match': match.group(0),
                        'id_name': None,
                        'exists': resolved_path.exists()
                    })
        
        return references
    
    def validate_workspace(self) -> List[Dict]:
        """
        Validate all file references in the workspace.
        
        Returns:
            List of missing reference dictionaries
        """
        # Directories to scan - updated for current OLAF structure
        scan_directories = [
            "olaf-core/competencies",
            "olaf-core/reference",
            "olaf-data",
            "docs"
        ]
        
        # File extensions to scan
        file_extensions = [".md", ".ps1", ".py", ".json", ".xml", ".txt", ".yml", ".yaml"]
        
        all_references = []
        total_files = 0
        
        print("Starting OLAF file reference validation...")
        print(f"Workspace root: {self.workspace_root}")
        
        for scan_dir in scan_directories:
            scan_path = self.workspace_root / scan_dir
            
            if not scan_path.exists():
                print(f"Warning: Directory not found: {scan_path}")
                continue
            
            print(f"Scanning directory: {scan_dir}")
            
            for ext in file_extensions:
                files = list(scan_path.rglob(f"*{ext}"))
                total_files += len(files)
                
                for file_path in files:
                    references = self.scan_file_for_references(file_path)
                    all_references.extend(references)
        
        # Find missing references
        missing_references = [ref for ref in all_references if not ref['exists']]
        
        print(f"\nValidation Results:")
        print(f"Total files scanned: {total_files}")
        print(f"Total references found: {len(all_references)}")
        print(f"Missing references: {len(missing_references)}")
        
        return missing_references
    
    def generate_report(self, missing_references: List[Dict], output_file: Path):
        """
        Generate validation report.
        
        Args:
            missing_references: List of missing reference dictionaries
            output_file: Path to output report file
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report_lines = [
            "# OLAF File Reference Validation Report",
            f"Generated: {timestamp}",
            f"Workspace: {self.workspace_root}",
            "",
            "## Summary",
            f"- Missing references found: {len(missing_references)}",
            ""
        ]
        
        if not missing_references:
            report_lines.extend([
                "✅ **All file references are valid!**",
                "",
                "No broken references found in the OLAF workspace."
            ])
        else:
            report_lines.extend([
                "❌ **Missing file references found:**",
                "",
                "| Source File | Referenced File | ID Mapping | Resolved Path |",
                "|-------------|-----------------|------------|---------------|"
            ])
            
            for ref in missing_references:
                source_file = Path(ref['source_file']).relative_to(self.workspace_root)
                id_mapping = ref['id_name'] if ref['id_name'] else "Direct"
                
                report_lines.append(
                    f"| {source_file} | {ref['referenced_file']} | {id_mapping} | {ref['resolved_path']} |"
                )
            
            report_lines.extend([
                "",
                "## Recommendations",
                "",
                "1. **Check file paths**: Verify the referenced files exist at the expected locations",
                "2. **Update references**: Fix broken [id:xxx] mappings or file paths",
                "3. **Create missing files**: Add missing files if they should exist",
                "4. **Remove dead references**: Clean up references to files that are no longer needed"
            ])
        
        # Write report
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_lines))
            print(f"Report saved to: {output_file}")
        except IOError as e:
            print(f"Error writing report: {e}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Validate file references in OLAF workspace",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --workspace /path/to/olaf/workspace
  %(prog)s --output validation-report.md
        """
    )
    
    parser.add_argument(
        '--workspace',
        type=Path,
        help='Path to OLAF workspace root (auto-detected if not provided)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        default='file-reference-validation.md',
        help='Output report file (default: file-reference-validation.md)'
    )
    
    args = parser.parse_args()
    
    # Determine workspace root
    if args.workspace:
        workspace_root = args.workspace.resolve()
        if not workspace_root.exists():
            print(f"Error: Workspace path does not exist: {workspace_root}", file=sys.stderr)
            sys.exit(1)
    else:
        validator_temp = OLAFReferenceValidator(Path.cwd())
        workspace_root = validator_temp.auto_detect_workspace()
        if not workspace_root:
            print("Error: Could not auto-detect OLAF workspace.", file=sys.stderr)
            print("Looking for directories 'olaf-core' and 'olaf-data'.", file=sys.stderr)
            print("Please provide --workspace parameter.", file=sys.stderr)
            sys.exit(1)
        print(f"Auto-detected workspace: {workspace_root}")
    
    # Initialize validator
    validator = OLAFReferenceValidator(workspace_root)
    
    try:
        # Validate references
        missing_references = validator.validate_workspace()
        
        # Generate report
        output_path = args.output
        if not output_path.is_absolute():
            output_path = workspace_root / output_path
        
        validator.generate_report(missing_references, output_path)
        
        # Exit with appropriate code
        if missing_references:
            print(f"\n❌ Found {len(missing_references)} missing references!")
            print("Check the report for details.")
            sys.exit(1)
        else:
            print("\n✅ All file references are valid!")
            sys.exit(0)
            
    except Exception as e:
        print(f"Error during validation: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()