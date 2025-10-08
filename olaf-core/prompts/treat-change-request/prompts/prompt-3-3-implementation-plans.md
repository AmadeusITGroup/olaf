<<<<<<< HEAD
---
name: convert-implementation-plans
description: Convert the Implementation Plans Creation prompt to standardized template, preserving adaptive task breakdown and TDD integration
tags: [prompt, conversion, implementation, planning]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **design_path**: path - Final `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - Approved `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **test_plan_path**: path - `TEST_PLAN_<PROJECT-ID>.md` (OPTIONAL)

## User Interaction Protocol
- Propose-Act for conversion and plan generation

## Process

### 1. Validation Phase
- Confirm inputs exist
- Load templates: `../templates/template-implementation-plans.md`, `../templates/template-implementation-task.md`

### 2. Execution Phase
**Core Logic**:
- Analyze design to identify natural implementation boundaries (data, service, API, integrations)
- Generate adaptive tasks matching actual complexity, not forced phases
- For each task, define acceptance criteria and integrate unit testing via TDD/BDD
- Organize tasks by implementation order based on dependencies

### 3. Validation Phase
- Ensure all design components are covered
- Ensure tasks are actionable, testable, and ordered with dependencies

## Output Format
- Primary deliverable: Implementation plan per `../templates/template-implementation-plans.md`

## User Communication
- Progress: task generation and ordering complete
- Completion: plan ready for development

## Domain-Specific Rules
- Rule 1: Integrate unit testing in every task (TDD/BDD)
- Rule 2: Do not artificially split or combine tasks

## Success Criteria
- [ ] All components covered by tasks
- [ ] Clear acceptance criteria and TDD prompts per task
- [ ] Realistic dependency-based ordering

## Error Handling
- **Gaps in Components**: Flag and request clarifications
- **Over-fragmented Tasks**: Consolidate and document rationale

⚠️ **Critical Requirements**
- MANDATORY: TDD integrated per task
- NEVER force structure contrary to actual complexity
=======
﻿# Prompt 3.3: Implementation Plans Creation

## Overview

Transform the approved technical design into a flexible, executable implementation plan with clear tasks, dependencies, and acceptance criteria. This prompt creates an adaptive implementation roadmap that guides development while allowing for project-specific complexity.

**CRITICAL**: This Implementation Plan includes **unit testing strategy and prompts**. Unit tests are created during development using TDD/BDD practices as part of each implementation task. The Test Plan (Step 3.1) covers integration, system, performance, and security testing only.

## Prerequisites

**Required Input Documents:**
- `DESIGN_<PROJECT-ID>.md` (finalized design from Phase 2)
- `SPECIFICATION_<PROJECT-ID>.md` (approved specification from Phase 1)
- `TEST_PLAN_<PROJECT-ID>.md` (from Step 3.1)

**Required Analysis:**
- Existing codebase patterns and conventions
- Technical complexity and risk areas
- Component dependencies and integration points
- Team capabilities and project constraints

## Prompt Instructions

### Context Setup
You are a Senior Technical Lead creating an adaptive implementation plan. Your goal is to break down the technical design into **natural, logical tasks** based on actual complexity—not forced into artificial structures. Generate tasks that match how developers actually work.

### Input Processing
1. **Analyze Specification Requirements**
   - Extract all functional requirements (FR-xxx) that need implementation
   - Identify business rules and validation logic requirements
   - Understand user workflows and acceptance criteria
   - Note non-functional requirements (performance, security, scalability)
   - Assess business criticality and implementation priorities

2. **Analyze Design Architecture**
   - Review all architectural components and their relationships
   - Understand technical implementation approach for each requirement
   - Identify integration points and external dependencies
   - Assess implementation complexity and technical risk areas
   - Map design components to specification requirements

3. **Cross-Reference and Plan Implementation**
   - Ensure every specification requirement has corresponding design component
   - Break down components into implementable tasks based on business value
   - Identify shared dependencies and common technical foundations
   - Determine optimal sequencing balancing business priorities and technical dependencies
   - Consider testing requirements and quality gates from both documents

### Task Generation Approach (ADAPTIVE)

**Use Template**: `../templates/template-implementation-plans.md`

**⚠️ CRITICAL PRINCIPLE**: Generate tasks based on **ACTUAL COMPLEXITY**, not forced templates.

#### Step 1: Analyze Design Components

Review the design document and **identify natural implementation boundaries:**

**For Data Layer Components:**
- Analyze entity relationships and complexity
- Simple entities (CRUD only) → Single task
- Complex entities (validation, relationships, lifecycle) → Multiple tasks per concern
- Example: "User entity with authentication" is different from "Audit log entity"

**For Service Layer Components:**
- Identify business logic complexity
- Simple services (thin wrappers) → Combine related services in one task
- Complex services (state machines, workflows) → Break by functional responsibility
- Example: "Email notification service" vs "Order processing workflow with 6 states"

**For API Layer Components:**
- Group related endpoints logically
- RESTful CRUD for one resource → Single task
- Complex API with multiple resources and relationships → Task per resource group
- Example: "/users CRUD" vs "/orders with nested items, payments, and fulfillment"

**For Integration Components:**
- One task per external system integration
- Include error handling, resilience, and testing in the same task
- Don't artificially split retry logic or circuit breakers into separate tasks

#### Step 2: Generate Task Structure (FLEXIBLE FORMAT)

Use **../templates/template-implementation-task.md** for each task structure.

#### Step 3: Organize Tasks by Implementation Order

**Group tasks logically** (not by forced "phases") - see **../templates/template-implementation-task-examples.md** for complete examples of task grouping and complexity-based task breakdowns.

**Quick Reference Guidelines:**

**Foundation First:**
- Core data models
- Base services and repositories
- Shared utilities and configurations

**Build Up from Dependencies:**
- Services that depend on data layer
- APIs that depend on services
- Integrations that depend on core functionality

**Complete with Quality:**
- Integration testing
- Performance optimization (if needed)
- Documentation and deployment automation

### Complexity-Based Task Examples

**Refer to**: `../templates/template-implementation-task-examples.md` for detailed examples including:
- Simple component task patterns
- Complex component multi-task patterns
- Task grouping by implementation order
- Complexity assessment guidelines for different layer components

### Quality Validation

Before finalizing, ensure:
- [ ] All design components are covered by implementation tasks
- [ ] Task breakdown matches actual complexity (no artificial splitting or combining)
- [ ] Dependencies are realistic and create clear implementation order
- [ ] Each task has specific, testable acceptance criteria
- [ ] **Unit testing is integrated into each task (TDD/BDD - write tests first, then implementation)**
- [ ] Tasks reference existing codebase patterns for consistency

### Quality Validation

Before finalizing, ensure:
- [ ] All design components are covered by implementation tasks
- [ ] Task breakdown is appropriately detailed (clear, actionable, testable)
- [ ] Dependencies are clearly identified and realistic
- [ ] Each task has specific implementation guidance
- [ ] **Unit testing requirements are integrated into each implementation task (TDD approach)**
- [ ] Progress tracking mechanisms are defined
- [ ] Risk mitigation strategies are included

### Expected Output

**Document Name**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md` (single comprehensive document)

**Format**: Professional markdown following template structure

**Content Structure**:
- Executive Summary (project scope, key risks)
- Task List organized by implementation order (not forced phases)
- **Unit Testing Guidance for each task (TDD/BDD - tests written first)**
- Dependency Graph or visual representation
- Quality gates and validation checkpoints
- Reference to existing codebase patterns

**Length**: As concise as possible while providing clear, actionable tasks
- Task count varies based on actual project complexity
- Each task should be independently implementable and testable
- Each task should include unit testing prompts following TDD principles

### Usage Notes

- This prompt should be used after design and test plan approval
- The resulting implementation plans guide daily development activities
- Tasks can be imported into project management tools (Jira, Azure DevOps)
- Plans should be reviewed with development team before execution begins

## Integration with Development Process

**Handoff to Development Team:**
- Task breakdown provides clear daily work assignments
- Implementation prompts offer specific technical guidance
- Dependencies enable proper sprint planning and resource allocation

**Project Management:**
- Task estimates enable accurate timeline planning
- Dependencies support critical path analysis
- Progress tracking enables milestone monitoring

**Quality Assurance:**
- **Unit testing prompts integrate TDD/BDD practices into each development task**
- Acceptance criteria provide objective completion validation
- Risk mitigation ensures proactive issue management

## Implementation Guidance Framework

**Task Implementation Prompts Should Include:**
- Specific code patterns and architectural guidance
- Technology-specific best practices and examples
- Integration patterns and error handling approaches
- Testing strategies and validation techniques

**Progress Tracking Mechanisms:**
- Daily task completion status
- Milestone achievement metrics
- Quality gate passage rates
- Risk issue identification and resolution

**Team Collaboration Support:**
- Code review requirements and standards
- Knowledge sharing and documentation practices
- Cross-team communication protocols
- Escalation procedures for blockers
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
