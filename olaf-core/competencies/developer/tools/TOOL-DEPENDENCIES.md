# Developer Competency - Tool Dependencies

## Required Tools by Competency

### augment-code-unit-test

- **Tool**: `hotspot_analyzer.py`
- **Type**: Python Script
- **Purpose**: Analyze code complexity hotspots by combining Git history with complexity metrics for iterative test augmentation
- **Location**: `tools/hotspot_analyzer.py` (in this directory)
- **Dependencies**: Python 3.7+, git

### review-code-accessibility

- **Tool**: `pa11y` (npm package)
- **Tool**: `axe-core` (npm package)
- **Type**: Node.js accessibility testing tools
- **Purpose**: Automated accessibility testing for WCAG compliance
- **Installation**: `npm install pa11y axe-core --save-dev`

## Installation Instructions

### For augment-code-unit-test

The `hotspot_analyzer.py` tool is available in the framework tools directory and requires Python 3.7+:

```bash
python olaf-core/tools/commons/project-onboarding/hotspot_analyzer.py --repo-path <repo_path> --output <output_file>
```

### For review-code-accessibility

```bash
# Install accessibility tools in project
npm install pa11y axe-core --save-dev
```

## Status

- [x] hotspot_analyzer.py - Available in `tools/` directory
- [ ] pa11y - External npm package (optional, used only if accessibility testing desired)
- [ ] axe-core - External npm package (optional, used only if accessibility testing desired)

---

**Note**: The Python tool has been created and is available in the framework tools directory. The npm packages are optional dependencies for `review-code-accessibility` competency.
