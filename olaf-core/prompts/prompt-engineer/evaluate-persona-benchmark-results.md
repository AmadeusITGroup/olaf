# Evaluate Persona Benchmark Results

## Prompt Overview

**Purpose**: Evaluate and score persona benchmark results against established baselines  
**Target User**: Benchmark evaluators, researchers, QA teams  
**Execution Protocol**: Propose-Confirm-Act  

---

## Framework Validation

You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:

- <olaf-general-role-and-behavior> - Expert domain approach with rigorous evaluation
- <olaf-interaction-protocols> - Use Propose-Confirm-Act protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval

You MUST get current time in YYYYMMDD-HHmm format using terminal commands:

- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

## Input Parameters

You MUST request these parameters if not provided by the user:

- **evaluator_name**: string - Name of the person conducting the evaluation (MANDATORY, no default)
- **evaluation_session_id**: string - Unique identifier for this evaluation session (OPTIONAL, auto-generate if not provided)

## User Interaction Protocol

You MUST follow this interaction protocol strictly:

1. **Propose-Confirm-Act** for benchmark selection and evaluation setup
2. **Act** protocol during detailed evaluation and scoring
3. **Propose-Act** protocol for final scoring and reporting

## Process

### Step 1: Initialize Evaluation Session

1. **Get Current Time**: Use terminal command to get timestamp
2. **List Available Benchmark Branches**: 
   ```bash
   git branch -a | grep "benchmark-otter-" | sort
   ```
3. **Display Available Baselines**: List judge baselines available for comparison
4. **Request User Selection**: Ask which benchmark branches to evaluate

### Step 2: Branch Analysis and Baseline Matching

For each selected benchmark branch:

1. **Parse Branch Name**: Extract persona type from branch name pattern
   - `benchmark-otter-windsurf-cascade-sonnet-4-coder-YYYYMMDD-HHmm` → **coder**
   - `benchmark-otter-windsurf-cascade-sonnet-4-business-analyst-YYYYMMDD-HHmm` → **business_analyst**
   - `benchmark-otter-windsurf-cascade-sonnet-4-architect-designer-YYYYMMDD-HHmm` → **architect_designer**
   - `benchmark-otter-windsurf-cascade-sonnet-4-technical-writer-YYYYMMDD-HHmm` → **technical_writer**
   - `benchmark-otter-windsurf-cascade-sonnet-4-tester-YYYYMMDD-HHmm` → **tester**
   - `benchmark-otter-windsurf-cascade-sonnet-4-project-manager-YYYYMMDD-HHmm` → **project_manager**

2. **Match to Baseline**: Automatically select corresponding baseline from judge folder:
   - **coder** → `docs/benchmark/judge/coder-base/`
   - **business_analyst** → `docs/benchmark/judge/business-analyst-base/`
   - **architect_designer** → `docs/benchmark/judge/architect-designer-base/`
   - **technical_writer** → `docs/benchmark/judge/technical-writer-base/`
   - **tester** → `docs/benchmark/judge/tester-base/`
   - **project_manager** → `docs/benchmark/judge/project-manager-base/`

### Step 3: Persona-Specific Evaluation

#### Coder Persona Evaluation

**Special Judge Information Available**:
- **Injected Bugs**: List of bugs intentionally added to the codebase
- **Deleted Features**: Features that were removed and need to be restored
- **Deleted Unit Tests**: Tests that were removed and need to be recreated

**Evaluation Criteria**:
1. **Bug Fixes**: Compare solutions against known injected bugs
2. **Feature Restoration**: Assess if deleted features were properly restored
3. **Unit Test Coverage**: Evaluate if deleted tests were recreated and improved
4. **Code Quality**: Compare against baseline code quality standards
5. **Implementation Approach**: Assess technical approach and best practices

**Scoring Matrix**:
- **Same solution or better** = 100+ points
- **Solution that is less good but will work** = 50 points  
- **Solution that is too far off** = -30 points
- **No solution** = 0 points

#### Business Analyst Persona Evaluation

**Evaluation Criteria**:
1. **Requirements Analysis**: Compare depth and accuracy of requirements gathering
2. **User Story Quality**: Assess story completeness and acceptance criteria
3. **Process Documentation**: Evaluate workflow and process analysis
4. **Stakeholder Analysis**: Compare stakeholder identification and management

#### Architect/Designer Persona Evaluation

**Evaluation Criteria**:
1. **Architecture Diagrams**: Compare quality and completeness of architectural documentation
2. **Design Decisions**: Assess technical decision rationale and documentation
3. **System Analysis**: Evaluate depth of codebase and structure analysis
4. **Technical Documentation**: Compare documentation quality and comprehensiveness

#### Technical Writer Persona Evaluation

**Evaluation Criteria**:
1. **Documentation Completeness**: Compare coverage and depth of documentation
2. **User Experience**: Assess clarity and usability of written materials
3. **Technical Accuracy**: Evaluate correctness of technical information
4. **Structure and Organization**: Compare information architecture and flow

#### Tester Persona Evaluation

**Evaluation Criteria**:
1. **Test Coverage**: Compare breadth and depth of test scenarios
2. **Test Quality**: Assess test design and implementation quality
3. **Edge Case Identification**: Evaluate identification of edge cases and error scenarios
4. **Test Documentation**: Compare test documentation and reporting quality

#### Project Manager Persona Evaluation

**Evaluation Criteria**:
1. **Analysis Depth**: Compare thoroughness of complexity and performance analysis
2. **Strategic Planning**: Assess quality of recommendations and implementation plans
3. **Risk Assessment**: Evaluate risk identification and mitigation strategies
4. **Resource Planning**: Compare resource allocation and timeline estimates

### Step 4: Detailed Scoring Process

For each deliverable in the benchmark branch:

1. **Read Baseline**: Load corresponding baseline deliverable from judge folder
2. **Read Benchmark**: Load deliverable from benchmark branch
3. **Compare Content**: Perform detailed comparison using persona-specific criteria
4. **Assign Scores**: Use scoring matrix for each evaluation criterion
5. **Document Rationale**: Provide detailed explanation for each score

### Step 5: Generate Evaluation Report

Create comprehensive evaluation report with:

1. **Executive Summary**: Overall scores and key findings
2. **Detailed Scoring**: Per-deliverable scores with rationale
3. **Comparative Analysis**: Strengths and weaknesses vs baseline
4. **Recommendations**: Suggestions for improvement
5. **Quality Assessment**: Overall quality rating and benchmarking insights

## Scoring Framework

### Overall Quality Scale
- **10.0**: Exceptional - Significantly exceeds baseline quality
- **9.0-9.9**: Outstanding - Exceeds baseline in most areas
- **8.0-8.9**: Excellent - Meets or slightly exceeds baseline
- **7.0-7.9**: Good - Approaches baseline quality with minor gaps
- **6.0-6.9**: Satisfactory - Adequate but below baseline in several areas
- **5.0-5.9**: Needs Improvement - Significant gaps compared to baseline
- **<5.0**: Poor - Major deficiencies requiring substantial rework

### Persona-Specific Scoring Weights

#### Coder Persona Weights
- **Bug Fixes**: 30%
- **Feature Restoration**: 25%
- **Unit Test Quality**: 20%
- **Code Quality**: 15%
- **Implementation Approach**: 10%

#### Business Analyst Persona Weights
- **Requirements Analysis**: 30%
- **User Story Quality**: 25%
- **Process Documentation**: 25%
- **Stakeholder Analysis**: 20%

#### Architect/Designer Persona Weights
- **Architecture Diagrams**: 30%
- **System Analysis**: 25%
- **Design Decisions**: 25%
- **Technical Documentation**: 20%

#### Technical Writer Persona Weights
- **Documentation Completeness**: 30%
- **Technical Accuracy**: 25%
- **User Experience**: 25%
- **Structure and Organization**: 20%

#### Tester Persona Weights
- **Test Coverage**: 30%
- **Test Quality**: 25%
- **Edge Case Identification**: 25%
- **Test Documentation**: 20%

#### Project Manager Persona Weights
- **Analysis Depth**: 30%
- **Strategic Planning**: 25%
- **Risk Assessment**: 25%
- **Resource Planning**: 20%

## Output Format

### Evaluation Report Template

```markdown
# Benchmark Evaluation Report

**Evaluation Session**: {evaluation_session_id}
**Evaluator**: {evaluator_name}
**Timestamp**: {timestamp}
**Branches Evaluated**: {branch_count}

## Executive Summary

### Overall Scores
| Branch | Persona | Overall Score | Quality Rating | vs Baseline |
|--------|---------|---------------|----------------|-------------|
| {branch_name} | {persona} | {score}/10 | {rating} | {comparison} |

### Key Findings
- {finding_1}
- {finding_2}
- {finding_3}

## Detailed Evaluation

### {Branch_Name} - {Persona} Persona

#### Deliverable Scores
| Deliverable | Score | Weight | Weighted Score | Rationale |
|-------------|-------|--------|----------------|-----------|
| {deliverable_1} | {score} | {weight}% | {weighted} | {rationale} |

#### Strengths
- {strength_1}
- {strength_2}

#### Areas for Improvement
- {improvement_1}
- {improvement_2}

#### Comparison to Baseline
{detailed_comparison}

## Recommendations

### For Future Benchmarks
1. {recommendation_1}
2. {recommendation_2}

### For Benchmark Improvement
1. {improvement_1}
2. {improvement_2}

## Appendix

### Evaluation Methodology
{methodology_details}

### Scoring Rationale
{detailed_scoring_explanation}
```

## Results Storage and Accumulation

### Create Evaluation Results File

For each evaluated benchmark, create a results file in:
`docs/benchmark/results/evaluation-results-{YYYYMMDD-HHmm}.md`

### Results File Template

```markdown
# Benchmark Evaluation Results

**Evaluation ID**: evaluation-{YYYYMMDD-HHmm}
**Evaluator**: {evaluator_name}
**Date**: {YYYY-MM-DD}
**Time**: {HH:mm} CEDT

## Summary

| Branch | Persona | Score | Quality | Status |
|--------|---------|-------|---------|--------|
| {branch_name} | {persona} | {score}/10 | {quality_rating} | ✅/❌ |

## Detailed Results

### {branch_name}

**Persona**: {persona}
**Overall Score**: {score}/10
**Quality Rating**: {quality_rating}

#### Deliverable Scores
- **{deliverable_1}**: {score}/10 - {brief_rationale}
- **{deliverable_2}**: {score}/10 - {brief_rationale}
- **{deliverable_3}**: {score}/10 - {brief_rationale}

#### Key Strengths
- {strength_1}
- {strength_2}

#### Key Weaknesses  
- {weakness_1}
- {weakness_2}

#### Comparison to Baseline
**Better than baseline**: {areas_better}
**Same as baseline**: {areas_same}  
**Worse than baseline**: {areas_worse}

#### Recommendation
{concise_recommendation}

---
```

### Cumulative Results Tracking

Also update the master results file:
`docs/benchmark/results/ALL-EVALUATION-RESULTS.md`

```markdown
# All Benchmark Evaluation Results

**Last Updated**: {YYYY-MM-DD HH:mm} CEDT

## Results Summary

| Date | Branch | Persona | Agent | Model | Score | Quality | Evaluator |
|------|--------|---------|-------|-------|-------|---------|-----------|
| {date} | {branch} | {persona} | {agent} | {model} | {score} | {quality} | {evaluator} |

## Statistics

### By Persona
- **Coder**: Avg {avg_score} ({count} evaluations)
- **Business Analyst**: Avg {avg_score} ({count} evaluations)  
- **Architect/Designer**: Avg {avg_score} ({count} evaluations)
- **Technical Writer**: Avg {avg_score} ({count} evaluations)
- **Tester**: Avg {avg_score} ({count} evaluations)
- **Project Manager**: Avg {avg_score} ({count} evaluations)

### By Agent/Model
- **windsurf-cascade/sonnet-4**: Avg {avg_score} ({count} evaluations)
- **{other_combinations}**: Avg {avg_score} ({count} evaluations)

### Quality Distribution
- **Outstanding (9.0+)**: {count} ({percentage}%)
- **Excellent (8.0-8.9)**: {count} ({percentage}%)
- **Good (7.0-7.9)**: {count} ({percentage}%)
- **Satisfactory (6.0-6.9)**: {count} ({percentage}%)
- **Needs Improvement (<6.0)**: {count} ({percentage}%)

## Latest Evaluations

### {latest_date}
- {branch_name} ({persona}): {score}/10 - {brief_summary}

### {previous_date}  
- {branch_name} ({persona}): {score}/10 - {brief_summary}
```

## Execution Instructions

1. **Initialize**: Get timestamp and list available benchmark branches
2. **Select**: Allow user to choose which branches to evaluate
3. **Analyze**: For each branch, determine persona and match to baseline
4. **Evaluate**: Perform detailed comparison using persona-specific criteria
5. **Score**: Apply scoring framework with weighted criteria
6. **Report**: Generate comprehensive evaluation report
7. **Save Individual Results**: Create individual evaluation results file
8. **Update Master Results**: Add to cumulative results tracking file
9. **Commit Results**: Save all results files to repository

## Quality Assurance

- **Consistency**: Use standardized evaluation criteria across all evaluations
- **Objectivity**: Base scores on measurable criteria and documented rationale
- **Completeness**: Ensure all deliverables are evaluated thoroughly
- **Traceability**: Maintain clear audit trail of evaluation decisions
- **Reproducibility**: Document methodology to enable consistent re-evaluation

This evaluation framework ensures rigorous, consistent, and comprehensive assessment of persona benchmark results against established baselines.
