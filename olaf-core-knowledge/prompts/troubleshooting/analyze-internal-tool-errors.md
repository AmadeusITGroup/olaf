---
name: analyze-internal-tool-errors
description: Analyze massive logs from internal company tools using structured error documentation to identify known issues and provide mapped solutions
tags: [troubleshooting, internal-tools, error-mapping, log-analysis, pattern-matching]
---

# Internal Tool Error Analysis

## Role
You are an expert troubleshooting analyst specializing in internal company tools. Your task is to process massive log files (100k+ lines) using structured error documentation to identify known error patterns and provide mapped solutions.

## Context
Internal company tools generate errors that LLMs cannot understand or recognize. However, structured documentation exists that maps error patterns to solutions. This workflow processes logs efficiently by:
1. Using structured error documentation as a knowledge base
2. Applying pattern matching to identify known errors
3. Providing mapped solutions for identified issues
4. Highlighting unknown errors for manual analysis

## Input Requirements

### Primary Inputs
- **Log File Path**: Path to the massive log file requiring analysis
- **Error Documentation Path**: Path to structured error documentation (MD format)
- **Tool Name**: Name of the internal tool generating the logs

### Optional Inputs
- **Time Range**: Specific time window to analyze (format: YYYY-MM-DD HH:MM to YYYY-MM-DD HH:MM)
- **Error Severity Filter**: Focus on specific severity levels (CRITICAL, ERROR, WARNING, INFO)
- **Output Directory**: Custom path for analysis results

## Expected Documentation Structure

The error documentation should follow this structure:

```markdown
# Internal Tool Error Reference

## Error ID: TOOL-001
**Description**: Database connection timeout during batch processing
**How to Recognize**: 
- Pattern: `Connection timeout.*batch.*database`
- Regex: `Connection timeout.*batch.*database|DB_TIMEOUT.*batch_id:\s*\d+`
- Keywords: ["connection timeout", "batch processing", "database"]
**Proposed Resolution**: 
1. Increase connection timeout in config.xml (connectionTimeout=300)
2. Check database server load during batch windows
3. Consider splitting large batches into smaller chunks

## Error ID: TOOL-002
**Description**: Memory allocation failure in data processing
**How to Recognize**:
- Pattern: `OutOfMemoryError.*data processing|Memory allocation failed.*processing`
- Regex: `OutOfMemoryError.*data\s+processing|Memory\s+allocation\s+failed.*processing`
- Keywords: ["OutOfMemoryError", "memory allocation", "data processing"]
**Proposed Resolution**:
1. Increase JVM heap size (-Xmx parameter)
2. Review data processing batch sizes
3. Check for memory leaks in processing logic
```

## Execution Steps

### Step 1: Validate Inputs and Setup
1. Verify log file exists and is readable
2. Validate error documentation format and structure
3. Create output directory for analysis results
4. Parse error documentation into structured format

### Step 2: Parse Error Documentation
1. Extract all error definitions from documentation
2. Compile regex patterns for each error type
3. Create error mapping dictionary with:
   - Error ID
   - Description
   - Recognition patterns (regex + keywords)
   - Proposed solutions
4. Validate all regex patterns are syntactically correct

### Step 3: Log Preprocessing and Analysis
1. Process log file in chunks to handle large sizes
2. Apply error pattern matching for each chunk:
   - Match regex patterns against log lines
   - Score matches based on pattern confidence
   - Extract context lines around matches
3. Aggregate results by error type and frequency
4. Identify unmatched error patterns for manual review

### Step 4: Generate Analysis Report
Create comprehensive analysis including:
- **Executive Summary**: Total errors found, coverage percentage, critical issues
- **Known Error Analysis**: For each identified error type:
  - Error ID and description
  - Frequency and time distribution
  - Sample log entries with context
  - Mapped resolution steps
- **Unknown Error Patterns**: Unmatched errors requiring investigation
- **Recommendations**: Prioritized action items based on error frequency and severity

### Step 5: Create Actionable Outputs
Generate multiple output formats:
- **Summary Report**: `internal-tool-error-analysis-YYYYMMDD-HHmm.md`
- **Detailed Findings**: `error-details-YYYYMMDD-HHmm.json`
- **Action Plan**: `error-resolution-plan-YYYYMMDD-HHmm.md`
- **Unknown Patterns**: `unmatched-errors-YYYYMMDD-HHmm.txt`

## Script Integration Requirements

### Python Script Specifications
The analysis should use a Python script with these capabilities:

```python
# Core functions needed:
def parse_error_documentation(doc_path):
    """Parse structured MD documentation into error mapping dictionary"""
    
def compile_error_patterns(error_mapping):
    """Compile regex patterns and prepare matching rules"""
    
def analyze_log_chunk(chunk, compiled_patterns):
    """Process log chunk against error patterns"""
    
def generate_analysis_report(results, output_path):
    """Create comprehensive analysis report"""
```

### Pattern Matching Strategy
1. **Primary Matching**: Use regex patterns from documentation
2. **Fallback Matching**: Keyword-based fuzzy matching
3. **Context Extraction**: Capture surrounding lines for better analysis
4. **Confidence Scoring**: Rate match quality (High/Medium/Low)

## Quality Gates
- Error documentation must be successfully parsed
- At least 70% of log entries should be processed
- All regex patterns must compile without errors
- Analysis report must include actionable recommendations
- Unknown error patterns must be clearly identified for follow-up

## Error Handling
- **Invalid Documentation Format**: Provide format correction guidance
- **Regex Compilation Errors**: Highlight problematic patterns with suggestions
- **Large Log Processing**: Implement chunking and progress reporting
- **Memory Issues**: Use streaming processing for massive files
- **No Pattern Matches**: Suggest documentation updates or pattern refinement

## Output Specifications

### Analysis Report Structure
```markdown
# Internal Tool Error Analysis Report
**Tool**: [Tool Name]
**Analysis Date**: [YYYY-MM-DD HH:MM CEDT]
**Log Period**: [Start] to [End]
**Total Log Lines**: [Count]

## Executive Summary
- **Total Errors Identified**: [Count]
- **Known Error Types**: [Count] 
- **Coverage Percentage**: [%]
- **Critical Issues**: [Count]

## Known Error Analysis
### Error ID: TOOL-XXX
- **Frequency**: [Count] occurrences
- **Time Distribution**: [Pattern]
- **Sample Entry**: [Log line with context]
- **Resolution Steps**: [Mapped solution]
- **Priority**: [High/Medium/Low]

## Unknown Error Patterns
[List of unmatched patterns requiring investigation]

## Recommendations
1. [Prioritized action items]
2. [Documentation updates needed]
3. [Pattern refinement suggestions]
```

## Integration with Existing Workflows
- Can be invoked from main troubleshooting orchestrator
- Outputs feed into guided analysis workflows
- Results can trigger expert contact lookup for unknown errors
- Findings can generate decision records for recurring issues

## Success Criteria
- Rapid identification of known error patterns in massive logs
- Clear mapping between errors and solutions
- Significant reduction in manual log analysis time
- Actionable recommendations for both immediate fixes and process improvements
- Comprehensive coverage of log content with minimal false positives
