# OLAF Strands Agent Tools

**Complete AWS Strands SDK Integration for OLAF Framework**

This directory provides a production-ready integration of AWS Strands SDK with the OLAF framework, enabling autonomous AI agents with local execution, background processing, and enterprise-scale concurrency.

---

## 📋 Table of Contents

- [Core Components](#core-components)
- [Quick Start](#quick-start)
- [Execution Modes](#execution-modes)
- [Tool Capabilities](#tool-capabilities)
- [Testing & Validation](#testing--validation)
- [AWS Bedrock Configuration](#aws-bedrock-configuration)
- [Requirements](#requirements)

---

## 🎯 Core Components

### Agent Execution


#### `olaf_strands_agent.py`
**Main OLAF Strands agent implementation**

- **AWS Bedrock Integration**: Native support for Claude models (Sonnet 4.5, Sonnet 4, Opus 4, Haiku 3.5)
- **Autonomous Execution**: Uses `null_callback_handler` for fully autonomous tool execution without user prompts
- **OLAF Memory Map**: Resolves `[id:findings_dir]`, `[id:prompts_dir]`, etc. automatically
- **Timestamp Management**: Proper YYYYMMDD-HHMM format handling for all operations
- **Built-in Tools**:
  - `file_read`, `file_write`, `editor` - File operations
  - `http_request` - Web research with HTML-to-markdown conversion
  - `execute_python_script` - Run Python scripts with arguments
  - `execute_powershell_command` - Execute PowerShell commands
  - `execute_python_code` - Run Python code snippets in REPL
  - `python_repl`, `shell` - Unix execution (when available)
  - `mcp_client` - MCP server connectivity

**Direct Usage**:
```bash
python olaf-core/tools/strands/olaf_strands_agent.py \
  --prompt developer/review-code.md \
  --context "Review the async agent implementation" \
  --aws-profile bedrock \
  --model-name us.anthropic.claude-sonnet-4-20250514-v1:0
```

#### `olaf_strands_wrapper.py`
**Async process manager and orchestrator**

- **Background Spawning**: Launch agents as detached background processes
- **Process Tracking**: Monitor CPU, memory, and execution status
- **Task Management**: Spawn, status check, output retrieval, process listing
- **Dual Modes**: Asynchronous (default) and synchronous (--wait) execution
- **AWS Configuration**: Automatic AWS environment setup with profile management
- **Process Persistence**: Stores process handles in `olaf-data/processes/`

**Key Features**:
- Spawn multiple agents concurrently (tested up to 45+ simultaneous agents)
- Non-blocking execution - spawn and continue immediately
- Status monitoring with resource usage metrics
- Result retrieval when tasks complete
- Automatic timestamp generation and task ID management

#### `olaf_strands_api.py`
**Programmatic Python API**

Simple Python interface for agent management from other scripts or agents.

**API Methods**:
- `spawn_agent()` - Launch background agent
- `check_status()` - Get current status and resource usage
- `get_output()` - Retrieve completed results
- `list_processes()` - List all agent processes
- `wait_for_completion()` - Block until agent finishes

**Example**:
```python
from olaf_strands_api import OLAFStrandsAPI

api = OLAFStrandsAPI()
result = api.spawn_agent(
    prompt="researcher/search-and-learn.md",
    context="Research AWS Strands SDK capabilities"
)
# Returns immediately with task_id
# Check status later: api.check_status(result['task_id'])
```

### Execution Tools

#### `windows_execution_tools.py`
**Windows-compatible execution capabilities**

Three specialized tools for Windows environments:

1. **`execute_python_script`**
   - Runs Python scripts with arguments
   - Working directory support
   - 5-minute timeout protection
   - Returns JSON with stdout, stderr, return code

2. **`execute_powershell_command`**
   - Executes PowerShell commands and scripts
   - Configurable execution policy (default: Bypass)
   - Full stderr/stdout capture
   - Windows system operations support

3. **`execute_python_code`**
   - Runs Python code snippets directly (REPL-style)
   - Temporary file management
   - Ideal for quick calculations and data processing

**Usage Example** (from agent context):
```python
# Agent can execute Python scripts
execute_python_script(
    script_path="olaf-core/tools/generate_dynamic_pptx.py",
    "presentation-plan.json",
    "output.pptx",
    working_directory="olaf-data/findings"
)

# Agent can run PowerShell commands
execute_powershell_command(
    command="Get-Process | Where-Object {$_.CPU -gt 10}",
    working_directory="C:/workspace"
)

# Agent can execute Python code snippets
execute_python_code(
    code="import json; print(json.dumps({'result': 42}))"
)
```

### AWS Configuration

#### `aws_config_manager.py`
**AWS Bedrock configuration and credential management**

- **Profile Management**: Automatic AWS profile setup (default: `bedrock`)
- **Credential Validation**: Tests AWS STS and Bedrock access
- **Model Recommendations**: Curated list of Claude models with inference profiles
- **Cache Clearing**: Prevents stale credential issues
- **Model Availability**: Checks which models are accessible

**Recommended Models**:
- `us.anthropic.claude-sonnet-4-5-20250929-v1:0` - Claude Sonnet 4.5 (latest)
- `us.anthropic.claude-sonnet-4-20250514-v1:0` - Claude Sonnet 4 (default)
- `us.anthropic.claude-opus-4-20250514-v1:0` - Claude Opus 4 (most capable)
- `us.anthropic.claude-3-5-sonnet-20241022-v2:0` - Claude 3.5 Sonnet v2
- `us.anthropic.claude-3-5-haiku-20241022-v1:0` - Claude 3.5 Haiku (fast)

**Usage**:
```python
from aws_config_manager import AWSConfigManager

manager = AWSConfigManager()
config = manager.setup_aws_environment(
    profile="bedrock",
    region="us-east-1",
    model="us.anthropic.claude-sonnet-4-20250514-v1:0"
)
```

#### `check_bedrock_models.py`
**Bedrock model discovery utility**

Lists all available Bedrock models in your AWS account:
- Groups models by provider (Anthropic, Amazon, AI21, etc.)
- Shows model lifecycle status
- Indicates streaming support
- Tests model access permissions

**Usage**:
```bash
python olaf-core/tools/strands/check_bedrock_models.py
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install strands-agents strands-agents-tools boto3 psutil requests beautifulsoup4
```

### 2. Configure AWS Credentials
```bash
# Create or update ~/.aws/credentials
[bedrock]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

# Or use AWS SSO
aws sso login --profile bedrock
```

### 3. Run Your First Agent
```bash
# Spawn agent in background
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --prompt researcher/search-and-learn.md \
  --context "Learning objective: AWS Strands SDK capabilities"

# Output: Task ID: 20250101-1430-search-and-learn

# Check status
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --status --task-id 20250101-1430-search-and-learn

# Get results
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --get-output --task-id 20250101-1430-search-and-learn
```

---

## 🔄 Execution Modes

### Asynchronous Mode (Default - Recommended)

**Spawn and continue immediately**:
```bash
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --prompt technical-writer/create-presentation-plan.md \
  --context "Topic: AWS Lambda, Audience: Developers, Duration: 15 minutes"
```

**Benefits**:
- Non-blocking execution
- Spawn multiple agents concurrently
- Monitor progress independently
- Retrieve results when ready

### Synchronous Mode (Wait for Completion)

**Block until completion**:
```bash
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --wait \
  --prompt developer/review-code.md \
  --context "Review the Strands integration code"
```

**Use Cases**:
- Simple scripts where blocking is acceptable
- Debugging and testing
- Sequential workflows

### Programmatic API Mode

**From Python code**:
```python
from olaf_strands_api import OLAFStrandsAPI

api = OLAFStrandsAPI()

# Spawn multiple agents
tasks = []
for prompt in ["researcher/search-and-learn.md", "developer/review-code.md"]:
    result = api.spawn_agent(prompt=prompt, context="Batch analysis")
    tasks.append(result['task_id'])

# Monitor all tasks
for task_id in tasks:
    status = api.check_status(task_id)
    print(f"{task_id}: {status['status']}")

# Wait for specific task
final = api.wait_for_completion(tasks[0], max_wait=300)
```

---

## 🛠️ Tool Capabilities

### File Operations
- **Read files**: Pattern search, statistics, full content
- **Write files**: Create, append, overwrite
- **Advanced editing**: Syntax highlighting, find/replace

### Code Execution
- **Python scripts**: Execute with arguments, working directory support
- **Python REPL**: Run code snippets directly
- **PowerShell**: Windows system commands and scripts
- **Shell**: Unix/Linux commands (when available)

### Web Research
- **HTTP requests**: GET/POST with headers
- **HTML to Markdown**: Automatic conversion for readability
- **Web scraping**: Extract and process web content

### System Integration
- **MCP servers**: Connect to Model Context Protocol servers
- **Process management**: Background execution and monitoring
- **Resource tracking**: CPU, memory usage monitoring

---

## 🧪 Testing & Validation

### Basic Spawn Test
```bash
python olaf-core/tools/strands/demo_full_async_workflow.py
```
Demonstrates complete workflow: spawn → monitor → retrieve results

### Concurrent Agent Test (5 agents)
```bash
python olaf-core/tools/strands/test_concurrent_agents.py
```
Tests system handling of 5 simultaneous agents with progress monitoring

### Stress Test (45+ agents)
```bash
python olaf-core/tools/strands/stress_test_agents.py
```
High-volume test with three batches:
- **Batch A**: 10 agents (moderate load)
- **Batch B**: 15 agents (high load)
- **Batch C**: 20 agents (stress load)

**Expected Results**:
- 40+ successful spawns = Excellent (production-ready)
- 25-40 successful spawns = Good (handles concurrent loads well)
- 15-25 successful spawns = Fair (adequate for moderate loads)

### Windows Tools Test
```bash
python olaf-core/tools/strands/test_windows_tools.py
```
Validates Python script, PowerShell, and Python code execution tools

---

## ⚙️ AWS Bedrock Configuration

### Profile Setup

The system uses the `bedrock` AWS profile by default:

```bash
# Option 1: Configure credentials file
cat ~/.aws/credentials
[bedrock]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET

# Option 2: Use AWS SSO
aws configure sso --profile bedrock

# Option 3: Use environment variables
export AWS_PROFILE=bedrock
export AWS_REGION=us-east-1
```

### Model Selection

**Default Model**: `us.anthropic.claude-sonnet-4-20250514-v1:0` (Claude Sonnet 4)

**Override Model**:
```bash
python olaf_strands_wrapper.py \
  --prompt your-prompt.md \
  --model us.anthropic.claude-sonnet-4-5-20250929-v1:0  # Claude Sonnet 4.5
```

**Available Models** (via inference profiles):
- Claude Sonnet 4.5: `us.anthropic.claude-sonnet-4-5-20250929-v1:0`
- Claude Sonnet 4: `us.anthropic.claude-sonnet-4-20250514-v1:0`
- Claude Opus 4: `us.anthropic.claude-opus-4-20250514-v1:0`
- Claude 3.5 Sonnet v2: `us.anthropic.claude-3-5-sonnet-20241022-v2:0`
- Claude 3.5 Haiku: `us.anthropic.claude-3-5-haiku-20241022-v1:0`

### Check Available Models
```bash
python olaf-core/tools/strands/check_bedrock_models.py
```

### Troubleshooting AWS Access

**Test AWS credentials**:
```bash
aws sts get-caller-identity --profile bedrock
```

**Test Bedrock access**:
```bash
aws bedrock list-foundation-models --profile bedrock --region us-east-1
```

**Common Issues**:
- **No credentials**: Configure AWS profile
- **Access denied**: Request Bedrock model access in AWS Console
- **Region mismatch**: Ensure region supports Bedrock (us-east-1 recommended)

---

## 📦 Requirements

### Python Packages
```bash
pip install strands-agents strands-agents-tools boto3 psutil requests beautifulsoup4
```

### System Requirements
- **Python**: 3.8+
- **OS**: Windows, Linux, macOS
- **AWS**: Configured credentials with Bedrock access
- **Memory**: 4GB+ recommended for concurrent agents
- **Disk**: Space for process logs and results

### AWS Permissions
Required IAM permissions:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 📚 Advanced Usage

### Custom Task IDs
```bash
python olaf_strands_wrapper.py \
  --spawn \
  --task-id my-custom-analysis-001 \
  --prompt developer/review-code.md
```

### Custom Timestamps
```bash
python olaf_strands_wrapper.py \
  --spawn \
  --timestamp 20250101-1500 \
  --prompt researcher/research-and-report.md
```

### Custom Project Root
```bash
python olaf_strands_wrapper.py \
  --spawn \
  --project-root /path/to/olaf \
  --prompt your-prompt.md
```

### List All Processes
```bash
python olaf_strands_wrapper.py --list-processes
```

### Usage Examples
```bash
python olaf_strands_wrapper.py --examples
```

---

## 🔍 Process Management

### Process Tracking
All spawned agents create process handles in `olaf-data/processes/`:
- `{task-id}.json` - Process metadata and status
- `{task-id}_stdout.log` - Standard output
- `{task-id}_stderr.log` - Standard error

### Status Information
```json
{
  "task_id": "20250101-1430-review-code",
  "pid": 12345,
  "status": "running",
  "started_at": "2025-01-01T14:30:00",
  "cpu_percent": 15.2,
  "memory_mb": 256.8,
  "command": ["python", "olaf_strands_agent.py", "..."]
}
```

### Results Location
Agent results are saved to `olaf-data/findings/`:
- `olaf-strands-results-{timestamp}.md` - Main results
- `olaf-strands-metadata-{timestamp}.json` - Execution metadata
- `olaf-strands-execution-{timestamp}.log` - Execution log

---

## 🎓 Example Workflows

### Research and Report
```bash
python olaf_strands_wrapper.py \
  --prompt researcher/research-and-report.md \
  --context "Research topic: Multi-agent orchestration patterns"
```

### Code Review
```bash
python olaf_strands_wrapper.py \
  --prompt developer/review-code.md \
  --context "Review the async agent implementation for performance"
```

### Create Presentation
```bash
python olaf_strands_wrapper.py \
  --prompt technical-writer/create-presentation-plan.md \
  --context "Topic: AWS Strands SDK, Audience: Developers, Duration: 20 minutes"
```

### Generate Decision Record
```bash
python olaf_strands_wrapper.py \
  --prompt project-manager/create-decision-record.md \
  --context "title: Adopt Strands SDK, type: Technical, context: Agent framework selection, decision_makers: Tech Lead, stakeholders: Dev Team"
```

---

## 🏗️ Architecture

```
OLAF Strands Integration
│
├── olaf_strands_agent.py          # Core agent with AWS Bedrock
│   ├── Strands SDK tools
│   ├── Windows execution tools
│   ├── OLAF memory map resolution
│   └── Autonomous execution
│
├── olaf_strands_wrapper.py        # Process orchestrator
│   ├── Background spawning
│   ├── Status monitoring
│   ├── AWS configuration
│   └── Process lifecycle
│
├── olaf_strands_api.py            # Python API
│   ├── spawn_agent()
│   ├── check_status()
│   ├── get_output()
│   └── wait_for_completion()
│
├── windows_execution_tools.py     # Execution capabilities
│   ├── execute_python_script
│   ├── execute_powershell_command
│   └── execute_python_code
│
├── aws_config_manager.py          # AWS setup
│   ├── Profile management
│   ├── Credential validation
│   └── Model recommendations
│
└── Testing & Utilities
    ├── test_concurrent_agents.py  # 5 agent test
    ├── stress_test_agents.py      # 45+ agent test
    ├── demo_full_async_workflow.py
    ├── check_bedrock_models.py
    └── test_windows_tools.py
```

---

## 📝 Notes

- **Branch**: `research-straf` - AWS Strands SDK integration research
- **Repository**: https://github.com/AmadeusITGroup/olaf
- **Branch URL**: https://github.com/AmadeusITGroup/olaf/tree/research-straf
- **Strands Documentation**: https://strandsagents.com/latest/documentation/docs/
- **Status**: Production-ready for OLAF framework integration
- **Tested**: Windows 10/11, Python 3.8-3.12, AWS Bedrock us-east-1
- **Concurrency**: Validated up to 45+ simultaneous agents
- **Models**: Optimized for Claude Sonnet 4, Sonnet 4.5, and Opus 4

---

## 🤝 Integration with OLAF

This Strands integration is fully compatible with OLAF framework conventions:
- ✅ Memory map references (`[id:findings_dir]`, etc.)
- ✅ Timestamp format (YYYYMMDD-HHMM)
- ✅ File naming (verb-entity-complement.md)
- ✅ US English
- ✅ Results saved to findings directory
- ✅ Prompt loading from olaf-core/prompts
- ✅ Template support

**Ready for production use in OLAF workflows.**
