# Modernization Opportunities — Catalog for JDK 21 Era

## Goal
Create a structured, prioritized catalog of modernization candidates to guide incremental improvements post core migrations.

## Prerequisites
- Language feature adoption completed
- Performance baseline established
- Integration tests stable
- Dependency alignment completed

## Preferred Approach (Automated)
1. **Candidate Discovery**:
   ```bash
   # Scan for modernization opportunities
   
   # Find TODO/FIXME comments for technical debt
   grep -r "TODO\|FIXME\|XXX" src/ > technical-debt-candidates.txt
   
   # Find deprecated API usage
   grep -r "@Deprecated\|deprecated" src/ > deprecated-usage.txt
   
   # Find synchronization that could use virtual threads
   grep -r "synchronized\|ExecutorService" src/ > concurrency-candidates.txt
   
   # Find configuration scattered across files
   find src/ -name "*.properties" -o -name "*.yml" -o -name "*.yaml" > config-files.txt
   ```

2. **Category Analysis**:
   ```bash
   # Language & API opportunities
   echo "## Language & API Modernization" > modernization-catalog.md
   wc -l technical-debt-candidates.txt >> modernization-catalog.md
   
   # Concurrency opportunities
   echo "## Concurrency Modernization" >> modernization-catalog.md
   wc -l concurrency-candidates.txt >> modernization-catalog.md
   
   # Configuration opportunities
   echo "## Configuration Modernization" >> modernization-catalog.md
   wc -l config-files.txt >> modernization-catalog.md
   ```

3. **Prioritization Matrix**:
   ```bash
   # Create prioritization template
   cat > modernization-template.md << 'EOF'
   | ID | Category | Description | Impact | Effort | Risk | Priority | Status |
   |----|----------|-------------|--------|--------|------|----------|--------|
   | M001 | Language | Convert to records | MED | S | LOW | HIGH | PLANNED |
   | M002 | Concurrency | Virtual threads | HIGH | M | MED | MED | PLANNED |
   EOF
   ```

4. **Catalog Generation**:
   ```bash
   # Combine findings into structured catalog
   echo "# Modernization Opportunities Catalog" > final-modernization-catalog.md
   echo "Generated: $(date)" >> final-modernization-catalog.md
   cat modernization-template.md >> final-modernization-catalog.md
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually review codebase for modernization opportunities
2. Create catalog using spreadsheet or document template
3. Gather team input through code review sessions
4. Prioritize based on team consensus and business value

## Verification Commands
```bash
# Verify catalog files created
test -f final-modernization-catalog.md && echo "PASS: Catalog created" || echo "FAIL: Catalog missing"

# Check candidate discovery results
wc -l technical-debt-candidates.txt concurrency-candidates.txt config-files.txt

# Validate catalog structure
grep -q "| ID |" final-modernization-catalog.md && echo "PASS: Catalog formatted" || echo "FAIL: Format issue"

# Count opportunities identified
grep -c "| M[0-9]" final-modernization-catalog.md
```

## Issue Detection & Remediation

### Insufficient Modernization Data (Severity: low)
**Detection Pattern**: Empty or sparse candidate files from discovery scans
**Remediation**:
1. Expand search patterns for modernization opportunities
2. Conduct manual code review sessions with team
3. Review technical debt backlog and issue tracker
**Validation**: Sufficient candidates identified across all categories

### Conflicting Modernization Dependencies (Severity: medium)
**Detection Pattern**: Modernization items with circular or conflicting dependencies
**Remediation**:
1. Map dependencies between modernization items
2. Identify prerequisite tasks and ordering constraints
3. Break down large items into smaller, independent tasks
**Validation**: Clear dependency ordering established

### Duplicate Modernization Candidates (Severity: low)
**Detection Pattern**: Similar or overlapping modernization opportunities
**Remediation**:
1. Consolidate duplicate or similar opportunities
2. Create parent/child relationships for related items
3. Remove redundant entries from catalog
**Validation**: No duplicate opportunities in final catalog

## Issue Collection
**Only collect issues if catalog creation is blocked**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `modernization-opportunities-<YYYYMMDD-HHmm>.json`
- **Categories**: data, priority, dependency, duplicate
- **Status**: OPEN (blocking catalog creation), RESOLVED (catalog complete), DEFERRED (data pending)

## Success Criteria
- ✅ Modernization catalog created with structured format
- ✅ Opportunities categorized by type (Language, Concurrency, Config, etc.)
- ✅ Priority scoring applied with Impact/Effort/Risk assessment
- ✅ Quick wins identified for immediate implementation
- ✅ Catalog stored in findings directory for future reference

## Modernization Categories Covered
1. **Language & API**: Records, pattern matching, sealed types, text blocks
2. **Concurrency**: Virtual threads, structured concurrency, reactive improvements
3. **Configuration**: Centralized config, externalized properties
4. **Performance**: Caching, serialization, GC tuning
5. **Security**: Modern auth flows, key rotation, secure defaults
6. **Build & Tooling**: Modularization, build optimization, container improvements
