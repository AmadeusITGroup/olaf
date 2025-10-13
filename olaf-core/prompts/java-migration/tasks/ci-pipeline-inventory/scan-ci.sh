#!/usr/bin/env bash
set -euo pipefail
PATH_TO_SCAN="${1:-.}"
OUTPUT_FILE="${OUTPUT:-ci-inventory.jsonl}"
: > "$OUTPUT_FILE"

patterns='actions_java|java-version:[[:space:]]*11
docker_base|^FROM .*11
release_flag|--release[[:space:]]+11
maven_compiler|<release>11</release>
gradle_sourceCompat|sourceCompatibility[[:space:]]*=[[:space:]]*11
toolchain_xml|<version>11</version>
env_var|JAVA_VERSION=11'

# Convert patterns into loop
while IFS='|' read -r category regex; do
  if [[ -z "$category" || -z "$regex" ]]; then continue; fi
  grep -RIn --exclude-dir .git -E "$regex" "$PATH_TO_SCAN" 2>/dev/null | while IFS=: read -r file line match; do
    printf '{"file":"%s","line":%s,"category":"%s","match":"%s"}' "${file}" "${line}" "${category}" "$(echo "$match" | sed 's/"/\\"/g')" >> "$OUTPUT_FILE"
    echo >> "$OUTPUT_FILE"
  done
done <<< "$patterns"

echo "Inventory written to $OUTPUT_FILE"
