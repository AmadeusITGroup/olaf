<<<<<<< HEAD
---
name: convert-test-plan
description: Convert the Test Plan Creation prompt to standardized template, preserving QA strategy, coverage, and validation gates
tags: [prompt, conversion, test-plan, QA]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **design_path**: path - Finalized `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - Approved `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and plan generation

## Process

### 1. Validation Phase
- Confirm both inputs exist
- Load template `../templates/template-test-plan.md`

### 2. Execution Phase
**Core Logic**:
- Analyze specification and design to derive strategy, integration/system/E2E coverage
- Define QA strategy, environments, tools, automation, and quality gates
- Generate integration/system/performance/security plans with tickable tasks

### 3. Validation Phase
- Verify coverage of FRs and NFRs
- Verify environments and data requirements are feasible

## Output Format
- Primary deliverable: Test plan per `../templates/template-test-plan.md`

## User Communication
- Progress: analysis complete, sections generated
- Completion: plan ready for review

## Domain-Specific Rules
- Rule 1: Focus on integration/system tests (unit tests in implementation step)
- Rule 2: Provide measurable acceptance criteria

## Success Criteria
- [ ] Coverage for FRs/NFRs
- [ ] Integration/system/performance/security sections complete
- [ ] Template structure followed

## Error Handling
- **Missing Inputs**: Request paths
- **Gaps in Coverage**: Flag and request clarifications

⚠️ **Critical Requirements**
- MANDATORY: Evidence-backed coverage mapping
- NEVER include unit test implementation guidance here
=======
﻿# Prompt 3.1: Test Plan Creation

## Overview

Transform the approved technical design into a comprehensive testing strategy that ensures quality delivery. This prompt creates detailed test plans covering all aspects of the system.

## Prerequisites

**Required Input Documents:**
- `DESIGN_<PROJECT-ID>.md` (finalized design from Phase 2)
- `SPECIFICATION_<PROJECT-ID>.md` (approved specification from Phase 1)

**Required Information:**
- Project timeline and testing phases
- Available testing environments
- QA team capabilities and tools
- Performance and security requirements

## Prompt Instructions

### Context Setup
You are a Senior QA Architect creating a comprehensive test plan for a software project. You have access to the complete specification and technical design documents. Your goal is to create a test strategy that ensures all requirements are validated through systematic testing.

### Input Processing
1. **Analyze the Specification Document**
   - Extract all functional requirements (FR-xxx) to ensure test coverage
   - Extract all non-functional requirements (NFR-xxx) for performance/security testing
   - Identify user stories and acceptance criteria for E2E testing
   - Determine business rules and validation requirements
   - Note critical user workflows and business processes

2. **Analyze the Design Document**
   - Review architectural components and their interactions for integration testing
   - Identify testable interfaces and API contracts
   - Understand data flows and technical implementation details
   - Note security mechanisms and performance considerations
   - Map design components to specification requirements

3. **Cross-Reference Both Documents**
   - Ensure every functional requirement has corresponding design components to test
   - Validate that design components support all specification requirements
   - Identify gaps where requirements lack implementation details
   - Determine test priorities based on business criticality and technical risk

### Output Generation

**Use Template**: `../templates/template-test-plan.md`

Create a comprehensive test plan document following the template structure with these specific requirements:

#### Test Strategy Section
- Define overall testing approach (shift-left, risk-based, etc.)
- Specify testing phases and entry/exit criteria
- Identify testing tools and automation strategy
- Define test data management approach

#### QA Strategy Section
**Define the overall QA approach focusing on integration, system, and acceptance testing:**

- [ ] **Task: Define QA testing strategy**
  - [ ] Subtask: Establish testing phases and entry/exit criteria
  - [ ] Subtask: Define test data management and environment requirements
  - [ ] Subtask: Set up test automation framework for integration/E2E tests
  - [ ] Subtask: Define defect management and reporting processes
  - [ ] Subtask: Establish quality gates and acceptance criteria

**Note**: Unit testing is handled as part of the Implementation Plan (Prompt 3.3) where developers create unit tests during development using TDD/BDD practices.

#### Integration Test Plan Section  
**Analyze both specification and design documents for integration requirements and implementation:**

**For each integration point identified in the design document, create a task like:**
- [ ] **Task: Test integration between [System A] and [System B from Design]**
  - [ ] Subtask: Test data exchange requirements (from specification) via design implementation
  - [ ] Subtask: Test business workflows (from specification) that span multiple systems
  - [ ] Subtask: Test error scenarios and business rule violations (from specification + design)
  - [ ] Subtask: Validate data transformation meets business requirements (specification requirements)
  - [ ] Subtask: Test non-functional requirements (performance, security from specification)

**Adaptation Guidelines:**
- **External API integrations**: Include timeout, rate limiting, and error response testing
- **Database integrations**: Focus on transaction integrity and connection handling
- **Internal service integrations**: Emphasize contract testing and service discovery
- **Simple integrations**: May need only 2-3 subtasks focusing on main scenarios

#### System Test Plan Section
**Analyze the specification for user stories and create E2E workflow tasks:**

**For each user story/workflow identified in the specification, create a task like:**
- [ ] **Task: Test [User Story Name from Specification] end-to-end workflow**
  - [ ] Subtask: Set up test data (adapt based on workflow data requirements)
  - [ ] Subtask: Execute main user journey (based on specification acceptance criteria)
  - [ ] Subtask: Test alternative paths (based on specification alternate flows)
  - [ ] Subtask: Verify business rules (based on specification business logic)
  - [ ] Subtask: Test UI/UX requirements (if applicable to this workflow)

**Adaptation Guidelines:**
- **Critical user workflows** (registration, payment, core business): Extensive testing with multiple paths
- **Standard workflows** (CRUD operations, reports): Focus on main path and error handling
- **Admin workflows** (configuration, maintenance): Basic functionality and permissions testing
- **Complex workflows**: Break into multiple tasks if workflow spans multiple sessions

#### Performance Test Plan Section
**Create specific, tickable performance tasks:**
- [ ] **Task: Execute load testing for [Feature/API]**
  - [ ] Subtask: Define performance benchmarks (response time, throughput)
  - [ ] Subtask: Create load testing scripts and scenarios
  - [ ] Subtask: Execute baseline performance tests
  - [ ] Subtask: Execute peak load tests (2x normal load)
  - [ ] Subtask: Analyze results and identify bottlenecks

#### Security Test Plan Section
**Create specific, tickable security tasks:**
- [ ] **Task: Security testing for [Component/API]**
  - [ ] Subtask: Test authentication mechanisms
  - [ ] Subtask: Test authorization and access controls
  - [ ] Subtask: Test input validation (SQL injection, XSS)
  - [ ] Subtask: Test data encryption in transit and at rest
  - [ ] Subtask: Run vulnerability scanning tools

#### Test Environment Setup Section
**Create specific, tickable environment tasks:**
- [ ] **Task: Set up test environment infrastructure**
  - [ ] Subtask: Provision test databases with sample data
  - [ ] Subtask: Configure test application servers
  - [ ] Subtask: Set up monitoring and logging
  - [ ] Subtask: Create test data refresh procedures
  - [ ] Subtask: Document environment access and credentials

### Quality Validation

Before finalizing, ensure:
- [ ] All functional requirements have corresponding integration/system test cases
- [ ] Non-functional requirements are adequately covered by performance/security tests
- [ ] Integration test scenarios cover all system boundaries
- [ ] E2E test workflows cover all major user journeys
- [ ] Test data requirements are realistic and achievable
- [ ] Environment requirements are clearly defined
- [ ] Acceptance criteria are measurable and objective

### Expected Output

**Document Name**: `TEST_PLAN_<PROJECT-ID>.md`
**Format**: Professional markdown following template structure
**Content**: Comprehensive testing strategy ready for QA team execution
**Length**: As concise as possible while covering all test scenarios thoroughly

### Usage Notes

- This prompt should be used after design approval but before implementation begins
- The resulting test plan guides all testing activities during development
- Test cases can be imported into test management tools
- The plan should be reviewed with QA team and stakeholders before finalization

## Integration with Development Process

**Handoff to Development Team:**
- Integration test scenarios inform service contract design
- Performance requirements influence architecture decisions
- E2E test workflows guide feature development priorities

**QA Team Execution:**
- Test cases provide detailed execution guidance
- Environment requirements inform setup procedures
- Acceptance criteria enable objective quality assessment

**Stakeholder Communication:**
- Test strategy demonstrates comprehensive quality approach
- Test coverage metrics provide confidence in delivery
- Risk assessment helps prioritize testing efforts
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
