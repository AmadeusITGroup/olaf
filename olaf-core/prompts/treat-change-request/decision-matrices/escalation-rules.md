---
name: escalation-rules
description: Rules and workflow for escalating or de-escalating change size classifications during execution
tags: [decision-matrix, escalation, de-escalation, governance]
---

# Escalation Rules

**Purpose**: Define when and how to escalate (or de-escalate) a change from one size classification to another during execution.

**Usage**: These rules are used by all orchestrators to determine if a change should be moved to a different orchestrator mid-execution.

---

## When to Escalate

### Trigger Points for Escalation

Changes should be escalated to the next larger size when:
#### 1. **Scope Expansion**
- **Trigger**: Number of files/modules/services exceeds the original estimate by >50%
- **Example**: Started as S (5 files) but now requires 10 files
- **Action**: S → M

#### 2. **Complexity Discovery**
- **Trigger**: Unexpected technical complexity discovered during design or implementation
- **Examples**:
  - Need for database schema changes (not originally planned)
  - Breaking API changes required
  - New external integrations needed
  - Architectural patterns need refactoring
- **Action**: Escalate by +1 level

#### 3. **Risk Identification**
- **Trigger**: Risks identified that weren't apparent during initial sizing
- **Examples**:
  - Security vulnerabilities discovered
  - Compliance/regulatory implications found
  - Production impact greater than estimated
  - Data migration complexity
- **Action**: Escalate by +1 level

#### 4. **Dependency Chain**
- **Trigger**: Change requires modifying multiple dependent systems
- **Example**: Started as M (2 services) but dependencies require changes in 4+ services
- **Action**: M → L or L → XL

#### 5. **Effort Overrun**
- **Trigger**: Estimated effort exceeded by >100%
- **Example**: S sized at 2 days, but after 4 days still not complete
- **Action**: Re-evaluate and potentially escalate

#### 6. **Uncertainty Level**
- **Trigger**: Multiple unknowns discovered that require investigation
- **Example**: Technology stack unfamiliar, integration behavior unclear
- **Action**: Escalate to ensure proper design phase

---

## When to De-escalate

### Trigger Points for De-escalation

Changes can be de-escalated to a smaller size when:

#### 1. **Scope Reduction**
- **Trigger**: Requirements clarified and scope significantly reduced
- **Example**: L sized for 5 services, but analysis shows only 2 services needed
- **Action**: L → M (with approval)

#### 2. **Complexity Lower Than Expected**
- **Trigger**: Design phase reveals the change is simpler than anticipated
- **Example**: Assumed architectural changes, but existing patterns can be reused
- **Action**: Consider de-escalation by -1 level

#### 3. **Existing Solution Found**
- **Trigger**: During design, discovered that similar functionality already exists
- **Example**: XL scoped for new feature, but can be achieved by configuring existing component
- **Action**: XL → M or L

#### 4. **Risk Mitigation**
- **Trigger**: Risks identified during sizing can be fully mitigated
- **Example**: Initially high risk due to unknowns, but proof-of-concept validated approach
- **Action**: Consider de-escalation with documented risk mitigation

---

## Escalation Process

### Step-by-Step Escalation Workflow

#### 1. **Identify Escalation Need**
- Developer/team recognizes escalation trigger
- Document specific reason(s) for escalation
- Gather evidence (code analysis, design docs, etc.)

#### 2. **Evaluate Current State**
- Review work completed so far
- Assess what can be reused in escalated workflow
- Identify which phase to resume at in new orchestrator

#### 3. **Notify Stakeholders**
- Inform team lead and product owner
- Explain escalation rationale
- Provide updated estimates (effort, timeline, risk)

#### 4. **Request Approval**
- **XS → S or S → M**: Team lead approval
- **M → L**: Tech lead + Product owner approval
- **L → XL**: Senior tech lead + Architect approval

#### 5. **Transition to New Orchestrator**
- Create transition document with:
  - Original size and rationale
  - New size and escalation reason
  - Work completed in original workflow
  - Starting point in new workflow
- Archive original workflow artifacts
- Begin new workflow from appropriate phase

#### 6. **Update Tracking**
- Update issue/ticket with new size classification
- Log escalation in project metrics
- Update timeline and resource allocation

---

## De-escalation Process

### Step-by-Step De-escalation Workflow

#### 1. **Identify De-escalation Opportunity**
- During design or early implementation
- Document why scope/complexity is lower than estimated

#### 2. **Evaluate Governance Trade-offs**
- **Important**: De-escalation means less validation and review
- Confirm that reduced governance is acceptable for the actual complexity
- Consider project complexity rating (Critical/Complex projects should be cautious)

#### 3. **Request Approval**
- **L → M or M → S**: Tech lead approval required
- **XL → L**: Architect approval required
- Document the risk assessment

#### 4. **Transition if Approved**
- Complete current phase before transitioning
- Ensure all artifacts from larger workflow are preserved
- Resume in smaller workflow at appropriate phase

---

## Escalation Decision Matrix

### Quick Reference Guide

| Current Size | Escalate To | Requires Approval From | Common Triggers |
|--------------|-------------|------------------------|-----------------|
| XS → S | Small | Team Lead | Scope +50%, effort >2x |
| S → M | Medium | Team Lead | Multiple files, some complexity |
| M → L | Large | Tech Lead + PO | API changes, multi-service |
| L → XL | Extra Large | Senior Tech Lead + Architect | Architectural impact, critical risk |

### De-escalation Approval Matrix

| Current Size | De-escalate To | Requires Approval From | Common Reasons |
|--------------|----------------|------------------------|----------------|
| XL → L | Large | Architect | Scope reduced, simpler than expected |
| L → M | Medium | Tech Lead | Fewer services, existing patterns |
| M → S | Small | Tech Lead | Simple change, well-defined |
| S → XS | Extra Small | Team Lead | Trivial change, isolated |

---

## Phase Transition Mapping

When escalating/de-escalating, map to the appropriate phase in the new orchestrator:

### Escalation Phase Mapping

| Completed Phase | Escalating From → To | Resume At |
|-----------------|----------------------|-----------|
| None | Any → Any | Beginning of new workflow |
| Design (2.1) | S → M or M → L | Design review (2.3) |
| Design Review (2.3) | S → M or M → L | Implementation (3.1) |
| Implementation (3.1) | Any → Any | Validation (4.1) |

### De-escalation Phase Mapping

| Completed Phase | De-escalating From → To | Resume At |
|-----------------|-------------------------|-----------|
| Specification (1.1) | L → M or XL → L | Design (2.1) |
| Architecture (1.3) | XL → L | Design (2.1) |
| Design (2.1) | L → M or M → S | Implementation (3.1) |

---

## Red Flags: When NOT to De-escalate

Even if scope is reduced, **do not de-escalate** if:

1. **Project is rated Critical or Complex** AND change affects core functionality
2. **Security implications** remain significant
3. **Compliance/regulatory requirements** still apply
4. **Production risk** is still high (even if scope is smaller)
5. **Multiple teams** still involved (coordination overhead remains)
6. **Already mid-implementation** (switching workflows creates more risk than benefit)

---

## Metrics & Learning

Track escalation/de-escalation events to improve sizing accuracy:

### Metrics to Collect
- **Escalation rate** by original size (% of XS that escalate, % of S, etc.)
- **De-escalation rate** by original size
- **Timing of escalation** (which phase triggered it)
- **Reasons for escalation** (categories)
- **Accuracy of initial sizing** over time

### Quarterly Review
- Analyze escalation patterns
- Identify common mis-sizing scenarios
- Update Change Evaluation Matrix criteria
- Improve sizing questions in Router workflow

---

## Examples

### Example 1: Escalation (S → M)

**Initial Sizing**: Small (S)
- 3 files, simple bug fix, 1 day estimate

**Escalation Trigger**: During implementation, discovered the bug is due to incorrect state management across 2 services
- Now affects 8 files, 2 services
- Requires API contract changes
- Estimate now 3-4 days

**Action**: Escalated to Medium (M)
- Completed: Basic implementation attempt
- Resume at: Design phase (2.1) to properly design the state management fix
- Approved by: Tech Lead

### Example 2: De-escalation (L → M)

**Initial Sizing**: Large (L)
- Estimated 5 services affected, new feature, architectural impact

**De-escalation Trigger**: During architecture review (1.3), discovered existing framework can handle requirement with minor configuration
- Actual impact: 2 services, configuration changes only
- No architectural changes needed
- Estimate revised from 12 days to 5 days

**Action**: De-escalated to Medium (M)
- Completed: Specification (1.1) and Architecture (1.3)
- Resume at: Design phase (2.1)
- Approved by: Tech Lead + Architect (confirmed no architectural impact)

---

**Last Updated**: October 8, 2025
**Owner**: Engineering Architecture Team
**Review Frequency**: Quarterly or after significant escalation events
