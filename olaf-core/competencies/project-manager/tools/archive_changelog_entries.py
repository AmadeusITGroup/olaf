#!/usr/bin/env python3
"""
Archive Changelog Entries

Script to archive changelog entries older than a specified number of days.
Moves old entries to an archive file and optionally adds a maintenance entry.
"""

import argparse
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple

def parse_date_from_heading(line: str) -> str:
    """Extract date from markdown heading (format: ## YYYY-MM-DD or ### YYYYMMDD)"""
    # Match both formats: ## YYYY-MM-DD and ### YYYYMMDD
    match = re.match(r'^\s*#{2,3}\s+(\d{4}-?\d{2}-?\d{2})\s*$', line)
    if match:
        date_str = match.group(1)
        # Normalize to YYYY-MM-DD format
        if '-' not in date_str:
            # Convert YYYYMMDD to YYYY-MM-DD
            if len(date_str) == 8:
                return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        return date_str
    return None

def is_date_before_cutoff(date_str: str, cutoff_date: datetime) -> bool:
    """Check if the date string represents a date before the cutoff"""
    try:
        # Handle both YYYY-MM-DD and YYYYMMDD formats
        if '-' in date_str:
            entry_date = datetime.strptime(date_str, '%Y-%m-%d')
        else:
            entry_date = datetime.strptime(date_str, '%Y%m%d')
        return entry_date < cutoff_date
    except ValueError:
        print(f"Warning: Could not parse date '{date_str}'")
        return False

def process_changelog(changelog_path: str, cutoff_date: datetime) -> Tuple[List[str], List[str]]:
    """
    Process changelog file and separate kept and archived lines.
    Returns (kept_lines, archived_lines)
    """
    try:
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading changelog file: {e}")
        sys.exit(1)
    
    lines = content.splitlines()
    kept_lines = []
    archived_lines = []
    in_header_section = True
    in_old_section = False
    current_date = ""
    
    for line in lines:
        # Capture the header section (everything before the first date heading)
        if in_header_section:
            date_str = parse_date_from_heading(line)
            if date_str:
                in_header_section = False
                current_date = date_str
                
                # Check if this date is before the cutoff
                if is_date_before_cutoff(current_date, cutoff_date):
                    in_old_section = True
                    archived_lines.append(line)
                else:
                    in_old_section = False
                    kept_lines.append(line)
            else:
                kept_lines.append(line)
        else:
            # Process content after the header
            date_str = parse_date_from_heading(line)
            if date_str:
                current_date = date_str
                
                # Check if this date is before the cutoff
                if is_date_before_cutoff(current_date, cutoff_date):
                    in_old_section = True
                else:
                    in_old_section = False
            
            # Add line to appropriate array
            if in_old_section:
                archived_lines.append(line)
            else:
                kept_lines.append(line)
    
    return kept_lines, archived_lines

def create_or_update_archive(archive_path: str, archived_lines: List[str], days_to_keep: int):
    """Create or update the archive file with new archived content"""
    archive_path_obj = Path(archive_path)
    
    if not archive_path_obj.exists():
        # Create new archive file
        archive_header = (
            f"# Archived Changelog Entries\n\n"
            f"This file contains archived changelog entries older than {days_to_keep} days "
            f"from the active changelog register.\n\n"
        )
        archive_content = archive_header
    else:
        # Read existing archive content
        try:
            with open(archive_path, 'r', encoding='utf-8') as f:
                archive_content = f.read()
        except Exception as e:
            print(f"Error reading archive file: {e}")
            sys.exit(1)
        
        # Ensure proper spacing
        if not archive_content.endswith('\n\n'):
            archive_content += '\n\n'
    
    # Add the archived content
    if archived_lines:
        archive_content += '\n'.join(archived_lines)
        
        # Ensure file ends with newline
        if not archive_content.endswith('\n'):
            archive_content += '\n'
        
        # Save the archive file
        try:
            with open(archive_path, 'w', encoding='utf-8') as f:
                f.write(archive_content)
            print(f"Archived {len(archived_lines)} lines to {archive_path}")
        except Exception as e:
            print(f"Error writing archive file: {e}")
            sys.exit(1)

def save_updated_changelog(changelog_path: str, kept_lines: List[str]):
    """Save the updated changelog with only kept entries"""
    kept_content = '\n'.join(kept_lines)
    try:
        with open(changelog_path, 'w', encoding='utf-8') as f:
            f.write(kept_content)
        print(f"Kept {len(kept_lines)} lines in {changelog_path}")
    except Exception as e:
        print(f"Error writing changelog file: {e}")
        sys.exit(1)

def add_maintenance_entry(changelog_path: str, kept_lines: List[str], archived_lines: List[str], 
                         days_to_keep: int, cutoff_date: datetime):
    """Add a maintenance entry to the changelog"""
    today = datetime.now()
    timestamp = today.strftime("%H:%M")
    entry_date = today.strftime("%Y%m%d")
    year_month = today.strftime("%Y-%m")
    
    # Count entries
    kept_entry_count = len([line for line in kept_lines if re.match(r'^\s*-\s+', line)])
    archived_entry_count = len([line for line in archived_lines if re.match(r'^\s*-\s+', line)])
    cutoff_date_str = cutoff_date.strftime("%Y%m%d")
    
    maintenance_entry = (
        f"- {timestamp} - Maintenance: Performed weekly changelog archiving. "
        f"Moved entries older than {days_to_keep} days (before {cutoff_date_str}) to "
        f"`changelog-register-archive.md`. Maintained {kept_entry_count} entries in the main file "
        f"and archived {archived_entry_count} entries for improved performance. (by @HAL)"
    )
    
    # Read current content
    try:
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading changelog for maintenance entry: {e}")
        return
    
    # Check if today's date section exists
    today_section = f"### {entry_date}"
    
    if today_section in content:
        # Insert at the top of today's entries
        pattern = rf"{re.escape(today_section)}\r?\n((?:- .*\r?\n)*)"
        match = re.search(pattern, content)
        if match:
            existing_entries = match.group(1)
            updated_entries = f"{maintenance_entry}\n{existing_entries}"
            new_content = re.sub(pattern, f"{today_section}\n{updated_entries}", content)
        else:
            # Today section exists but no entries yet
            new_content = content.replace(today_section, f"{today_section}\n{maintenance_entry}")
    else:
        # Today's section doesn't exist, check if month section exists
        month_section = f"## {year_month}"
        
        if month_section in content:
            # Insert after month heading
            month_pattern = rf"{re.escape(month_section)}\r?\n"
            new_content = re.sub(month_pattern, f"{month_section}\n\n{today_section}\n{maintenance_entry}\n", content)
        else:
            # Need to add both month and day sections
            header_pattern = r"# Changelog\r?\n"
            new_content = re.sub(header_pattern, f"# Changelog\n\n## {year_month}\n\n{today_section}\n{maintenance_entry}\n", content)
    
    # Save the updated changelog with maintenance entry
    try:
        with open(changelog_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Added maintenance entry to changelog")
    except Exception as e:
        print(f"Error adding maintenance entry: {e}")

def main():
    parser = argparse.ArgumentParser(description='Archive changelog entries older than specified days')
    parser.add_argument('changelog_path', help='Path to the changelog file')
    parser.add_argument('archive_path', help='Path to the archive file')
    parser.add_argument('--days-to-keep', type=int, default=7,
                       help='Number of days to keep in main changelog (default: 7)')
    parser.add_argument('--no-maintenance-entry', action='store_true',
                       help='Skip adding maintenance entry to changelog')
    
    args = parser.parse_args()
    
    # Validate paths
    changelog_path = Path(args.changelog_path)
    if not changelog_path.exists():
        print(f"Error: Changelog file not found at path: {args.changelog_path}")
        sys.exit(1)
    
    # Calculate cutoff date
    today = datetime.now()
    cutoff_date = today - timedelta(days=args.days_to_keep)
    cutoff_string = cutoff_date.strftime("%Y%m%d")
    
    print(f"Today: {today}")
    print(f"Cutoff date ({args.days_to_keep} days ago): {cutoff_date}")
    print(f"Will archive entries before: {cutoff_string}")
    
    # Process the changelog
    kept_lines, archived_lines = process_changelog(str(changelog_path), cutoff_date)
    
    # Create or update archive file
    if archived_lines:
        create_or_update_archive(args.archive_path, archived_lines, args.days_to_keep)
    else:
        print("No entries to archive.")
    
    # Save the updated changelog
    save_updated_changelog(str(changelog_path), kept_lines)
    
    # Add maintenance entry if requested
    if not args.no_maintenance_entry:
        add_maintenance_entry(str(changelog_path), kept_lines, archived_lines, 
                            args.days_to_keep, cutoff_date)
    
    print("Changelog archiving completed successfully")

if __name__ == "__main__":
    main()
