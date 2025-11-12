# Find Expert Contact

## Overview

Locates and provides contact information for subject matter experts within your organization or professional network.

## Purpose

Quickly identifies the right person to contact for specific expertise, technical questions, or domain knowledge, saving time searching through organizational charts or directories.

## Usage

**Command**: `find expert contact`

**Protocol**: Act

**When to Use**: When you need to find someone with specific expertise, technical knowledge, or domain experience.

## Parameters

### Required Inputs
- **Expertise Area**: The domain, technology, or subject matter you need help with

### Optional Inputs
- **Organization/Team**: Narrow search to specific org or team
- **Location**: Geographic or timezone preferences
- **Context**: Why you need the expert (helps refine search)

### Context Requirements
- Access to organizational directory or contact information
- Clear description of the expertise needed

## Output

**Deliverables**:
- Expert contact information (name, email, role)
- Expertise areas and background
- Availability or best contact method
- Alternative contacts if primary is unavailable

**Format**: Structured list with contact details and expertise summary

## Examples

### Example 1: Technical Expertise

**Scenario**: Need help with Kubernetes deployment issues

**Command**:
```
find expert contact
```

**Input**: "I need someone who knows Kubernetes and container orchestration"

**Result**: Contact information for DevOps engineers or SREs with Kubernetes expertise

### Example 2: Domain Knowledge

**Scenario**: Questions about regulatory compliance

**Command**:
```
find expert contact
```

**Input**: "Who can help with GDPR compliance requirements?"

**Result**: Contact for compliance officer or legal team member with GDPR expertise

## Related Competencies

- **assess-genai-initiative**: Use this first to evaluate initiatives, then find experts to implement
- **use-competency**: Can route to this competency when expert finding is needed
- **olaf-help**: General help discovery for OLAF capabilities

## Tips & Best Practices

- Be specific about the expertise area for better matches
- Mention the context or problem you're trying to solve
- Ask for alternative contacts in case primary is unavailable
- Consider timezone and availability when provided

## Limitations

- Requires access to organizational contact information
- Cannot guarantee expert availability
- May not have information for external experts
- Contact information may be outdated
