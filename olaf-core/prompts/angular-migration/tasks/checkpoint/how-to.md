# Migration Checkpoint — Angular Migration

## Goal
Validate that all phase tasks are completed successfully and exit criteria are met before proceeding to the next phase.

## Checkpoint Process

### 1. Task Completion Verification
```bash
# Check all tasks in current phase are marked complete
grep -c "\- \[x\]" migration-plan.md
grep -c "\- \[ \]" migration-plan.md

# Verify no pending tasks remain
echo "Completed tasks: $(grep -c '\- \[x\]' migration-plan.md)"
echo "Pending tasks: $(grep -c '\- \[ \]' migration-plan.md)"
```

### 2. Build Verification
```bash
# Verify production build works
ng build --configuration=production --verbose

# Check for build warnings
ng build --configuration=production 2>&1 | grep -i "warning" || echo "No build warnings"

# Verify development build works
ng build --configuration=development
```

### 3. Test Suite Validation
```bash
# Run unit tests
ng test --watch=false --code-coverage --browsers=ChromeHeadless

# Run e2e tests (if available)
ng e2e || echo "No e2e tests configured"

# Check test coverage
echo "Test coverage report generated in coverage/ directory"
```

### 4. Application Functionality Check
```bash
# Start development server for manual testing
ng serve --port 4200 &
SERVER_PID=$!

# Wait for server to start
sleep 10

# Basic health check
curl -f http://localhost:4200 > /dev/null && echo "Application accessible" || echo "Application not accessible"

# Stop development server
kill $SERVER_PID
```

## Phase-Specific Exit Criteria

### Phase 1 Exit Criteria
- [ ] Angular core updated to target version
- [ ] TypeScript updated to compatible version
- [ ] Angular CLI updated to target version
- [ ] All dependencies compatible and installed
- [ ] Production build successful
- [ ] All unit tests passing
- [ ] No critical compilation errors
- [ ] Application starts and loads correctly

### Phase 2 Exit Criteria
- [ ] All deprecated APIs updated
- [ ] Component templates modernized
- [ ] Services and dependency injection updated
- [ ] Routing configuration updated
- [ ] Forms migrated (if applicable)
- [ ] HTTP client updated
- [ ] Testing framework updated
- [ ] All integration tests passing
- [ ] No runtime errors in basic functionality

### Phase 3 Exit Criteria
- [ ] Modern features adopted (standalone components, signals, etc.)
- [ ] Bundle size optimized
- [ ] Performance benchmarks met
- [ ] Accessibility compliance verified
- [ ] Modern tooling integrated (if applicable)
- [ ] All tests passing
- [ ] Production deployment ready
- [ ] Documentation updated

## Automated Checkpoint Validation

### Build and Test Validation
```bash
#!/bin/bash
# checkpoint-validation.sh

echo "=== Angular Migration Checkpoint Validation ==="

# Check Angular version
echo "Current Angular version:"
ng version | grep "Angular CLI\|Angular:"

# Build validation
echo "Building production..."
if ng build --configuration=production; then
    echo "✅ Production build successful"
else
    echo "❌ Production build failed"
    exit 1
fi

# Test validation
echo "Running tests..."
if ng test --watch=false --browsers=ChromeHeadless; then
    echo "✅ Tests passed"
else
    echo "❌ Tests failed"
    exit 1
fi

# Bundle size check
echo "Checking bundle size..."
BUNDLE_SIZE=$(du -sh dist/ | cut -f1)
echo "Bundle size: $BUNDLE_SIZE"

# Dependency check
echo "Checking dependencies..."
if npm audit --audit-level=high; then
    echo "✅ No high-severity vulnerabilities"
else
    echo "⚠️ High-severity vulnerabilities found"
fi

echo "=== Checkpoint validation complete ==="
```

### Performance Validation
```bash
#!/bin/bash
# performance-checkpoint.sh

echo "=== Performance Checkpoint ==="

# Build with stats
ng build --configuration=production --stats-json

# Check main bundle size
MAIN_SIZE=$(cat dist/stats.json | jq '.assets[] | select(.name | contains("main")) | .size')
echo "Main bundle size: $MAIN_SIZE bytes"

# Check if bundle size is within acceptable limits
MAX_BUNDLE_SIZE=2000000  # 2MB
if [ "$MAIN_SIZE" -lt "$MAX_BUNDLE_SIZE" ]; then
    echo "✅ Bundle size within limits"
else
    echo "⚠️ Bundle size exceeds $MAX_BUNDLE_SIZE bytes"
fi

# Check for lazy loading
LAZY_CHUNKS=$(cat dist/stats.json | jq '.chunks[] | select(.initial == false) | length')
echo "Lazy-loaded chunks: $LAZY_CHUNKS"

echo "=== Performance checkpoint complete ==="
```

## Issue Detection & Resolution

### Build Failures (Severity: critical)
**Detection**: `ng build` command fails
**Resolution**:
1. Review build error messages
2. Check for missing dependencies
3. Verify TypeScript configuration
4. Fix compilation errors
**Validation**: Build completes successfully

### Test Failures (Severity: high)
**Detection**: Test suite has failing tests
**Resolution**:
1. Review test failure messages
2. Update test configurations
3. Fix broken test cases
4. Update mock objects and test data
**Validation**: All tests pass

### Runtime Errors (Severity: critical)
**Detection**: Application fails to start or has console errors
**Resolution**:
1. Check browser console for errors
2. Review network requests for failures
3. Fix service injection issues
4. Update component initialization
**Validation**: Application runs without errors

### Performance Regression (Severity: medium)
**Detection**: Bundle size or load time significantly increased
**Resolution**:
1. Analyze bundle composition
2. Check for unnecessary imports
3. Optimize lazy loading
4. Review dependency additions
**Validation**: Performance metrics within acceptable range

## Checkpoint Documentation

### Generate Checkpoint Report
```bash
# Create checkpoint report
cat > checkpoint-report-$(date +%Y%m%d-%H%M).md << EOF
# Migration Checkpoint Report

**Date**: $(date)
**Phase**: Phase X
**Angular Version**: $(ng version | grep "Angular:" | cut -d: -f2)

## Exit Criteria Status
$(grep -E "\- \[.\].*Exit Criteria" migration-plan.md)

## Build Status
- Production Build: $(ng build --configuration=production > /dev/null 2>&1 && echo "✅ Success" || echo "❌ Failed")
- Test Suite: $(ng test --watch=false --browsers=ChromeHeadless > /dev/null 2>&1 && echo "✅ Passed" || echo "❌ Failed")

## Bundle Analysis
- Main Bundle Size: $(du -sh dist/main*.js 2>/dev/null | cut -f1 || echo "N/A")
- Total Bundle Size: $(du -sh dist/ 2>/dev/null | cut -f1 || echo "N/A")

## Next Steps
- [ ] Proceed to next phase
- [ ] Address any remaining issues
- [ ] Update migration plan

EOF
```

## Success Criteria
- ✅ All phase tasks completed and verified
- ✅ Exit criteria met for current phase
- ✅ Build and test validation passed
- ✅ No critical issues remaining
- ✅ Performance within acceptable range
- ✅ Checkpoint report generated
- ✅ Ready to proceed to next phase or complete migration