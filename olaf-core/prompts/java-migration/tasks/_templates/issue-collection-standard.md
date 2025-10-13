# Standard Issue Collection Format

## Directory Structure
```
olaf-data/findings/migrations/migration_<ts>/collected-issues/
├── <task-name>-<YYYYMMDD-HHmm>.json
└── remediation-status.json (aggregated)
```

## JSON Schema
```json
{
  "task_id": "1.4",
  "task_name": "apply-jdk17-upgrade", 
  "execution_timestamp": "20251012-1430",
  "issues": [
    {
      "id": "uuid-or-sequential",
      "detected_at": "2025-10-12T14:30:00Z",
      "category": "compile|test|config|dependency|jakarta|security|performance",
      "severity": "low|medium|high|critical",
      "file_path": "src/main/java/com/example/Service.java",
      "line_number": 42,
      "error_snippet": "package javax.servlet does not exist",
      "remediation_key": "jakarta-namespace-missing",
      "status": "OPEN|RESOLVED|DEFERRED",
      "rationale_for_deferral": "Will be resolved in jakarta-migration task",
      "resolution_notes": "Applied jakarta.servlet import",
      "resolved_at": "2025-10-12T15:00:00Z"
    }
  ],
  "summary": {
    "total_issues": 5,
    "by_severity": {"high": 1, "medium": 2, "low": 2},
    "by_status": {"OPEN": 1, "RESOLVED": 3, "DEFERRED": 1}
  }
}
```

## Remediation Key Registry
Maintain consistent remediation keys across tasks:

### Compilation Issues
- `jakarta-namespace-missing`
- `dependency-version-conflict` 
- `plugin-version-incompatible`
- `jdk-api-removed`

### Test Issues
- `test-failure-junit4-annotations`
- `test-flaky`
- `integration-startup-failure`
- `integration-serialization-issue`

### Configuration Issues
- `config-property-removed-boot3`
- `hard-coded-java-home`
- `outdated-jdk-reference`

### Dependency Issues
- `dependency-jakarta-relocation`
- `dependency-missing-transitive`
- `dependency-temp-override`