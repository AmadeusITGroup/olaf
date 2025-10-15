#!/bin/bash
# Angular Migration CI Pipeline Scanner
# Scans repository for CI/CD configurations and Node.js/Angular settings

set -e

TIMESTAMP=$(date +%Y%m%d-%H%M)
FINDINGS_DIR="olaf-data/findings/migrations/migration_${TIMESTAMP}/ci"
REPORT_FILE="${FINDINGS_DIR}/ci_inventory.md"
JSON_FILE="${FINDINGS_DIR}/ci_inventory.json"

# Create findings directory
mkdir -p "$FINDINGS_DIR"

echo "=== Angular Migration CI Pipeline Inventory ==="
echo "Timestamp: $TIMESTAMP"
echo "Findings Directory: $FINDINGS_DIR"

# Initialize report
cat > "$REPORT_FILE" << EOF
# CI Pipeline Inventory - Angular Migration

**Generated:** $(date)
**Repository:** $(pwd)
**Scan Type:** Automated

## CI Configuration Files Found

EOF

# Initialize JSON report
echo '{"timestamp": "'$TIMESTAMP'", "repository": "'$(pwd)'", "ci_files": [], "node_configs": [], "angular_configs": [], "issues": []}' > "$JSON_FILE"

# Find CI configuration files
echo "Scanning for CI configuration files..."
CI_FILES=$(find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | grep -E "(\.github|\.gitlab|jenkins|ci)" | head -20)

if [ -n "$CI_FILES" ]; then
    echo "### Found CI Files" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    for file in $CI_FILES; do
        echo "- \`$file\`" >> "$REPORT_FILE"
        
        # Add to JSON
        jq --arg file "$file" '.ci_files += [$file]' "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"
        
        echo "  Analyzing: $file"
        
        # Check for Node.js configurations
        if grep -q "node\|NODE" "$file" 2>/dev/null; then
            echo "  - Contains Node.js configuration" >> "$REPORT_FILE"
            
            # Extract Node.js versions
            NODE_VERSIONS=$(grep -E "node.*version|NODE_VERSION" "$file" 2>/dev/null | head -5)
            if [ -n "$NODE_VERSIONS" ]; then
                echo "  - Node.js versions found:" >> "$REPORT_FILE"
                echo "$NODE_VERSIONS" | sed 's/^/    /' >> "$REPORT_FILE"
            fi
        fi
        
        # Check for Angular configurations
        if grep -q "angular\|@angular\|ng " "$file" 2>/dev/null; then
            echo "  - Contains Angular configuration" >> "$REPORT_FILE"
            
            # Extract Angular CLI usage
            ANGULAR_USAGE=$(grep -E "ng |@angular|angular" "$file" 2>/dev/null | head -5)
            if [ -n "$ANGULAR_USAGE" ]; then
                echo "  - Angular usage found:" >> "$REPORT_FILE"
                echo "$ANGULAR_USAGE" | sed 's/^/    /' >> "$REPORT_FILE"
            fi
        fi
        
        echo "" >> "$REPORT_FILE"
    done
else
    echo "### No CI Files Found" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "No CI configuration files detected in standard locations." >> "$REPORT_FILE"
fi

# Scan for hardcoded Node.js versions
echo "" >> "$REPORT_FILE"
echo "## Issue Detection" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Scanning for hardcoded Node.js versions..."
HARDCODED_NODE=$(find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | xargs grep -l "NODE_VERSION.*=" 2>/dev/null | head -10)

if [ -n "$HARDCODED_NODE" ]; then
    echo "### ❌ Hardcoded Node.js Versions (High Severity)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    for file in $HARDCODED_NODE; do
        echo "**File:** \`$file\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        grep -n "NODE_VERSION.*=" "$file" 2>/dev/null | head -3 >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        
        # Add to JSON issues
        jq --arg file "$file" --arg type "hardcoded-node-version" '.issues += [{"file": $file, "type": $type, "severity": "high"}]' "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"
    done
else
    echo "### ✅ No Hardcoded Node.js Versions Found" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
fi

# Scan for outdated Angular CLI references
echo "Scanning for outdated Angular CLI references..."
OUTDATED_CLI=$(find . -name "*.yml" -o -name "*.yaml" -o -name "Jenkinsfile" | xargs grep -l "@angular/cli@[0-9]" 2>/dev/null | head -10)

if [ -n "$OUTDATED_CLI" ]; then
    echo "### ⚠️ Outdated Angular CLI References (Medium Severity)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    for file in $OUTDATED_CLI; do
        echo "**File:** \`$file\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        grep -n "@angular/cli@" "$file" 2>/dev/null | head -3 >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        
        # Add to JSON issues
        jq --arg file "$file" --arg type "outdated-angular-cli" '.issues += [{"file": $file, "type": $type, "severity": "medium"}]' "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"
    done
else
    echo "### ✅ No Outdated Angular CLI References Found" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
fi

# Scan for container image issues
echo "Scanning for container Node.js versions..."
CONTAINER_ISSUES=$(find . -name "Dockerfile*" -o -name "*.yml" -o -name "*.yaml" | xargs grep -l "FROM.*node:[0-9]" 2>/dev/null | head -10)

if [ -n "$CONTAINER_ISSUES" ]; then
    echo "### ⚠️ Container Node.js Versions (Medium Severity)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    for file in $CONTAINER_ISSUES; do
        echo "**File:** \`$file\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        grep -n "FROM.*node:" "$file" 2>/dev/null | head -3 >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
        
        # Add to JSON issues
        jq --arg file "$file" --arg type "container-node-version" '.issues += [{"file": $file, "type": $type, "severity": "medium"}]' "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"
    done
else
    echo "### ✅ No Container Node.js Version Issues Found" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
fi

# Generate summary
echo "" >> "$REPORT_FILE"
echo "## Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

TOTAL_FILES=$(echo "$CI_FILES" | wc -l)
TOTAL_ISSUES=$(jq '.issues | length' "$JSON_FILE")

echo "- **CI Files Scanned:** $TOTAL_FILES" >> "$REPORT_FILE"
echo "- **Issues Found:** $TOTAL_ISSUES" >> "$REPORT_FILE"
echo "- **Report Generated:** $(date)" >> "$REPORT_FILE"

# Add summary to JSON
jq --arg total_files "$TOTAL_FILES" --arg total_issues "$TOTAL_ISSUES" '.summary = {"total_files": $total_files, "total_issues": $total_issues}' "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"

echo ""
echo "=== Scan Complete ==="
echo "Report: $REPORT_FILE"
echo "JSON: $JSON_FILE"
echo "Issues found: $TOTAL_ISSUES"

# Exit with error code if high severity issues found
HIGH_SEVERITY=$(jq '.issues[] | select(.severity == "high") | length' "$JSON_FILE" | wc -l)
if [ "$HIGH_SEVERITY" -gt 0 ]; then
    echo "⚠️ High severity issues found. Review required."
    exit 1
fi

echo "✅ CI pipeline inventory complete"