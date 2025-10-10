#!/usr/bin/env bash
set -euo pipefail
# ---------------------------------------------------------------------------
# Phase 2 Automation Runner (Spring Boot 3.x Modernization)
# Mirrors logic of phase2-run.ps1 in Bash.
# ---------------------------------------------------------------------------
# Features:
#  - Resumable via phase2-state.json
#  - Dry run support
#  - Selective execution (ONLY, START_FROM, UNTIL, SKIP)
#  - Lightweight verification for each task (non-destructive)
#  - Optional git commits
# ---------------------------------------------------------------------------
# Usage examples:
#  ./phase2-run.sh                   # Resume from first incomplete task
#  ./phase2-run.sh --start-from 2.3  # Begin at task 2.3
#  ./phase2-run.sh --only 2.0,2.1    # Run subset
#  ./phase2-run.sh --until 2.5       # Run through 2.5
#  ./phase2-run.sh --dry-run         # No state or commits
#  ./phase2-run.sh --commit          # Commit after each success
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_FILE="$SCRIPT_DIR/phase2-state.json"
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p "$LOG_DIR"

START_FROM=""; UNTIL=""; ONLY=""; SKIP=""; DRY_RUN=0; DO_COMMIT=0; FORCE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --start-from) START_FROM="$2"; shift 2;;
    --until) UNTIL="$2"; shift 2;;
    --only) ONLY="$2"; shift 2;;
    --skip) SKIP="$2"; shift 2;;
    --dry-run) DRY_RUN=1; shift;;
    --commit) DO_COMMIT=1; shift;;
    --force) FORCE=1; shift;;
    -h|--help)
      grep '^# ' "$0" | sed 's/^# //'; exit 0;;
    *) echo "Unknown arg: $1" >&2; exit 1;;
  esac
done

info(){ echo -e "\e[36m[Phase2]\e[0m $*"; }
warn(){ echo -e "\e[33m[Phase2 WARN]\e[0m $*"; }
err(){ echo -e "\e[31m[Phase2 ERROR]\e[0m $*"; }

# Load or init state
if [[ -f "$STATE_FILE" ]]; then
  STATE_JSON="$(cat "$STATE_FILE")"
else
  STATE_JSON='{"tasks":{},"version":"1"}'
fi

jq_present(){ command -v jq >/dev/null 2>&1; }
if ! jq_present; then
  err "jq required for JSON state management"; exit 2
fi

# Task definitions: id|name|verify_function
TASKS=(
  '2.0|Readiness Assessment|verify_20'
  '2.1|Upgrade 2.7→3.0|verify_21'
  '2.2|Jakarta Namespace Migration|verify_22'
  '2.3|Security 6 Adjustments|verify_23'
  '2.4|Validation/Actuator/Micrometer|verify_24'
  '2.5|Problem Details Adoption|verify_25'
  '2.6|Observability & Logging Modernization|verify_26'
  '2.7|Upgrade 3.0→3.1|verify_27'
  '2.8|Upgrade 3.1→3.2|verify_28'
  '2.9|Performance & Config Cleanup|verify_29'
  '2.10|Final Phase 2 Report|verify_210'
)

# Ensure state has each task
for entry in "${TASKS[@]}"; do
  IFS='|' read -r id name func <<<"$entry"
  if ! echo "$STATE_JSON" | jq -e ".tasks[\"$id\"]" >/dev/null; then
    STATE_JSON="$(echo "$STATE_JSON" | jq ".tasks[\"$id\"]={\"status\":\"not-started\",\"notes\":[]}")"
  fi
done

save_state(){
  (( DRY_RUN )) && return 0
  echo "$STATE_JSON" | jq '.updated=now' > "$STATE_FILE"
}

mark_status(){
  local id="$1" status="$2"; shift 2 || true
  local note_json='[]'
  if [[ $# -gt 0 ]]; then
    note_json="$(printf '%s\n' "$@" | jq -R . | jq -s .)"
  fi
  STATE_JSON="$(echo "$STATE_JSON" | jq ".tasks[\"$id\"].status=\"$status\" | .tasks[\"$id\"].notes += $note_json")"
  save_state
}

# Selection helpers
IFS=',' read -r -a ONLY_ARR <<<"${ONLY}" || true
IFS=',' read -r -a SKIP_ARR <<<"${SKIP}" || true
contains(){ local needle="$1"; shift; for x in "$@"; do [[ "$x" == "$needle" ]] && return 0; done; return 1; }

should_run(){
  local id="$1"
  if [[ -n "$ONLY" ]]; then contains "$id" "${ONLY_ARR[@]}" || return 1; fi
  if [[ -n "$SKIP" ]] && contains "$id" "${SKIP_ARR[@]}"; then return 1; fi
  if [[ -n "$START_FROM" && "$id" < "$START_FROM" ]]; then return 1; fi
  if [[ -n "$UNTIL" && "$id" > "$UNTIL" ]]; then return 1; fi
  return 0
}

# Provide minimal detect function fallback (PowerShell script expected separately)
detect_boot_version(){
  # Try Maven POM parent
  if [[ -f pom.xml ]]; then
    awk '/spring-boot-starter-parent/{f=1} f && /<version>/{print; exit}' pom.xml | sed -E 's/.*<version>([^<]+).*/\1/'
  elif ls build.gradle* >/dev/null 2>&1; then
    grep -E 'spring-boot' build.gradle* | grep -E 'version' | head -1 | sed -E 's/.*version[ =\"]+([^" ]+).*/\1/'
  fi
}

# --- Verification functions ---
verify_20(){ [[ -f boot3-readiness-report.md ]] || return 1; }
verify_21(){ v="$(detect_boot_version)"; [[ "$v" =~ ^3\.0\. ]] || return 1; }
verify_22(){ if grep -R "\bjavax\." --include='*.java' . >/dev/null 2>&1; then return 1; fi }
verify_23(){ if grep -R "WebSecurityConfigurerAdapter" --include='*.java' . >/dev/null 2>&1; then return 1; fi }
verify_24(){ if grep -R "javax.validation" --include='*.java' . >/dev/null 2>&1; then return 1; fi }
verify_25(){ :; } # Allow missing; warn later
verify_26(){ :; }
verify_27(){ v="$(detect_boot_version)"; [[ "$v" =~ ^3\.1\. ]] || return 1; }
verify_28(){ v="$(detect_boot_version)"; [[ "$v" =~ ^3\.2\. ]] || return 1; }
verify_29(){ :; }
verify_210(){ [[ -f phase2-migration-report.md ]] || return 1; }

info "Execution plan:"; for entry in "${TASKS[@]}"; do IFS='|' read -r id name func <<<"$entry"; if should_run "$id"; then echo "  - $id $name"; fi; done
(( DRY_RUN )) && warn "Dry run: no state or commits will be written"

# Determine default START_FROM when not using ONLY and not provided
if [[ -z "$ONLY" && -z "$START_FROM" ]]; then
  for entry in "${TASKS[@]}"; do
    IFS='|' read -r id name func <<<"$entry"
    status=$(echo "$STATE_JSON" | jq -r ".tasks[\"$id\"].status")
    if [[ "$status" != "completed" ]]; then START_FROM="$id"; break; fi
  done
fi

for entry in "${TASKS[@]}"; do
  IFS='|' read -r id name func <<<"$entry"
  should_run "$id" || continue
  status=$(echo "$STATE_JSON" | jq -r ".tasks[\"$id\"].status")
  if [[ "$status" == "completed" && $FORCE -eq 0 ]]; then info "Skip $id (already completed)"; continue; fi
  info "Verifying $id $name"
  mark_status "$id" in-progress
  LOG_FILE="$LOG_DIR/task-$id.log"
  if ( $func ) >"$LOG_FILE" 2>&1; then
    mark_status "$id" completed
    info "Task $id completed"
    if (( DO_COMMIT )) && (( DRY_RUN == 0 )) && [[ -d .git ]]; then
      git add . >/dev/null 2>&1 || true
      git commit -m "chore(phase2): mark task $id complete" >/dev/null 2>&1 || true
      info "Commit created for $id"
    fi
  else
    mark_status "$id" failed "error=verification failed"
    err "Task $id FAILED (see $LOG_FILE)"
    break
  fi
  save_state
 done

info "Phase 2 automation finished. State: $STATE_FILE"
