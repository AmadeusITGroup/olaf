#!/usr/bin/env python3
"""
OLAF Documentation Generator

Scans competency manifests and generates documentation structure including:
- Competency pack /docs folders
- README.md index files for each pack
- competency-packs-overview.md with links to all competencies
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class CompetencyManifest:
    """Represents a parsed competency manifest."""
    
    def __init__(self, manifest_path: Path, data: Dict):
        self.path = manifest_path
        self.pack_dir = manifest_path.parent
        self.id = data.get('id', '')
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.category = data.get('category', 'uncategorized')
        self.entry_points = data.get('entry_points', [])
        self.status = data.get('status', 'unknown')
        
    def get_docs_dir(self) -> Path:
        """Get the docs directory path for this competency pack."""
        return self.pack_dir / 'docs'
    
    def is_valid(self) -> bool:
        """Check if manifest has minimum required fields."""
        return bool(self.id and self.name)


class DocumentationGenerator:
    """Generates OLAF competency documentation structure."""
    
    def __init__(self, workspace_root: Path, dry_run: bool = False):
        self.workspace_root = workspace_root
        self.competencies_dir = workspace_root / 'olaf-core' / 'competencies'
        self.docs_dir = workspace_root / 'docs'
        self.dry_run = dry_run
        
    def find_manifests(self, specific_competency: Optional[str] = None) -> List[CompetencyManifest]:
        """Find and parse all competency manifests."""
        manifests = []
        
        if not self.competencies_dir.exists():
            print(f"Error: Competencies directory not found: {self.competencies_dir}")
            return manifests
        
        for pack_dir in self.competencies_dir.iterdir():
            if not pack_dir.is_dir():
                continue
                
            # Skip if specific competency requested and this isn't it
            if specific_competency and pack_dir.name != specific_competency:
                continue
                
            manifest_path = pack_dir / 'competency-manifest.json'
            if not manifest_path.exists():
                continue
                
            try:
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    manifest = CompetencyManifest(manifest_path, data)
                    
                    if manifest.is_valid():
                        manifests.append(manifest)
                    else:
                        print(f"Warning: Invalid manifest at {manifest_path}")
                        
            except json.JSONDecodeError as e:
                print(f"Error: Failed to parse {manifest_path}: {e}")
            except Exception as e:
                print(f"Error: Failed to read {manifest_path}: {e}")
        
        return sorted(manifests, key=lambda m: (m.category, m.name))
    
    def create_structure(self, manifests: List[CompetencyManifest]) -> None:
        """Create documentation folder structure for competency packs."""
        print("\n=== Creating Documentation Structure ===\n")
        
        for manifest in manifests:
            docs_dir = manifest.get_docs_dir()
            
            if self.dry_run:
                print(f"[DRY RUN] Would create: {docs_dir}")
            else:
                docs_dir.mkdir(parents=True, exist_ok=True)
                print(f"Created: {docs_dir}")
            
            # Check if competency pack uses tools or scripts
            tools_folder = self._detect_tools_folder(manifest)
            if tools_folder:
                if self.dry_run:
                    print(f"[DRY RUN] Detected {tools_folder}/ folder usage in prompts")
                else:
                    print(f"  Detected {tools_folder}/ folder usage in prompts")
            
            # Create entry point subdirectories
            for entry_point in manifest.entry_points:
                entry_name = self._to_kebab_case(entry_point.get('name', ''))
                if not entry_name:
                    continue
                    
                entry_dir = docs_dir / entry_name
                
                if self.dry_run:
                    print(f"[DRY RUN] Would create: {entry_dir}")
                else:
                    entry_dir.mkdir(parents=True, exist_ok=True)
                    print(f"  Created: {entry_dir}")
            
            # Generate README for this competency pack
            self._generate_pack_readme(manifest)
    
    def _generate_pack_readme(self, manifest: CompetencyManifest) -> None:
        """Generate README.md index file for a competency pack."""
        docs_dir = manifest.get_docs_dir()
        readme_path = docs_dir / 'README.md'
        
        content = f"# {manifest.name}\n\n"
        content += f"## Overview\n\n{manifest.description}\n\n"
        
        if manifest.entry_points:
            content += "## Entry Points\n\n"
            
            for entry_point in manifest.entry_points:
                name = entry_point.get('name', 'Unknown')
                command = entry_point.get('command', '')
                protocol = entry_point.get('protocol', '')
                use_case = entry_point.get('use_case', '')
                
                entry_name_kebab = self._to_kebab_case(name)
                
                content += f"### {name}\n\n"
                content += f"**Command**: `{command}`\n\n"
                content += f"**Protocol**: {protocol}\n\n"
                content += f"**Use Case**: {use_case}\n\n"
                content += f"- [Description](./{entry_name_kebab}/description.md)\n"
                content += f"- [Tutorial](./{entry_name_kebab}/tutorial.md)\n\n"
        else:
            content += "## Entry Points\n\nNo entry points defined.\n\n"
        
        if self.dry_run:
            print(f"[DRY RUN] Would create: {readme_path}")
        else:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Generated: {readme_path}")
    
    def generate_overview(self, manifests: List[CompetencyManifest]) -> None:
        """Generate competency-packs-overview.md with links to all competencies."""
        print("\n=== Generating Competency Packs Overview ===\n")
        
        overview_path = self.docs_dir / 'competency-packs-overview.md'
        
        # Group by category
        by_category: Dict[str, List[CompetencyManifest]] = {}
        for manifest in manifests:
            category = manifest.category.title()
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(manifest)
        
        content = "# Competency Packs Overview\n\n"
        content += "This document provides a comprehensive listing of all OLAF competency packs and their entry points.\n\n"
        content += "> **Note**: Only entry points with existing documentation are linked. Entry points marked as *(Coming Soon)* are defined but documentation is not yet available.\n\n"
        
        total_entry_points = 0
        documented_entry_points = 0
        
        for category in sorted(by_category.keys()):
            content += f"## {category}\n\n"
            
            for manifest in by_category[category]:
                content += f"### {manifest.name}\n\n"
                content += f"{manifest.description}\n\n"
                
                if manifest.entry_points:
                    for entry_point in manifest.entry_points:
                        name = entry_point.get('name', 'Unknown')
                        use_case = entry_point.get('use_case', '')
                        entry_name_kebab = self._to_kebab_case(name)
                        
                        total_entry_points += 1
                        
                        # Check if documentation files exist
                        entry_dir = manifest.get_docs_dir() / entry_name_kebab
                        description_exists = (entry_dir / 'description.md').exists()
                        tutorial_exists = (entry_dir / 'tutorial.md').exists()
                        
                        # Create relative path from docs/ to competency pack docs/
                        rel_path = os.path.relpath(
                            entry_dir,
                            self.docs_dir
                        ).replace('\\', '/')
                        
                        # Only create links if at least one file exists
                        if description_exists or tutorial_exists:
                            documented_entry_points += 1
                            content += f"- **{name}**: {use_case}\n"
                            
                            if description_exists:
                                content += f"  - [Description]({rel_path}/description.md)\n"
                            else:
                                content += f"  - Description *(Coming Soon)*\n"
                                
                            if tutorial_exists:
                                content += f"  - [Tutorial]({rel_path}/tutorial.md)\n"
                            else:
                                content += f"  - Tutorial *(Coming Soon)*\n"
                        else:
                            # No documentation exists yet
                            content += f"- **{name}**: {use_case} *(Coming Soon)*\n"
                    
                    content += "\n"
                else:
                    content += "*No entry points defined.*\n\n"
        
        # Add statistics at the end
        content += "---\n\n"
        content += f"**Documentation Coverage**: {documented_entry_points}/{total_entry_points} entry points have documentation\n"
        
        if self.dry_run:
            print(f"[DRY RUN] Would create: {overview_path}")
            print(f"Documentation coverage: {documented_entry_points}/{total_entry_points} entry points")
            print("\n--- Preview ---")
            print(content[:500] + "..." if len(content) > 500 else content)
        else:
            with open(overview_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Generated: {overview_path}")
            print(f"Documentation coverage: {documented_entry_points}/{total_entry_points} entry points")
    
    def _detect_tools_folder(self, manifest: CompetencyManifest) -> Optional[str]:
        """
        Detect whether the competency pack uses 'tools' or 'scripts' folder
        by checking prompt files and manifest structure.
        Returns 'tools', 'scripts', or None.
        """
        # Check if manifest has scripts section (like prompt-engineer)
        if hasattr(manifest, 'scripts') or 'scripts' in manifest.path.read_text():
            scripts_dir = manifest.pack_dir / 'scripts'
            if scripts_dir.exists():
                return 'scripts'
        
        # Check if tools directory exists
        tools_dir = manifest.pack_dir / 'tools'
        if tools_dir.exists():
            return 'tools'
        
        # Check prompt files for references to tools/ or scripts/
        prompts_dir = manifest.pack_dir / 'prompts'
        if prompts_dir.exists():
            for prompt_file in prompts_dir.glob('*.md'):
                try:
                    content = prompt_file.read_text(encoding='utf-8')
                    if 'scripts/' in content.lower():
                        return 'scripts'
                    if 'tools/' in content.lower():
                        return 'tools'
                except Exception:
                    continue
        
        return None
    
    @staticmethod
    def _to_kebab_case(text: str) -> str:
        """Convert text to kebab-case."""
        # Replace spaces and underscores with hyphens
        text = text.replace(' ', '-').replace('_', '-')
        # Remove special characters except hyphens
        text = ''.join(c for c in text if c.isalnum() or c == '-')
        # Convert to lowercase and remove multiple consecutive hyphens
        text = '-'.join(filter(None, text.lower().split('-')))
        return text


def main():
    """Main entry point for the documentation generator."""
    parser = argparse.ArgumentParser(
        description='Generate OLAF competency documentation structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate overview document
  python generate-competency-docs.py --generate-overview
  
  # Create documentation structure for all packs
  python generate-competency-docs.py --create-structure
  
  # Process specific competency pack
  python generate-competency-docs.py --create-structure --competency architect
  
  # Dry run to preview changes
  python generate-competency-docs.py --generate-overview --dry-run
  
  # Do everything
  python generate-competency-docs.py --generate-overview --create-structure
        """
    )
    
    parser.add_argument(
        '--generate-overview',
        action='store_true',
        help='Generate competency-packs-overview.md'
    )
    
    parser.add_argument(
        '--create-structure',
        action='store_true',
        help='Create /docs folders and README files for competency packs'
    )
    
    parser.add_argument(
        '--competency',
        type=str,
        help='Process specific competency pack only'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be created without creating'
    )
    
    args = parser.parse_args()
    
    # If no action specified, show help
    if not (args.generate_overview or args.create_structure):
        parser.print_help()
        return 0
    
    # Find workspace root (script is in olaf-core/competencies/olaf-specific-tools/scripts/)
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent.parent.parent.parent
    
    print(f"Workspace root: {workspace_root}")
    
    generator = DocumentationGenerator(workspace_root, dry_run=args.dry_run)
    
    # Find manifests
    print(f"\nScanning for competency manifests...")
    manifests = generator.find_manifests(specific_competency=args.competency)
    
    if not manifests:
        print("No valid competency manifests found.")
        return 1
    
    print(f"Found {len(manifests)} competency pack(s)")
    
    # Execute requested actions
    if args.create_structure:
        generator.create_structure(manifests)
    
    if args.generate_overview:
        generator.generate_overview(manifests)
    
    print("\n=== Complete ===\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
