#!/usr/bin/env python3
# ============================================================================
# OLAF Competency Collection Creator
# ============================================================================
# Purpose: Administrative tool to create, edit, and delete competency collections
#          for different personas or teams
#
# Usage: python create_collection.py [--list] [--edit NAME] [--delete NAME]
#
# ============================================================================

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

class CollectionManager:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.repo_root = self.script_dir.parent.parent.parent
        self.collections_file = self.repo_root / "reference" / "competency-collections.json"
        self.competencies_dir = self.repo_root / "competencies"
        
        # Protected collections that cannot be deleted
        self.protected_collections = {"core"}
    
    def show_logo(self):
        print("\n" + "="*60)
        print("  OLAF Competency Collection Manager v1.0")
        print("  Admin tool to create and manage competency collections")
        print("="*60 + "\n")
    
    def load_collections(self) -> Dict:
        """Load collections from JSON file"""
        try:
            with open(self.collections_file, 'r') as f:
                collections = json.load(f)
        except FileNotFoundError:
            print(f"❌ Collections file not found: {self.collections_file}")
            return self.create_default_collections()
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in: {self.collections_file}")
            sys.exit(1)
        
        # Enforce kernel competencies
        return self.enforce_kernel_competencies(collections)
    
    def enforce_kernel_competencies(self, collections: Dict) -> Dict:
        """Ensure kernel competencies (from core collection) are in all collections"""
        # First, clean all invalid competencies from all collections
        collections = self.clean_invalid_competencies(collections)
        
        # Get kernel competencies from core collection
        core = next((c for c in collections.get('collections', []) if c.get('id') == 'core'), None)
        if not core:
            print("⚠️  Warning: No core collection found")
            return collections
        
        kernel_comps = core.get('competencies', [])
        
        if not kernel_comps:
            print("⚠️  Warning: Core collection has no competencies defined")
            return collections
        
        # Validate that kernel competencies actually exist
        available_competencies = self.get_available_competencies()
        available_ids = [c['id'] for c in available_competencies]
        
        # Filter out invalid kernel competencies and keep only valid ones
        valid_kernels = [comp for comp in kernel_comps if comp in available_ids]
        invalid_kernels = [comp for comp in kernel_comps if comp not in available_ids]
        
        if invalid_kernels:
            print(f"⚠️  Removing invalid kernel competencies: {', '.join(invalid_kernels)}")
            print(f"✅ Valid kernel competencies: {', '.join(valid_kernels)}")
            # Update core collection with only valid kernels
            core['competencies'] = valid_kernels
        
        if not valid_kernels:
            print("❌ ERROR: No valid kernel competencies after filtering")
            return collections
        
        # Add kernel competencies to all non-core collections if missing
        for collection in collections.get('collections', []):
            if collection.get('id') != 'core':
                # Merge kernel competencies with collection competencies (preserve order, no duplicates)
                existing = collection.get('competencies', [])
                merged = list(dict.fromkeys(valid_kernels + existing))
                collection['competencies'] = merged
        
        return collections
    
    def clean_invalid_competencies(self, collections: Dict) -> Dict:
        """Remove any competencies that don't exist from all collections"""
        available_competencies = self.get_available_competencies()
        available_ids = [c['id'] for c in available_competencies]
        
        removed_any = False
        for collection in collections.get('collections', []):
            current_comps = collection.get('competencies', [])
            valid_comps = [comp for comp in current_comps if comp in available_ids]
            invalid_comps = [comp for comp in current_comps if comp not in available_ids]
            
            if invalid_comps:
                print(f"[CLEAN] {collection.get('id')}: Removing non-existent competencies: {', '.join(invalid_comps)}")
                collection['competencies'] = valid_comps
                removed_any = True
        
        return collections
    
    def save_collections(self, collections: Dict):
        """Save collections to JSON file"""
        try:
            # Clean invalid competencies and enforce kernel competencies before saving
            collections = self.clean_invalid_competencies(collections)
            collections = self.enforce_kernel_competencies(collections)
            
            # Ensure metadata exists with active_collection field
            if 'metadata' not in collections:
                collections['metadata'] = {}
            
            collections['metadata']['lastUpdated'] = datetime.now().isoformat()
            
            # Set active_collection if not already set (default to 'core')
            if 'active_collection' not in collections['metadata']:
                collections['metadata']['active_collection'] = 'core'
            
            self.collections_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.collections_file, 'w') as f:
                json.dump(collections, f, indent=2)
            print(f"✅ Collections saved to {self.collections_file}")
        except Exception as e:
            print(f"❌ Error saving collections: {e}")
            sys.exit(1)
    
    def create_default_collections(self) -> Dict:
        """Create default collections if file doesn't exist"""
        print("📝 Creating default collections...")
        
        default = {
            "version": "1.0.0",
            "last_updated": datetime.now().isoformat(),
            "collections": [
                {
                    "id": "core",
                    "name": "Core Competencies",
                    "description": "Essential competencies required for all users",
                    "competencies": ["prompt-engineer"],
                    "locked": True,
                    "created": datetime.now().isoformat()
                },
                {
                    "id": "developer",
                    "name": "Developer Collection",
                    "description": "Competencies for software developers",
                    "competencies": ["prompt-engineer"],
                    "locked": False,
                    "created": datetime.now().isoformat()
                },
                {
                    "id": "business-analyst",
                    "name": "Business Analyst Collection",
                    "description": "Competencies for business analysts and product managers",
                    "competencies": ["prompt-engineer"],
                    "locked": False,
                    "created": datetime.now().isoformat()
                },
                {
                    "id": "technical-writer",
                    "name": "Technical Writer Collection",
                    "description": "Competencies for technical documentation",
                    "competencies": ["prompt-engineer"],
                    "locked": False,
                    "created": datetime.now().isoformat()
                },
                {
                    "id": "researcher",
                    "name": "Researcher Collection",
                    "description": "Competencies for researchers and data analysts",
                    "competencies": ["prompt-engineer"],
                    "locked": False,
                    "created": datetime.now().isoformat()
                },
                {
                    "id": "full-stack",
                    "name": "Full Stack Collection",
                    "description": "Complete competency set with all available items",
                    "competencies": ["prompt-engineer"],
                    "locked": False,
                    "created": datetime.now().isoformat()
                }
            ]
        }
        
        self.save_collections(default)
        return default
    
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
                                    "version": manifest.get('version', 'unknown')
                                })
                        except:
                            pass
        
        return sorted(competencies, key=lambda x: x['id'])
    
    def show_collections(self, collections: Dict):
        """Display all collections"""
        print("📚 Existing Collections:")
        print("-" * 60)
        
        menu_num = 1
        for collection in collections['collections']:
            lock_icon = "🔒" if collection.get('locked') else "🔓"
            comp_count = len(collection.get('competencies', []))
            
            # Show locked collections without numbering
            if collection.get('locked'):
                print(f"\n  {lock_icon} {collection['name']} (locked - not editable)")
                print(f"      ID: {collection['id']}")
                print(f"      Description: {collection['description']}")
                print(f"      Competencies: {comp_count}")
            else:
                # Number only editable collections
                print(f"\n  [{menu_num}] {lock_icon} {collection['name']}")
                print(f"      ID: {collection['id']}")
                print(f"      Description: {collection['description']}")
                print(f"      Competencies: {comp_count}")
                menu_num += 1
            
            for comp in collection.get('competencies', []):
                print(f"         • {comp}")
            print(f"      Created: {collection.get('created', 'N/A')}")
        
        print()
    
    def show_menu(self, collections: Dict) -> str:
        """Admin menu"""
        print("🎯 Collection Management Menu:")
        print("-" * 60)
        print("  [1] View all collections")
        print("  [2] Create new collection")
        print("  [3] Edit collection")
        print("  [4] Delete collection")
        print("  [5] Add competency to collection")
        print("  [6] Remove competency from collection")
        print("  [0] Exit")
        print()
        
        while True:
            try:
                choice = input("Enter your choice (0-6): ").strip()
                if choice in ['0', '1', '2', '3', '4', '5', '6']:
                    return choice
                print("❌ Invalid choice")
            except KeyboardInterrupt:
                print("\n\nExiting...")
                sys.exit(0)
    
    def create_collection(self, collections: Dict) -> Dict:
        """Create a new collection"""
        print("\n📝 Create New Collection")
        print("-" * 60)
        
        while True:
            collection_id = input("Collection ID (kebab-case, e.g., my-team): ").strip()
            if not collection_id or collection_id.replace('-', '').replace('_', '').isalnum():
                if not any(c['id'] == collection_id for c in collections['collections']):
                    break
                print("❌ Collection ID already exists")
            else:
                print("❌ Invalid ID format")
        
        name = input("Collection name (e.g., My Team): ").strip()
        description = input("Description: ").strip()
        
        available = self.get_available_competencies()
        print("\nAvailable competencies:")
        for i, comp in enumerate(available, 1):
            print(f"  [{i}] {comp['id']} - {comp['name']}")
        
        selected = []
        while True:
            try:
                choices = input("\nSelect competencies (comma-separated numbers, e.g., 1,2,3): ").strip()
                if not choices:
                    # Use core collection competencies as default
                    core = next((c for c in collections['collections'] if c['id'] == 'core'), None)
                    if core:
                        selected = core['competencies'].copy()
                    break
                
                indices = [int(x.strip()) - 1 for x in choices.split(',')]
                for idx in indices:
                    if 0 <= idx < len(available):
                        selected.append(available[idx]['id'])
                    else:
                        print(f"Invalid index: {idx + 1}")
                
                if selected:
                    break
            except ValueError:
                print("Please enter valid numbers")
        
        new_collection = {
            "id": collection_id,
            "name": name,
            "description": description,
            "competencies": list(set(selected)),
            "locked": False,
            "created": datetime.now().isoformat()
        }
        
        collections['collections'].append(new_collection)
        collections['last_updated'] = datetime.now().isoformat()
        
        print(f"\n✅ Collection '{name}' created successfully!")
        
        # Offer to select and activate the new collection immediately
        self._offer_collection_selection(collection_id, name)
        
        return collections
    
    def _offer_collection_selection(self, collection_id: str, collection_name: str):
        """Offer to select and activate the newly created collection"""
        print("\n" + "🎯" + " Next Steps:")
        print("-" * 60)
        print(f"Your collection '{collection_name}' is ready to use!")
        print("\nWould you like to select and activate it now?")
        print("  [y] Yes, select this collection and generate OLAF commands")
        print("  [n] No, I'll select it later manually")
        
        choice = input("\nChoice [y/n]: ").strip().lower()
        
        if choice in ['y', 'yes']:
            self._activate_collection(collection_id, collection_name)
        else:
            print(f"\n💡 To use this collection later, run:")
            print(f"   python select_collection.py --collection {collection_id}")
            print(f"\n🔄 Or to reinitialize with a different collection:")
            print(f"   python select_collection.py")
    
    def _activate_collection(self, collection_id: str, collection_name: str):
        """Activate the collection by calling select_collection.py"""
        import subprocess
        import sys
        
        print(f"\n🚀 Activating collection '{collection_name}'...")
        
        try:
            # Path to select_collection.py (same directory)
            select_script = self.script_dir / "select_collection.py"
            
            # Run select_collection.py with the new collection
            result = subprocess.run([
                sys.executable, str(select_script), 
                "--collection", collection_id
            ], capture_output=True, text=True, cwd=self.script_dir)
            
            if result.returncode == 0:
                print("✅ Collection activated successfully!")
                print("\n📋 Summary:")
                print(f"   • Collection '{collection_name}' is now active")
                print("   • OLAF commands generated in .github/prompts/ and .windsurf/workflows/")
                print("   • Git exclude patterns updated")
                print(f"\n🎉 Ready to use! Try '/olaf-' commands in your IDE.")
            else:
                print(f"❌ Failed to activate collection. Error:")
                print(result.stderr)
                print(f"\n💡 You can activate manually with:")
                print(f"   python select_collection.py --collection {collection_id}")
                
        except Exception as e:
            print(f"❌ Error activating collection: {e}")
            print(f"\n💡 You can activate manually with:")
            print(f"   python select_collection.py --collection {collection_id}")
    
    def edit_collection(self, collections: Dict) -> Dict:
        """Edit an existing collection"""
        print("\n✏️  Edit Collection")
        print("-" * 60)
        
        # Show list of collections to select from
        editable = [c for c in collections['collections'] if not c.get('locked')]
        if not editable:
            print("❌ No editable collections available")
            return collections
        
        for i, coll in enumerate(editable, 1):
            print(f"  [{i}] {coll['name']} (ID: {coll['id']})")
        
        try:
            choice = int(input("\nSelect collection number to edit: ").strip())
            if choice < 1 or choice > len(editable):
                print("❌ Invalid selection")
                return collections
            collection_id = editable[choice - 1]['id']
        except ValueError:
            print("❌ Please enter a valid number")
            return collections
        
        # Find the actual collection in the main list
        collection = next((c for c in collections['collections'] if c['id'] == collection_id), None)
        if not collection:
            print("❌ Collection not found")
            return collections
        
        if collection.get('locked'):
            print(f"🔒 This collection is locked and cannot be edited")
            return collections
        
        print(f"\nCurrent collection: {collection['name']}")
        print("-" * 60)
        print(f"  Description: {collection['description']}")
        print(f"  Competencies: {', '.join(collection['competencies'])}")
        print()
        
        new_name = input("New name (press Enter to keep current): ").strip()
        if new_name:
            collection['name'] = new_name
        
        new_desc = input("New description (press Enter to keep current): ").strip()
        if new_desc:
            collection['description'] = new_desc
        
        print(f"\n✅ Collection '{collection_id}' updated!")
        collections['last_updated'] = datetime.now().isoformat()
        return collections
    
    def delete_collection(self, collections: Dict) -> Dict:
        """Delete a collection"""
        print("\n🗑️  Delete Collection")
        print("-" * 60)
        
        # Show list of editable collections to select from
        editable = [c for c in collections['collections'] if c['id'] not in self.protected_collections]
        if not editable:
            print("❌ No editable collections available")
            return collections
        
        for i, coll in enumerate(editable, 1):
            print(f"  [{i}] {coll['name']} (ID: {coll['id']})")
        
        try:
            choice = int(input("\nSelect collection number to delete: ").strip())
            if choice < 1 or choice > len(editable):
                print("❌ Invalid selection")
                return collections
            collection = editable[choice - 1]
            collection_id = collection['id']
        except ValueError:
            print("❌ Please enter a valid number")
            return collections
        
        confirm = input(f"⚠️  Really delete '{collection['name']}'? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            collections['collections'] = [c for c in collections['collections'] if c['id'] != collection_id]
            print(f"✅ Collection '{collection_id}' deleted!")
            collections['last_updated'] = datetime.now().isoformat()
        else:
            print("Cancelled")
        
        return collections
    
    def add_competency(self, collections: Dict) -> Dict:
        """Add competency to a collection"""
        print("\n➕ Add Competency to Collection")
        print("-" * 60)
        
        # Show list of collections to select from
        colls = collections['collections']
        for i, coll in enumerate(colls, 1):
            print(f"  [{i}] {coll['name']} (ID: {coll['id']})")
        
        try:
            choice = int(input("\nSelect collection number: ").strip())
            if choice < 1 or choice > len(colls):
                print("❌ Invalid selection")
                return collections
            collection = colls[choice - 1]
        except ValueError:
            print("❌ Please enter a valid number")
            return collections
        
        available = self.get_available_competencies()
        print("\nAvailable competencies:")
        for i, comp in enumerate(available, 1):
            status = "✓" if comp['id'] in collection['competencies'] else " "
            print(f"  [{i}] [{status}] {comp['id']}")
        
        while True:
            try:
                choice = int(input("\nSelect competency (number): ").strip())
                if 1 <= choice <= len(available):
                    comp_id = available[choice - 1]['id']
                    if comp_id not in collection['competencies']:
                        collection['competencies'].append(comp_id)
                        print(f"✅ Added '{comp_id}' to {collection['id']}")
                        collections['last_updated'] = datetime.now().isoformat()
                    else:
                        print(f"ℹ️  '{comp_id}' already in collection")
                    break
                print("❌ Invalid selection")
            except ValueError:
                print("Please enter a number")
        
        return collections
    
    def remove_competency(self, collections: Dict) -> Dict:
        """Remove competency from a collection"""
        print("\n➖ Remove Competency from Collection")
        print("-" * 60)
        
        # Get kernel competencies from core collection
        core = next((c for c in collections.get('collections', []) if c.get('id') == 'core'), None)
        kernel_comps = core.get('competencies', []) if core else []
        
        # Show list of collections to select from
        colls = collections['collections']
        for i, coll in enumerate(colls, 1):
            print(f"  [{i}] {coll['name']} (ID: {coll['id']})")
        
        try:
            choice = int(input("\nSelect collection number: ").strip())
            if choice < 1 or choice > len(colls):
                print("❌ Invalid selection")
                return collections
            collection = colls[choice - 1]
        except ValueError:
            print("❌ Please enter a valid number")
            return collections
        
        if not collection['competencies']:
            print("❌ Collection has no competencies")
            return collections
        
        print("\nCompetencies in collection:")
        for i, comp in enumerate(collection['competencies'], 1):
            is_kernel = comp in kernel_comps
            kernel_marker = " 🔒 (KERNEL - Cannot remove)" if is_kernel else ""
            print(f"  [{i}] {comp}{kernel_marker}")
        
        while True:
            try:
                choice = int(input("\nSelect competency to remove (number): ").strip())
                if 1 <= choice <= len(collection['competencies']):
                    comp_to_remove = collection['competencies'][choice - 1]
                    # Prevent removal of kernel competencies
                    if comp_to_remove in kernel_comps:
                        print(f"❌ Cannot remove '{comp_to_remove}' - it is a kernel competency required in all collections")
                        continue
                    removed = collection['competencies'].pop(choice - 1)
                    print(f"✅ Removed '{removed}' from {collection['id']}")
                    collections['last_updated'] = datetime.now().isoformat()
                    break
                print("❌ Invalid selection")
            except ValueError:
                print("Please enter a number")
        
        return collections
    
    def run_interactive(self):
        """Run interactive mode"""
        self.show_logo()
        
        collections = self.load_collections()
        print("✓ Collections loaded\n")
        
        while True:
            choice = self.show_menu(collections)
            
            if choice == '0':
                print("\n✨ Goodbye!\n")
                break
            elif choice == '1':
                self.show_collections(collections)
                # Always show selection guidance after viewing collections
                self._show_collection_selection_guidance(collections)
            elif choice == '2':
                collections = self.create_collection(collections)
                self.save_collections(collections)
                # Note: create_collection already calls _offer_collection_selection
            elif choice == '3':
                collections = self.edit_collection(collections)
                self.save_collections(collections)
                self._show_collection_selection_guidance(collections)
            elif choice == '4':
                collections = self.delete_collection(collections)
                self.save_collections(collections)
                self._show_collection_selection_guidance(collections)
            elif choice == '5':
                collections = self.add_competency(collections)
                self.save_collections(collections)
                self._show_collection_selection_guidance(collections)
            elif choice == '6':
                collections = self.remove_competency(collections)
                self.save_collections(collections)
                self._show_collection_selection_guidance(collections)
    
    def _show_collection_selection_guidance(self, collections: Dict):
        """Show guidance on how to select and use collections"""
        print("\n" + "🎯" + " Quick Selection Guide:")
        print("-" * 60)
        
        # Show available collections for quick selection
        available_collections = [c for c in collections['collections'] if not c.get('locked', False)]
        
        if available_collections:
            print("📋 Available collections to select:")
            for i, coll in enumerate(available_collections[:5], 1):  # Show first 5
                print(f"   python select_collection.py --collection {coll['id']}")
            
            if len(available_collections) > 5:
                print(f"   ... and {len(available_collections) - 5} more collections")
            
            print(f"\n💡 Or run interactively:")
            print(f"   python select_collection.py")
            
            # Show current active collection
            active_collection = collections.get('metadata', {}).get('active_collection')
            if active_collection:
                active_name = next((c['name'] for c in collections['collections'] 
                                  if c['id'] == active_collection), active_collection)
                print(f"\n📌 Current active: {active_name} ({active_collection})")
                print(f"   To regenerate commands: python select_collection.py --reinit")
        else:
            print("ℹ️  No collections available for selection")
    
    def list_collections(self):
        """List collections (non-interactive)"""
        collections = self.load_collections()
        
        # Clean invalid competencies before displaying
        collections = self.clean_invalid_competencies(collections)
        
        # Save cleaned collections back to file
        self.save_collections(collections)
        
        print()
        self.show_collections(collections)


def main():
    parser = argparse.ArgumentParser(description='OLAF Competency Collection Manager')
    parser.add_argument('--list', '-l', action='store_true', help='List all collections')
    
    args = parser.parse_args()
    
    manager = CollectionManager()
    
    if args.list:
        manager.list_collections()
    else:
        manager.run_interactive()


if __name__ == '__main__':
    main()
