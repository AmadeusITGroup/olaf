# Prompt 0-1-2: Technical Scope Analysis

## Purpose

Analyze the technical scope and impact of the change request across the codebase, estimating files, modules, LOC, and identifying API/database changes.

---

## Input

- **1-change-request-summary.md** (from Prompt 0-1-1)
- **Workspace**: bird-java-api codebase
- **Tools**: semantic_search, grep_search, file_search, list_dir

---

## Task Instructions

### Step 1: Identify Affected Modules/Services

Based on the requirements from `1-change-request-summary.md`, determine:

1. **Which modules are affected?**
   - Use `semantic_search` to find relevant modules based on feature keywords
   - Use `grep_search` to locate specific classes/interfaces mentioned
   - Use `list_dir` to explore module structure

2. **Evidence Collection**
   - Document module names (e.g., `bird-core`, `bird-persistence`, `bird-ui`)
   - Count the number of modules affected
   - Identify primary vs. secondary modules

**Example**:
```
Affected Modules (8):
1. bird-core (primary) - Core business logic
2. bird-persistence (primary) - Database entities
3. bird-api-dto (primary) - API contracts
4. bird-ui (secondary) - UI components
5. bird-deploymentmanager-client (secondary)
6. bird-aqd-client (secondary)
7. bird-notification-ms-teams (secondary)
8. bird-testing (secondary) - Test updates
```

### Step 2: Estimate Files and Lines of Code

For each affected module:

1. **File Count Estimation**
   - Use `grep_search` with relevant keywords to find affected files
   - Search for entity classes, services, controllers, DTOs
   - Count Java classes, TypeScript components, test files

2. **LOC Estimation**
   - **New code**: Estimate new classes/functions to be created
   - **Modified code**: Estimate changes to existing files
   - **Test code**: Estimate test coverage (typically 40-60% of production LOC)

**Example**:
```
Estimated Files: 40-50
- Java files: 25-30
- TypeScript files: 10-15
- Test files: 15-20
- Configuration files: 5-10

Estimated LOC: 6,000-8,000
- Production code: 4,000-5,000
- Test code: 2,000-3,000
```

### Step 3: Analyze API Changes

Identify all API changes required:

1. **New APIs**
   - What new REST endpoints are needed?
   - What are the request/response structures?
   - Document HTTP methods and paths

2. **Modified APIs**
   - Which existing endpoints need changes?
   - Are these breaking changes?
   - What is the versioning strategy?

3. **Deprecated APIs**
   - Are any APIs being retired?
   - What is the deprecation plan?

**Example**:
```
API Changes:
- New Endpoints (5):
  - POST /api/config-only-deployments
  - GET /api/config-only-deployments/{id}
  - PUT /api/config-only-deployments/{id}/approve
  - GET /api/config-only-deployments/list
  - DELETE /api/config-only-deployments/{id}

- Modified Endpoints (3):
  - PUT /api/deployments/{id} - Add isConfigOnly flag
  - GET /api/deployments - Add filter for config-only
  - POST /api/workflows - Add config-only workflow type

- Breaking Changes: None (all backwards compatible)
```

### Step 4: Analyze Database Changes

Identify database impacts:

1. **Schema Changes**
   - New tables needed?
   - New columns in existing tables?
   - Index changes?
   - Foreign key relationships?

2. **Data Migration**
   - Is data migration required?
   - How many records affected?
   - Migration complexity?

3. **Database Performance**
   - New queries required?
   - Query optimization needed?
   - Index strategy?

**Example**:
```
Database Changes:
- New Tables (2):
  - config_only_deployment (8 columns)
  - config_deployment_approval (5 columns)

- Modified Tables (3):
  - deployment: Add column is_config_only (boolean)
  - workflow_instance: Add column config_deployment_id (FK)
  - audit_log: Add config-only event types

- Data Migration:
  - No historical data migration required
  - Seed data for new tables

- New Queries (5):
  - Find config-only deployments by status
  - List pending approvals
  - Audit trail query
  - Statistics aggregation
  - Deployment history with filters
```

### Step 5: Identify Integration Points

Document all integration impacts:

1. **Internal Integrations**
   - Which other BIRD modules/services are called?
   - Are there event/message bus interactions?
   - Are there shared data structures?

2. **External Integrations**
   - Which external systems are involved?
   - Are there API calls to external services?
   - Are there authentication/authorization changes?

**Example**:
```
Integration Points:
- Internal (5):
  - Flowable BPMN (workflow engine)
  - bird-deploymentmanager-services
  - bird-notification-ms-teams
  - bird-aqd-client (AQD validation)
  - bird-events (event publishing)

- External (2):
  - AQD (Architecture Quality Dashboard) - validation calls
  - OMS (Operational Management System) - deployment API

- Message Bus:
  - Publish: ConfigDeploymentCreatedEvent
  - Publish: ConfigDeploymentApprovedEvent
  - Subscribe: DeploymentCompletedEvent
```

### Step 6: Assess Architecture Impact

Evaluate architectural considerations:

1. **Design Patterns**
   - Do new patterns need to be introduced?
   - Are existing patterns being modified?

2. **Layer Impact**
   - Which architectural layers are affected? (Presentation, Business, Persistence)
   - Are there cross-cutting concerns?

3. **Technology Stack**
   - Are new libraries/frameworks needed?
   - Are there technology upgrades?

**Example**:
```
Architecture Impact:
- Layers Affected:
  - Presentation Layer: New Angular components, REST controllers
  - Business Layer: New service classes, workflow definitions
  - Persistence Layer: New entities, repositories

- Design Patterns:
  - Strategy Pattern: For config validation
  - Observer Pattern: For event notifications
  - Repository Pattern: For data access

- New Dependencies:
  - No new major frameworks
  - Possible addition of validation library
```

---

## Output Format

Use **../templates/template-technical-scope-analysis.md** to structure the output.

---

## Success Criteria

- [ ] All affected modules identified with evidence (not assumptions)
- [ ] File and LOC estimates are based on codebase search results
- [ ] API changes inventory is complete (new, modified, deprecated)
- [ ] Database changes documented (schema, data, queries)
- [ ] All integration points mapped (internal and external)
- [ ] Architecture impact assessed
- [ ] Output follows template exactly

---

## Tools to Use

**MUST USE**:
- `semantic_search`: Find modules related to feature keywords
- `grep_search`: Search for classes, interfaces, specific code patterns
- `file_search`: Locate files by pattern (e.g., `**/*Deployment*.java`)
- `list_dir`: Explore module structure

**Optional**:
- `read_file`: Read specific configuration files or existing similar features

---

## Exit Criteria

Declare: **"Step 1.2 complete. Proceeding to Step 1.3 (Risk Assessment)."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Prompt**: `prompt-0-1-3-risk-assessment.md`
