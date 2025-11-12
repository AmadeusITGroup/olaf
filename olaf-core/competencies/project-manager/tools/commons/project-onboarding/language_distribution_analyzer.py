#!/usr/bin/env python3
"""
Language Distribution Analyzer for Project Onboarding

Analyzes programming language distribution across repositories,
detecting project types, build systems, and technology stacks.

Based on PowerShell detect-project-type.ps1 from OLAF toolkit.
"""

import os
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LanguageDistributionAnalyzer:
    """Analyzes programming language distribution and project characteristics."""
    
    # Language mappings with their extensions
    LANGUAGE_MAP = {
        "JavaScript/TypeScript": [".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs"],
        "Python": [".py", ".pyx", ".pyi"],
        "Java": [".java"],
        "C#": [".cs"],
        "C/C++": [".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx"],
        "Go": [".go"],
        "Rust": [".rs"],
        "PHP": [".php", ".phtml"],
        "Ruby": [".rb", ".rake"],
        "HTML/CSS": [".html", ".htm", ".css", ".scss", ".sass", ".less"],
        "Shell": [".sh", ".bash", ".zsh", ".fish", ".ps1", ".bat", ".cmd"],
        "SQL": [".sql"],
        "XML/Config": [".xml", ".yaml", ".yml", ".json", ".toml", ".ini", ".conf"],
        "Markdown": [".md", ".markdown", ".rst"],
        "Other": []  # Catch-all for unrecognized extensions
    }
    
    # Configuration file patterns for project type detection
    CONFIG_PATTERNS = {
        "Node.js": ["package.json", "yarn.lock", "package-lock.json", "pnpm-lock.yaml"],
        "Java/Maven": ["pom.xml"],
        "Java/Gradle": ["build.gradle", "build.gradle.kts", "gradlew", "gradlew.bat"],
        "Python": ["requirements.txt", "pyproject.toml", "setup.py", "Pipfile", "poetry.lock"],
        "Rust": ["Cargo.toml", "Cargo.lock"],
        "Go": ["go.mod", "go.sum"],
        ".NET": ["*.sln", "*.csproj", "*.vbproj", "*.fsproj"],
        "PHP": ["composer.json", "composer.lock"],
        "Ruby": ["Gemfile", "Gemfile.lock"],
        "C/C++": ["CMakeLists.txt", "Makefile", "configure.ac"],
        "Docker": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
        "Kubernetes": ["*.yaml", "*.yml"]  # In k8s context
    }
    
    def __init__(self, project_path: str, output_file: str = None):
        self.project_path = Path(project_path).resolve()
        self.output_file = output_file or self.project_path / "language-distribution.md"
        self.exclude_patterns = [
            'node_modules', 'dist', 'bin', 'obj', 'build', 'target', 
            'vendor', 'packages', '.git', '__pycache__', '.pytest_cache',
            '.next', '.turbo', '.cache', 'coverage', 'out', 'tmp'
        ]
        
    def should_exclude_path(self, path: Path) -> bool:
        """Check if path should be excluded from analysis."""
        path_str = str(path)
        return any(pattern in path_str for pattern in self.exclude_patterns)
    
    def get_all_files(self) -> List[Path]:
        """Get all files in the project, excluding specified patterns."""
        all_files = []
        
        for root, dirs, files in os.walk(self.project_path):
            # Remove excluded directories from traversal
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in self.exclude_patterns)]
            
            for file in files:
                file_path = Path(root) / file
                if not self.should_exclude_path(file_path):
                    all_files.append(file_path)
        
        return all_files
    
    def analyze_language_distribution(self) -> Dict:
        """Analyze language distribution across all files."""
        all_files = self.get_all_files()
        language_stats = {}
        file_examples = {}
        total_loc = 0
        
        # Initialize language counters
        for language in self.LANGUAGE_MAP.keys():
            language_stats[language] = {
                'file_count': 0,
                'total_lines': 0,
                'extensions': set()
            }
            file_examples[language] = []
        
        logger.info(f"Analyzing {len(all_files)} files...")
        
        for file_path in all_files:
            extension = file_path.suffix.lower()
            
            # Find matching language
            matched_language = None
            for language, extensions in self.LANGUAGE_MAP.items():
                if extension in extensions:
                    matched_language = language
                    break
            
            if not matched_language and extension:
                matched_language = "Other"
            
            if matched_language:
                # Count lines of code
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        language_stats[matched_language]['total_lines'] += lines
                        total_loc += lines
                except (IOError, UnicodeDecodeError):
                    lines = 0
                
                # Update statistics
                language_stats[matched_language]['file_count'] += 1
                language_stats[matched_language]['extensions'].add(extension)
                
                # Store file examples (limit to 5 per language)
                if len(file_examples[matched_language]) < 5:
                    relative_path = file_path.relative_to(self.project_path)
                    file_examples[matched_language].append(str(relative_path))
        
        # Convert sets to lists for JSON serialization
        for language in language_stats:
            language_stats[language]['extensions'] = list(language_stats[language]['extensions'])
        
        return {
            'language_stats': language_stats,
            'file_examples': file_examples,
            'total_files': len(all_files),
            'total_loc': total_loc
        }
    
    def detect_project_types(self) -> Dict:
        """Detect project types based on configuration files."""
        detected_types = {}
        config_files_found = []
        
        # Search for configuration files
        for project_type, patterns in self.CONFIG_PATTERNS.items():
            found_configs = []
            
            for pattern in patterns:
                if pattern.startswith('*'):
                    # Handle wildcard patterns
                    glob_pattern = pattern
                    matches = list(self.project_path.glob(glob_pattern))
                    found_configs.extend([m.name for m in matches])
                else:
                    # Handle exact file names
                    config_path = self.project_path / pattern
                    if config_path.exists():
                        found_configs.append(pattern)
            
            if found_configs:
                detected_types[project_type] = found_configs
                config_files_found.extend(found_configs)
        
        return {
            'detected_types': detected_types,
            'config_files': config_files_found
        }
    
    def analyze_project_structure(self) -> Dict:
        """Analyze overall project structure."""
        structure_info = {
            'is_monorepo': False,
            'directory_structure': {},
            'common_patterns': []
        }
        
        # Check for monorepo indicators
        monorepo_indicators = ['packages', 'apps', 'libs', 'services', 'modules']
        found_indicators = []
        
        for indicator in monorepo_indicators:
            indicator_path = self.project_path / indicator
            if indicator_path.exists() and indicator_path.is_dir():
                subdirs = [d for d in indicator_path.iterdir() if d.is_dir()]
                if len(subdirs) > 1:  # Multiple subdirectories suggest monorepo
                    found_indicators.append({
                        'directory': indicator,
                        'subdirectory_count': len(subdirs)
                    })
                    structure_info['is_monorepo'] = True
        
        structure_info['monorepo_indicators'] = found_indicators
        
        # Analyze top-level directory structure
        top_level_dirs = []
        for item in self.project_path.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in self.exclude_patterns:
                file_count = len(list(item.rglob('*')))
                top_level_dirs.append({
                    'name': item.name,
                    'file_count': file_count
                })
        
        structure_info['top_level_directories'] = sorted(top_level_dirs, key=lambda x: x['file_count'], reverse=True)
        
        return structure_info
    
    def extract_technology_details(self, detected_types: Dict) -> Dict:
        """Extract detailed technology information from configuration files."""
        tech_details = {}
        
        # Node.js details
        if 'Node.js' in detected_types:
            package_json = self.project_path / 'package.json'
            if package_json.exists():
                try:
                    with open(package_json, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        tech_details['Node.js'] = {
                            'name': data.get('name', 'Unknown'),
                            'version': data.get('version', 'Unknown'),
                            'node_version': data.get('engines', {}).get('node', 'Not specified'),
                            'dependencies_count': len(data.get('dependencies', {})),
                            'dev_dependencies_count': len(data.get('devDependencies', {})),
                            'scripts': list(data.get('scripts', {}).keys())
                        }
                except (json.JSONDecodeError, IOError) as e:
                    logger.warning(f"Could not parse package.json: {e}")
        
        # Python details
        if 'Python' in detected_types:
            python_info = {}
            
            # Check pyproject.toml
            pyproject = self.project_path / 'pyproject.toml'
            if pyproject.exists():
                try:
                    import tomli
                    with open(pyproject, 'rb') as f:
                        data = tomli.load(f)
                        if 'project' in data:
                            python_info.update({
                                'name': data['project'].get('name', 'Unknown'),
                                'version': data['project'].get('version', 'Unknown'),
                                'python_version': data['project'].get('requires-python', 'Not specified'),
                                'dependencies_count': len(data['project'].get('dependencies', []))
                            })
                except (ImportError, IOError) as e:
                    logger.warning(f"Could not parse pyproject.toml: {e}")
            
            # Check requirements.txt
            requirements = self.project_path / 'requirements.txt'
            if requirements.exists():
                try:
                    with open(requirements, 'r', encoding='utf-8') as f:
                        deps = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                        python_info['requirements_count'] = len(deps)
                except IOError as e:
                    logger.warning(f"Could not read requirements.txt: {e}")
            
            if python_info:
                tech_details['Python'] = python_info
        
        # Java details
        if 'Java/Maven' in detected_types:
            pom_xml = self.project_path / 'pom.xml'
            if pom_xml.exists():
                try:
                    with open(pom_xml, 'r', encoding='utf-8') as f:
                        content = f.read()
                        java_info = {}
                        
                        # Extract Java version (simplified)
                        import re
                        java_version_match = re.search(r'<maven\.compiler\.source>(\d+)</maven\.compiler\.source>', content)
                        if java_version_match:
                            java_info['java_version'] = java_version_match.group(1)
                        
                        # Count dependencies (simplified)
                        dependency_count = len(re.findall(r'<dependency>', content))
                        java_info['dependencies_count'] = dependency_count
                        
                        tech_details['Java/Maven'] = java_info
                except IOError as e:
                    logger.warning(f"Could not read pom.xml: {e}")
        
        return tech_details
    
    def generate_report(self, analysis_data: Dict) -> str:
        """Generate comprehensive language distribution report."""
        language_stats = analysis_data['language_stats']
        file_examples = analysis_data['file_examples']
        total_files = analysis_data['total_files']
        total_loc = analysis_data['total_loc']
        
        project_types = analysis_data['project_types']
        structure = analysis_data['structure']
        tech_details = analysis_data['tech_details']
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Filter out languages with no files
        active_languages = {k: v for k, v in language_stats.items() if v['file_count'] > 0}
        
        report = f"""# Language Distribution Analysis Report

**Analysis Date**: {timestamp}  
**Project Path**: {self.project_path}  
**Total Files**: {total_files:,}  
**Total Lines of Code**: {total_loc:,}

## Language Distribution Overview

| Language | Files | % of Files | Lines of Code | % of LOC | Avg Lines/File |
|----------|-------|------------|---------------|----------|----------------|
"""
        
        # Sort by file count (descending)
        sorted_languages = sorted(active_languages.items(), key=lambda x: x[1]['file_count'], reverse=True)
        
        for language, stats in sorted_languages:
            file_count = stats['file_count']
            lines = stats['total_lines']
            file_percent = round((file_count / total_files) * 100, 1) if total_files > 0 else 0
            loc_percent = round((lines / total_loc) * 100, 1) if total_loc > 0 else 0
            avg_lines = round(lines / file_count, 1) if file_count > 0 else 0
            
            report += f"| {language} | {file_count:,} | {file_percent}% | {lines:,} | {loc_percent}% | {avg_lines} |\n"
        
        report += """
## Project Type Detection

Based on configuration files and project structure:

"""
        
        if project_types['detected_types']:
            for project_type, configs in project_types['detected_types'].items():
                report += f"**{project_type}**: {', '.join(configs)}\n"
        else:
            report += "No specific project types detected based on configuration files.\n"
        
        report += """
## Technology Stack Details

"""
        
        if tech_details:
            for tech, details in tech_details.items():
                report += f"### {tech}\n\n"
                for key, value in details.items():
                    if isinstance(value, list):
                        value = ', '.join(value) if value else 'None'
                    report += f"- **{key.replace('_', ' ').title()}**: {value}\n"
                report += "\n"
        else:
            report += "No detailed technology information extracted.\n"
        
        report += """
## Project Structure Analysis

"""
        
        if structure['is_monorepo']:
            report += "**Structure Type**: Monorepo detected\n\n"
            report += "**Monorepo Indicators**:\n"
            for indicator in structure['monorepo_indicators']:
                report += f"- `{indicator['directory']}/` with {indicator['subdirectory_count']} subdirectories\n"
        else:
            report += "**Structure Type**: Single project\n"
        
        report += "\n**Top-Level Directories**:\n\n"
        report += "| Directory | File Count |\n|-----------|------------|\n"
        
        for dir_info in structure['top_level_directories'][:10]:  # Top 10
            report += f"| {dir_info['name']} | {dir_info['file_count']:,} |\n"
        
        report += """
## Language-Specific File Examples

"""
        
        for language, examples in file_examples.items():
            if examples and language in active_languages:
                report += f"### {language}\n"
                for example in examples:
                    report += f"- `{example}`\n"
                report += "\n"
        
        # Primary language determination
        primary_language = sorted_languages[0][0] if sorted_languages else "Unknown"
        secondary_languages = [lang for lang, _ in sorted_languages[1:4]]  # Top 3 secondary
        
        report += f"""
## Summary and Recommendations

### Primary Technology Stack
- **Primary Language**: {primary_language}
- **Secondary Languages**: {', '.join(secondary_languages) if secondary_languages else 'None'}
- **Project Type**: {'Monorepo' if structure['is_monorepo'] else 'Single Project'}

### Polyglot Architecture Assessment
"""
        
        if len(active_languages) > 3:
            report += f"""
This project uses **{len(active_languages)} programming languages**, indicating a polyglot architecture:

**Benefits**:
- Flexibility to use best tool for each task
- Potential for microservices architecture
- Team specialization opportunities

**Challenges**:
- Increased complexity in build and deployment
- Need for diverse skill sets
- Potential integration challenges
- Multiple toolchains to maintain

**Recommendations**:
1. Establish clear boundaries between language domains
2. Implement consistent logging and monitoring across languages
3. Consider containerization for deployment consistency
4. Document inter-service communication patterns
"""
        else:
            report += """
This project has a **focused technology stack** with few languages:

**Benefits**:
- Simplified toolchain and build processes
- Easier team onboarding and knowledge sharing
- Consistent coding standards and practices
- Reduced operational complexity

**Recommendations**:
1. Maintain consistency in coding standards
2. Leverage language-specific best practices
3. Consider gradual adoption of complementary technologies
"""
        
        report += """
### Next Steps

1. **Technology Audit**: Review each technology's role and necessity
2. **Dependency Analysis**: Examine dependencies for security and maintenance
3. **Build System**: Ensure efficient build processes for all languages
4. **Testing Strategy**: Implement comprehensive testing across all languages
5. **Documentation**: Document technology choices and architectural decisions

---
*Generated by OLAF Language Distribution Analyzer*
"""
        
        return report
    
    def run_analysis(self) -> None:
        """Run complete language distribution analysis."""
        logger.info(f"Starting language distribution analysis of: {self.project_path}")
        
        # Analyze language distribution
        logger.info("Analyzing language distribution...")
        language_analysis = self.analyze_language_distribution()
        
        # Detect project types
        logger.info("Detecting project types...")
        project_types = self.detect_project_types()
        
        # Analyze project structure
        logger.info("Analyzing project structure...")
        structure = self.analyze_project_structure()
        
        # Extract technology details
        logger.info("Extracting technology details...")
        tech_details = self.extract_technology_details(project_types['detected_types'])
        
        # Combine all analysis data
        analysis_data = {
            **language_analysis,
            'project_types': project_types,
            'structure': structure,
            'tech_details': tech_details
        }
        
        # Generate report
        logger.info("Generating report...")
        report = self.generate_report(analysis_data)
        
        # Save report
        output_path = Path(self.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Analysis complete. Report saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Analyze programming language distribution')
    parser.add_argument('project_path', help='Path to project directory')
    parser.add_argument('-o', '--output', help='Output file path', default=None)
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not os.path.exists(args.project_path):
        logger.error(f"Project path does not exist: {args.project_path}")
        sys.exit(1)
    
    analyzer = LanguageDistributionAnalyzer(args.project_path, args.output)
    analyzer.run_analysis()


if __name__ == '__main__':
    main()
