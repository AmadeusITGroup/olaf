#!/usr/bin/env python3
"""
OLAF Stash Manager - Cross-platform file stashing and restoration system

This tool provides a clean Python interface for the OLAF stash system,
replacing complex shell commands with simple Python methods.
"""

import os
import sys
import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class OLAFStashManager:
    """Cross-platform stash management for OLAF framework"""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root).resolve()
        self.stash_dir = self.workspace_root / "olaf-stashes"
        self.gitignore_path = self.workspace_root / ".gitignore"
        
    def ensure_stash_directory(self) -> None:
        """Create stash directory and ensure it's git-ignored"""
        self.stash_dir.mkdir(exist_ok=True)
        
        # Add to .gitignore if not present
        gitignore_content = ""
        if self.gitignore_path.exists():
            gitignore_content = self.gitignore_path.read_text()
            
        if "olaf-stashes/" not in gitignore_content:
            with open(self.gitignore_path, "a", encoding="utf-8") as f:
                f.write("\n# OLAF Stash directories\nolaf-stashes/\n")
    
    def get_git_status(self) -> Tuple[List[str], List[str]]:
        """Get unstaged and untracked files from git status"""
        import subprocess
        
        try:
            # Get unstaged files
            result = subprocess.run(
                ["git", "diff", "--name-only"], 
                capture_output=True, text=True, cwd=self.workspace_root
            )
            unstaged = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            # Get untracked files
            result = subprocess.run(
                ["git", "ls-files", "--others", "--exclude-standard"], 
                capture_output=True, text=True, cwd=self.workspace_root
            )
            untracked = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            return unstaged, untracked
            
        except subprocess.SubprocessError as e:
            print(f"Git command failed: {e}")
            return [], []
    
    def create_stash(self, subject: str, reason: str = "Manual stash") -> Optional[Path]:
        """Create a new stash with all unstaged/untracked files"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        stash_name = f"{timestamp}-{subject}"
        stash_path = self.stash_dir / stash_name
        
        self.ensure_stash_directory()
        
        # Get files to stash
        unstaged, untracked = self.get_git_status()
        all_files = [f for f in unstaged + untracked if f and Path(f).exists()]
        
        if not all_files:
            print("No unstaged or untracked files found to stash")
            return None
        
        # Create stash directory
        stash_path.mkdir(parents=True, exist_ok=True)
        
        # Copy files maintaining structure
        copied_files = []
        for file_path in all_files:
            source = self.workspace_root / file_path
            target = stash_path / file_path
            
            if source.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)  # Preserves timestamps
                copied_files.append(file_path)
        
        # Create context documentation
        context_data = {
            "timestamp": datetime.now().isoformat(),
            "subject": subject,
            "reason": reason,
            "stash_location": str(stash_path.relative_to(self.workspace_root)),
            "files_preserved": {
                "unstaged": unstaged,
                "untracked": untracked,
                "copied": copied_files
            },
            "git_state": self._get_git_state()
        }
        
        context_file = stash_path / "_stash-context.json"
        with open(context_file, "w", encoding="utf-8") as f:
            json.dump(context_data, f, indent=2)
        
        # Also create markdown for human readability
        self._create_context_markdown(stash_path, context_data)
        
        print(f"✅ Stash created: {stash_name}")
        print(f"📁 Location: {stash_path}")
        print(f"📄 Files: {len(copied_files)} files preserved")
        
        return stash_path
    
    def list_stashes(self) -> List[Dict]:
        """List all available stashes with metadata"""
        if not self.stash_dir.exists():
            return []
        
        stashes = []
        for stash_dir in sorted(self.stash_dir.iterdir(), reverse=True):
            if stash_dir.is_dir():
                context_file = stash_dir / "_stash-context.json"
                
                if context_file.exists():
                    # New format with JSON
                    try:
                        with open(context_file, "r", encoding="utf-8") as f:
                            context = json.load(f)
                        
                        file_count = len(context.get("files_preserved", {}).get("copied", []))
                        
                        stashes.append({
                            "name": stash_dir.name,
                            "path": stash_dir,
                            "subject": context.get("subject", "Unknown"),
                            "timestamp": context.get("timestamp", ""),
                            "reason": context.get("reason", ""),
                            "file_count": file_count,
                            "context": context
                        })
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"Warning: Invalid JSON stash context in {stash_dir.name}: {e}")
                
                elif (stash_dir / "_stash-context.md").exists():
                    # Legacy format with only Markdown
                    file_count = sum(1 for item in stash_dir.rglob("*") 
                                   if item.is_file() and item.name != "_stash-context.md")
                    
                    # Extract subject from directory name (format: YYYYMMDD-HHMM-subject)
                    parts = stash_dir.name.split('-', 2)
                    subject = parts[2] if len(parts) > 2 else "legacy-stash"
                    
                    stashes.append({
                        "name": stash_dir.name,
                        "path": stash_dir,
                        "subject": subject.replace('-', ' ').title(),
                        "timestamp": "",  # Legacy stashes don't have ISO timestamps
                        "reason": "Legacy stash (no JSON context)",
                        "file_count": file_count,
                        "context": {}
                    })
        
        return stashes
    
    def check_conflicts(self, stash_path: Path) -> List[Dict]:
        """Check for conflicts between stash files and current workspace"""
        conflicts = []
        
        # Try JSON context first (new format)
        context_file = stash_path / "_stash-context.json"
        copied_files = []
        
        if context_file.exists():
            try:
                with open(context_file, "r", encoding="utf-8") as f:
                    context = json.load(f)
                copied_files = context.get("files_preserved", {}).get("copied", [])
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error reading JSON context: {e}")
        else:
            # Fallback: scan directory for files (legacy format)
            print("No JSON context found, scanning stash directory...")
            for item in stash_path.rglob("*"):
                if item.is_file() and item.name != "_stash-context.md":
                    relative_path = str(item.relative_to(stash_path))
                    copied_files.append(relative_path)
        
        # Check each file for conflicts
        for file_path in copied_files:
            stash_file = stash_path / file_path
            current_file = self.workspace_root / file_path
            
            if current_file.exists() and stash_file.exists():
                stash_time = stash_file.stat().st_mtime
                current_time = current_file.stat().st_mtime
                
                print(f"Checking {file_path}:")
                print(f"  Stash time: {datetime.fromtimestamp(stash_time)}")
                print(f"  Current time: {datetime.fromtimestamp(current_time)}")
                
                if current_time > stash_time:
                    conflicts.append({
                        "file": file_path,
                        "stash_time": datetime.fromtimestamp(stash_time),
                        "current_time": datetime.fromtimestamp(current_time),
                        "time_diff": current_time - stash_time
                    })
        
        return conflicts
    
    def restore_stash(self, stash_name: str, backup_conflicts: bool = False, 
                     force: bool = False) -> bool:
        """Restore files from a stash"""
        stash_path = self.stash_dir / stash_name
        
        if not stash_path.exists():
            print(f"Stash not found: {stash_name}")
            return False
        
        # Check for conflicts unless force is used
        if not force:
            conflicts = self.check_conflicts(stash_path)
            if conflicts and not backup_conflicts:
                print("⚠️  CONFLICTS DETECTED:")
                for conflict in conflicts:
                    print(f"❌ {conflict['file']}")
                    print(f"   Current: {conflict['current_time'].strftime('%Y-%m-%d %H:%M')}")
                    print(f"   Stash:   {conflict['stash_time'].strftime('%Y-%m-%d %H:%M')}")
                return False
        
        # Load stash context
        context_file = stash_path / "_stash-context.json" 
        with open(context_file, "r", encoding="utf-8") as f:
            context = json.load(f)
        
        copied_files = context.get("files_preserved", {}).get("copied", [])
        
        # Create backups if requested
        backup_dir = None
        if backup_conflicts:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M")
            backup_dir = self.workspace_root / f"backup-{timestamp}"
            backup_dir.mkdir(exist_ok=True)
        
        # Restore files
        restored_count = 0
        for file_path in copied_files:
            stash_file = stash_path / file_path
            target_file = self.workspace_root / file_path
            
            if stash_file.exists():
                # Create backup if needed
                if backup_dir and target_file.exists():
                    backup_target = backup_dir / file_path
                    backup_target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(target_file, backup_target)
                
                # Restore file
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(stash_file, target_file)
                restored_count += 1
        
        print(f"✅ Stash restored: {stash_name}")
        print(f"📄 Files: {restored_count} files restored")
        if backup_dir:
            print(f"📁 Backups: {backup_dir}")
        
        return True
    
    def delete_stash(self, stash_name: str, confirm: bool = False) -> bool:
        """Delete a stash permanently"""
        stash_path = self.stash_dir / stash_name
        
        if not stash_path.exists():
            print(f"Stash not found: {stash_name}")
            return False
        
        # Safety check - require confirmation for deletion
        if not confirm:
            print(f"⚠️  Are you sure you want to delete stash '{stash_name}'?")
            print("This action cannot be undone!")
            response = input("Type 'DELETE' to confirm: ")
            if response != "DELETE":
                print("Deletion cancelled.")
                return False
        
        # Delete the entire stash directory
        import shutil
        try:
            shutil.rmtree(stash_path)
            print(f"✅ Stash deleted: {stash_name}")
            return True
        except Exception as e:
            print(f"❌ Error deleting stash: {e}")
            return False
    
    def _get_git_state(self) -> Dict:
        """Get current git repository state"""
        import subprocess
        
        try:
            # Get current branch
            result = subprocess.run(
                ["git", "branch", "--show-current"], 
                capture_output=True, text=True, cwd=self.workspace_root
            )
            branch = result.stdout.strip()
            
            # Get last commit
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"], 
                capture_output=True, text=True, cwd=self.workspace_root
            )
            commit = result.stdout.strip()
            
            return {"branch": branch, "last_commit": commit}
            
        except subprocess.SubprocessError:
            return {"branch": "unknown", "last_commit": "unknown"}
    
    def _create_context_markdown(self, stash_path: Path, context_data: Dict) -> None:
        """Create human-readable markdown context file"""
        markdown_content = f"""# STASH CONTEXT - {context_data['timestamp']}
==============================

## Work Transition Notice:
🔄 **CURRENT WORK PAUSED** - Moving to new work session
📋 **STASH REASON**: {context_data['reason']}
📁 **STASH LOCATION**: {context_data['stash_location']}

## Files Preserved:
### Unstaged Files:
{chr(10).join(f"- {f}" for f in context_data['files_preserved']['unstaged'])}

### Untracked Files: 
{chr(10).join(f"- {f}" for f in context_data['files_preserved']['untracked'])}

### Git State:
- Branch: {context_data['git_state']['branch']}
- Last commit: {context_data['git_state']['last_commit']}

## Restoration Commands:
```
python olaf-core/competencies/common/tools/stash_manager.py restore {stash_path.name}
```

## Transition Notes:
✅ Files preserved in stash directory
✅ Work context documented  
🚀 Ready for new work session
"""
        
        markdown_file = stash_path / "_stash-context.md"
        with open(markdown_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)


def main():
    """Command line interface for OLAF Stash Manager"""
    parser = argparse.ArgumentParser(description="OLAF Stash Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create stash command
    create_parser = subparsers.add_parser("create", help="Create a new stash")
    create_parser.add_argument("subject", help="Subject/name for the stash")
    create_parser.add_argument("--reason", default="Manual stash", help="Reason for stashing")
    
    # List stashes command
    list_parser = subparsers.add_parser("list", help="List available stashes")
    
    # Check conflicts command
    conflicts_parser = subparsers.add_parser("conflicts", help="Check conflicts for a stash")
    conflicts_parser.add_argument("stash_name", help="Name of the stash to check")
    
    # Restore stash command
    restore_parser = subparsers.add_parser("restore", help="Restore a stash")
    restore_parser.add_argument("stash_name", help="Name of the stash to restore")
    restore_parser.add_argument("--backup", action="store_true", help="Backup conflicting files")
    restore_parser.add_argument("--force", action="store_true", help="Force restore (dangerous)")
    
    # Delete stash command
    delete_parser = subparsers.add_parser("delete", help="Delete a stash permanently")
    delete_parser.add_argument("stash_name", help="Name of the stash to delete")
    delete_parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = OLAFStashManager()
    
    if args.command == "create":
        manager.create_stash(args.subject, args.reason)
    
    elif args.command == "list":
        stashes = manager.list_stashes()
        if not stashes:
            print("No stashes found")
        else:
            print("🔄 Available Work Stashes:\n")
            for i, stash in enumerate(stashes, 1):
                if stash['timestamp']:
                    timestamp = datetime.fromisoformat(stash['timestamp']).strftime('%b %d, %H:%M')
                else:
                    # Extract from directory name for legacy stashes
                    parts = stash['name'].split('-')
                    if len(parts) >= 2:
                        date_str = f"{parts[0]}-{parts[1]}"
                        try:
                            timestamp = datetime.strptime(date_str, "%Y%m%d-%H%M").strftime('%b %d, %H:%M')
                        except ValueError:
                            timestamp = "Unknown"
                    else:
                        timestamp = "Unknown"
                        
                print(f"{i}. **{stash['subject']}** - {timestamp}")
                print(f"   📁 Directory: {stash['name']}")
                print(f"   📄 Files: {stash['file_count']} files preserved")
                print(f"   📝 Reason: {stash['reason']}")
                print()
    
    elif args.command == "conflicts":
        stash_path = manager.stash_dir / args.stash_name
        conflicts = manager.check_conflicts(stash_path)
        if not conflicts:
            print("✅ No conflicts detected - safe to restore")
        else:
            print("⚠️ CONFLICT DETECTED: Files with newer modifications found\n")
            print("Conflicting Files:")
            for conflict in conflicts:
                current_str = conflict['current_time'].strftime('%Y-%m-%d %H:%M')
                stash_str = conflict['stash_time'].strftime('%Y-%m-%d %H:%M')
                print(f"❌ {conflict['file']} - Current: {current_str}, Stash: {stash_str}")
    
    elif args.command == "restore":
        success = manager.restore_stash(args.stash_name, args.backup, args.force)
        if not success:
            sys.exit(1)
    
    elif args.command == "delete":
        success = manager.delete_stash(args.stash_name, args.yes)
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    main()