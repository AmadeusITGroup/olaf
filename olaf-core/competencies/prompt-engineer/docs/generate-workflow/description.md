# Generate Workflow

**Source**: olaf-core/competencies/prompt-engineer/prompts/generate-workflow.md

## Overview

Generate Workflow creates structured workflow documents from templates or specifications. It supports multiple workflow patterns (sequential, iterative, decision-based, orchestrator) and generates comprehensive workflow definitions with clear phases, decision points, error handling, and success criteria.

## Purpose

Complex tasks require well-defined workflows to ensure consistency and completeness. This competency solves the challenge of designing and documenting multi-step processes by providing structured templates and intelligent workflow generation. It ensures workflows are comprehensive, maintainable, and follow established patterns for different types of processes.

## Usage

**Command**: `generate workflow`

**Protocol**: Act

**When to Use**: Use this competency when designing new multi-step processes, when formalizing ad-hoc procedures into structured workflows, when creating orchestration patterns for complex tasks, or when standardizing team processes across projects.

## Parameters

### Required Inputs
- **workflow_type**: Type of workflow pattern ("sequential", "iterative", "decision", "orchestrator")
- **workflow_name**: Name for the workflow being created
- **workflow_purpose**: High-level description of what the workflow accomplishes

### Optional Inputs
- **workflow_phases**: Number of major phases (auto-determined if not specified)
- **decision_points**: Key decision points for decision-based workflows
- **iteration_criteria**: Conditions for iterative workflows
- **sub_workflows**: Child workflows for orchestrator patterns

### Context Requirements
- Access to workflow templates for selected pattern type
- Understanding of the process being formalized
- Write access to workflow output directory
- Knowledge of workflow participants and dependencies

## Output

**Deliverables**:
- Complete workflow document following selected template pattern
- Phase definitions with clear entry/exit criteria
- Decision points with branching logic (for decision workflows)
- Iteration conditions and termination criteria (for iterative workflows)
- Error handling and recovery procedures
- Success criteria and validation checkpoints

**Format**: Markdown file saved to `[findings_dir]/workflows/[workflow-name]-workflow-YYYYMMDD-HHmm.md`

## Examples

### Example 1: Sequential Workflow for Code Review

**Scenario**: Creating a standardized code review process

**Command**:
```
olaf generate workflow
```

**Input**:
- workflow_type: "sequential"
- workflow_name: "code-review-process"
- workflow_purpose: "Systematic code review ensuring quality, security, and maintainability"

**Result**: Generated 5-phase sequential workflow: (1) Initial Assessment, (2) Static Analysis, (3) Manual Review, (4) Security Scan, (5) Approval/Feedback. Each phase includes specific tasks, success criteria, and transition conditions.

### Example 2: Iterative Workflow for Prompt Refinement

**Scenario**: Formalizing the prompt improvement cycle

**Command**:
```
olaf generate workflow
```

**Input**:
- workflow_type: "iterative"
- workflow_name: "prompt-refinement-cycle"
- workflow_purpose: "Continuously improve prompt quality through testing and feedback"
- iteration_criteria: "Continue until compliance score >= 95% or max 5 iterations"

**Result**: Created iterative workflow with phases: (1) Test Prompt, (2) Analyze Results, (3) Identify Improvements, (4) Apply Changes, (5) Validate. Includes termination conditions, iteration tracking, and convergence criteria.

### Example 3: Decision-Based Workflow for Issue Triage

**Scenario**: Automating issue classification and routing

**Command**:
```
olaf generate workflow
```

**Input**:
- workflow_type: "decision"
- workflow_name: "issue-triage-workflow"
- workflow_purpose: "Classify and route issues to appropriate teams based on type and severity"
- decision_points: ["Issue Type", "Severity Level", "Component Affected"]

**Result**: Generated decision tree workflow with branching logic at each decision point, routing rules for different combinations, escalation paths for critical issues, and fallback procedures for ambiguous cases.

## Related Competencies

- **Generate Tutorial**: Create tutorials from generated workflows to document execution
- **Create Prompt**: Use workflows to structure complex prompt logic
- **Create Competency Package**: Include workflows as part of competency documentation
- **Check Prompt Compliance**: Validate that prompts follow workflow patterns correctly

## Tips & Best Practices

- Choose workflow type based on process characteristics: sequential for linear processes, iterative for refinement cycles, decision for branching logic, orchestrator for complex multi-workflow coordination
- Define clear success criteria for each phase to enable validation
- Include error handling and recovery procedures for each phase
- Document decision criteria explicitly for decision-based workflows
- Specify termination conditions clearly for iterative workflows
- Use orchestrator pattern when coordinating multiple independent workflows
- Test workflows with real scenarios before deploying
- Keep workflows focused - break complex processes into multiple coordinated workflows

## Limitations

- Cannot automatically determine optimal workflow type - requires human judgment
- Generated workflows need customization for specific domain requirements
- Decision logic must be explicitly specified - cannot infer complex business rules
- Orchestrator patterns require understanding of workflow dependencies
- Effectiveness depends on clarity of workflow purpose and requirements
- May need manual refinement for edge cases and exceptional scenarios
