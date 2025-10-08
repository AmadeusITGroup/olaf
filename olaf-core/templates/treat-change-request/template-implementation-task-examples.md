# Template: Implementation Task Examples

## Simple Task Grouping Example

```markdown
## Foundation Tasks (Week 1)
- Task 001: Core entity models with JPA annotations
- Task 002: Repository layer following existing patterns
- Task 003: Base service implementations with transactions

## Feature Implementation (Week 2-3)
- Task 004: User authentication service
- Task 005: Business workflow implementation
- Task 006: REST API controllers with security

## Integration & Quality (Week 4)
- Task 007: External system integration with resilience
- Task 008: End-to-end testing suite
- Task 009: Deployment automation
```

## Simple Component Task Example

```markdown
### Task 015: Implement Audit Log Entity and Repository

**Description**: Create audit log entity for tracking system events

**Depends On**: Task 001 (Base entity classes)

**Acceptance Criteria**:
- [ ] AuditLogEntity extends AbstractAuditingEntity
- [ ] Repository with findByDateRange() method
- [ ] Unit tests with 80%+ coverage
- [ ] Database migration script created

**Implementation Notes**: Follow existing entity patterns in `DeploymentRequestIdentifierEntity.java`
```

## Complex Component Multi-Task Example

```markdown
### Task 020: Implement Order State Machine Core

**Description**: Create order state machine handling 6 states (DRAFT→SUBMITTED→APPROVED→FULFILLED→CANCELLED→FAILED)

**Depends On**: Task 015 (Order entity)

**Acceptance Criteria**:
- [ ] OrderState enum with all 6 states
- [ ] State transition validation logic
- [ ] Event publishing on state changes
- [ ] Unit tests for all valid/invalid transitions
- [ ] Integration test for full order lifecycle

**Implementation Notes**: Reference existing DeploymentRequestState enum pattern

---

### Task 021: Implement Order Payment Processing

**Description**: Handle payment processing with external payment gateway

**Depends On**: Task 020 (Order state machine)

**Acceptance Criteria**:
- [ ] PaymentService with retry logic
- [ ] Circuit breaker for payment gateway calls
- [ ] Payment state tracking
- [ ] Failed payment handling and refunds
- [ ] Integration tests with mock payment gateway

**Implementation Notes**: Use existing resilience patterns from integration layer
```

## Task Grouping Guidelines

### Foundation First
- Core data models
- Base services and repositories
- Shared utilities and configurations

### Build Up from Dependencies
- Services that depend on data layer
- APIs that depend on services
- Integrations that depend on core functionality

### Complete with Quality
- Integration testing
- Performance optimization (if needed)
- Documentation and deployment automation

## Complexity Assessment Guide

### Data Layer Components
- **Simple entities** (CRUD only) → Single task
- **Complex entities** (validation, relationships, lifecycle) → Multiple tasks per concern
- Example: "User entity with authentication" is different from "Audit log entity"

### Service Layer Components
- **Simple services** (thin wrappers) → Combine related services in one task
- **Complex services** (state machines, workflows) → Break by functional responsibility
- Example: "Email notification service" vs "Order processing workflow with 6 states"

### API Layer Components
- **RESTful CRUD** for one resource → Single task
- **Complex API** with multiple resources and relationships → Task per resource group
- Example: "/users CRUD" vs "/orders with nested items, payments, and fulfillment"

### Integration Components
- One task per external system integration
- Include error handling, resilience, and testing in the same task
- Don't artificially split retry logic or circuit breakers into separate tasks

## Notes

- Generate tasks based on **ACTUAL COMPLEXITY**, not forced templates
- Task breakdown should match how developers actually work
- Each task should be independently implementable and testable
- Use `template-implementation-task.md` for the detailed structure of each individual task
