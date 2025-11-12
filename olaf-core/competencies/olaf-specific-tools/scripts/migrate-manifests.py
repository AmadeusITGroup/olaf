#!/usr/bin/env python3
"""
Manifest Migration Script

Migrates competency manifests to the standard schema by:
- Converting entry_points[].id to entry_points[].name (title case)
- Adding entry_points[].command from id or aliases
- Capitalizing protocol values
- Adding use_case from description field
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


def to_title_case(text: str) -> str:
    """Convert kebab-case or snake_case to Title Case"""
    return text.replace('-', ' ').replace('_', ' ').title()


def migrate_entry_point(entry: Dict) -> Dict:
    """Migrate a single entry point to standard schema"""
    migrated = entry.copy()
    
    # Convert id to name if name is missing
    if 'id' in entry and 'name' not in entry:
        migrated['name'] = to_title_case(entry['id'])
    
    # Add command from id or aliases if missing
    if 'command' not in entry:
        if 'id' in entry:
            # Use first alias if available, otherwise use id
            if 'aliases' in entry and entry['aliases']:
                migrated['command'] = entry['aliases'][0]
            else:
                migrated['command'] = entry['id'].replace('-', ' ')
        elif 'name' in migrated:
            migrated['command'] = migrated['name'].lower()
    
    # Capitalize protocol
    if 'protocol' in entry:
        protocol = entry['protocol']
        if protocol == 'act':
            migrated['protocol'] = 'Act'
        elif protocol == 'propose-act':
            migrated['protocol'] = 'Propose-Act'
        elif protocol == 'propose-confirm-act':
            migrated['protocol'] = 'Propose-Confirm-Act'
    
    # Add use_case from description if missing
    if 'use_case' not in entry and 'description' in entry:
        migrated['use_case'] = entry['description']
    
    return migrated


def migrate_manifest(manifest_path: Path, dry_run: bool = False) -> bool:
    """Migrate a single manifest file"""
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {manifest_path}: {e}")
        return False
    
    modified = False
    
    # Migrate entry_points
    if 'entry_points' in data and isinstance(data['entry_points'], list):
        new_entry_points = []
        for entry in data['entry_points']:
            if isinstance(entry, dict):
                migrated_entry = migrate_entry_point(entry)
                new_entry_points.append(migrated_entry)
                if migrated_entry != entry:
                    modified = True
            else:
                new_entry_points.append(entry)
        
        if modified:
            data['entry_points'] = new_entry_points
    
    # Fix classification if it's a string
    if 'classification' in data and isinstance(data['classification'], str):
        data['classification'] = {
            'type': data['classification'],
            'reason': 'Migrated from string value'
        }
        modified = True
    
    if modified:
        if dry_run:
            print(f"[DRY RUN] Would update: {manifest_path}")
        else:
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Migrated: {manifest_path}")
        return True
    else:
        print(f"  No changes needed: {manifest_path}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Migrate OLAF manifests to standard schema')
    parser.add_argument('--all', action='store_true', help='Migrate all manifests')
    parser.add_argument('--manifest', type=str, help='Migrate specific manifest')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed')
    
    args = parser.parse_args()
    
    if not (args.all or args.manifest):
        parser.print_help()
        return 1
    
    # Find workspace root
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent.parent.parent.parent
    competencies_dir = workspace_root / 'olaf-core' / 'competencies'
    
    manifests_to_migrate = []
    
    if args.all:
        # Find all manifests
        for pack_dir in competencies_dir.rglob('*'):
            if pack_dir.is_dir():
                manifest_path = pack_dir / 'competency-manifest.json'
                if manifest_path.exists():
                    manifests_to_migrate.append(manifest_path)
    elif args.manifest:
        manifest_path = Path(args.manifest)
        if not manifest_path.exists():
            manifest_path = competencies_dir / args.manifest / 'competency-manifest.json'
        if manifest_path.exists():
            manifests_to_migrate.append(manifest_path)
        else:
            print(f"Error: Manifest not found: {args.manifest}")
            return 1
    
    print(f"\nFound {len(manifests_to_migrate)} manifest(s) to process\n")
    
    migrated_count = 0
    for manifest_path in sorted(manifests_to_migrate):
        if migrate_manifest(manifest_path, dry_run=args.dry_run):
            migrated_count += 1
    
    print(f"\n{'[DRY RUN] Would migrate' if args.dry_run else 'Migrated'} {migrated_count} manifest(s)")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
