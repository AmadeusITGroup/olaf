#!/usr/bin/env python3
"""
Manifest Schema Migration Tool for OLAF Framework

Semi-automated migration of non-compliant manifests to standard schema.
Creates backups and requires human approval before applying changes.

Usage:
    python migrate-manifest-schema.py [options]

Options:
    --manifest PATH         Migrate specific manifest file
    --all                   Migrate all non-compliant manifests
    --dry-run              Preview changes without applying
    --no-backup            Skip backup creation (not recommended)
    --auto-approve         Apply migrations without confirmation (use with caution)
"""

import json
import sys
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class MigrationAction:
    """Represents a single migration action"""
    action_type: str  # "add", "rename", "restructure", "convert"
    field: str
    description: str
    old_value: Any = None
    new_value: Any = None


@dataclass
class MigrationPlan:
    """Migration plan for a single manifest"""
    manifest_path: Path
    actions: List[MigrationAction]
    backup_path: Optional[Path] = None
    
    def is_empty(self) -> bool:
        return len(self.actions) == 0


class ManifestMigrator:
    """Migrates OLAF competency manifests to standard schema"""
    
    def __init__(self, dry_run: bool = False, create_backup: bool = True):
        self.dry_run = dry_run
        self.create_backup = create_backup
    
    def analyze_manifest(self, manifest_path: Path) -> MigrationPlan:
        """Analyze manifest and create migration plan"""
        plan = MigrationPlan(manifest_path=manifest_path, actions=[])
        
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {manifest_path}: {e}", file=sys.stderr)
            return plan
        
        # Detect schema variant and plan migrations
        self._plan_field_migrations(data, plan)
        self._plan_entry_points_migration(data, plan)
        self._plan_structure_migrations(data, plan)
        
        return plan
    
    def _plan_field_migrations(self, data: Dict, plan: MigrationPlan):
        """Plan field-level migrations"""
        # Handle 'package' -> 'name' migration
        if "package" in data and "name" not in data:
            plan.actions.append(MigrationAction(
                action_type="rename",
                field="package → name",
                description="Rename 'package' field to 'name'",
                old_value=data["package"],
                new_value=data["package"]
            ))
        
        # Add missing 'id' field if not present
        if "id" not in data:
            # Try to derive from name or package
            id_value = None
            if "name" in data:
                id_value = self._derive_id(data["name"])
            elif "package" in data:
                id_value = self._derive_id(data["package"])
            
            if id_value:
                plan.actions.append(MigrationAction(
                    action_type="add",
                    field="id",
                    description="Add missing 'id' field",
                    new_value=id_value
                ))
        
        # Add missing required fields with placeholder values
        required_fields = {
            "name": "NEEDS_VALUE",
            "version": "1.0.0",
            "description": "NEEDS_DESCRIPTION",
            "category": "NEEDS_CATEGORY"
        }
        
        for field, default_value in required_fields.items():
            if field not in data and field != "name":  # name handled above
                plan.actions.append(MigrationAction(
                    action_type="add",
                    field=field,
                    description=f"Add missing required field '{field}'",
                    new_value=default_value
                ))
        
        # Add recommended fields if missing
        if "author" not in data:
            plan.actions.append(MigrationAction(
                action_type="add",
                field="author",
                description="Add recommended 'author' field",
                new_value="OLAF Framework"
            ))
        
        if "created" not in data:
            plan.actions.append(MigrationAction(
                action_type="add",
                field="created",
                description="Add recommended 'created' field",
                new_value=datetime.now().strftime("%Y-%m-%d")
            ))
        
        if "updated" not in data:
            plan.actions.append(MigrationAction(
                action_type="add",
                field="updated",
                description="Add recommended 'updated' field",
                new_value=datetime.now().strftime("%Y-%m-%d")
            ))
    
    def _plan_entry_points_migration(self, data: Dict, plan: MigrationPlan):
        """Plan entry_points structure migration"""
        if "entry_points" not in data:
            return
        
        entry_points = data["entry_points"]
        
        # Handle old format: list of strings (file paths)
        if isinstance(entry_points, list) and entry_points:
            if isinstance(entry_points[0], str):
                plan.actions.append(MigrationAction(
                    action_type="restructure",
                    field="entry_points",
                    description="Convert entry_points from string list to object list",
                    old_value=f"{len(entry_points)} file paths",
                    new_value="Structured entry point objects"
                ))
        
        # Handle old format: dict with 'prompts' key
        elif isinstance(entry_points, dict):
            if "prompts" in entry_points:
                plan.actions.append(MigrationAction(
                    action_type="restructure",
                    field="entry_points",
                    description="Convert entry_points from dict format to list format",
                    old_value="Dict with 'prompts' key",
                    new_value="List of entry point objects"
                ))
        
        # Validate existing entry point objects
        elif isinstance(entry_points, list):
            for idx, entry in enumerate(entry_points):
                if isinstance(entry, dict):
                    # Check for missing required fields
                    required = ["name", "command", "file", "protocol"]
                    missing = [f for f in required if f not in entry]
                    
                    if missing:
                        plan.actions.append(MigrationAction(
                            action_type="add",
                            field=f"entry_points[{idx}]",
                            description=f"Add missing fields: {', '.join(missing)}",
                            old_value=entry.get("name", f"Entry {idx}"),
                            new_value=f"Add: {', '.join(missing)}"
                        ))
                    
                    # Check for old 'id' field (should be 'name')
                    if "id" in entry and "name" not in entry:
                        plan.actions.append(MigrationAction(
                            action_type="rename",
                            field=f"entry_points[{idx}].id → name",
                            description="Rename 'id' to 'name' in entry point",
                            old_value=entry["id"],
                            new_value=entry["id"]
                        ))
    
    def _plan_structure_migrations(self, data: Dict, plan: MigrationPlan):
        """Plan structural migrations"""
        # Ensure classification is a dict
        if "classification" in data and not isinstance(data["classification"], dict):
            if isinstance(data["classification"], list):
                plan.actions.append(MigrationAction(
                    action_type="restructure",
                    field="classification",
                    description="Convert classification from list to object",
                    old_value="List format",
                    new_value="Object with 'type' and 'reason'"
                ))
        
        # Ensure target_users is a dict
        if "target_users" in data and not isinstance(data["target_users"], dict):
            if isinstance(data["target_users"], list):
                plan.actions.append(MigrationAction(
                    action_type="restructure",
                    field="target_users",
                    description="Convert target_users from list to object",
                    old_value="List format",
                    new_value="Object with 'primary', 'secondary', 'description'"
                ))
    
    def apply_migration(self, plan: MigrationPlan) -> bool:
        """Apply migration plan to manifest"""
        if plan.is_empty():
            return True
        
        # Create backup
        if self.create_backup and not self.dry_run:
            backup_path = self._create_backup(plan.manifest_path)
            plan.backup_path = backup_path
            print(f"Created backup: {backup_path}")
        
        # Load manifest
        try:
            with open(plan.manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading manifest: {e}", file=sys.stderr)
            return False
        
        # Apply migrations
        data = self._apply_migrations(data, plan.actions)
        
        # Write migrated manifest
        if not self.dry_run:
            try:
                with open(plan.manifest_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write('\n')  # Add trailing newline
                print(f"✓ Migrated: {plan.manifest_path}")
                return True
            except Exception as e:
                print(f"Error writing manifest: {e}", file=sys.stderr)
                return False
        else:
            print(f"[DRY RUN] Would migrate: {plan.manifest_path}")
            return True
    
    def _apply_migrations(self, data: Dict, actions: List[MigrationAction]) -> Dict:
        """Apply migration actions to data"""
        result = data.copy()
        
        for action in actions:
            if action.action_type == "rename":
                if "→" in action.field:
                    old_field, new_field = action.field.split(" → ")
                    old_field = old_field.strip()
                    new_field = new_field.strip()
                    
                    # Handle nested fields (e.g., entry_points[0].id)
                    if "[" in old_field:
                        # Complex nested field - handle entry points
                        if old_field.startswith("entry_points["):
                            idx = int(old_field.split("[")[1].split("]")[0])
                            old_key = old_field.split(".")[-1]
                            new_key = new_field
                            if "entry_points" in result and idx < len(result["entry_points"]):
                                if old_key in result["entry_points"][idx]:
                                    result["entry_points"][idx][new_key] = result["entry_points"][idx].pop(old_key)
                    else:
                        # Simple field rename
                        if old_field in result:
                            result[new_field] = result.pop(old_field)
            
            elif action.action_type == "add":
                # Handle nested fields
                if "[" in action.field:
                    # Skip complex additions for now - require manual intervention
                    continue
                elif "." in action.field:
                    # Nested field like "classification.type"
                    parts = action.field.split(".")
                    parent = parts[0]
                    child = parts[1]
                    if parent not in result:
                        result[parent] = {}
                    if isinstance(result[parent], dict):
                        result[parent][child] = action.new_value
                else:
                    # Simple field addition
                    if action.field not in result:
                        result[action.field] = action.new_value
            
            elif action.action_type == "restructure":
                if action.field == "entry_points":
                    result["entry_points"] = self._restructure_entry_points(result.get("entry_points", []))
                elif action.field == "classification":
                    result["classification"] = self._restructure_classification(result.get("classification"))
                elif action.field == "target_users":
                    result["target_users"] = self._restructure_target_users(result.get("target_users"))
        
        return result
    
    def _restructure_entry_points(self, entry_points: Any) -> List[Dict]:
        """Restructure entry_points to standard format"""
        if isinstance(entry_points, list):
            if not entry_points:
                return []
            
            # If already objects, return as-is
            if isinstance(entry_points[0], dict):
                return entry_points
            
            # Convert string list to object list
            if isinstance(entry_points[0], str):
                result = []
                for file_path in entry_points:
                    # Extract name from file path
                    name = Path(file_path).stem.replace("-", " ").title()
                    result.append({
                        "name": name,
                        "command": name.lower(),
                        "file": file_path,
                        "protocol": "Act",
                        "use_case": "NEEDS_DESCRIPTION"
                    })
                return result
        
        elif isinstance(entry_points, dict):
            # Convert dict format to list
            if "prompts" in entry_points:
                result = []
                for file_path in entry_points["prompts"]:
                    name = Path(file_path).stem.replace("-", " ").title()
                    result.append({
                        "name": name,
                        "command": name.lower(),
                        "file": file_path,
                        "protocol": "Act",
                        "use_case": "NEEDS_DESCRIPTION"
                    })
                return result
        
        return []
    
    def _restructure_classification(self, classification: Any) -> Dict:
        """Restructure classification to standard format"""
        if isinstance(classification, list):
            # Convert list to dict
            return {
                "type": classification[0] if classification else "NEEDS_VALUE",
                "reason": "NEEDS_DESCRIPTION"
            }
        elif isinstance(classification, dict):
            return classification
        return {"type": "NEEDS_VALUE", "reason": "NEEDS_DESCRIPTION"}
    
    def _restructure_target_users(self, target_users: Any) -> Dict:
        """Restructure target_users to standard format"""
        if isinstance(target_users, list):
            # Convert list to dict
            return {
                "primary": target_users[0] if target_users else "NEEDS_VALUE",
                "secondary": target_users[1:] if len(target_users) > 1 else [],
                "description": "NEEDS_DESCRIPTION"
            }
        elif isinstance(target_users, dict):
            return target_users
        return {"primary": "NEEDS_VALUE", "secondary": [], "description": "NEEDS_DESCRIPTION"}
    
    @staticmethod
    def _derive_id(name: str) -> str:
        """Derive kebab-case id from name"""
        return name.lower().replace(" ", "-").replace("_", "-")
    
    @staticmethod
    def _create_backup(manifest_path: Path) -> Path:
        """Create backup of manifest file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = manifest_path.with_suffix(f".backup_{timestamp}.json")
        shutil.copy2(manifest_path, backup_path)
        return backup_path


def format_migration_plan(plan: MigrationPlan) -> str:
    """Format migration plan for display"""
    lines = []
    lines.append(f"\nMigration Plan: {plan.manifest_path}")
    lines.append("-" * 80)
    
    if plan.is_empty():
        lines.append("No migrations needed - manifest is compliant")
        return "\n".join(lines)
    
    for idx, action in enumerate(plan.actions, 1):
        lines.append(f"\n{idx}. [{action.action_type.upper()}] {action.field}")
        lines.append(f"   {action.description}")
        if action.old_value is not None:
            lines.append(f"   Old: {action.old_value}")
        if action.new_value is not None:
            lines.append(f"   New: {action.new_value}")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Migrate OLAF competency manifests to standard schema"
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Migrate specific manifest file"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Migrate all non-compliant manifests"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip backup creation (not recommended)"
    )
    parser.add_argument(
        "--auto-approve",
        action="store_true",
        help="Apply migrations without confirmation (use with caution)"
    )
    
    args = parser.parse_args()
    
    if not args.all and not args.manifest:
        parser.error("Must specify either --all or --manifest")
    
    migrator = ManifestMigrator(
        dry_run=args.dry_run,
        create_backup=not args.no_backup
    )
    
    manifests = []
    
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
            print(f"Error: Cannot find olaf-core/competencies", file=sys.stderr)
            sys.exit(1)
        
        manifests = list(competencies_path.rglob("competency-manifest.json"))
        print(f"Found {len(manifests)} manifest files\n")
    
    elif args.manifest:
        if not args.manifest.exists():
            print(f"Error: Manifest not found: {args.manifest}", file=sys.stderr)
            sys.exit(1)
        manifests = [args.manifest]
    
    # Analyze all manifests
    plans = []
    for manifest in manifests:
        plan = migrator.analyze_manifest(manifest)
        if not plan.is_empty():
            plans.append(plan)
    
    if not plans:
        print("✓ All manifests are compliant - no migrations needed")
        sys.exit(0)
    
    print(f"Found {len(plans)} manifests requiring migration\n")
    print("=" * 80)
    
    # Display migration plans
    import sys
    import io
    # Ensure stdout can handle Unicode
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    for plan in plans:
        print(format_migration_plan(plan))
        print()
    
    print("=" * 80)
    
    # Confirm before applying
    if not args.dry_run and not args.auto_approve:
        response = input("\nApply these migrations? (yes/no): ").strip().lower()
        if response not in ["yes", "y"]:
            print("Migration cancelled")
            sys.exit(0)
    
    # Apply migrations
    print("\nApplying migrations...\n")
    success_count = 0
    for plan in plans:
        if migrator.apply_migration(plan):
            success_count += 1
    
    print(f"\n✓ Successfully migrated {success_count}/{len(plans)} manifests")
    
    if args.dry_run:
        print("\n[DRY RUN] No changes were actually applied")
        print("Run without --dry-run to apply migrations")


if __name__ == "__main__":
    main()
