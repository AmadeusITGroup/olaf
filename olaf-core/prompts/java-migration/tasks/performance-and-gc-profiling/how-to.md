# Performance and GC Profiling — JDK 21

## Goal
Measure and compare key performance & memory metrics between JDK 17 baseline and JDK 21 to identify regressions or optimization opportunities.

## Prerequisites
- Application stable on both JDK 17 and JDK 21
- Integration tests passing
- Dependency alignment completed

## Preferred Approach (Automated)
1. **Environment Setup**:
   ```bash
   # Ensure consistent environment
   echo "Setting up performance testing environment"
   
   # Stop unnecessary services
   # Set consistent JVM heap size
   export JVM_OPTS="-Xmx2g -Xms2g"
   ```

2. **JDK 17 Baseline**:
   ```bash
   # Switch to JDK 17
   export JAVA_HOME=/path/to/jdk17
   
   # Start with GC logging
   java $JVM_OPTS -Xlog:gc*:gc17.log:time,uptime,level,tags \
        -XX:StartFlightRecording=filename=profile17.jfr,dumponexit=true \
        -jar target/app.jar &
   
   # Wait for startup
   sleep 30
   
   # Run performance test
   curl -w "@curl-format.txt" -s -o /dev/null http://localhost:8080/actuator/health
   
   # Capture metrics
   curl -s http://localhost:8080/actuator/metrics/jvm.memory.used > memory-jdk17.json
   curl -s http://localhost:8080/actuator/metrics/jvm.gc.pause > gc-jdk17.json
   ```

3. **JDK 21 Comparison**:
   ```bash
   # Switch to JDK 21
   export JAVA_HOME=/path/to/jdk21
   
   # Start with same configuration
   java $JVM_OPTS -Xlog:gc*:gc21.log:time,uptime,level,tags \
        -XX:StartFlightRecording=filename=profile21.jfr,dumponexit=true \
        -jar target/app.jar &
   
   # Wait for startup
   sleep 30
   
   # Run same performance test
   curl -w "@curl-format.txt" -s -o /dev/null http://localhost:8080/actuator/health
   
   # Capture metrics
   curl -s http://localhost:8080/actuator/metrics/jvm.memory.used > memory-jdk21.json
   curl -s http://localhost:8080/actuator/metrics/jvm.gc.pause > gc-jdk21.json
   ```

4. **Analysis and Comparison**:
   ```bash
   # Compare GC logs
   grep "GC(" gc17.log | wc -l > gc-count-17.txt
   grep "GC(" gc21.log | wc -l > gc-count-21.txt
   
   # Generate comparison report
   echo "# Performance Comparison JDK 17 vs JDK 21" > performance-comparison.md
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually start application on each JDK version
2. Use JConsole or VisualVM for basic metrics collection
3. Record startup times and memory usage manually
4. Document findings in comparison report

## Verification Commands
```bash
# Verify performance artifacts exist
ls -la gc17.log gc21.log profile17.jfr profile21.jfr

# Check comparison report created
test -f performance-comparison.md && echo "PASS: Comparison report exists" || echo "FAIL: Report missing"

# Validate metrics captured
test -f memory-jdk17.json && test -f memory-jdk21.json && echo "PASS: Memory metrics captured"

# Check GC log analysis
wc -l gc17.log gc21.log
```

## Issue Detection & Remediation

### GC Pause Time Regression (Severity: medium)
**Detection Pattern**: Increased GC pause times in JDK 21 vs JDK 17
**Remediation**:
1. Analyze GC logs for pause time patterns
2. Consider different GC algorithms (G1, ZGC, Shenandoah)
3. Tune GC parameters for JDK 21
**Validation**: GC pause times within acceptable range

### Memory Usage Increase (Severity: medium)
**Detection Pattern**: Higher heap usage or allocation rate on JDK 21
**Remediation**:
1. Analyze heap dumps for memory usage patterns
2. Check for memory leaks or increased object allocation
3. Tune heap sizing parameters
**Validation**: Memory usage comparable or improved vs JDK 17

### Startup Time Regression (Severity: low)
**Detection Pattern**: Slower application startup on JDK 21
**Remediation**:
1. Analyze startup sequence and class loading
2. Consider JVM warmup optimizations
3. Check for initialization bottlenecks
**Validation**: Startup time within 15% of JDK 17 baseline

### Throughput Degradation (Severity: high)
**Detection Pattern**: Reduced request throughput on JDK 21
**Remediation**:
1. Profile application under load to identify bottlenecks
2. Check for JIT compilation differences
3. Analyze thread contention and synchronization
**Validation**: Throughput maintained or improved vs JDK 17

## Issue Collection
**Only collect issues if significant regressions detected**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `performance-and-gc-profiling-<YYYYMMDD-HHmm>.json`
- **Categories**: latency, throughput, memory, gc, cpu, startup
- **Status**: OPEN (regression needs investigation), RESOLVED (acceptable performance), DEFERRED (minor regressions)

## Success Criteria
- ✅ Performance comparison report created with JDK 17 vs JDK 21 metrics
- ✅ GC logs captured and analyzed for both JDK versions
- ✅ No HIGH severity performance regressions detected
- ✅ Memory usage and startup times within acceptable ranges
- ✅ Performance artifacts stored in findings directory
