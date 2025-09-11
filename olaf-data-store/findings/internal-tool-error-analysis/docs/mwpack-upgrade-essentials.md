In the context of BMS MiddleWarePack migration, the following highlights key definitions and the necessary commands to complete the workflow.
In case the information you are looking for is not present, consult `[id:product_dir]bms/bms_quick_reference.md` to get guidance on in-depth BMS documentation.

## Key Definitions

### BMS Project
A **BMS project** is a software development workspace that uses the BMS (Build Management System) build system. It can contain either:
- A single **BMS component** (standalone component)
- Multiple **BMS components** organized in a **Forest** structure

### BMS Component
A **BMS component** is a fundamental unit of software in the BMS ecosystem, defined by:
- A `Description.xml` file that specifies its metadata, dependencies, and build configuration
- Source code, headers, and other assets
- A unique name and version following the format `A-B-C-D` (where A.B is the major version, C is the minor version, D is the patch level)
- Can be a library, executable, or aggregated component

### bmsrc (BMS Configuration File)
The **bmsrc** file is BMS's configuration system with a specific reading hierarchy:
1. Built-in configuration (BMS distribution defaults)
2. Site-wide configuration (`~app-bms-admin/bms-shared/site.bmsrc`)
3. System configuration (`/etc/bms/bmsrc.d/*.bmsrc`)
4. User configuration (`~/.bmsrc`)
5. Forest configuration (`FOREST_ROOT/.bms/bmsrc`)
6. Component configuration (`DESCRIPTION_ROOT/.bms/bmsrc` or `DESCRIPTION_ROOT/bmsrc`)

The **bmsrc** actually used during BMS operations is the effective configuration obtained by merging all applicable bmsrc configurations from the hierarchy, where higher ranks override lower rank configurations (6>5>4>3>2>1). Refer to the actual bmsrc to know the effective BMS configuration. Configuration uses INI-style format with sections like `[bms]`, `[build]`, `[test]`, etc.

### Description.xml
The **Description.xml** file is the component's manifest that defines:
- Component metadata (name, version, description)
- Dependencies (both build and runtime)
- Build configuration (source files, compile flags)
- Test configuration
- Delivery settings
- Interface/implementation relationships

### Forest.xml
The **Forest.xml** file manages multi-component projects by:
- Listing all components in the forest with their versions
- Defining the forest structure and component relationships
- Enabling coordinated builds and version management across components
- Supporting both local and external component references

### Replication Directory
A **replication directory** is a local cache of external BMS components that:
- Speeds up builds by avoiding remote repository access
- Contains `Description.xml` files and built artifacts of external dependencies
- Is automatically managed by BMS's replication system
- Can be found in locations like `/gctmp/%u/bms_replication` or configured paths

### Middleware Pack (mwpack/mdwpack)
A **middleware pack** is a versioned collection of:
- Core BMS configuration files
- Standard build toolchains and compilers
- Common libraries and frameworks
- Build system configurations
- Located typically at `/opt/1A/mdw-configuration/{version}/` or `/nastools/mdw/{version}/` paths

### Binary Compatibility
**Binary compatibility** in BMS follows strict version rules:
- **A-B-C-D** version format where:
  - **A.B** = Major version (breaking changes)
  - **C** = Minor version (backward compatible additions)
  - **D** = Patch level (bug fixes)
- Components are binary compatible if they share the same A.B major version
- Higher minor/patch versions are compatible with lower ones
- Breaking compatibility requires incrementing the major version (A.B)

---

## Essential Skills & Commands

Only use commands defined below. If you need to apply a BMS command not listed here, ask the user.
BMS commands can take very long and consume a lot of memory and CPU resources, so use them wisely:
 - do not launch more than one command at once.
 - always redirect output to a log file in `[id:findings_dir]/obe/**BMS Project**/` (bms_deps_*.log, bms_build_*.log, bms_test_*.log, etc.). * is an incremental number.

### Health Checks
```bash
# Check dependency graph health
bms -v deps -b > bms_deps_*.log 2>&1 # Verbose dependency analysis

# Verify project builds
bms build -b > bms_build_*.log 2>&1 # Build the project
```

### MiddleWarePack Version Management
```bash

# Change mwpack version (edit bmsrc file)
[bms]
include_conf = /opt/1A/mdw-configuration/23.0.0/bms/config/bmsrc/bmsrc.global

```

### Configuration Investigation
```bash
# Printout actually used bmsrc (as a compiled unit of the chain of bmsrcs)
bms -s

# Identify bms replication directory
bms -s | grep replication_dir
# replication_dir = default means the replication directory is /data/mwrep/res
```

## Essential Processes

### **Dependency Error Protocol**
  Known errors for component named **compA**:
    - Label: **Missing Component Version**
      - Error Message in **bms_deps_*.log**:
          Component **compA** (unknown version) not found
          It is required by:-
            **compB** version
      - Diagnosis:
          This means **compA** is listed in the Description.xml of **compB**, but no version has been defined for it.
          This can mean that new versioners do not include **compA**.
      - Fix:
          Remove the dependency **compA** from **compB**'s Description.xml.
          Notify the user in the report.
          No user action needed.

    - Label: **Incompatible Component Version**
      - Error Message in **bms_deps_*.log**:
          Binary incompatibility detected with **compA**:
          **compA** **versionA1** main
              |-> ...
              |-> **compC** **versionC** main
              |-> **compB** **versionB** main
          **compA** **versionA2** main
              |-> **compB** **versionB** main
      - Diagnosis:
          This error highlights conflicting versions for **compA** in the project dependency graph. Either **versionA1** or **versionA2** will be 23.* which is the target version. So the focus is on the other one, which we need to follow its dependency chain from **compB** to identify the faulty dependency.
      - Expected output in **deps_issues_{^[0-9]+}.log**:
          Navigate the dependency chain of the non 23. **versionA** starting from the bottom (last |->) until you find the first non-23.* version.
          List the incompatible dependencies with both versions grouped by name prefix (eg: mdw, ahpmw...) and which component is the root cause of introducing the incompatible dependency.
          User Action on the list of root cause components.
          Document this dependency in the log file like follows:
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
    For each known error, give the number of components affected and the list of components that need a user action.

### **Known Migration Changes**

Locate below the list of known changes to consult depending on the **Source Version** and **Target Version** of your migration.
For example, if you are migrating from MWPack 18 to MWPack 23, then you need to consult the following sections and apply their relevant changes:
- 18 to 19
- 19 to 21
- 21 to 23

#### From 18 to 19

Head to the migration guide here: `[id:product_dir]bms/mwpack_migration_guides/18_to_19.md`

#### From 19 to 21

Head to the migration guide here: `[id:product_dir]bms/mwpack_migration_guides/19_to_21.md`

#### From 21 to 23

Head to the migration guide here: `[id:product_dir]bms/mwpack_migration_guides/21_to_23.md`
