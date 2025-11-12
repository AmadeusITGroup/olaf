#!/usr/bin/env python3
"""
Workspace Content Analyzer for Project Onboarding

Analyzes workspace structure, identifies repositories, maps dependencies,
and generates comprehensive workspace analysis reports.

Based on PowerShell script patterns from OLAF toolkit.
"""

import os
import json
import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WorkspaceContentAnalyzer:
    """Analyzes workspace content structure and repository relationships."""
    
    def __init__(self, workspace_path: str, output_file: str = None):
        self.workspace_path = Path(workspace_path).resolve()
        self.output_file = output_file or self.workspace_path / "workspace-analysis.md"
        self.repositories = []
        self.dependency_map = {}
        self.workspace_structure = {}
        
    def find_git_repositories(self) -> List[Dict]:
        """Find all Git repositories in the workspace."""
        repositories = []
        
        for root, dirs, files in os.walk(self.workspace_path):
            if '.git' in dirs:
                repo_path = Path(root)
                relative_path = repo_path.relative_to(self.workspace_path)
                
                repo_info = {
                    'name': repo_path.name,
                    'path': str(relative_path),
                    'absolute_path': str(repo_path),
                    'type': self._detect_repository_type(repo_path),
                    'size': self._calculate_directory_size(repo_path),
                    'last_modified': self._get_last_modified(repo_path)
                }
                
                repositories.append(repo_info)
                # Don't traverse into .git directories
                dirs.remove('.git')
                
        return repositories
    
    def _detect_repository_type(self, repo_path: Path) -> str:
        """Detect the type of repository based on configuration files."""
        config_files = {
            'package.json': 'Node.js',
            'pom.xml': 'Java/Maven',
            'build.gradle': 'Java/Gradle',
            'Cargo.toml': 'Rust',
            'go.mod': 'Go',
            'requirements.txt': 'Python',
            'pyproject.toml': 'Python',
            '*.sln': '.NET',
            'composer.json': 'PHP',
            'Gemfile': 'Ruby'
        }
        
        for config_file, repo_type in config_files.items():
            if config_file.startswith('*'):
                # Handle wildcard patterns
                pattern = config_file[1:]  # Remove *
                if list(repo_path.glob(f"*{pattern}")):
                    return repo_type
            elif (repo_path / config_file).exists():
                return repo_type
                
        return 'Unknown'
    
    def _calculate_directory_size(self, directory: Path) -> int:
        """Calculate total size of directory in bytes."""
        total_size = 0
        try:
            for root, dirs, files in os.walk(directory):
                # Skip .git directories for size calculation
                if '.git' in dirs:
                    dirs.remove('.git')
                for file in files:
                    file_path = Path(root) / file
                    try:
                        total_size += file_path.stat().st_size
                    except (OSError, IOError):
                        continue
        except (OSError, IOError):
            pass
        return total_size
    
    def _get_last_modified(self, directory: Path) -> str:
        """Get last modification time of directory."""
        try:
            return datetime.fromtimestamp(directory.stat().st_mtime).isoformat()
        except (OSError, IOError):
            return datetime.now().isoformat()
    
    def analyze_dependencies(self) -> Dict:
        """Analyze dependencies between repositories."""
        dependency_map = {}
        
        for repo in self.repositories:
            repo_path = Path(repo['absolute_path'])
            dependencies = []
            
            # Analyze different dependency files
            if repo['type'] == 'Node.js':
                dependencies.extend(self._analyze_nodejs_dependencies(repo_path))
            elif repo['type'] in ['Java/Maven', 'Java/Gradle']:
                dependencies.extend(self._analyze_java_dependencies(repo_path))
            elif repo['type'] == 'Python':
                dependencies.extend(self._analyze_python_dependencies(repo_path))
            elif repo['type'] == 'Go':
                dependencies.extend(self._analyze_go_dependencies(repo_path))
            elif repo['type'] == 'Rust':
                dependencies.extend(self._analyze_rust_dependencies(repo_path))
                
            dependency_map[repo['name']] = dependencies
            
        return dependency_map
    
    def _analyze_nodejs_dependencies(self, repo_path: Path) -> List[str]:
        """Analyze Node.js package.json dependencies."""
        dependencies = []
        package_json = repo_path / 'package.json'
        
        if package_json.exists():
            try:
                with open(package_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                    if dep_type in data:
                        dependencies.extend(data[dep_type].keys())
                        
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Could not parse {package_json}: {e}")
                
        return dependencies
    
    def _analyze_java_dependencies(self, repo_path: Path) -> List[str]:
        """Analyze Java Maven/Gradle dependencies."""
        dependencies = []
        
        # Maven pom.xml
        pom_xml = repo_path / 'pom.xml'
        if pom_xml.exists():
            try:
                with open(pom_xml, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Simple regex-based extraction (could be improved with XML parsing)
                    import re
                    artifact_pattern = r'<artifactId>([^<]+)</artifactId>'
                    dependencies.extend(re.findall(artifact_pattern, content))
            except IOError as e:
                logger.warning(f"Could not read {pom_xml}: {e}")
        
        # Gradle build files
        for gradle_file in ['build.gradle', 'build.gradle.kts']:
            gradle_path = repo_path / gradle_file
            if gradle_path.exists():
                try:
                    with open(gradle_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Simple pattern matching for dependencies
                        import re
                        dep_pattern = r'["\']([^"\']+:[^"\']+):[^"\']+["\']'
                        matches = re.findall(dep_pattern, content)
                        dependencies.extend([match.split(':')[1] for match in matches])
                except IOError as e:
                    logger.warning(f"Could not read {gradle_path}: {e}")
                    
        return dependencies
    
    def _analyze_python_dependencies(self, repo_path: Path) -> List[str]:
        """Analyze Python dependencies."""
        dependencies = []
        
        # requirements.txt
        req_file = repo_path / 'requirements.txt'
        if req_file.exists():
            try:
                with open(req_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            # Extract package name (before ==, >=, etc.)
                            import re
                            match = re.match(r'^([a-zA-Z0-9_-]+)', line)
                            if match:
                                dependencies.append(match.group(1))
            except IOError as e:
                logger.warning(f"Could not read {req_file}: {e}")
        
        # pyproject.toml
        pyproject_file = repo_path / 'pyproject.toml'
        if pyproject_file.exists():
            try:
                import tomli
                with open(pyproject_file, 'rb') as f:
                    data = tomli.load(f)
                    if 'project' in data and 'dependencies' in data['project']:
                        for dep in data['project']['dependencies']:
                            import re
                            match = re.match(r'^([a-zA-Z0-9_-]+)', dep)
                            if match:
                                dependencies.append(match.group(1))
            except (ImportError, IOError) as e:
                logger.warning(f"Could not parse {pyproject_file}: {e}")
                
        return dependencies
    
    def _analyze_go_dependencies(self, repo_path: Path) -> List[str]:
        """Analyze Go module dependencies."""
        dependencies = []
        go_mod = repo_path / 'go.mod'
        
        if go_mod.exists():
            try:
                with open(go_mod, 'r', encoding='utf-8') as f:
                    in_require_block = False
                    for line in f:
                        line = line.strip()
                        if line.startswith('require ('):
                            in_require_block = True
                            continue
                        elif line == ')' and in_require_block:
                            in_require_block = False
                            continue
                        elif in_require_block or line.startswith('require '):
                            # Extract module name
                            parts = line.split()
                            if len(parts) >= 2:
                                module = parts[0] if in_require_block else parts[1]
                                dependencies.append(module)
            except IOError as e:
                logger.warning(f"Could not read {go_mod}: {e}")
                
        return dependencies
    
    def _analyze_rust_dependencies(self, repo_path: Path) -> List[str]:
        """Analyze Rust Cargo dependencies."""
        dependencies = []
        cargo_toml = repo_path / 'Cargo.toml'
        
        if cargo_toml.exists():
            try:
                import tomli
                with open(cargo_toml, 'rb') as f:
                    data = tomli.load(f)
                    for dep_section in ['dependencies', 'dev-dependencies', 'build-dependencies']:
                        if dep_section in data:
                            dependencies.extend(data[dep_section].keys())
            except (ImportError, IOError) as e:
                logger.warning(f"Could not parse {cargo_toml}: {e}")
                
        return dependencies
    
    def analyze_workspace_structure(self) -> Dict:
        """Analyze overall workspace structure."""
        structure = {
            'total_repositories': len(self.repositories),
            'repository_types': {},
            'total_size_bytes': 0,
            'directory_structure': {},
            'common_patterns': []
        }
        
        # Count repository types
        for repo in self.repositories:
            repo_type = repo['type']
            structure['repository_types'][repo_type] = structure['repository_types'].get(repo_type, 0) + 1
            structure['total_size_bytes'] += repo['size']
        
        # Analyze directory patterns
        common_dirs = set()
        for repo in self.repositories:
            repo_path = Path(repo['absolute_path'])
            for item in repo_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    common_dirs.add(item.name)
        
        # Find patterns that appear in multiple repositories
        dir_counts = {}
        for repo in self.repositories:
            repo_path = Path(repo['absolute_path'])
            for item in repo_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    dir_counts[item.name] = dir_counts.get(item.name, 0) + 1
        
        structure['common_patterns'] = [
            {'directory': dir_name, 'frequency': count}
            for dir_name, count in dir_counts.items()
            if count > 1
        ]
        
        return structure
    
    def generate_report(self) -> str:
        """Generate comprehensive workspace analysis report."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        
        report = f"""# Workspace Content Analysis Report

**Analysis Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Workspace Path**: {self.workspace_path}  
**Total Repositories**: {len(self.repositories)}

## Repository Overview

| Repository | Type | Path | Size (MB) | Last Modified |
|------------|------|------|-----------|---------------|
"""
        
        for repo in sorted(self.repositories, key=lambda x: x['name']):
            size_mb = round(repo['size'] / (1024 * 1024), 2)
            last_mod = repo['last_modified'][:10]  # Date only
            report += f"| {repo['name']} | {repo['type']} | {repo['path']} | {size_mb} | {last_mod} |\n"
        
        report += f"""
## Workspace Structure Analysis

- **Total Repositories**: {self.workspace_structure['total_repositories']}
- **Total Size**: {round(self.workspace_structure['total_size_bytes'] / (1024 * 1024), 2)} MB
- **Repository Types**: {', '.join([f"{k}: {v}" for k, v in self.workspace_structure['repository_types'].items()])}

## Common Directory Patterns

The following directories appear across multiple repositories:

| Directory | Frequency | Purpose |
|-----------|-----------|---------|
"""
        
        for pattern in sorted(self.workspace_structure['common_patterns'], key=lambda x: x['frequency'], reverse=True):
            purpose = self._get_directory_purpose(pattern['directory'])
            report += f"| {pattern['directory']} | {pattern['frequency']} | {purpose} |\n"
        
        report += """
## Dependency Analysis

### Repository Dependencies Summary

"""
        
        for repo_name, deps in self.dependency_map.items():
            if deps:
                report += f"**{repo_name}** ({len(deps)} dependencies):\n"
                # Show top 10 dependencies
                for dep in sorted(deps)[:10]:
                    report += f"- {dep}\n"
                if len(deps) > 10:
                    report += f"- ... and {len(deps) - 10} more\n"
                report += "\n"
        
        report += """
## Recommendations

Based on the workspace analysis:

1. **Repository Organization**: Consider grouping related repositories by purpose or technology stack
2. **Dependency Management**: Review shared dependencies for potential consolidation
3. **Documentation**: Ensure each repository has adequate README and documentation
4. **Build Automation**: Consider workspace-level build scripts for multi-repository operations

## Next Steps

1. Review individual repository configurations
2. Analyze technology stack compatibility
3. Identify opportunities for code sharing
4. Plan dependency updates and security reviews

---
*Generated by OLAF Workspace Content Analyzer*
"""
        
        return report
    
    def _get_directory_purpose(self, dir_name: str) -> str:
        """Get the likely purpose of a directory based on common conventions."""
        purposes = {
            'src': 'Source code',
            'lib': 'Libraries',
            'bin': 'Binaries',
            'build': 'Build artifacts',
            'dist': 'Distribution files',
            'docs': 'Documentation',
            'test': 'Test files',
            'tests': 'Test files',
            'config': 'Configuration',
            'scripts': 'Scripts',
            'tools': 'Tools and utilities',
            'assets': 'Static assets',
            'public': 'Public files',
            'private': 'Private files',
            'vendor': 'Third-party code',
            'node_modules': 'Node.js dependencies',
            'target': 'Rust/Java build output',
            'pkg': 'Package files'
        }
        return purposes.get(dir_name.lower(), 'Unknown')
    
    def run_analysis(self) -> None:
        """Run complete workspace analysis."""
        logger.info(f"Starting workspace analysis of: {self.workspace_path}")
        
        # Find repositories
        logger.info("Finding Git repositories...")
        self.repositories = self.find_git_repositories()
        logger.info(f"Found {len(self.repositories)} repositories")
        
        # Analyze dependencies
        logger.info("Analyzing dependencies...")
        self.dependency_map = self.analyze_dependencies()
        
        # Analyze structure
        logger.info("Analyzing workspace structure...")
        self.workspace_structure = self.analyze_workspace_structure()
        
        # Generate report
        logger.info("Generating report...")
        report = self.generate_report()
        
        # Save report
        output_path = Path(self.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Analysis complete. Report saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Analyze workspace content structure')
    parser.add_argument('workspace_path', help='Path to workspace directory')
    parser.add_argument('-o', '--output', help='Output file path', default=None)
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not os.path.exists(args.workspace_path):
        logger.error(f"Workspace path does not exist: {args.workspace_path}")
        sys.exit(1)
    
    analyzer = WorkspaceContentAnalyzer(args.workspace_path, args.output)
    analyzer.run_analysis()


if __name__ == '__main__':
    main()
