# OLAF Getting Started Guide

**Target Audience:** New OLAF users and developers

## Overview

OLAF (Open Lightweight Assistant Framework) is a competency-driven AI agent framework that enables structured, protocol-based interactions with Large Language Models. This guide demonstrates OLAF's core capabilities through practical examples and real conversation records.

---

## What You'll Learn

This getting started guide walks you through OLAF's key features:

1. **Competency Discovery** - How to find available AI capabilities
2. **Conversation Documentation** - How to capture and analyze AI interactions  
3. **Knowledge Research** - How to conduct structured research with AI
4. **Prompt Engineering** - How to create standardized AI prompts
5. **Research Planning** - How to manage complex, multi-session research projects

Each section includes:
- ✅ **Live Examples** - Real conversation records showing actual usage
- 🔗 **Linked Resources** - Direct links to prompts, templates, and outputs
- 📋 **Step-by-Step Instructions** - How to replicate the examples
- 🎯 **Best Practices** - Tips for effective usage

---

## Section 1: Discovering Available Competencies

### The `olaf list-competencies` Competency

OLAF provides a simple way to discover all available AI competencies through the `olaf list-competencies` competency.

**What it does:**
- Lists all available competencies organized by role (developer, researcher, project-manager, etc.)
- Shows the trigger phrases that activate each competency
- Displays the execution protocol (Act, Propose-Act, Propose-Confirm-Act)

**How to use it:**
1. Type `olaf list-competencies` in your AI chat
2. The system will read the competency index and display all available capabilities
3. Use the trigger phrases to activate specific competencies

**Example Output Structure:**
```
Developer Competencies:
- "olaf review code" → developer/review-code.md (Act protocol)
- "olaf code review" → developer/review-code.md (Act protocol)

Researcher Competencies:  
- "olaf search and learn" → researcher/search-and-learn.md (Act protocol)
- "olaf research and report" → researcher/research-and-report.md (Propose-Confirm-Act protocol)

Project Manager Competencies:
- "olaf store conversation" → project-manager/store-conversation-record.md (Act protocol)
- "olaf create job" → project-manager/create-job.md (Act protocol)
```

**Key Benefits:**
- **Discoverability**: Find capabilities you didn't know existed
- **Consistency**: Standardized trigger phrases across all competencies
- **Protocol Awareness**: Understand how each competency will interact with you

---

## Section 2: Documenting AI Conversations

### The "Store Conversation" Competency

One of OLAF's most powerful features is automatic conversation documentation using the **"olaf store conversation"** competency.

**📋 Live Example:** [Conversation Record 20250926-1453](conversations/conversation-record-20250926-1453.md)

This example shows a complete research session where the user:
1. Requested research on AWS Strands and AgentCore
2. Approved a research plan  
3. Received a comprehensive technical report
4. Used "olaf store conversation" to document the entire session

**What the competency captures:**
- **Timeline**: Exact timestamps of each interaction
- **Actions Taken**: Every file read, search performed, and output created
- **Files Created/Modified**: Complete audit trail of all changes
- **User Interactions**: Full conversation flow with context

**How to use it:**
1. At the end of any AI session, simply say: **"olaf store conversation"**
2. OLAF automatically:
   - Finds the store-conversation competency
   - Retrieves current timestamp
   - Creates a detailed narrative record
   - Saves it to the conversations directory

**Generated Output Location:**
```
.olaf/olaf-data/product/documentations/conversations/
└── conversation-record-YYYYMMDD-HHmm.md
```

**Why this matters:**
- **Accountability**: Full audit trail of AI assistance
- **Knowledge Transfer**: Share exactly what was accomplished
- **Session Continuity**: Resume work across multiple sessions
- **Learning**: Understand how competencies work in practice

---

## Section 3: Creating Custom AI Prompts

### The "Create Prompt" Competency

OLAF enables you to create standardized AI prompts that follow framework principles and templates.

**How it works:**
1. **Template-Based**: Uses standardized templates from `.olaf/olaf-core/templates/`
2. **Role Organization**: Automatically categorizes prompts by role (developer, researcher, etc.)
3. **Consistency**: Ensures all prompts follow OLAF core principles
4. **Deduplication**: Checks for existing similar prompts to avoid duplicates

**Prompt Structure Analysis:**

All OLAF prompts follow this standardized structure:

```markdown
---
name: prompt-name
description: Brief description of what the prompt does
tags: [relevant, tags, for, categorization]
---

## Framework Validation
[Standard OLAF framework requirements]

## Time Retrieval  
[Timestamp handling instructions]

## Input Parameters
[Required and optional parameters]

## User Interaction Protocol
[Act/Propose-Act/Propose-Confirm-Act specification]

## Process
[Step-by-step execution instructions]

## Output Format
[Expected deliverables and file locations]

## Success Criteria
[Checklist for completion validation]
```

**Example: Finding Created Prompts**

After using the "create prompt" competency, you can find your new prompt in:
```
.olaf/olaf-core/prompts/<category>/
└── your-new-prompt.md
```

**Categories include:**
- `developer/` - Code analysis, review, testing prompts
- `researcher/` - Research, analysis, investigation prompts  
- `project-manager/` - Planning, documentation, tracking prompts
- `business-analyst/` - Requirements, specifications, user stories

**Template Analysis:**

The create-prompt competency uses templates from:
```
.olaf/olaf-core/templates/<category>/
└── prompt-template.md
```

These templates ensure:
- **Consistency**: All prompts follow the same structure
- **Completeness**: Required sections are never missed
- **Standards Compliance**: Automatic adherence to OLAF principles
- **Quality**: Built-in validation and success criteria

---

## Section 4: Understanding OLAF Protocols

### Interaction Protocols Explained

OLAF uses three distinct interaction protocols to balance safety and efficiency:

#### **Act Protocol** (Direct Execution)
- **When used**: Safe, read-only operations
- **Behavior**: Executes immediately without asking
- **Examples**: Reading files, listing directories, searching code
- **User experience**: Fast, efficient, minimal interruption

#### **Propose-Act Protocol** (Analysis Before Action)  
- **When used**: Actions requiring user agreement
- **Behavior**: Presents plan, waits for approval, then executes
- **Examples**: Code modifications, file creation, research execution
- **User experience**: One confirmation step, maintains control

#### **Propose-Confirm-Act Protocol** (Multi-Step Validation)
- **When used**: Complex, multi-step operations with significant impact
- **Behavior**: 
  1. **Propose**: Present detailed plan
  2. **Review**: Wait for user feedback
  3. **Confirm**: Ask for final sign-off  
  4. **Act**: Execute only after confirmation
- **Examples**: Large research projects, system modifications, complex analysis
- **User experience**: Maximum control, suitable for complex tasks

**Protocol Selection:**
Each competency specifies its protocol in the competency index. This ensures consistent behavior and appropriate safety levels.

---

## Section 5: File Organization and Memory Map

### Understanding OLAF's Structure

OLAF uses a standardized file organization system with ID-based references:

#### **Core Framework** (`olaf-core/`)
- **Prompts**: `olaf-core/prompts/<role>/` - All AI competency definitions
- **Templates**: `olaf-core/templates/<role>/` - Standardized templates  
- **Tools**: `olaf-core/tools/` - Utility scripts and analyzers
- **Reference**: `olaf-core/reference/` - Core principles and guides

#### **Work Environment** (`olaf-data/`)
- **Projects**: `olaf-data/projects/` - Jobs, changelogs, project tracking
- **Product**: `olaf-data/product/` - Decision records, documentation
- **Findings**: `olaf-data/findings/` - Research outputs, analysis results
- **Peoples**: `olaf-data/peoples/` - Team member information

#### **File Referencing Convention**
OLAF uses ID-based file references for consistency:
- **Files**: `[id:file_id]` → `olaf-data/specific-file.md`
- **Directories**: `[id:dir_id]` → `olaf-data/specific-directory/`
- **Files in Directories**: `[id:dir_id]filename.ext`

This system ensures:
- **Consistency**: Same references across all prompts and documentation
- **Maintainability**: Easy to update paths in one location
- **Clarity**: Clear understanding of file locations

---

## Next Steps

### Getting Started Checklist

- [ ] **Try `olaf list competencies`** - Discover available AI capabilities
- [ ] **Use "olaf store conversation"** - Document your first AI session  
- [ ] **Create a custom prompt by using `olaf create prompt`** - Build your own AI competency
- [ ] **Explore the file structure** - Understand OLAF's organization

### Advanced Usage

Once comfortable with basics:
- **Create Jobs**: Use project management competencies for task tracking
- **Code Analysis**: Leverage developer competencies for code review and improvement
- **Team Collaboration**: Share conversation records and research reports

### Getting Help

- **Competency Index**: Check `.olaf/olaf-core/reference/query-competency-index.md` for all available capabilities
- **Core Principles**: Review `.olaf/olaf-core/reference/core-principles.md` for framework guidelines
- **Examples**: Explore `docs/getting-started/` for real usage examples

---

## Summary

OLAF transforms AI interactions from ad-hoc conversations into structured, documented, and repeatable processes. By using competencies, protocols, and standardized templates, you can:

- **Discover** AI capabilities systematically
- **Document** all AI interactions automatically  
- **Research** complex topics with proper oversight
- **Create** standardized AI prompts and workflows
- **Collaborate** effectively using shared conversation records

The framework ensures consistency, safety, and knowledge preservation across all AI-assisted work.

**Ready to start?** Try `olaf list competencies` in your next AI conversation!

---

*This documentation was generated using OLAF competencies and demonstrates the framework's capabilities through real examples and conversation records.*
