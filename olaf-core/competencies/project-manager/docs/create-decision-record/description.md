# Create Decision Record

## Overview

Creates structured decision records following a standardized template to document important project, architectural, business, and technical decisions with full traceability and stakeholder tracking.

## Purpose

Project teams need to maintain a clear record of why decisions were made, what alternatives were considered, and who was involved. This competency solves the problem of lost institutional knowledge by creating formal decision records that capture context, rationale, and outcomes in a consistent format that can be referenced throughout the project lifecycle.

## Usage

**Command**: `create decision record`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency whenever a significant decision needs to be documented, including architectural choices, project direction changes, business strategy decisions, technical implementations, security policies, or any decision that will impact the project's future direction or stakeholders.

## Parameters

### Required Inputs
- **title**: Concise description of the decision being made
- **type**: Category of decision (Architecture, Project, Business, Functional, People, Technical, Security, or Other)
- **context**: Background information and problem statement that led to this decision
- **drivers**: Key factors, constraints, or requirements influencing the decision
- **options**: Alternative options that were considered, including pros and cons for each
- **decision_makers**: Individuals responsible for making the final decision
- **stakeholders**: Parties affected by or interested in this decision

### Optional Inputs
- **status**: Current status of the decision (Proposed, Accepted, Replaced, Superseded) - defaults to "Proposed"
- **decision**: The selected option if already determined (can be left blank for proposed decisions)

### Context Requirements
- Access to decision records directory (`[id:decision_records_dir]`)
- Access to decision records register (`[id:decision-records-register]`)
- Access to changelog register for tracking the creation
- Decision record template available at competency templates folder

## Output

**Deliverables**:
- New decision record file with unique ID (DR-YYYYMMDD-NN format)
- Updated decision records register with new entry
- Changelog entry documenting the record creation

**Format**: Markdown file following the standard decision record template structure with metadata, context, options analysis, decision rationale, and consequences sections.

## Examples

### Example 1: Architecture Decision

**Scenario**: Team needs to decide between microservices and monolithic architecture for a new application

**Command**:
```
create decision record
```

**Input**:
```
Title: Application Architecture Pattern Selection
Type: Architecture
Context: Building new customer portal with expected growth to 100K users
Drivers: Scalability requirements, team expertise, deployment complexity, maintenance costs
Options: 
  1. Microservices - Better scalability but higher complexity
  2. Monolithic - Simpler to start but harder to scale
  3. Modular monolith - Middle ground approach
Decision Makers: CTO, Lead Architect, Engineering Manager
Stakeholders: Development team, DevOps team, Product team
```

**Result**: Created `DR-20251027-01.md` with full decision documentation, updated register, and changelog entry

### Example 2: Project Decision

**Scenario**: Deciding whether to postpone a feature to meet release deadline

**Command**:
```
create decision record
```

**Input**:
```
Title: Q4 Feature Scope Reduction
Type: Project
Status: Proposed
Context: Current sprint velocity indicates we'll miss Q4 release date with all planned features
Drivers: Release deadline commitment, customer expectations, technical debt concerns
Options:
  1. Postpone advanced reporting feature to Q1
  2. Extend deadline by 2 weeks
  3. Add resources to complete on time
Decision Makers: Product Owner, Project Manager
Stakeholders: Sales team, Customer Success, Development team
```

**Result**: Created decision record for team review and approval before finalizing

## Related Competencies

- **create-changelog-entry**: Use after creating a decision record to log the activity in the project changelog
- **review-progress**: Decision records are reviewed during progress assessments to track decision outcomes
- **create-job**: Decisions often lead to new work items that need to be tracked as jobs
- **store-conversation-record**: Related decision discussions can be stored for additional context

## Tips & Best Practices

- Document decisions as close to the decision-making moment as possible while context is fresh
- Include all seriously considered alternatives, not just the winner - this prevents revisiting rejected options
- Be specific about drivers and constraints - vague rationale leads to confusion later
- Update decision status when circumstances change (e.g., from Proposed to Accepted, or Accepted to Superseded)
- Link related decisions together to show decision evolution over time
- Keep decision records concise but complete - aim for clarity over comprehensiveness

## Limitations

- Requires manual input of decision details - does not automatically extract from meeting notes or conversations
- Does not automatically notify stakeholders - notification must be handled separately
- Cannot retroactively create decision records with past dates - uses current timestamp
- Does not validate that all stakeholders have been consulted before recording the decision

**Source**: `olaf-core/competencies/project-manager/prompts/create-decision-record.md`
