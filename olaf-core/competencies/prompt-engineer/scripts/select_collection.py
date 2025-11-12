#!/usr/bin/env python3
# ============================================================================
# OLAF Competency Collection Selector
# ============================================================================
# Purpose: Allow end-users to select a competency collection (or create custom)
#          and generate the query-competency-index.md file
#
# Usage: python select_collection.py [--collection developer] [--custom] [--list]
#
# ============================================================================

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

class CollectionSelector:
    # Constants for maintainability
    TIMESTAMP_FORMAT = "%Y%m%d-%H%M"
    INDEX_FILENAME = "query-competency-index.md"
    COLLECTIONS_FILENAME = "competency-collections.json"
    CONDENSED_FILENAME = "olaf-framework-condensed.md"
    MANIFEST_FILENAME = "competency-manifest.json"
    
    # Pattern extraction constants
    MAPPINGS_START_MARKER = "## Mappings\n\n["
    MAPPINGS_END_MARKER = "]\n\nend-of-competency-index"
    COMPETENCIES_START_MARKER = "<!-- OLAF_COMPETENCIES_START -->\n"
    COMPETENCIES_END_MARKER = "\n<!-- OLAF_COMPETENCIES_END -->"
    
    # Menu constants
    MIN_MENU_CHOICE = 1
    MAX_ALIASES_DISPLAY = 3
    
    def __init__(self, execution_mode=2):
        self.script_dir = Path(__file__).parent
        self.repo_root = self.script_dir.parent.parent.parent
        self.collections_file = self.repo_root / "reference" / self.COLLECTIONS_FILENAME
        self.competencies_dir = self.repo_root / "competencies"
        self.index_output = self.repo_root / "reference" / self.INDEX_FILENAME
        self.execution_mode = execution_mode  # Configurable auto_execution_mode
        
    def _handle_error(self, message: str, exit_code: int = 1):
        """Consistent error handling with exit"""
        print(f"❌ {message}")
        sys.exit(exit_code)
    
    def show_logo(self):
        print("\n" + "="*60)
        print("  OLAF Competency Collection Selector v1.0")
        print("  Generate personalized competency index")
        print("="*60 + "\n")
    
    def load_collections(self) -> Dict:
        """Load collections from JSON file"""
        try:
            with open(self.collections_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self._handle_error(f"Collections file not found: {self.collections_file}")
        except json.JSONDecodeError:
            self._handle_error(f"Invalid JSON in: {self.collections_file}")
    
    def clean_invalid_competencies(self, collections: Dict) -> Dict:
        """Remove any competencies that don't exist from all collections"""
        available_competencies = self.get_available_competencies()
        available_ids = [c['id'] for c in available_competencies]
        
        for collection in collections.get('collections', []):
            current_comps = collection.get('competencies', [])
            valid_comps = [comp for comp in current_comps if comp in available_ids]
            invalid_comps = [comp for comp in current_comps if comp not in available_ids]
            
            if invalid_comps:
                print(f"[CLEAN] {collection.get('id')}: Removing non-existent competencies: {', '.join(invalid_comps)}")
                collection['competencies'] = valid_comps
        
        return collections
    
    def _get_timestamp(self) -> str:
        """Get formatted timestamp for consistency"""
        return datetime.now().strftime(self.TIMESTAMP_FORMAT)
    
    def show_execution_mode_info(self):
        """Display information about execution modes"""
        modes = {
            0: "Manual - User confirmation required for each step",
            1: "Safe - Automatic execution with safety checks (recommended)",
            2: "Normal - Balanced automatic execution",
            3: "Turbo - Maximum automation (experimental)"
        }
        
        print(f"🚀 Execution Mode: {self.execution_mode} - {modes.get(self.execution_mode, 'Unknown')}")
        print("   Modes: 0=Manual | 1=Safe | 2=Normal | 3=Turbo")
    
    def load_manifest(self, competency_id: str) -> Dict:
        """Load competency manifest"""
        manifest_path = self.competencies_dir / competency_id / self.MANIFEST_FILENAME
        try:
            with open(manifest_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"⚠️  Manifest not found or invalid for: {competency_id}")
            return None
    
    def show_collections(self, collections: Dict):
        """Display all available collections"""
        print("📋 Available Collections:")
        print("-" * 60)
        
        for i, collection in enumerate(collections['collections'], 1):
            comp_count = len(collection.get('competencies', []))
            print(f"\n  [{i}] {collection['name']}")
            print(f"      ID: {collection['id']}")
            print(f"      Description: {collection['description']}")
            print(f"      Competencies: {comp_count}")
            for comp in collection.get('competencies', []):
                print(f"         • {comp}")
        print()
    
    def show_menu(self, collections: Dict) -> str:
        """Interactive menu to select collection"""
        options = [c['id'] for c in collections['collections']] + ["custom"]
        
        print("🎯 Select Collection:")
        print("-" * 60)
        
        for i, option in enumerate(options, 1):
            if option == "custom":
                print(f"  [{i}] Create Custom Selection")
            else:
                coll = next(c for c in collections['collections'] if c['id'] == option)
                print(f"  [{i}] {coll['name']}")
        
        print()
        while True:
            try:
                choice = int(input(f"Enter number (1-{len(options)}): "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print("❌ Invalid selection")
            except ValueError:
                print("❌ Please enter a number")
    
    def get_available_competencies(self) -> List[Dict]:
        """Get all available competencies"""
        competencies = []
        
        if self.competencies_dir.exists():
            for comp_dir in self.competencies_dir.iterdir():
                if comp_dir.is_dir():
                    manifest_path = comp_dir / "competency-manifest.json"
                    if manifest_path.exists():
                        try:
                            with open(manifest_path, 'r') as f:
                                manifest = json.load(f)
                                competencies.append({
                                    "id": comp_dir.name,
                                    "name": manifest.get('name', comp_dir.name),
                                    "description": manifest.get('description', '')
                                })
                        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
                            print(f"⚠️  Skipping {comp_dir.name}: {e}")
                            continue
        
        return sorted(competencies, key=lambda x: x['id'])
    
    def select_competencies_interactive(self, collections: Dict) -> List[str]:
        """Allow user to select competencies"""
        competencies = self.get_available_competencies()
        
        self._display_competency_menu(competencies)
        selected = self._get_user_selections(competencies)
        
        if not selected:
            selected = self._get_default_selections(collections)
        
        return list(set(selected))
    
    def _display_competency_menu(self, competencies: List[Dict]):
        """Display available competencies in a formatted menu"""
        print("\n🎯 Select competencies for custom collection:")
        print("-" * 60)
        
        for i, comp in enumerate(competencies, 1):
            print(f"  [{i}] {comp['id']}")
            print(f"      {comp['name']}")
        print()
    
    def _get_user_selections(self, competencies: List[Dict]) -> List[str]:
        """Get and validate user selections from input"""
        selected = []
        while True:
            try:
                choices = input("Enter numbers separated by commas (e.g., 1,3,5): ").strip()
                if not choices:
                    break
                
                indices = self._parse_user_choices(choices)
                selected = self._validate_indices(indices, competencies)
                break
            except ValueError:
                print("Please enter valid numbers")
        
        return selected
    
    def _parse_user_choices(self, choices: str) -> List[int]:
        """Parse user input into list of indices"""
        return [int(x.strip()) - 1 for x in choices.split(',')]
    
    def _validate_indices(self, indices: List[int], competencies: List[Dict]) -> List[str]:
        """Validate indices and return selected competency IDs"""
        selected = []
        for idx in indices:
            if 0 <= idx < len(competencies):
                selected.append(competencies[idx]['id'])
            else:
                print(f"Invalid index: {idx + 1}")
        return selected
    
    def _get_default_selections(self, collections: Dict) -> List[str]:
        """Get default selections when user provides no input"""
        core_coll = next((c for c in collections['collections'] if c['id'] == 'core'), None)
        return list(core_coll['competencies']) if core_coll else []
    
    def build_index_entry(self, entry_point: Any, competency_id: str) -> str:
        """Build a single index entry"""
        # Handle both dict and string entry_point formats
        if isinstance(entry_point, str):
            # Simple file path string
            file_path = f"{competency_id}/{entry_point}"
            return f'  [[], "{file_path}", "Act"]'
        
        # Dictionary format with metadata
        aliases = entry_point.get('aliases', [])
        file_path = f"{competency_id}/{entry_point.get('file', '')}"
        protocol = entry_point.get('protocol', 'Act')
        
        # Format: [["alias1", "alias2", ...], "path/to/file.md", "Protocol"]
        aliases_str = ', '.join(f'"{a}"' for a in aliases)
        return f'  [{{{aliases_str}}}, "{file_path}", "{protocol}"]'
    
    def _validate_kernel_competencies(self, kernel_competencies: List[str]) -> List[str]:
        """Validate and filter kernel competencies, removing invalid ones"""
        available_competencies = self.get_available_competencies()
        available_ids = [c['id'] for c in available_competencies]
        
        valid_kernels = [comp for comp in kernel_competencies if comp in available_ids]
        invalid_kernels = [comp for comp in kernel_competencies if comp not in available_ids]
        
        if invalid_kernels:
            print(f"⚠️  Removing invalid kernel competencies: {', '.join(invalid_kernels)}")
            print(f"✅ Valid kernel competencies: {', '.join(valid_kernels)}")
            
        if not valid_kernels:
            self._handle_error("No valid kernel competencies after filtering")
            
        return valid_kernels

    def generate_index(self, selected_competencies: List[str], collection_name: str) -> str:
        """Generate the competency index"""
        print("\n🔧 Generating index from selected competencies...")
        
        index_entries = []
        timestamp = self._get_timestamp()
        
        for competency_id in selected_competencies:
            manifest = self.load_manifest(competency_id)
            
            if not manifest:
                print(f"  ⚠️  Skipping (no manifest): {competency_id}")
                continue
            
            print(f"  ✓ Processing: {competency_id}")
            
            # Handle entry_points - only array format is supported now
            if isinstance(manifest.get('entry_points'), list):
                for entry_point in manifest['entry_points']:
                    entry = self.build_index_entry(entry_point, competency_id)
                    index_entries.append(entry)
            elif manifest.get('entry_points'):
                print(f"  ⚠️  Invalid entry_points format in {competency_id} (expected array)")

        
        # Build the markdown content
        content = f"""<olaf-query-competency-index>
# Competency Index

**Last Updated:** {timestamp} CEDT
**Collection:** {collection_name}
**Generated By:** select_collection.py

## How to Use This Index

If requested for a competency, iterate through the mappings below.
For each mapping, check if the user request matches the patterns.
Use the first matching mapping with its file and protocol.

## Collection Information

- **Name:** {collection_name}
- **Competencies Included:** {', '.join(selected_competencies)}
- **Total Entry Points:** {len(index_entries)}

## Mappings

[
{chr(10).join(index_entries)}
]

end-of-competency-index
</olaf-query-competency-index>
"""
        return content
    
    def save_index(self, content: str):
        """Save generated index to file"""
        try:
            self.index_output.parent.mkdir(parents=True, exist_ok=True)
            with open(self.index_output, 'w') as f:
                f.write(content)
            print(f"\n✅ Index generated successfully!")
            print(f"   Output: {self.index_output}")
        except Exception as e:
            self._handle_error(f"Error saving index: {e}")
    
    def save_active_collection(self, collection_id: str):
        """Update the active_collection field in collections JSON file"""
        try:
            with open(self.collections_file, 'r') as f:
                collections = json.load(f)
            
            # Update the active_collection in metadata
            if 'metadata' not in collections:
                collections['metadata'] = {}
            
            collections['metadata']['active_collection'] = collection_id
            collections['metadata']['lastUpdated'] = datetime.now().isoformat()
            
            # Write back to file
            with open(self.collections_file, 'w') as f:
                json.dump(collections, f, indent=2)
            
            print(f"✅ Active collection updated: {collection_id}")
        except Exception as e:
            print(f"⚠️  Warning: Could not update active collection in JSON: {e}")
    
    def extract_patterns_from_index(self, content: str) -> List[str]:
        """Extract competency patterns from index content for condensed framework (compressed format without aliases)"""
        mappings_section = self._extract_mappings_section(content)
        if not mappings_section:
            return []
        
        return self._parse_mapping_lines(mappings_section)
    
    def _extract_mappings_section(self, content: str) -> str:
        """Extract the mappings section from index content"""
        start_marker = "## Mappings\n\n["
        end_marker = "]\n\nend-of-competency-index"
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            print("⚠️  Could not extract patterns from index")
            return ""
        
        # Extract mapping entries (skip opening '[' from marker)
        return content[start_idx + len(start_marker):end_idx]
    
    def _parse_mapping_lines(self, mappings_section: str) -> List[str]:
        """Parse individual mapping lines into patterns"""
        patterns = []
        lines = mappings_section.strip().split('\n')
        
        for line in lines:
            pattern = self._parse_single_mapping_line(line.strip())
            if pattern:
                patterns.append(pattern)
        
        return patterns
    
    def _parse_single_mapping_line(self, line: str) -> str:
        """Parse a single mapping line into a pattern"""
        if not line:
            return ""
        
        # Clean up line formatting
        line = self._clean_mapping_line(line)
        if not line:
            return ""
        
        try:
            # Extract components: aliases, file_path, protocol
            aliases = self._extract_aliases_from_line(line)
            file_path = self._extract_file_path_from_line(line)
            protocol = self._extract_protocol_from_line(line)
            
            if not all([aliases, file_path, protocol]):
                return ""
            
            # Build pattern: →path|Protocol (compressed format - no aliases for condensed framework)
            return '→' + file_path + '|' + protocol
            
        except Exception as e:
            print(f"⚠️  Error parsing line: {line} ({e})")
            return ""
    
    def _clean_mapping_line(self, line: str) -> str:
        """Clean and normalize a mapping line"""
        # Remove leading/trailing brackets
        if line.startswith('['):
            line = line[1:]
        if line.endswith(']'):
            line = line[:-1]
        
        return line.strip()
    
    def _extract_aliases_from_line(self, line: str) -> List[str]:
        """Extract aliases from a mapping line"""
        aliases_start = line.find('{')
        aliases_end = line.find('}')
        if aliases_start == -1 or aliases_end == -1:
            return []
        
        aliases_str = line[aliases_start+1:aliases_end]
        return [a.strip().strip('"') for a in aliases_str.split(',')]
    
    def _extract_file_path_from_line(self, line: str) -> str:
        """Extract file path from a mapping line"""
        aliases_end = line.find('}')
        if aliases_end == -1:
            return ""
        
        file_start = line.find('"', aliases_end)
        file_end = line.find('"', file_start + 1)
        if file_start == -1 or file_end == -1:
            return ""
        
        return line[file_start+1:file_end]
    
    def _extract_protocol_from_line(self, line: str) -> str:
        """Extract protocol from a mapping line"""
        protocol_start = line.rfind(',')
        if protocol_start == -1:
            return ""
        
        return line[protocol_start+1:].strip().strip('"')
    
    def _merge_with_kernels(self, kernel_competencies: List[str], selected_competencies: List[str]) -> List[str]:
        """Merge kernel competencies with selected ones, avoiding duplicates"""
        return list(dict.fromkeys(kernel_competencies + selected_competencies))

    def update_condensed_framework(self, index_content: str, collection_name: str):
        """Update condensed framework - skip competency patterns generation as requested"""
        print(f"✅ Condensed framework update skipped (as configured)")
        print(f"   Competency patterns section will not be modified")
        print(f"   Collection: {collection_name}")
        return True
    
    def sync_olaf_commands(self, selected_competencies: List[str]):
        """Synchronize /olaf-* command files for selected competencies"""
        print("\n🔧 Synchronizing /olaf-* commands...")
        
        # Get all competency IDs and file paths from manifests entry_points
        competency_map = {}  # id -> file_path
        for comp_id in selected_competencies:
            manifest = self.load_manifest(comp_id)
            if manifest and 'entry_points' in manifest:
                for entry_point in manifest['entry_points']:
                    if 'id' in entry_point:
                        competency_id = entry_point['id']
                    elif 'file' in entry_point:
                        # Extract ID from file path (e.g., "prompts/create-prompt.md" -> "create-prompt")
                        file_path = entry_point['file']
                        competency_id = Path(file_path).stem
                    else:
                        continue
                    
                    if 'file' in entry_point:
                        full_path = f"olaf-core/competencies/{comp_id}/{entry_point['file']}"
                        competency_map[competency_id] = full_path
        
        competency_names = set(competency_map.keys())
        
        # Sync both .github/prompts and .windsurf/workflows
        github_prompts_dir = self.repo_root.parent / ".github" / "prompts"
        windsurf_workflows_dir = self.repo_root.parent / ".windsurf" / "workflows"
        
        stats = {
            'created': 0,
            'deleted': 0,
            'kept': 0
        }
        
        for target_dir, extension in [(github_prompts_dir, '.prompt.md'), (windsurf_workflows_dir, '.md')]:
            if not target_dir.exists():
                print(f"⚠️  Directory not found: {target_dir}")
                continue
            
            dir_stats = self._sync_directory_commands(target_dir, competency_names, competency_map, extension)
            stats['created'] += dir_stats['created']
            stats['deleted'] += dir_stats['deleted']
            stats['kept'] += dir_stats['kept']
        
        print(f"✅ Command sync complete!")
        print(f"   Created: {stats['created']}")
        print(f"   Deleted: {stats['deleted']}")
        print(f"   Kept: {stats['kept']}")
    
    def _sync_directory_commands(self, target_dir: Path, competency_names: set, competency_map: dict, extension: str) -> Dict[str, int]:
        """Sync commands in a specific directory by deleting all and recreating"""
        stats = {'created': 0, 'deleted': 0, 'kept': 0}
        
        # Delete ALL existing olaf-* files first
        existing_files = list(target_dir.glob(f"olaf-*{extension}"))
        for file in existing_files:
            file.unlink()
            stats['deleted'] += 1
        
        if stats['deleted'] > 0:
            print(f"   🗑️  Deleted {stats['deleted']} existing files")
        
        # Recreate files for all competencies in selection
        for comp_name in competency_names:
            file_path = competency_map.get(comp_name)
            self._create_command_file(target_dir, comp_name, file_path, extension)
            stats['created'] += 1
        
        return stats
    
    def _create_command_file(self, target_dir: Path, competency_name: str, comp_file_path: str, extension: str):
        """Create a command file for a competency"""
        file_path = target_dir / f"olaf-{competency_name}{extension}"
        
        if not comp_file_path:
            print(f"⚠️  Could not find competency file path for: {competency_name}")
            return
        
        # Determine content based on extension
        if extension == '.prompt.md':
            # GitHub Copilot format
            content = f"\nExecute the `{comp_file_path}` competency.\n"
        else:
            # Windsurf format - with auto_execution_mode for seamless execution
            description = competency_name.replace('-', ' ')
            # Use configurable auto_execution_mode 
            execution_mode = getattr(self, 'execution_mode', 1)
            content = f"---\ndescription: {description}\nauto_execution_mode: {execution_mode}\n---\n\nExecute the `{comp_file_path}` competency.\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"   ✨ Created: {file_path.name}")

    def generate_git_exclude(self):
        """Generate .git/info/exclude file to keep OLAF workflows out of git while visible to Windsurf"""
        exclude_path = self.repo_root.parent / ".git" / "info" / "exclude"
        
        # Ensure .git/info directory exists
        exclude_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Content to exclude OLAF workflows
        exclude_content = """# Local excludes for this repository
# OLAF dynamic workflow files - visible to Windsurf but not tracked by git
.windsurf/workflows/olaf-*.md
"""
        
        try:
            with open(exclude_path, 'w', encoding='utf-8') as f:
                f.write(exclude_content)
            
            print(f"✅ Generated .git/info/exclude")
            print(f"   Pattern: .windsurf/workflows/olaf-*.md")
            print(f"   Effect: Workflows visible to Windsurf but ignored by git")
            return True
            
        except Exception as e:
            print(f"⚠️  Failed to generate .git/info/exclude: {e}")
            return False

    def run(self, collection_name: str = None, custom: bool = False, list_only: bool = False, output_path: str = None, reinit: bool = False):
        """Main execution - orchestrates the collection selection process"""
        self.show_logo()
        
        collections = self._initialize_collections()
        if output_path:
            self.index_output = Path(output_path)
        
        if list_only:
            self.show_collections(collections)
            return
        
        # Handle reinit mode - regenerate /olaf-* commands from active collection
        if reinit:
            self._handle_reinit(collections)
            return
        
        kernel_competencies = self._prepare_kernel_competencies(collections)
        selected_competencies, selected_id = self._determine_selection(
            collections, kernel_competencies, collection_name, custom
        )
        
        self._generate_and_save_outputs(selected_competencies, selected_id)
        print("\n✨ Done! Your competency index is ready to use.\n")
    
    def _initialize_collections(self) -> Dict:
        """Initialize and clean collections data"""
        collections = self.load_collections()
        print("✓ Collections loaded")
        return self.clean_invalid_competencies(collections)
    
    def _prepare_kernel_competencies(self, collections: Dict) -> List[str]:
        """Extract and validate kernel competencies from core collection"""
        core_collection = next((c for c in collections['collections'] if c['id'] == 'core'), None)
        kernel_competencies = core_collection['competencies'] if core_collection else []
        valid_kernels = self._validate_kernel_competencies(kernel_competencies)
        
        # Update core collection in memory
        if core_collection:
            core_collection['competencies'] = valid_kernels
        
        return valid_kernels
    
    def _determine_selection(self, collections: Dict, kernel_competencies: List[str], 
                           collection_name: str, custom: bool) -> tuple[List[str], str]:
        """Determine which competencies to select based on user input"""
        if collection_name and not custom:
            return self._select_named_collection(collections, kernel_competencies, collection_name)
        elif custom:
            return self._select_custom_collection(collections, kernel_competencies)
        else:
            return self._select_interactive_collection(collections, kernel_competencies)
    
    def _select_named_collection(self, collections: Dict, kernel_competencies: List[str], 
                               collection_name: str) -> tuple[List[str], str]:
        """Select a specific collection by name"""
        coll = next((c for c in collections['collections'] if c['id'] == collection_name), None)
        if not coll:
            self._handle_error(f"Collection not found: {collection_name}")
        
        selected_competencies = self._merge_with_kernels(kernel_competencies, coll['competencies'])
        return selected_competencies, collection_name
    
    def _select_custom_collection(self, collections: Dict, kernel_competencies: List[str]) -> tuple[List[str], str]:
        """Handle custom collection selection"""
        selected_competencies = self.select_competencies_interactive(collections)
        selected_competencies = self._merge_with_kernels(kernel_competencies, selected_competencies)
        selected_id = f"custom-{self._get_timestamp()}"
        
        print(f"\n💡 Tip: Your custom selection is temporary (ID: {selected_id})")
        print("   To create a permanent collection, use: python create_collection.py")
        
        return selected_competencies, selected_id
    
    def _select_interactive_collection(self, collections: Dict, kernel_competencies: List[str]) -> tuple[List[str], str]:
        """Handle interactive menu selection"""
        selected_id = self.show_menu(collections)
        if selected_id == "custom":
            return self._select_custom_collection(collections, kernel_competencies)
        else:
            coll = next(c for c in collections['collections'] if c['id'] == selected_id)
            selected_competencies = self._merge_with_kernels(kernel_competencies, coll['competencies'])
            return selected_competencies, selected_id
    
    def _generate_and_save_outputs(self, selected_competencies: List[str], selected_id: str):
        """Generate index and save all outputs"""
        index_content = self.generate_index(selected_competencies, selected_id)
        self.save_index(index_content)
        self.save_active_collection(selected_id)
        self.update_condensed_framework(index_content, selected_id)
        self.sync_olaf_commands(selected_competencies)
        self.generate_git_exclude()
    
    def _handle_reinit(self, collections: Dict):
        """Handle reinit mode - regenerate /olaf-* commands from active collection"""
        print("\n🔄 Reinitializing /olaf-* commands from active collection...\n")
        
        # Show execution mode info
        self.show_execution_mode_info()
        print()
        
        # Get active collection from metadata
        active_collection_id = collections.get('metadata', {}).get('active_collection')
        if not active_collection_id:
            self._handle_error("No active collection found. Run the script normally first to select a collection.")
        
        # Find the collection
        collection = next((c for c in collections['collections'] if c['id'] == active_collection_id), None)
        if not collection:
            self._handle_error(f"Active collection '{active_collection_id}' not found in collections.")
        
        print(f"📦 Active Collection: {collection['name']}")
        print(f"   Competencies: {', '.join(collection['competencies'])}\n")
        
        # Regenerate /olaf-* commands
        self.sync_olaf_commands(collection['competencies'])
        
        # Generate git exclude file
        self.generate_git_exclude()
        
        print("\n✨ Reinitialization complete! /olaf-* commands regenerated.\n")


def main():
    parser = argparse.ArgumentParser(description='OLAF Competency Collection Selector')
    parser.add_argument('--collection', '-c', help='Select a specific collection by name')
    parser.add_argument('--custom', action='store_true', help='Create custom selection')
    parser.add_argument('--list', '-l', action='store_true', help='List all collections')
    parser.add_argument('--output', '-o', help='Output file path for generated index')
    parser.add_argument('--reinit', '-r', action='store_true', help='Reinitialize: regenerate /olaf-* commands from active collection')
    parser.add_argument('--execution-mode', '-e', type=int, default=2, choices=[0, 1, 2, 3], help='Auto execution mode for Windsurf workflows (0=manual, 1=safe, 2=normal, 3=turbo)')
    
    args = parser.parse_args()
    
    selector = CollectionSelector(execution_mode=args.execution_mode)
    selector.run(
        collection_name=args.collection,
        custom=args.custom,
        list_only=args.list,
        output_path=args.output,
        reinit=args.reinit
    )


if __name__ == '__main__':
    main()
