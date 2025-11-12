# OLAF Project Onboarding Python Scripts

This directory contains Python automation scripts for the OLAF project onboarding workflow, providing automated analysis capabilities for comprehensive project assessment.

## Overview

These scripts replace and enhance the original PowerShell automation, providing cross-platform compatibility and advanced analysis features for the 28-task project onboarding workflow.

## Scripts

### Core Analysis Scripts

1. **`workspace_content_analyzer.py`** - Task #1
   - Analyzes workspace structure and identifies repositories
   - Maps dependencies between repositories
   - Generates comprehensive workspace reports

2. **`language_distribution_analyzer.py`** - Task #3  
   - Analyzes programming language distribution
   - Detects project types and technology stacks
   - Provides polyglot architecture assessment

3. **`repo_size_metrics_calculator.py`** - Task #4
   - Calculates repository size metrics
   - Analyzes file categories and code density
   - Provides storage and optimization recommendations

4. **`complexity_analyzer.py`** - Task #19
   - Performs cyclomatic complexity analysis
   - Supports multiple programming languages
   - Identifies high-complexity functions for refactoring

5. **`hotspot_analyzer.py`** - Task #18
   - Combines Git history with complexity metrics
   - Identifies code hotspots requiring attention
   - Provides risk assessment and prioritization

## Installation

### Prerequisites
- Python 3.8 or higher
- Git (for hotspot analysis)

### Setup
```bash
# Navigate to the scripts directory
cd olaf-core/tools/commons/project-onboarding

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Individual Script Usage

```bash
# Workspace Content Analysis
python workspace_content_analyzer.py /path/to/workspace -o workspace-analysis.md

# Language Distribution Analysis  
python language_distribution_analyzer.py /path/to/project -o language-distribution.md

# Repository Size Metrics
python repo_size_metrics_calculator.py /path/to/repo -o size-metrics.md

# Complexity Analysis
python complexity_analyzer.py /path/to/repo -o complexity-analysis.md -t 10

# Hotspot Analysis
python hotspot_analyzer.py /path/to/repo -o hotspots.md -m 12
```

### Command Line Options

All scripts support:
- `-o, --output`: Specify output file path
- `-v, --verbose`: Enable verbose logging
- `-h, --help`: Show help information

Additional options:
- **Complexity Analyzer**: `-t, --threshold`: Set complexity threshold (default: 10)
- **Hotspot Analyzer**: `-m, --months`: Months of Git history to analyze (default: 12)

## Integration with OLAF Prompts

These scripts are designed to work seamlessly with the OLAF project onboarding prompts located in:
`olaf-core/prompts/onboard/prompts/`

Each prompt references the corresponding Python script for automated analysis execution.

## Output Formats

All scripts generate comprehensive Markdown reports with:
- Executive summaries
- Detailed analysis tables
- Visualizations and metrics
- Actionable recommendations
- Risk assessments

## Features

### Multi-Language Support
- **JavaScript/TypeScript**: Node.js, React, Angular, Vue
- **Python**: Django, Flask, FastAPI, standard libraries
- **Java**: Maven, Gradle, Spring ecosystem
- **C#**: .NET Framework, .NET Core, ASP.NET
- **Go**: Standard library and modules
- **Rust**: Cargo ecosystem
- **C/C++**: CMake, Make build systems
- **PHP**: Composer, Laravel, Symfony
- **Ruby**: Bundler, Rails

### Advanced Analysis Capabilities
- **Dependency Mapping**: Cross-repository dependency analysis
- **Complexity Metrics**: Function-level cyclomatic complexity
- **Git Integration**: Change frequency and hotspot identification
- **Size Optimization**: Storage recommendations and file categorization
- **Technology Detection**: Automatic project type and stack identification

### Error Handling
- Graceful handling of binary files
- Unicode encoding support
- Missing file tolerance
- Git repository validation

## Architecture

### Design Principles
- **Modular Design**: Each script handles a specific analysis domain
- **Cross-Platform**: Pure Python implementation for Windows/Linux/macOS
- **Extensible**: Easy to add new language support and analysis types
- **Performance**: Efficient file processing with progress tracking
- **Logging**: Comprehensive logging for debugging and monitoring

### Code Structure
```
project-onboarding/
├── workspace_content_analyzer.py     # Workspace structure analysis
├── language_distribution_analyzer.py # Language and technology detection
├── repo_size_metrics_calculator.py   # Size and storage metrics
├── complexity_analyzer.py            # Cyclomatic complexity analysis
├── hotspot_analyzer.py              # Git history + complexity hotspots
├── requirements.txt                  # Python dependencies
└── README.md                        # This documentation
```

## Troubleshooting

### Common Issues

**Git not found**: Ensure Git is installed and in PATH for hotspot analysis
```bash
git --version  # Should return version information
```

**Permission errors**: Ensure read access to all analyzed directories
```bash
chmod -R r-- /path/to/analyze  # Linux/macOS
```

**Large repository timeouts**: Use verbose mode to monitor progress
```bash
python script.py /path/to/repo -v
```

**Missing dependencies**: Install all requirements
```bash
pip install -r requirements.txt
```

### Performance Optimization

For large repositories:
- Use SSD storage for better I/O performance
- Increase available RAM for large file processing
- Consider excluding unnecessary directories via .gitignore patterns

## Contributing

When extending these scripts:
1. Follow existing code structure and naming conventions
2. Add comprehensive error handling
3. Include progress logging for long operations
4. Update this README with new features
5. Test with various project types and sizes

## Version History

- **v1.0.0**: Initial release with 5 core analysis scripts
- Based on PowerShell scripts from OLAF toolkit
- Enhanced with cross-platform Python implementation
- Integrated with OLAF project onboarding workflow

---
*Part of the OLAF (Organizational Learning and Analysis Framework) toolkit*
