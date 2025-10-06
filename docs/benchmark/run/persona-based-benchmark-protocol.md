# Persona-Based Benchmark Protocol

**Version**: 1.0  
**Date**: October 6, 2025  
**Target Codebase**: Otter

## Overview

This protocol enables comprehensive benchmarking of AI agents and models across different software development personas. Each persona represents a specific role in software development with tailored tasks that test role-specific capabilities.

## Supported Personas

### 1. Coder
**Focus**: Implementation, debugging, and technical development
**Key Skills**: Code analysis, bug fixing, feature implementation, testing

### 2. Business Analyst  
**Focus**: Requirements analysis, functional specification, process documentation
**Key Skills**: Business process modeling, requirements gathering, documentation

### 3. Architect/Designer
**Focus**: System design, architecture documentation, technical planning
**Key Skills**: System architecture, design patterns, technical documentation

### 4. Technical Writer
**Focus**: Documentation creation, user guides, API documentation
**Key Skills**: Technical writing, user experience, documentation standards

### 5. Tester
**Focus**: Test planning, test case creation, quality assurance
**Key Skills**: Test design, workflow analysis, quality validation

### 6. Project Manager
**Focus**: Project analysis, risk assessment, improvement planning
**Key Skills**: Code analysis, performance assessment, project planning

## Benchmark Structure

### Directory Structure

**Git Branch Strategy** (Replaces expensive folder copying):

- **Branch Name**: `benchmark-otter-[agent]-[model]-[persona]-YYYYMMDD-HHmm`
- **Working Directory**: `otter/` (existing repository)
- **Results Directory**: `olaf-data/benchmarks/otter-[YYYYMMDD-HHmm]-[persona]-[agent]-[model]/`

```text
olaf-data/benchmarks/otter-[YYYYMMDD-HHmm]-[persona]-[agent]-[model]/
├── session-info.json            # Benchmark configuration + branch reference
├── persona-tasks.json           # Task definitions and status
├── interventions.json           # User intervention log
├── PERSONA-BENCHMARK-REPORT.md  # Results and analysis
├── README.md                    # Summary and instructions
└── git-branch-info.json         # Branch metadata and commit references
```

**Git Workflow**:

1. Create benchmark branch from `main` or specified base branch
2. Switch to benchmark branch for all work
3. Commit deliverables and modifications to branch
4. Store branch reference and final commit hash in results
5. Branch can be deleted after benchmark analysis (optional)

### Task Execution Model
- Each persona has 3-5 specific tasks
- Tasks are executed sequentially
- All tasks must be completed for valid benchmark
- Autonomous execution with minimal user intervention
- Quality assessment per deliverable

## Success Metrics

### Completion Rate
- Percentage of tasks completed successfully
- Quality score per deliverable (1-10 scale)
- Time efficiency vs. expected duration

### Autonomy Score
- Number of user interventions required
- Type and severity of interventions
- Self-correction capabilities

### Quality Assessment
- Technical accuracy of deliverables
- Completeness and thoroughness
- Professional presentation quality
- Adherence to best practices

## Usage Instructions

1. **Initialize**: Run persona benchmark evaluation prompt
2. **Configure**: Specify agent, model, and persona type
3. **Execute**: Agent performs all persona-specific tasks
4. **Review**: Analyze results and quality metrics
5. **Compare**: Use for agent/model comparison studies
