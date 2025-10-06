#!/bin/bash
#
# Benchmark Setup Script
# Prepares environment for running AI agent benchmarks
#

set -euo pipefail

# Configuration
BENCHMARK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_REPOS_DIR="${BENCHMARK_DIR}/test-repositories"
RESULTS_DIR="${BENCHMARK_DIR}/results"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
RUN_ID="benchmark-${TIMESTAMP}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Parse command line arguments
LANGUAGE=""
REPO_SIZE=""
AGENT_NAME=""
MODEL_NAME=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -l|--language)
            LANGUAGE="$2"
            shift 2
            ;;
        -s|--size)
            REPO_SIZE="$2"
            shift 2
            ;;
        -a|--agent)
            AGENT_NAME="$2"
            shift 2
            ;;
        -m|--model)
            MODEL_NAME="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo "Options:"
            echo "  -l, --language LANG    Language (java|csharp|cpp|python)"
            echo "  -s, --size SIZE        Repository size (small|medium|large)"
            echo "  -a, --agent NAME       Agent name (copilot|cursor|aider|etc)"
            echo "  -m, --model MODEL      Model name (gpt-4|claude-sonnet|etc)"
            echo "  -h, --help             Show this help message"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate required parameters
if [[ -z "$LANGUAGE" ]] || [[ -z "$REPO_SIZE" ]] || [[ -z "$AGENT_NAME" ]]; then
    log_error "Missing required parameters"
    echo "Usage: $0 -l LANGUAGE -s SIZE -a AGENT [-m MODEL]"
    exit 1
fi

# Validate language
case $LANGUAGE in
    java|csharp|cpp|python)
        ;;
    *)
        log_error "Invalid language: $LANGUAGE"
        log_error "Must be one of: java, csharp, cpp, python"
        exit 1
        ;;
esac

# Validate size
case $REPO_SIZE in
    small|medium|large)
        ;;
    *)
        log_error "Invalid size: $REPO_SIZE"
        log_error "Must be one of: small, medium, large"
        exit 1
        ;;
esac

log_info "Setting up benchmark environment"
log_info "Language: $LANGUAGE"
log_info "Size: $REPO_SIZE"
log_info "Agent: $AGENT_NAME"
log_info "Model: ${MODEL_NAME:-N/A}"
log_info "Run ID: $RUN_ID"

# Create results directory
RUN_DIR="${RESULTS_DIR}/${RUN_ID}"
mkdir -p "$RUN_DIR"
log_info "Created results directory: $RUN_DIR"

# Find test repository
REPO_PATH="${TEST_REPOS_DIR}/${LANGUAGE}/${REPO_SIZE}"
if [[ ! -d "$REPO_PATH" ]]; then
    log_error "Test repository not found: $REPO_PATH"
    exit 1
fi

log_info "Found test repository: $REPO_PATH"

# Copy repository to run directory
WORKSPACE_DIR="${RUN_DIR}/workspace"
log_info "Copying repository to workspace..."
cp -r "$REPO_PATH" "$WORKSPACE_DIR"

# Load baseline metrics
BASELINE_FILE="${REPO_PATH}/baseline-metrics.json"
if [[ -f "$BASELINE_FILE" ]]; then
    cp "$BASELINE_FILE" "${RUN_DIR}/baseline-metrics.json"
    log_info "Loaded baseline metrics"
else
    log_warn "Baseline metrics not found"
fi

# Create session info file
cat > "${RUN_DIR}/session-info.json" <<EOF
{
  "run_id": "$RUN_ID",
  "timestamp": "$TIMESTAMP",
  "language": "$LANGUAGE",
  "repository_size": "$REPO_SIZE",
  "agent": "$AGENT_NAME",
  "model": "${MODEL_NAME:-""}",
  "repository_path": "$REPO_PATH",
  "workspace_path": "$WORKSPACE_DIR",
  "status": "initialized"
}
EOF

log_info "Created session info file"

# Create task tracking file
cat > "${RUN_DIR}/tasks.json" <<EOF
{
  "tasks": [
    {
      "id": "task1",
      "name": "Repository Comprehension & Documentation Suite",
      "status": "pending",
      "start_time": null,
      "end_time": null,
      "duration_seconds": null,
      "score": null,
      "interventions": []
    },
    {
      "id": "task2",
      "name": "Build & Test Infrastructure Automation",
      "status": "pending",
      "start_time": null,
      "end_time": null,
      "duration_seconds": null,
      "score": null,
      "interventions": []
    },
    {
      "id": "task3",
      "name": "Test Coverage Enhancement & Quality Improvement",
      "status": "pending",
      "start_time": null,
      "end_time": null,
      "duration_seconds": null,
      "score": null,
      "interventions": []
    },
    {
      "id": "task4",
      "name": "Language-Specific Refactoring Challenge",
      "status": "pending",
      "start_time": null,
      "end_time": null,
      "duration_seconds": null,
      "score": null,
      "interventions": []
    },
    {
      "id": "task5",
      "name": "Advanced Multi-Objective Improvement",
      "status": "pending",
      "start_time": null,
      "end_time": null,
      "duration_seconds": null,
      "score": null,
      "interventions": []
    }
  ]
}
EOF

log_info "Created task tracking file"

# Install language-specific tools
log_info "Checking language-specific tools..."

case $LANGUAGE in
    java)
        command -v java >/dev/null 2>&1 || log_warn "Java not found"
        command -v mvn >/dev/null 2>&1 || log_warn "Maven not found"
        command -v gradle >/dev/null 2>&1 || log_warn "Gradle not found"
        ;;
    csharp)
        command -v dotnet >/dev/null 2>&1 || log_warn "dotnet CLI not found"
        ;;
    cpp)
        command -v cmake >/dev/null 2>&1 || log_warn "CMake not found"
        command -v g++ >/dev/null 2>&1 || log_warn "g++ not found"
        ;;
    python)
        command -v python3 >/dev/null 2>&1 || log_warn "Python3 not found"
        command -v pip3 >/dev/null 2>&1 || log_warn "pip3 not found"
        ;;
esac

# Create task instruction files
log_info "Creating task instruction files..."

cat > "${RUN_DIR}/task1-instructions.md" <<'EOF'
# Task 1: Repository Comprehension & Documentation Suite

## Objective
Analyze this codebase and create comprehensive documentation.

## Time Budget
60 minutes

## Required Deliverables
1. FUNCTIONALITY.md
2. ARCHITECTURE.md
3. BUILD.md
4. TESTING.md
5. DEVELOPMENT.md

See benchmarks/REAL-BENCHMARK.md for detailed requirements.

## Starting Point
Repository location: workspace/

## Success Criteria
- All 5 documents created
- All required sections present
- Information accurate and verified
- Clear and useful to new developers
EOF

# (Similar task files for task2-5 would be created here)

# Create README for the run
cat > "${RUN_DIR}/README.md" <<EOF
# Benchmark Run: $RUN_ID

**Date**: $(date +%Y-%m-%d)  
**Time**: $(date +%H:%M:%S)  
**Language**: $LANGUAGE  
**Repository Size**: $REPO_SIZE  
**Agent**: $AGENT_NAME  
**Model**: ${MODEL_NAME:-N/A}

## Directory Structure

\`\`\`
${RUN_ID}/
├── workspace/              # Working directory (copy of test repo)
├── session-info.json       # Session metadata
├── tasks.json              # Task tracking
├── baseline-metrics.json   # Pre-benchmark metrics
├── task*-instructions.md   # Task instructions
└── results/                # Task results will go here
\`\`\`

## Instructions

1. Navigate to the workspace directory
2. Read task1-instructions.md
3. Begin benchmark with: benchmark-start.sh task1
4. When complete: benchmark-end.sh task1
5. Repeat for each task

## Monitoring

Monitor progress with: benchmark-status.sh

## Scoring

After completion: benchmark-score.sh
EOF

log_info "Created run README"

# Print summary
echo ""
log_info "========================================="
log_info "Benchmark environment ready!"
log_info "========================================="
echo ""
log_info "Run Directory: $RUN_DIR"
log_info "Workspace: $WORKSPACE_DIR"
echo ""
log_info "Next steps:"
log_info "  1. cd $WORKSPACE_DIR"
log_info "  2. Read ../task1-instructions.md"
log_info "  3. Run: ../../../scripts/benchmark-start.sh task1"
log_info "  4. Begin Task 1"
echo ""

# Create convenience script
cat > "${RUN_DIR}/start-task.sh" <<EOF
#!/bin/bash
cd "${WORKSPACE_DIR}"
"${BENCHMARK_DIR}/scripts/benchmark-start.sh" "\$@"
EOF
chmod +x "${RUN_DIR}/start-task.sh"

cat > "${RUN_DIR}/end-task.sh" <<EOF
#!/bin/bash
cd "${WORKSPACE_DIR}"
"${BENCHMARK_DIR}/scripts/benchmark-end.sh" "\$@"
EOF
chmod +x "${RUN_DIR}/end-task.sh"

log_info "Created convenience scripts"
log_info "Setup complete!"