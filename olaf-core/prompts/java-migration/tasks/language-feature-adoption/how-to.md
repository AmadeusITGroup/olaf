# Language Feature Adoption — JDK 21

## Goal
Introduce JDK 21 language and platform features where they deliver clear readability, safety, or performance benefits without destabilizing production behavior.

## Prerequisites
- JDK 21 baseline build stable and green
- Performance baseline captured from performance profiling task
- Application running successfully on JDK 21

## Preferred Approach (Automated)
1. **Candidate Identification**:
   ```bash
   # Find instanceof patterns for pattern matching
   grep -r "instanceof" src/ | grep -v test > instanceof-candidates.txt
   
   # Find data classes suitable for records
   grep -r "class.*{" src/ | grep -E "(final|immutable)" > record-candidates.txt
   
   # Find multiline string concatenations for text blocks
   grep -r '"\s*+\s*"' src/ > textblock-candidates.txt
   
   # Find switch statements for enhancement
   grep -r "switch\s*(" src/ > switch-candidates.txt
   ```

2. **Pattern Matching Implementation**:
   ```bash
   # Example: Replace instanceof + cast patterns
   # Before: if (obj instanceof String) { String s = (String) obj; ... }
   # After:  if (obj instanceof String s) { ... }
   
   # Validate changes compile
   mvn compile -q
   ```

3. **Records Conversion**:
   ```bash
   # Convert simple data classes to records
   # Before: public class Point { private final int x, y; ... }
   # After:  public record Point(int x, int y) {}
   
   # Ensure serialization compatibility if needed
   mvn test -Dtest="*SerializationTest" -q
   ```

4. **Text Blocks Adoption**:
   ```bash
   # Replace multiline string concatenations
   # Before: String json = "{\n" + "  \"key\": \"value\"\n" + "}";
   # After:  String json = """
   #         {
   #           "key": "value"
   #         }
   #         """;
   
   # Validate string content unchanged
   mvn test -Dtest="*StringTest" -q
   ```

5. **Virtual Threads (Optional)**:
   ```bash
   # Add feature flag for virtual threads
   echo "app.features.virtualThreads=false" >> src/main/resources/application.yml
   
   # Implement virtual thread executor behind flag
   # Test with flag enabled/disabled
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually identify and convert simple cases first
2. Use IDE refactoring tools for pattern matching and records
3. Test each feature adoption incrementally
4. Rollback individual changes if issues arise

## Verification Commands
```bash
# Verify compilation after language feature adoption
mvn clean compile -q && echo "PASS: Compilation successful" || echo "FAIL: Compilation failed"

# Run tests to ensure behavior unchanged
mvn test -q && echo "PASS: Tests successful" || echo "FAIL: Tests failed"

# Check for candidate files processed
wc -l instanceof-candidates.txt record-candidates.txt textblock-candidates.txt

# Validate no syntax errors introduced
grep -r "syntax error" target/maven-status/ || echo "No syntax errors"
```

## Issue Detection & Remediation

### Record Behavior Changes (Severity: medium)
**Detection Pattern**: Test failures after converting classes to records
**Remediation**:
1. Check equals/hashCode behavior changes in record conversion
2. Verify serialization compatibility if records are serialized
3. Update tests expecting specific toString format
**Validation**: All tests pass with record implementations

### Pattern Matching Null Handling (Severity: medium)
**Detection Pattern**: NullPointerException in pattern matching code
**Remediation**:
1. Add null checks before pattern matching where needed
2. Use pattern matching with null-safe operators
3. Update null handling logic for new pattern syntax
**Validation**: No null-related test failures

### Switch Expression Changes (Severity: low)
**Detection Pattern**: Compilation errors in switch expression conversion
**Remediation**:
1. Ensure switch expressions are exhaustive
2. Handle fall-through behavior changes carefully
3. Add default cases where required
**Validation**: Switch expressions compile and behave correctly

### Virtual Thread Resource Issues (Severity: high)
**Detection Pattern**: Resource exhaustion or performance degradation with virtual threads
**Remediation**:
1. Identify blocking operations that should not use virtual threads
2. Configure appropriate thread pool limits
3. Monitor virtual thread creation and lifecycle
**Validation**: Virtual threads improve or maintain performance

### Text Block Formatting Issues (Severity: low)
**Detection Pattern**: String content changes after text block conversion
**Remediation**:
1. Verify indentation and escaping in text blocks
2. Check for trailing whitespace changes
3. Ensure string equality in tests
**Validation**: Text block content matches original strings

## Issue Collection
**Only collect issues if feature adoption causes problems**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `language-feature-adoption-<YYYYMMDD-HHmm>.json`
- **Categories**: pattern, record, sealed, text-block, virtual-thread, switch
- **Status**: OPEN (feature causing issues), RESOLVED (feature working correctly), DEFERRED (complex cases postponed)

## Success Criteria
- ✅ Language features adopted without breaking existing functionality
- ✅ All tests pass: `mvn test` exits 0
- ✅ No performance regression >5% vs baseline
- ✅ Candidate identification and adoption documented
- ✅ No HIGH severity language feature issues remain OPEN
