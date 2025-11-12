---
name: extend-specification
description: Review and extend a functional specification document to ensure it's comprehensive and ready for application modernization.
tags: [documentation, specification, requirements, analysis, frontend]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **specification_path**: string - Path to the specification document to extend
- **focus_areas**: array[UI,UX,data,api,error_handling,state_management] - (Optional) Specific areas to focus on
- **target_audience**: string - (Optional) Primary users of the specification (default: "frontend developers")

## Process

1. **Document Analysis**:
   - Review the current functional specification
   - Identify incomplete, vague, or ambiguous sections
   - Assess coverage of key frontend concerns

2. **Gap Identification**:
   - Map user flows and interactions
   - Document missing UI/UX details
   - Identify data handling requirements
   - Note API interaction points
   - List system messages and error states

3. **Specification Enhancement**:
   - Propose detailed extensions
   - Add explicit requirements
   - Include wireframes and interaction details
   - Document edge cases
   - Ensure technical completeness

## Output/Result Format
- Markdown document in [id:findings_dir] with:
  - Section-by-section review
  - Identified gaps and issues
  - Proposed enhancements
  - Action items for completion

## Output to USER
1. **Review Summary**:
   - Overall assessment
   - Key areas needing attention
   - Priority recommendations

2. **Detailed Findings**:
   - Per-section analysis
   - Specific gaps identified
   - Proposed resolutions

3. **Action Plan**:
   - List of required updates
   - Suggested next steps
   - Resources needed

## Domain-Specific Rules
- Rule 1: Be explicit in all requirements
- Rule 2: Document the "why" behind features
- Rule 3: Maintain consistent terminology
- Rule 4: Focus on user experience
- Rule 5: Ensure frontend implementation clarity

## Required Actions
1. Analyze current specification
2. Identify gaps and ambiguities
3. Propose detailed enhancements
4. Document action items
5. Create implementation checklist

## Review Focus Areas

### UI Details
- Element descriptions and states
- Layout specifications
- Interactive behaviors
- Responsive design requirements

### UX Flows
- User workflows
- Navigation paths
- Edge cases
- User decision points

### Data Handling
- Display requirements
- Input validation rules
- Data transformations
- Formatting specifications

### API Interaction
- Data requirements per view
- Request/response formats
- Error handling
- Loading states

### Error Handling
- User-facing messages
- Error recovery paths
- Validation feedback
- System status indicators

### State Management
- Client-side state needs
- Session management
- Data persistence
- Offline capabilities

⚠️ **Critical Notes**
- Never assume implementation details
- Document all edge cases
- Include visual references when possible
- Maintain version control
- Get stakeholder sign-off on changes
