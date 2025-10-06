# Benchmark Evaluation Results

This directory contains evaluation results for persona benchmarks compared against established baselines.

## File Structure

- `ALL-EVALUATION-RESULTS.md` - Master file with cumulative results and statistics
- `evaluation-results-{YYYYMMDD-HHmm}.md` - Individual evaluation session results

## Usage

### Running Evaluations

Use the evaluation prompt to assess benchmark branches:

```bash
# The evaluation prompt will:
# 1. List available benchmark-otter-* branches
# 2. Allow selection of branches to evaluate  
# 3. Automatically match persona to baseline
# 4. Generate detailed scores and rationale
# 5. Save results to this directory
```

### Evaluation Process

1. **Branch Detection**: Automatically finds `benchmark-otter-*` branches
2. **Persona Matching**: Extracts persona from branch name
3. **Baseline Comparison**: Compares against judge baseline
4. **Scoring**: Uses persona-specific criteria and weights
5. **Results Storage**: Saves individual and cumulative results

### Scoring System

- **100+ points**: Same solution or better than baseline
- **50 points**: Less good but workable solution  
- **-30 points**: Solution too far off target
- **0 points**: No solution provided

### Quality Ratings

- **10.0**: Exceptional - Significantly exceeds baseline
- **9.0-9.9**: Outstanding - Exceeds baseline in most areas
- **8.0-8.9**: Excellent - Meets or slightly exceeds baseline
- **7.0-7.9**: Good - Approaches baseline with minor gaps
- **6.0-6.9**: Satisfactory - Adequate but below baseline
- **<6.0**: Needs Improvement - Significant gaps

## Persona-Specific Evaluation

### Coder Persona
- **Special Features**: Evaluates bug fixes, feature restoration, unit test recreation
- **Judge Information**: Has details on injected bugs and deleted functionality
- **Weights**: Bug fixes (30%), Features (25%), Tests (20%), Quality (15%), Approach (10%)

### Business Analyst Persona  
- **Focus**: Requirements analysis, user stories, process documentation
- **Weights**: Requirements (30%), User Stories (25%), Process (25%), Stakeholders (20%)

### Architect/Designer Persona
- **Focus**: Architecture diagrams, system analysis, design decisions
- **Weights**: Diagrams (30%), Analysis (25%), Decisions (25%), Documentation (20%)

### Technical Writer Persona
- **Focus**: Documentation completeness, technical accuracy, user experience
- **Weights**: Completeness (30%), Accuracy (25%), UX (25%), Structure (20%)

### Tester Persona
- **Focus**: Test coverage, quality, edge cases, documentation
- **Weights**: Coverage (30%), Quality (25%), Edge Cases (25%), Documentation (20%)

### Project Manager Persona
- **Focus**: Analysis depth, strategic planning, risk assessment
- **Weights**: Analysis (30%), Planning (25%), Risk (25%), Resources (20%)

## Results Analysis

The `ALL-EVALUATION-RESULTS.md` file provides:

- **Summary Table**: All evaluations with key metrics
- **Statistics by Persona**: Average scores and evaluation counts
- **Statistics by Agent/Model**: Performance comparison across AI systems
- **Quality Distribution**: Breakdown of quality ratings
- **Latest Evaluations**: Recent assessment summaries

This enables tracking of:
- AI agent performance over time
- Persona-specific strengths and weaknesses  
- Model comparison and benchmarking
- Quality trends and improvements
