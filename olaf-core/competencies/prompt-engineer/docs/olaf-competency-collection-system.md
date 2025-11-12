# Competency Collection System

## Overview

The OLAF competency collection system allows users to:

1. **Select predefined or custom collections** to generate personalized competency indices
2. **Create, edit, and manage collections** for different personas and teams
3. **Organize competencies** based on user role and needs

---

## Components

### 1. Competency Collections Registry
**File:** `olaf-core/reference/competency-collections.json`

Defines all available collections with:
- Collection metadata (name, description, ID)
- Competencies included in each collection
- Access control (locked collections cannot be modified)
- Default persona-based collections

**Default Collections:**
- `core` - Always-on (locked) - Essential framework competencies
- `developer` - For software developers
- `business-analyst` - For BAs and product managers
- `technical-writer` - For documentation specialists
- `researcher` - For researchers and analysts
- `full-stack` - All available competencies

---

## User Script: Select Competency Collection

### Purpose
End users run this to select a collection and generate their personalized `query-competency-index.md`

### Usage

```powershell
# Interactive mode (default)
.\select-collection.ps1

# Select specific collection
.\select-collection.ps1 -CollectionName "developer"

# Create custom selection interactively
.\select-collection.ps1 -Custom

# List all available collections
.\select-collection.ps1 -List

# Save output to custom path
.\select-collection.ps1 -CollectionName "developer" -OutputPath "C:\custom\path\index.md"
```

### Features

✅ **Interactive menu** - Browse and select collections  
✅ **Custom selection** - Pick specific competencies manually  
✅ **Preview** - See what's in each collection before selecting  
✅ **Auto-generation** - Creates `query-competency-index.md` based on selection  
✅ **Smart aliasing** - Automatically extracts entry point aliases from manifests  
✅ **Protocol mapping** - Includes protocol info (Act, Propose-Act, Propose-Confirm-Act)

### Workflow

START → Load Collections → Choose Mode → Generate Index → Save → END

### Example Output

Generated `query-competency-index.md` contains:
```markdown
[["create prompt", "new prompt", "write prompt"], "prompt-engineer/prompts/create-prompt.md", "Propose-Confirm-Act"]
```

---

## Admin Script: Create Competency Collection

### Purpose
Prompt engineers create, edit, and manage collections for different teams/personas

### Usage

```powershell
# Interactive mode (menu-driven)
.\create-collection.ps1

# Create new collection (interactive)
.\create-collection.ps1 -CollectionName "backend-team"

# Edit existing collection
.\create-collection.ps1 -CollectionName "developer" -Edit

# Delete collection
.\create-collection.ps1 -CollectionName "my-collection" -Delete

# List all collections
.\create-collection.ps1 -List
```

### Features

✅ **Create collections** - Define new persona/team groupings  
✅ **Edit collections** - Update description and competencies  
✅ **Delete collections** - Remove collections (except locked ones)  
✅ **List view** - Browse all existing collections  
✅ **Competency browser** - Select from available competencies  
✅ **Validation** - Prevent duplicate IDs and locked modifications

---

## Manifest Requirements

For a competency to work with the collection system, its `competency-manifest.json` must include:

```json
{
  "id": "prompt-engineer",
  "index_metadata": {
    "include_in_index": true,
    "always_required": true,
    "persona_tags": ["prompt-engineer", "developer", "project-manager"],
    "description_short": "Prompt engineering capabilities"
  },
  "entry_points": [
    {
      "id": "create-prompt",
      "file": "prompts/create-prompt.md",
      "protocol": "Propose-Confirm-Act",
      "aliases": ["create prompt", "new prompt", "write prompt"],
      "required": true
    }
  ]
}
```

---

## Integration with Prompt Engineer Competency

These scripts are part of the **prompt-engineer** competency package:
- **Location:** `olaf-core/competencies/prompt-engineer/scripts/`
- **select-collection.ps1** - User selection tool
- **create-collection.ps1** - Admin management tool

---

**Version:** 1.0.0 | **Status:** Ready for use
