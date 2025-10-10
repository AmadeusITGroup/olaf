# Performance and GC Profiling — JDK 21

## Preferred approach
1. Establish baseline on JDK 17 (if available) and compare to JDK 21.
2. Collect metrics:
   - Startup time, steady-state memory, P95 latency of key endpoints.
3. Enable basic GC logging:
   - JVM args: `-Xlog:gc*,safepoint:file=gc.log:time,uptime,level,tags`
4. Run a representative load (e.g., `wrk`, `k6`, Gatling) for N minutes.
5. Analyze diffs and note regressions/improvements.

## Backup option
- If no load tool is available, capture manual timings and heap usage via actuator metrics or JFR:
  - JFR start: `-XX:StartFlightRecording=filename=profile.jfr,dumponexit=true`

## Verify
- Report includes: startup, memory, latency (P50/P95), and notable GC observations.
- No severe regressions vs JDK 17 (or prior baseline).
