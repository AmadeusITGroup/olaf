# Coding Standards Structure

## Overview

This directory contains universal coding standards and team-specific scaffolding templates. The structure allows teams to maintain consistent coding practices while accommodating team-specific requirements.

## File Structure

```
olaf-data/practices/standards/
├── README.md                           # This file
├── universal-coding-standards.md       # Universal standards (all teams)
├── coding-standards-template.md        # Scaffold template for teams
├── integration-testing-standards.md    # Integration testing guidelines
└── [team-specific-files]/              # Team-customized standards
```

## How to Use

### For Code Reviews

The enhanced `review-code` competency will automatically:
1. Apply universal coding standards from `universal-coding-standards.md`
2. Search for team-specific standards in this directory
3. Apply any team-specific overrides or extensions

### For Teams

1. **Copy the template**: Use `coding-standards-template.md` as your starting point
2. **Customize**: Replace `[placeholders]` with your team's specific requirements
3. **Save with team name**: e.g., `frontend-team-coding-standards.md`
4. **Reference in code reviews**: The review process will automatically find and apply your standards

### Standard Types Available

#### Universal Standards (`universal-coding-standards.md`)
- Code quality principles (readability, maintainability)
- Security standards (input validation, authentication, etc.)
- Performance standards (algorithm efficiency, resource management)
- Architecture & design patterns
- Testing requirements
- Version control & documentation

#### Specialized Standards
- `integration-testing-standards.md` - Integration testing guidelines
- Additional specialized standards can be added as needed

#### Team-Specific Standards (using template)
- Language-specific conventions
- Framework-specific patterns
- Team security requirements
- Custom testing requirements
- CI/CD standards
- Documentation requirements

## Integration with Code Review Process

When you run a code review, specify:
```
Review Standards: olaf-data/practices/standards/[your-team-standards].md
```

Or the review process will automatically:
1. Apply universal standards
2. Search for team-specific files matching the repository/team name
3. Combine both sets of standards for comprehensive review

## Creating New Standards

### For Universal Standards
- Add to `universal-coding-standards.md` for organization-wide requirements
- These apply to ALL code reviews automatically

### For Team Standards  
1. Copy `coding-standards-template.md`
2. Rename to `[team-name]-coding-standards.md`
3. Customize all `[placeholder]` values
4. Remove sections that don't apply
5. Add team-specific requirements

### For Specialized Standards
- Create focused standard files (like `integration-testing-standards.md`)
- Reference from team-specific standards as needed

## Maintenance

- **Universal Standards**: Review quarterly, update for org-wide changes
- **Team Standards**: Teams own their files, update as needed
- **Templates**: Update when new categories of standards are identified

## Benefits

✅ **Consistency**: Universal standards ensure baseline quality across teams  
✅ **Flexibility**: Teams can extend/override standards for their specific needs  
✅ **Automation**: Standards are automatically applied in code reviews  
✅ **Discoverability**: Centralized location for all coding standards  
✅ **Scalability**: Easy to add new teams and specialized standards  

---

**Next Steps**: Copy the template and create your team's coding standards file!