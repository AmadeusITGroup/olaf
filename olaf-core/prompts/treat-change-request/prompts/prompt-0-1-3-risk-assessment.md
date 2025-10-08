# Prompt 0-1-3: Risk Assessment

## Purpose

Evaluate risks across all dimensions (Business, Technical, Security, Operational) to inform sizing decisions and identify mitigation strategies.

---

## Input

- **1-change-request-summary.md** (from Prompt 0-1-1)
- **2-technical-scope-analysis.md** (from Prompt 0-1-2)

---

## Task Instructions

### Step 1: Assess Business Risk

Evaluate business impact and continuity risks:

1. **User Impact Risk**
   - How many users are affected?
   - What is the criticality of affected functionality?
   - Is this a customer-facing change?
   - What happens if this fails in production?

   **Rating Guide**:
   - **High**: Critical functionality, >1000 users, customer-facing, high visibility
   - **Medium**: Important functionality, 100-1000 users, internal teams
   - **Low**: Minor functionality, <100 users, admin/support tools

2. **Rollback Complexity**
   - Can this be rolled back easily?
   - Are there database migrations that can't be reversed?
   - Are there external system dependencies that complicate rollback?

   **Rating Guide**:
   - **High**: Database migration, external system changes, no rollback plan
   - **Medium**: Some data changes, requires coordination, rollback possible
   - **Low**: Code-only changes, easy rollback, no data impact

3. **Business Continuity**
   - What is the impact if deployment fails?
   - Is there a workaround for failures?
   - What is the recovery time objective (RTO)?

   **Rating Guide**:
   - **High**: No workaround, critical business process, <1hr RTO
   - **Medium**: Workaround available, important process, <4hr RTO
   - **Low**: Easy workaround, non-critical, >4hr RTO acceptable

**Business Risk Level**: Aggregate the above (High if any High, Medium if any Medium, else Low)

### Step 2: Assess Technical Risk

Evaluate technical complexity and unknowns:

1. **Technical Complexity**
   - How complex is the implementation?
   - Are there multiple systems/modules involved?
   - Are there architectural changes?
   - Is this a well-understood pattern?

   **Rating Guide**:
   - **High**: Novel architecture, >5 modules, cross-system changes, unknowns
   - **Medium**: Some complexity, 3-5 modules, standard patterns with variations
   - **Low**: Simple change, 1-2 modules, well-known patterns

2. **Technology Unknowns**
   - Are there new technologies being used?
   - Is the team familiar with the technology stack?
   - Are there third-party dependencies with unknowns?

   **Rating Guide**:
   - **High**: New technology, team unfamiliar, unproven third-party libs
   - **Medium**: Some unknowns, team partially familiar, established libs
   - **Low**: Known technology, team expert, no unknowns

3. **Integration Complexity**
   - How many integration points?
   - Are external systems involved?
   - Is there event-driven communication?
   - Are there timing/race condition concerns?

   **Rating Guide**:
   - **High**: >5 integration points, external systems, async complexity
   - **Medium**: 3-5 integration points, internal systems, some async
   - **Low**: <3 integration points, synchronous calls, simple

**Technical Risk Level**: Aggregate the above (High if any High, Medium if any Medium, else Low)

### Step 3: Assess Security Risk

Evaluate security implications:

1. **Authentication & Authorization**
   - Are there changes to auth/authz?
   - Are new permissions required?
   - Is there role-based access control (RBAC) impact?

   **Rating Guide**:
   - **High**: New auth mechanism, RBAC changes, privilege escalation risk
   - **Medium**: New permissions, existing auth modified
   - **Low**: No auth changes OR simple permission additions

2. **Data Protection**
   - Is sensitive data involved?
   - Are there PII (Personal Identifiable Information) concerns?
   - Is data encrypted at rest/in transit?
   - Are there data retention requirements?

   **Rating Guide**:
   - **High**: PII/sensitive data, encryption changes, compliance requirements
   - **Medium**: Some sensitive data, existing encryption, standard retention
   - **Low**: No sensitive data, no encryption changes

3. **Compliance & Audit**
   - Are there regulatory requirements (GDPR, SOX, etc.)?
   - Is audit logging required?
   - Are there compliance approvals needed?

   **Rating Guide**:
   - **High**: Regulatory compliance, new audit requirements, legal review
   - **Medium**: Enhanced audit logging, compliance documentation
   - **Low**: No compliance impact, standard audit logging

**Security Risk Level**: Aggregate the above (High if any High, Medium if any Medium, else Low)

### Step 4: Assess Operational Risk

Evaluate deployment and operational concerns:

1. **Deployment Complexity**
   - How complex is the deployment?
   - Are there database migrations?
   - Is downtime required?
   - Are there multi-step deployments?

   **Rating Guide**:
   - **High**: Downtime required, multi-phase deployment, coordination needed
   - **Medium**: Zero-downtime with complexity, migration scripts, some coordination
   - **Low**: Simple deployment, no downtime, single-step

2. **Monitoring & Observability**
   - Are new monitoring metrics needed?
   - Can issues be detected quickly?
   - Are there alerting requirements?

   **Rating Guide**:
   - **High**: New metrics required, poor visibility, alerting gaps
   - **Medium**: Some new metrics, good visibility, alerts need tuning
   - **Low**: Existing metrics sufficient, excellent visibility

3. **Support & Maintenance**
   - How easy is this to support post-deployment?
   - Are runbooks needed?
   - What is the on-call impact?

   **Rating Guide**:
   - **High**: Complex support, new runbooks, high on-call risk
   - **Medium**: Moderate support, runbook updates, some on-call risk
   - **Low**: Easy to support, existing runbooks, minimal on-call risk

**Operational Risk Level**: Aggregate the above (High if any High, Medium if any Medium, else Low)

---

## Output Format

Use **../templates/template-risk-assessment.md** to structure the output.

---

## Success Criteria

- [ ] All 4 risk dimensions assessed (Business, Technical, Security, Operational)
- [ ] Each dimension has a clear risk level (High/Medium/Low)
- [ ] Risk assessments are specific (not generic)
- [ ] Mitigation strategies are actionable
- [ ] Top 5 risks are prioritized
- [ ] Risk matrix is complete
- [ ] Output follows template exactly

---

## Tools to Use

**Analysis Tools**:
- Use information from `1-change-request-summary.md` for business context
- Use information from `2-technical-scope-analysis.md` for technical scope
- Apply rating guides systematically for each dimension

**No codebase search required** - this is an analytical task based on previous artifacts.

---

## Exit Criteria

Declare: **"Step 1.3 complete. Workflow 0-1 finished. Ready for Workflow 0-2 (Size Evaluation)."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Workflow**: `../workflows/workflow-0-2-size-evaluation.md`
