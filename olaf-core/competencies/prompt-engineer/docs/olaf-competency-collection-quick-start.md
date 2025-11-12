# Competency Collection System - Quick Start

## 🚀 For End Users: Select Your Competencies

### Interactive Selection (Recommended)

```powershell
cd olaf-core/competencies/prompt-engineer/scripts
.\select-collection.ps1
```

Then:
1. Choose your persona (Developer, BA/PM, Writer, etc.)
2. Or select "Custom" to pick individual competencies
3. Script generates your personalized `query-competency-index.md`

### Quick Selection by Persona

```powershell
.\select-collection.ps1 -CollectionName "developer"
```

**Available personas:**
- `developer` - Software developers
- `business-analyst` - Product managers & BAs
- `technical-writer` - Documentation specialists
- `researcher` - Researchers & analysts
- `full-stack` - All competencies

---

## 👨‍💼 For Administrators: Manage Collections

### Create New Collection

```powershell
cd olaf-core/competencies/prompt-engineer/scripts
.\create-collection.ps1
```

Then:
1. Choose "Create new collection"
2. Enter collection name and description
3. Select competencies from the list
4. Collection is saved automatically

### Edit Existing Collection

```powershell
.\create-collection.ps1 -CollectionName "my-collection" -Edit
```

### Delete Collection

```powershell
.\create-collection.ps1 -CollectionName "my-collection" -Delete
```

### List All Collections

```powershell
.\create-collection.ps1 -List
# Or to see user selections:
.\select-collection.ps1 -List
```

---

## 📋 What Happens Behind the Scenes

1. **You select competencies** via one of the scripts
2. **Scripts read competency manifests** from `olaf-core/competencies/*/competency-manifest.json`
3. **Scripts extract entry points** with aliases and protocols
4. **Index is generated** at `olaf-core/reference/query-competency-index.md`
5. **Your aliases work!** E.g., "create prompt", "new prompt", "write prompt" all invoke the same capability

---

## 💡 Example: Team Workflow

### Day 1: Team Lead Sets Up Collections

```powershell
.\create-collection.ps1 -CollectionName "backend-team"
```

When prompted, select:
- prompt-engineer (core)
- java-migration
- feature-creation

### Day 2: Team Members Use Collection

```powershell
.\select-collection.ps1 -CollectionName "backend-team"
```

They all get the same competency index with java migration + feature creation + prompting capabilities.

---

## ✅ Checklist for Setup

- [ ] Run `.\select-collection.ps1` to select your collection
- [ ] Generated index appears at `olaf-core/reference/query-competency-index.md`
- [ ] Try invoking competencies: "create prompt", "java migration", "write tutorial"
- [ ] Share your collection with teammates using same collection name

---

## 📁 File Locations

- **Collections definitions:** `olaf-core/reference/competency-collections.json`
- **Your generated index:** `olaf-core/reference/query-competency-index.md`
- **Scripts:** `olaf-core/competencies/prompt-engineer/scripts/`
- **Documentation:** `olaf-core/competencies/prompt-engineer/docs/`

---

**Version:** 1.0.0 | **Status:** Ready to use
