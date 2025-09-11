# LLM-Optimized Migration Guide Template

## Format Design Principles
- **Structured sections** with clear headers
- **Error patterns** explicitly listed with regex-friendly formats
- **Resolution mappings** directly linked to error types
- **Searchable keywords** for each change
- **Consistent formatting** across all guides

## Template Structure

### 1. ERROR_PATTERNS
```yaml
error_type: "missing_header"
patterns:
  - "fatal error: (.+): No such file or directory"
  - "(.+\.h): No such file or directory"
keywords: ["header", "include", "file not found"]
```

### 2. COMPONENT_CHANGES
```yaml
component: "mdw::OracleClient"
change_type: "RENAMED"
old_name: "mdw::OracleClient"
new_name: "rdb::OracleClient"
migration_version: "18_to_19"
required_actions:
  - "Update Description.xml dependencies"
  - "Add rdb::Pack to application.xml"
  - "Use CMK version >= 4-82-1-8"
```

### 3. RESOLUTION_MAPPINGS
```yaml
error_pattern: "otf/ReroutingTokens.h: No such file or directory"
resolution:
  guide_section: "OTF Migration"
  actions:
    - "Replace #include <otf/ReroutingTokens.h>"
    - "Check OTF header restructuring in 18_to_19.md"
  related_changes: ["otf_service_interface", "rest_service_migration"]
```

### 4. QUICK_REFERENCE
```yaml
search_terms: ["ReroutingTokens", "otf header", "missing otf"]
component_affected: "OTF"
versions: ["18_to_19", "19_to_21"]
severity: "FATAL"
fix_complexity: "SIMPLE"
```
