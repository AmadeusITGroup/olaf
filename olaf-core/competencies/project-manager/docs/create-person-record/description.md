# Create Person Record

## Overview

Creates structured person records following a standardized template to document team members and stakeholders with contact information, roles, expertise, responsibilities, and working preferences for effective team coordination.

## Purpose

Projects involve multiple people with different roles, expertise, and availability. This competency solves the problem of scattered or missing team information by creating comprehensive person records that capture all relevant details in a consistent format, enabling better communication, coordination, and knowledge management across the project team.

## Usage

**Command**: `create person record`

**Protocol**: Propose-Act

**When to Use**: Use this competency when onboarding new team members, documenting stakeholders, creating a team directory, or whenever you need to formally record information about people involved in the project for coordination and communication purposes.

## Parameters

### Required Inputs
- **full_name**: Person's complete name
- **email**: Professional email address for contact
- **role**: Current role in the project or organization
- **project_start_date**: When they joined the project (format: YYYYMMDD)
- **contact_guidance**: When and how to contact this person (e.g., "Available Mon-Fri 9-5 EST, prefer email for non-urgent")
- **areas_of_expertise**: Skills, technologies, and domains they specialize in
- **project_responsibilities**: Key responsibilities and accountabilities on the project
- **preferred_contact_methods**: How they prefer to be reached (email, Slack, phone, etc.)
- **working_hours**: Time zone and typical availability

### Optional Inputs
- **nickname**: Preferred nickname or shortened name
- **project_end_date**: When they left the project (format: YYYYMMDD) - for former team members
- **notes**: Additional relevant information, preferences, or context

### Context Requirements
- Access to peoples directory (`[id:peoples_dir]`)
- Access to people register (`[id:people-register]`)
- Access to person record template
- Privacy and data protection guidelines

## Output

**Deliverables**:
- New person record file with format: `[role]-[name]-[date].md`
- Updated people register with new entry
- Changelog entry documenting the record creation

**Format**: Markdown file following the people template structure with all contact information, expertise, responsibilities, and working preferences clearly documented.

## Examples

### Example 1: New Team Member Onboarding

**Scenario**: Senior developer joining the project

**Command**:
```
create person record
```

**Input**:
```
Full Name: Sarah Chen
Email: sarah.chen@company.com
Role: Senior Backend Developer
Project Start Date: 20251027
Contact Guidance: Available Mon-Fri 9am-6pm PST, responds to Slack within 2 hours during work hours
Areas of Expertise: Python, PostgreSQL, API design, microservices, AWS
Project Responsibilities: Backend API development, database optimization, code reviews
Preferred Contact Methods: Slack for urgent, email for non-urgent, video calls for complex discussions
Working Hours: 9am-6pm Pacific Time (UTC-8)
Notes: Prefers morning meetings, works from home Wednesdays
```

**Result**: Created `senior-backend-developer-sarah-chen-20251027.md`, updated people register, logged in changelog

### Example 2: Stakeholder Documentation

**Scenario**: Recording product owner information

**Command**:
```
create person record
```

**Input**:
```
Full Name: Michael Rodriguez
Nickname: Mike
Email: m.rodriguez@company.com
Role: Product Owner
Project Start Date: 20250901
Contact Guidance: Available for questions during sprint planning and reviews, async communication preferred otherwise
Areas of Expertise: Product strategy, user research, market analysis, agile methodologies
Project Responsibilities: Product vision, backlog prioritization, stakeholder communication, acceptance criteria
Preferred Contact Methods: Email for updates, Slack for quick questions, scheduled meetings for decisions
Working Hours: 8am-5pm Eastern Time (UTC-5), limited availability Fridays
```

**Result**: Created product owner record with all stakeholder contact and coordination information

### Example 3: Former Team Member Record

**Scenario**: Documenting departing team member for knowledge retention

**Command**:
```
create person record
```

**Input**:
```
Full Name: Alex Thompson
Email: alex.thompson@company.com
Role: DevOps Engineer
Project Start Date: 20240315
Project End Date: 20251020
Contact Guidance: No longer with project, contact DevOps team for handover questions
Areas of Expertise: Kubernetes, CI/CD, monitoring, infrastructure as code
Project Responsibilities: Deployment pipelines, infrastructure management, monitoring setup
Notes: Left comprehensive documentation in /docs/devops/, handover completed with Jamie Lee
```

**Result**: Created historical record documenting Alex's contributions and handover information

## Related Competencies

- **create-decision-record**: Person records identify decision makers and stakeholders for decision documentation
- **create-job**: Person records help with job assignment and identifying expertise for specific work
- **prepare-conversation-handover**: Person records provide contact information for handover coordination
- **review-progress**: Team member information informs resource allocation and capacity planning

## Tips & Best Practices

- Create person records during onboarding to ensure information is captured while fresh
- Keep contact information and working hours up to date - review quarterly
- Document communication preferences to respect people's working styles
- Include time zones explicitly to avoid scheduling conflicts
- Record areas of expertise to help with task assignment and knowledge sharing
- Update records when roles or responsibilities change significantly
- Create records for key stakeholders, not just team members
- Respect privacy - only include information relevant to project coordination

## Limitations

- Requires manual input of all person details - does not integrate with HR systems or directories
- Does not automatically notify the person when their record is created
- Cannot enforce privacy policies - relies on users to follow data protection guidelines
- Does not automatically update when information changes - requires manual maintenance
- Person records are local to the project - not synchronized with organization-wide directories
- Cannot validate email addresses or contact information accuracy

**Source**: `olaf-core/competencies/project-manager/prompts/create-person-record.md`
