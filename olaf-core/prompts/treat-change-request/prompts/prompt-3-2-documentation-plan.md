# Prompt 3.2: Documentation Plan Creation

## Overview

Transform the approved technical design into a comprehensive documentation strategy that addresses all stakeholder needs. This prompt creates detailed documentation plans covering user guides, technical documentation, and training materials.

## Prerequisites

**Required Input Documents:**
- `DESIGN_<PROJECT-ID>.md` (finalized design from Phase 2)
- `SPECIFICATION_<PROJECT-ID>.md` (approved specification from Phase 1)

**Required Information:**
- Stakeholder types and their roles
- Existing documentation standards and tools
- Training requirements and delivery methods
- Documentation maintenance processes

## Prompt Instructions

### Context Setup
You are a Senior Technical Writer and Documentation Architect creating a comprehensive documentation strategy for a software project. You have access to the complete specification and technical design documents. Your goal is to create a documentation plan that ensures all stakeholders have the information they need to successfully use, maintain, and support the system.

### Input Processing
1. **Analyze Specification Document**
   - Identify all user types and their roles (end users, admins, power users)
   - Extract user stories and workflows to document
   - Understand business processes and user goals
   - Note functional requirements that need user documentation
   - Identify training needs based on user complexity

2. **Analyze Design Document**
   - Extract API specifications and technical integration points
   - Identify system architecture components for developer documentation
   - Understand operational procedures and maintenance tasks
   - Note configuration options and technical customization capabilities
   - Map technical implementation to user-facing features

3. **Cross-Reference Both Documents**
   - Ensure user documentation covers all specification user stories
   - Verify technical documentation covers all design components
   - Identify gaps where user needs lack technical implementation details
   - Determine documentation priorities based on user importance and technical complexity

### Output Generation

**Use Template**: `../templates/template-documentation-plan.md`

Create a comprehensive documentation plan document following the template structure with these specific requirements:

#### Stakeholder Analysis Section
- Define all stakeholder types with specific personas
- Map each stakeholder to their information needs
- Assess technical expertise and preferred formats
- Identify critical workflows requiring documentation

#### User Documentation Plan Section
**Analyze the specification to identify user types and their documentation needs:**

**For each user type identified in the specification, create documentation tasks:**
- [ ] **Task: Create documentation for [User Type] (e.g., End Users, Administrators, Power Users)**
  - [ ] Subtask: Write getting started guide (adapt complexity based on user technical level)
  - [ ] Subtask: Document primary workflows (based on user's main tasks from specification)
  - [ ] Subtask: Create reference materials (adapt format to user preferences)
  - [ ] Subtask: Add troubleshooting content (based on anticipated user challenges)
  - [ ] Subtask: Test documentation with real users from this user type

**For each major feature identified in the specification, create feature documentation:**
- [ ] **Task: Document [Feature Name from Specification]**
  - [ ] Subtask: Write feature overview and benefits
  - [ ] Subtask: Create step-by-step usage instructions
  - [ ] Subtask: Document feature settings and customization options
  - [ ] Subtask: Add examples and use cases relevant to this feature
  - [ ] Subtask: Create FAQ for feature-specific questions

**Adaptation Guidelines:**
- **Complex features**: Break into multiple documentation tasks
- **Simple features**: Combine into a single comprehensive guide
- **Technical users**: Focus on configuration and advanced options
- **Business users**: Emphasize workflows and business benefits

#### API Documentation Plan Section
**Create specific, tickable API documentation tasks:**
- [ ] **Task: Document authentication and setup**
  - [ ] Subtask: Write API key generation and management guide
  - [ ] Subtask: Document authentication methods and examples
  - [ ] Subtask: Create "first API call" tutorial
  - [ ] Subtask: Document rate limiting and error responses

- [ ] **Task: Document each API endpoint group**
  - [ ] Subtask: Document [Endpoint Group A] with code examples
  - [ ] Subtask: Document [Endpoint Group B] with code examples
  - [ ] Subtask: Create Postman/Insomnia collection
  - [ ] Subtask: Write SDK integration examples

#### Operational Documentation Plan Section
**Create specific, tickable operations tasks:**
- [ ] **Task: Create deployment documentation**
  - [ ] Subtask: Write step-by-step deployment checklist
  - [ ] Subtask: Document environment configuration
  - [ ] Subtask: Create rollback procedures
  - [ ] Subtask: Document monitoring setup and alerts

- [ ] **Task: Create maintenance documentation**
  - [ ] Subtask: Write backup and restore procedures  
  - [ ] Subtask: Document log management and retention
  - [ ] Subtask: Create incident response playbook
  - [ ] Subtask: Document security patching procedures

#### Developer Documentation Plan Section
**Create specific, tickable developer tasks:**
- [ ] **Task: Create development setup guide**
  - [ ] Subtask: Write local environment setup (step-by-step)
  - [ ] Subtask: Document required tools and versions
  - [ ] Subtask: Create "first contribution" guide
  - [ ] Subtask: Document code review process

- [ ] **Task: Document architecture and patterns**
  - [ ] Subtask: Create system architecture diagram with explanations
  - [ ] Subtask: Document coding standards and patterns
  - [ ] Subtask: Write component interaction guides
  - [ ] Subtask: Document testing guidelines and examples

#### Training Materials Plan Section  
**Create specific, tickable training tasks:**
- [ ] **Task: Create role-based training modules**
  - [ ] Subtask: Design end-user training agenda
  - [ ] Subtask: Create administrator training materials
  - [ ] Subtask: Develop hands-on exercises and scenarios
  - [ ] Subtask: Create training assessment/quiz questions

- [ ] **Task: Create multimedia training content**
  - [ ] Subtask: Record overview demo video (5-10 minutes)
  - [ ] Subtask: Create feature-specific tutorial videos
  - [ ] Subtask: Design interactive training scenarios
  - [ ] Subtask: Create downloadable quick reference guides

#### Documentation Maintenance Strategy Section
**Create specific, tickable maintenance tasks:**
- [ ] **Task: Establish documentation processes**
  - [ ] Subtask: Define content review and approval workflow
  - [ ] Subtask: Set up documentation version control
  - [ ] Subtask: Create content update schedule and responsibilities
  - [ ] Subtask: Design user feedback collection system

- [ ] **Task: Set up documentation metrics**
  - [ ] Subtask: Implement usage analytics tracking
  - [ ] Subtask: Create monthly content freshness reports
  - [ ] Subtask: Set up user satisfaction surveys
  - [ ] Subtask: Define success metrics and KPIs

### Quality Validation

Before finalizing, ensure:
- [ ] All stakeholder types have appropriate documentation coverage
- [ ] Documentation scope aligns with project deliverables
- [ ] Content creation timeline is realistic and resourced
- [ ] Maintenance processes ensure documentation stays current
- [ ] Training materials address knowledge transfer requirements
- [ ] Documentation standards are consistent and professional

### Expected Output

**Document Name**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`
**Format**: Professional markdown following template structure
**Content**: Comprehensive documentation strategy ready for content team execution
**Length**: As concise as possible while covering all documentation needs thoroughly

### Usage Notes

- This prompt should be used after design approval but before implementation begins
- The resulting documentation plan guides all content creation during development
- Training materials should be developed alongside system implementation
- The plan should be reviewed with stakeholders and content teams before finalization

## Integration with Development Process

**Handoff to Development Team:**
- API documentation requirements inform interface design
- Developer documentation guides code commenting and standards
- Architecture documentation influences design decisions

**Content Team Execution:**
- Documentation plan provides detailed content creation guidance
- Template references ensure consistent formatting and structure
- Timeline aligns content creation with development milestones

**Stakeholder Communication:**
- Documentation strategy demonstrates comprehensive support approach
- Training plan ensures successful system adoption
- Maintenance strategy provides long-term content quality assurance

## Content Creation Guidelines

**Documentation Standards:**
- Use clear, concise language appropriate for target audience
- Include practical examples and real-world scenarios
- Maintain consistent formatting and structure
- Provide searchable and accessible content

**Delivery Mechanisms:**
- Online documentation portals with search capabilities
- Downloadable PDF guides for offline reference
- Interactive tutorials and guided walkthroughs
- Video content for complex procedures

**Success Metrics:**
- User adoption rates and documentation usage analytics
- Support ticket reduction in areas covered by documentation
- Time-to-productivity for new users and developers
- Content freshness and accuracy ratings