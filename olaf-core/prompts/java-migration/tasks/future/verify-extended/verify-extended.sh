#!/usr/bin/env bash
set +e
JSON=false
if [[ "$1" == "-j" || "$1" == "--json" ]]; then JSON=true; fi

RESULT_TS=$(date -Iseconds)
JDK_DIR="/mnt/c/migration-toolkit/jdk"
if [[ ! -d "$JDK_DIR" ]]; then JDK_DIR="/opt/migration-toolkit/jdk"; fi

mand_ok=()
mand_fail=()

have(){ command -v "$1" >/dev/null 2>&1; }
add_result(){ # cat tool status details
  local cat="$1"; local tool="$2"; local status="$3"; shift 3; local details="$*"
  if $JSON; then
    printf '%s\t%s\t%s\t%s\n' "$cat" "$tool" "$status" "$details" >> "$TMP_TAB"
  else
    printf '  %-12s %-7s %s\n' "$tool" "$status" "$details"
  fi
  if [[ "$cat" == "mandatory" ]]; then
    if [[ "$status" == ok ]]; then mand_ok+=("$tool") else mand_fail+=("$tool") fi
  fi
}

TMP_TAB=$(mktemp)
trap 'rm -f "$TMP_TAB"' EXIT

echo "=== Extended Toolkit Verification (Task 0.3) ==="

echo "Mandatory:"
# git
if have git; then add_result mandatory git ok "$(git --version)"; else add_result mandatory git missing "git not found"; fi

# java dirs
present=()
for v in 11 17 21; do [[ -d "$JDK_DIR/$v" ]] && present+=("$v"); done
java_line=$(java -version 2>&1 | head -1)
if [[ ${#present[@]} -ge 2 ]]; then add_result mandatory java ok "present=${present[*]} default=$java_line"; else add_result mandatory java warn "present=${present[*]} default=$java_line"; fi

# maven
if have mvn; then
  mvn_line=$(mvn --version 2>&1 | head -1)
  if [[ $mvn_line =~ Apache\ Maven\ ([0-9]+)\.([0-9]+)\.([0-9]+) ]]; then
    maj=${BASH_REMATCH[1]}; min=${BASH_REMATCH[2]}; pat=${BASH_REMATCH[3]}
    if (( maj>3 || (maj==3 && (min>9 || (min==9 && pat>=5))) )); then add_result mandatory maven ok "$mvn_line"; else add_result mandatory maven fail "$mvn_line (<3.9.5)"; fi
  else add_result mandatory maven fail "parse error"; fi
else add_result mandatory maven missing "mvn not found"; fi

# python
if have python; then add_result mandatory python ok "$(python --version 2>&1)"; elif have python3; then add_result mandatory python ok "$(python3 --version 2>&1)"; else add_result mandatory python missing "python not found"; fi

# curl
if have curl; then add_result mandatory curl ok "$(curl --version | head -1)"; else add_result mandatory curl missing "curl not found"; fi

# container
if have docker; then add_result mandatory container ok "$(docker --version)"; elif have podman; then add_result mandatory container ok "$(podman --version)"; else add_result mandatory container missing "docker or podman not found"; fi

# appcat
if have appcat; then add_result mandatory appcat ok "$(appcat version 2>&1 | head -1)"; else add_result mandatory appcat missing "appcat CLI not installed"; fi

echo "\nRecommended:"
rec_tools=(gradle jq yq node rewrite kubectl helm)
for t in "${rec_tools[@]}"; do
  if have "$t"; then
    case "$t" in
      gradle) line=$(gradle -v 2>&1 | head -2 | tail -1);;
      jq) line=$(jq --version);;
      yq) line=$(yq --version 2>&1 | head -1);;
      node) line=$(node --version);;
      rewrite) line=$(rewrite --version 2>&1 | head -1);;
      kubectl) line=$(kubectl version --client --short 2>&1 | head -1);;
      helm) line=$(helm version --short 2>&1 | head -1);;
    esac
    add_result recommended "$t" ok "$line"
  else
    add_result recommended "$t" missing "not found"
  fi
done

if $JSON; then
  # Convert tab table to JSON
  # cat tool status details
  awk -F '\t' 'BEGIN{print "{\"timestamp\":\"'$RESULT_TS'\",\"mandatory\":{}}"}' >/dev/null
  # Simpler: just emit lines; (placeholder for future structured JSON)
  echo "JSON mode placeholder"; exit 2
fi

if [[ ${#mand_fail[@]} -eq 0 ]]; then
  echo "\nALL MANDATORY TOOLS OK"; exit 0
else
  echo "\nMISSING / FAIL: ${mand_fail[*]}"; exit 1
fi
