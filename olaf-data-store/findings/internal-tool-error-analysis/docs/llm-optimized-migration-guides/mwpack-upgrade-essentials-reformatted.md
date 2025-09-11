# MWPack Upgrade Essentials (LLM-Optimized Format)

## OVERVIEW
**Purpose:** BMS MiddleWarePack migration workflow guide  
**Context:** Build Management System (BMS) component upgrades  
**Reference:** Consult `[id:product_dir]bms/bms_quick_reference.md` for detailed BMS documentation

---

## KEY_DEFINITIONS

### BMS_PROJECT
```yaml
definition: "Software development workspace using BMS build system"
structure_types:
  - "Single BMS component (standalone)"
  - "Multiple BMS components (Forest structure)"
```

### BMS_COMPONENT
```yaml
definition: "Fundamental unit of software in BMS ecosystem"
required_files:
  - "Description.xml (metadata, dependencies, build config)"
characteristics:
  - "Source code, headers, and assets"
  - "Unique name and version (A-B-C-D format)"
  - "Can be library, executable, or aggregated component"
version_format:
  pattern: "A-B-C-D"
  major_version: "A.B (breaking changes)"
  minor_version: "C (backward compatible additions)"
  patch_level: "D (bug fixes)"
```

### BMSRC_CONFIGURATION
```yaml
definition: "BMS configuration system with hierarchical reading"
hierarchy_order:
  1: "Built-in configuration (BMS distribution defaults)"
  2: "Site-wide configuration (~app-bms-admin/bms-shared/site.bmsrc)"
  3: "System configuration (/etc/bms/bmsrc.d/*.bmsrc)"
  4: "User configuration (~/.bmsrc)"
  5: "Forest configuration (FOREST_ROOT/.bms/bmsrc)"
  6: "Component configuration (DESCRIPTION_ROOT/.bms/bmsrc or DESCRIPTION_ROOT/bmsrc)"
override_rule: "Higher ranks override lower ranks (6>5>4>3>2>1)"
format: "INI-style with sections [bms], [build], [test], etc."
effective_config: "Merged result of all applicable bmsrc configurations"
```

### DESCRIPTION_XML
```yaml
definition: "Component manifest file"
contains:
  - "Component metadata (name, version, description)"
  - "Dependencies (build and runtime)"
  - "Build configuration (source files, compile flags)"
  - "Test configuration"
  - "Delivery settings"
  - "Interface/implementation relationships"
```

### FOREST_XML
```yaml
definition: "Multi-component project manager"
functions:
  - "Lists all components with versions"
  - "Defines forest structure and relationships"
  - "Enables coordinated builds and version management"
  - "Supports local and external component references"
```

### REPLICATION_DIRECTORY
```yaml
definition: "Local cache of external BMS components"
benefits:
  - "Speeds up builds (avoids remote repository access)"
  - "Contains Description.xml files and built artifacts"
  - "Automatically managed by BMS replication system"
locations:
  - "/gctmp/%u/bms_replication"
  - "User-configured paths"
```

### MIDDLEWARE_PACK
```yaml
definition: "Versioned collection of BMS infrastructure"
aliases: ["mwpack", "mdwpack"]
contains:
  - "Core BMS configuration files"
  - "Standard build toolchains and compilers"
  - "Common libraries and frameworks"
  - "Build system configurations"
typical_locations:
  - "/opt/1A/mdw-configuration/{version}/"
  - "/nastools/mdw/{version}/"
```

### BINARY_COMPATIBILITY
```yaml
definition: "BMS version compatibility rules"
version_format: "A-B-C-D"
compatibility_rules:
  major_version: "A.B (breaking changes require increment)"
  minor_version: "C (backward compatible additions)"
  patch_level: "D (bug fixes only)"
compatibility_matrix:
  compatible: "Same A.B major version"
  direction: "Higher minor/patch compatible with lower"
  breaking: "Different A.B versions incompatible"
```

---

## ESSENTIAL_COMMANDS

### COMMAND_USAGE_RULES
```yaml
restrictions:
  - "Use only commands defined in this guide"
  - "Ask user for unlisted BMS commands"
  - "Do not launch multiple commands simultaneously"
  - "Always redirect output to log files"
performance_considerations:
  - "BMS commands consume significant memory and CPU"
  - "Use commands wisely"
log_location: "[id:findings_dir]/obe/**BMS Project**/"
log_naming: "bms_deps_*.log, bms_build_*.log, bms_test_*.log (incremental numbers)"
```

### HEALTH_CHECKS
```yaml
dependency_analysis:
  command: "bms -v deps -b > bms_deps_*.log 2>&1"
  purpose: "Verbose dependency graph analysis"
  
build_verification:
  command: "bms build -b > bms_build_*.log 2>&1"
  purpose: "Verify project builds successfully"
```

### MWPACK_VERSION_MANAGEMENT
```yaml
version_change:
  method: "Edit bmsrc file"
  configuration: |
    [bms]
    include_conf = /opt/1A/mdw-configuration/23.0.0/bms/config/bmsrc/bmsrc.global
  example_path: "/opt/1A/mdw-configuration/{VERSION}/bms/config/bmsrc/bmsrc.global"
```

### CONFIGURATION_INVESTIGATION
```yaml
effective_bmsrc:
  command: "bms -s"
  purpose: "Print compiled bmsrc from entire chain"
  
replication_directory:
  command: "bms -s | grep replication_dir"
  default_meaning: "replication_dir = default means /data/mwrep/res"
```

---

## DEPENDENCY_ERROR_PROTOCOLS

### MISSING_COMPONENT_VERSION
```yaml
error_label: "Missing Component Version"
error_pattern: |
  Component **compA** (unknown version) not found
  It is required by:-
    **compB** version
diagnosis:
  cause: "compA listed in compB's Description.xml but no version defined"
  reason: "New versioners do not include compA"
resolution:
  action: "Remove dependency compA from compB's Description.xml"
  notification: "Notify user in report"
  user_action: "None required"
```

### INCOMPATIBLE_COMPONENT_VERSION
```yaml
error_label: "Incompatible Component Version"
error_pattern: |
  Binary incompatibility detected with **compA**:
  **compA** **versionA1** main
      |-> ...
      |-> **compC** **versionC** main
      |-> **compB** **versionB** main
  **compA** **versionA2** main
      |-> **compB** **versionB** main
diagnosis:
  cause: "Conflicting versions for compA in dependency graph"
  identification: "One version is 23.*, other is non-23.*"
  focus: "Follow dependency chain of non-23.* version"
resolution_process:
  1: "Navigate dependency chain from bottom (last |->)"
  2: "Find first non-23.* version"
  3: "List incompatible dependencies grouped by name prefix (mdw, ahpmw, etc.)"
  4: "Identify root cause component"
  5: "Document user actions needed"
log_format: |
  Example error:
    Binary incompatibility detected with 'osp::SSH2':
    osp::SSH2 18-0-0-24 main
        |-> mdw::OTF 18-0-0-227 main
        |-> ahpmw::shp::currencyConversionAndRounding 23-0-0-0 main
        |-> ahp::shp::messages::xml 0-0-0-0 main
    osp::SSH2 23-0-0-2 main
        |-> ahp::shp::messages::xml 0-0-0-0 main
  Expected log:
    Binary incompatibility detected with 'osp::SSH2':
    osp::SSH2 18-0-0-24 main
        |-> mdw::OTF 18-0-0-227 main
        |-> ahpmw::shp::currencyConversionAndRounding 23-0-0-0 main
        |-> ahp::shp::messages::xml 0-0-0-0 main
    Probable cause: ahpmw::shp::currencyConversionAndRounding 23-0-0-0 dependencies not fully migrated.
output_requirements:
  - "Number of components affected per error type"
  - "List of components requiring user action"
  - "Log file: deps_issues_{incremental_number}.log"
```

---

## MIGRATION_PATHS

### MIGRATION_STRATEGY
```yaml
approach: "Incremental migration through intermediate versions"
example:
  source: "MWPack 18"
  target: "MWPack 23"
  required_steps:
    - "18 to 19"
    - "19 to 21" 
    - "21 to 23"
rule: "Apply all intermediate migration guides in sequence"
```

### MIGRATION_GUIDES
```yaml
18_to_19:
  guide_location: "[id:product_dir]bms/mwpack_migration_guides/18_to_19.md"
  
19_to_21:
  guide_location: "[id:product_dir]bms/mwpack_migration_guides/19_to_21.md"
  
21_to_23:
  guide_location: "[id:product_dir]bms/mwpack_migration_guides/21_to_23.md"
```

---

## WORKFLOW_CHECKLIST

### PRE_MIGRATION
```yaml
steps:
  - "Identify source and target MWPack versions"
  - "Determine required intermediate migration steps"
  - "Backup current project state"
  - "Review applicable migration guides"
```

### HEALTH_CHECK_PROCESS
```yaml
steps:
  - "Run dependency analysis: bms -v deps -b > bms_deps_*.log 2>&1"
  - "Analyze dependency errors using protocols above"
  - "Run build verification: bms build -b > bms_build_*.log 2>&1"
  - "Document all issues in findings directory"
```

### VERSION_UPDATE_PROCESS
```yaml
steps:
  - "Update bmsrc configuration with new MWPack version"
  - "Verify effective configuration: bms -s"
  - "Check replication directory: bms -s | grep replication_dir"
  - "Re-run health checks"
```

### ERROR_RESOLUTION_PROCESS
```yaml
steps:
  - "Categorize errors using dependency error protocols"
  - "Apply appropriate fixes (remove dependencies, update versions)"
  - "Document root causes and user actions required"
  - "Generate summary report with component counts and actions"
```

### POST_MIGRATION_VALIDATION
```yaml
steps:
  - "Verify all dependency errors resolved"
  - "Confirm successful build completion"
  - "Test critical functionality"
  - "Update project documentation"
```
