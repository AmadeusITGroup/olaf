#!/usr/bin/env python3
"""
migrate-junit4-to-junit5.py
Automatically migrates JUnit 4 test files to JUnit 5 (Jupiter)
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple

def print_header():
    print("=" * 60)
    print("JUnit 4 to JUnit 5 Migration Script")
    print("=" * 60)
    print()

def find_java_test_files(project_path: Path) -> List[Path]:
    """Find all Java test files in the project."""
    test_path = project_path / "src" / "test" / "java"
    
    if not test_path.exists():
        print(f"ERROR: Test directory not found: {test_path}")
        sys.exit(1)
    
    java_files = list(test_path.rglob("*.java"))
    print(f"Found {len(java_files)} Java test files")
    print()
    
    return java_files

def migrate_file(file_path: Path, dry_run: bool = False) -> Tuple[int, List[str]]:
    """
    Migrate a single Java test file from JUnit 4 to JUnit 5.
    Returns: (number_of_changes, list_of_change_descriptions)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # 1. Import replacements
    replacements = [
        (r'import org\.junit\.Test;', 
         'import org.junit.jupiter.api.Test;',
         'Import: org.junit.Test → org.junit.jupiter.api.Test'),
        
        (r'import org\.junit\.Before;', 
         'import org.junit.jupiter.api.BeforeEach;',
         'Import: org.junit.Before → org.junit.jupiter.api.BeforeEach'),
        
        (r'import org\.junit\.After;', 
         'import org.junit.jupiter.api.AfterEach;',
         'Import: org.junit.After → org.junit.jupiter.api.AfterEach'),
        
        (r'import org\.junit\.BeforeClass;', 
         'import org.junit.jupiter.api.BeforeAll;',
         'Import: org.junit.BeforeClass → org.junit.jupiter.api.BeforeAll'),
        
        (r'import org\.junit\.AfterClass;', 
         'import org.junit.jupiter.api.AfterAll;',
         'Import: org.junit.AfterClass → org.junit.jupiter.api.AfterAll'),
        
        (r'import org\.junit\.Ignore;', 
         'import org.junit.jupiter.api.Disabled;',
         'Import: org.junit.Ignore → org.junit.jupiter.api.Disabled'),
        
        (r'import org\.junit\.Rule;', 
         '// import org.junit.Rule; // JUnit 5: Use @RegisterExtension instead',
         'Import: Commented org.junit.Rule (use @RegisterExtension in JUnit 5)'),
        
        (r'import org\.junit\.rules\.ExpectedException;', 
         '// import org.junit.rules.ExpectedException; // JUnit 5: Use assertThrows() instead',
         'Import: Commented ExpectedException (use assertThrows in JUnit 5)'),
        
        (r'import org\.junit\.runner\.RunWith;', 
         '// import org.junit.runner.RunWith; // Not needed in Spring Boot 2.4+',
         'Import: Commented RunWith (not needed in Spring Boot 2.4+)'),
        
        (r'import static org\.junit\.Assume\.assumeTrue;', 
         'import static org.junit.jupiter.api.Assumptions.assumeTrue;',
         'Import: org.junit.Assume.assumeTrue → org.junit.jupiter.api.Assumptions.assumeTrue'),
        
        (r'import static org\.junit\.Assert\.fail;', 
         'import static org.junit.jupiter.api.Assertions.fail;',
         'Import: org.junit.Assert.fail → org.junit.jupiter.api.Assertions.fail'),
    ]
    
    for pattern, replacement, description in replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"  - {description}")
    
    # 2. Annotation replacements
    annotation_replacements = [
        (r'@Before\b', '@BeforeEach', 'Annotation: @Before → @BeforeEach'),
        (r'@After\b', '@AfterEach', 'Annotation: @After → @AfterEach'),
        (r'@BeforeClass\b', '@BeforeAll', 'Annotation: @BeforeClass → @BeforeAll'),
        (r'@AfterClass\b', '@AfterAll', 'Annotation: @AfterClass → @AfterAll'),
        (r'@Ignore\b', '@Disabled', 'Annotation: @Ignore → @Disabled'),
    ]
    
    for pattern, replacement, description in annotation_replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"  - {description}")
    
    # 3. Remove @RunWith(SpringRunner.class) - not needed in Spring Boot 2.4+
    if re.search(r'@RunWith\(SpringRunner\.class\)', content):
        content = re.sub(r'@RunWith\(SpringRunner\.class\)\s*\n', '', content)
        changes.append('  - Removed: @RunWith(SpringRunner.class) [not needed in Spring Boot 2.4+]')
    
    # 4. Convert @RunWith(MockitoJUnitRunner.class) to @ExtendWith(MockitoExtension.class)
    if re.search(r'@RunWith\(MockitoJUnitRunner\.class\)', content):
        content = re.sub(r'@RunWith\(MockitoJUnitRunner\.class\)', 
                        '@ExtendWith(MockitoExtension.class)', content)
        
        # Add imports if not present
        if 'import org.junit.jupiter.api.extension.ExtendWith;' not in content:
            content = re.sub(r'(package .*?;)', 
                           r'\1\nimport org.junit.jupiter.api.extension.ExtendWith;\nimport org.mockito.junit.jupiter.MockitoExtension;',
                           content)
        
        changes.append('  - Annotation: @RunWith(MockitoJUnitRunner.class) → @ExtendWith(MockitoExtension.class)')
    
    # 5. Comment out @Rule ExpectedException
    if re.search(r'@Rule\s+public\s+final\s+ExpectedException', content):
        content = re.sub(r'(@Rule\s+public\s+final\s+ExpectedException[^;]+;)', 
                        r'// \1 // TODO: Migrate to assertThrows() in JUnit 5',
                        content)
        changes.append('  - Commented @Rule ExpectedException [TODO: Manual migration to assertThrows() needed]')
    
    # 6. Add missing @Test import if @Test annotation is used but import is missing
    if re.search(r'@Test\b', content) and not re.search(r'import org\.junit\.jupiter\.api\.Test;', content):
        # Add the import after the package statement
        content = re.sub(r'(package .*?;)', r'\1\nimport org.junit.jupiter.api.Test;', content, count=1)
        changes.append('  - Added missing import: org.junit.jupiter.api.Test')
    
    # 7. Remove @Test(expected=...) - not supported in JUnit 5
    if re.search(r'@Test\(expected\s*=', content):
        content = re.sub(r'@Test\(expected\s*=\s*([^)]+)\)', 
                        r'@Test // TODO: Convert to assertThrows(\1.class, () -> { ... });',
                        content)
        changes.append('  - Removed @Test(expected=...) [TODO: Convert to assertThrows()]')
    
    # 8. Fully comment out ExpectedException field declaration
    if re.search(r'public\s+final\s+ExpectedException\s+\w+', content):
        content = re.sub(r'(\s+)(//\s*@Rule\s+)?public\s+final\s+ExpectedException\s+(\w+)[^;]*;[^\n]*', 
                        r'\1// ExpectedException \3 - removed (JUnit 5: use assertThrows instead)',
                        content)
        changes.append('  - Removed ExpectedException field [use assertThrows in JUnit 5]')
    
    # 9. Comment out standalone @Rule annotations for OutputCaptureRule (Spring Boot specific)
    if re.search(r'@Rule\s*\n\s*public\s+final\s+OutputCaptureRule', content):
        content = re.sub(r'@Rule(\s*\n\s*public\s+final\s+OutputCaptureRule)', 
                        r'// @Rule - OutputCaptureRule not needed in Spring Boot 2.4+ (use OutputCaptureExtension)\1',
                        content)
        changes.append('  - Commented @Rule for OutputCaptureRule')
    
    # Write changes if any
    if content != original_content:
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
        return len(changes), changes
    
    return 0, []

def main():
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: python migrate-junit4-to-junit5.py <project-path> [--dry-run]")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    dry_run = '--dry-run' in sys.argv
    
    if not project_path.exists():
        print(f"ERROR: Project path not found: {project_path}")
        sys.exit(1)
    
    print_header()
    print(f"Project path: {project_path.absolute()}")
    if dry_run:
        print("Mode: DRY RUN (no files will be modified)")
    print()
    
    # Find test files
    java_files = find_java_test_files(project_path)
    
    # Migrate each file
    files_modified = 0
    total_changes = 0
    
    for java_file in java_files:
        num_changes, change_list = migrate_file(java_file, dry_run)
        
        if num_changes > 0:
            files_modified += 1
            total_changes += num_changes
            
            relative_path = java_file.relative_to(project_path)
            print(f"✓ {relative_path}")
            for change in change_list:
                print(change)
            print()
    
    # Summary
    print("=" * 60)
    print("Migration Summary:")
    print(f"  Files processed: {len(java_files)}")
    print(f"  Files modified:  {files_modified}")
    print(f"  Total changes:   {total_changes}")
    
    if dry_run:
        print()
        print("DRY RUN - No files were actually modified")
        print("Run without --dry-run to apply changes")
    else:
        print()
        print("✓ Migration complete!")
        print()
        print("Next steps:")
        print("  1. Review changes: git diff")
        print("  2. Compile tests: mvn clean test-compile")
        print("  3. Run tests: mvn test")

if __name__ == '__main__':
    main()
