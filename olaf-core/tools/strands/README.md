# OLAF Strands Agent Tools

This directory contains tools for integrating AWS Strands SDK with the OLAF framework.

## Files

### Core Agent Files


#### `olaf_strands_agent.py`
- **Purpose**: Main OLAF Strands agent implementation using AWS Strands SDK
- **Features**: 
  - Real AWS Bedrock integration with Claude models
  - Built-in Strands SDK tools (file operations, web requests, code execution)
  - Windows-compatible execution tools
  - Proper timestamp handling and memory-map support
  - MCP server integration capabilities

#### `olaf_strands_wrapper.py`
- **Purpose**: Async process manager and command-line wrapper for OLAF Strands agents
- **Features**:
  - Spawn agents as background processes
  - Status tracking and process management
  - Synchronous and asynchronous execution modes
  - Command-line interface for all operations
  - Automatic project root detection
  - Default AWS Bedrock configuration
  - Timestamp management

#### `olaf_strands_api.py`
- **Purpose**: Programmatic Python API for agent management
- **Features**:
  - Simple Python interface for spawning agents
  - Status checking and output retrieval
  - Process lifecycle management
  - Integration-friendly for calling agents

### Supporting Tools

#### `windows_execution_tools.py`
- **Purpose**: Windows-specific execution tools for the Strands agent
- **Features**:
  - Python script execution tool
  - PowerShell command execution tool
  - Windows-compatible subprocess handling

#### `check_bedrock_models.py`
- **Purpose**: Utility to check available AWS Bedrock models
- **Features**:
  - Lists accessible models in your AWS account
  - Helps with model selection and debugging



#### `test_windows_tools.py`
- **Purpose**: Test suite for Windows execution capabilities
- **Features**:
  - Validates Windows tool functionality
  - Debugging and development support

## Usage

### Asynchronous Mode (Default - Background Execution)
```bash
# Spawn agent as background process
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --prompt technical-writer/create-presentation-plan.md \
  --context "Topic: AWS Lambda. Audience: Developers. Duration: 15 minutes"
# Returns immediately with task ID

# Check status of running task
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --status --task-id 20241229-1430-create-presentation-plan

# Get results when completed
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --get-output --task-id 20241229-1430-create-presentation-plan

# List all processes
python olaf-core/tools/strands/olaf_strands_wrapper.py --list-processes
```

### Synchronous Mode (Wait for Completion)
```bash
# Run and wait for completion (original behavior)
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --wait \
  --prompt researcher/search-and-learn.md \
  --context "Learning objective: AWS best practices"
```

### Programmatic API Usage
```python
from olaf_strands_api import OLAFStrandsAPI

# Initialize API
api = OLAFStrandsAPI()

# Spawn agent
result = api.spawn_agent(
    prompt="developer/review-code.md",
    context="Review current codebase for improvements"
)
task_id = result['task_id']

# Check status
status = api.check_status(task_id)
print(f"Status: {status['status']}")

# Get output when done
if status['status'] == 'completed':
    output = api.get_output(task_id)
    print(output['main_result'])

# Or wait for completion
final_result = api.wait_for_completion(task_id)
```

### Advanced Usage
```bash
# Custom model and task ID
python olaf-core/tools/strands/olaf_strands_wrapper.py \
  --spawn \
  --task-id my-custom-analysis \
  --prompt your-prompt.md \
  --model us.anthropic.claude-3-5-sonnet-20241022-v2:0 \
  --context "Your context here" \
  --project-root /path/to/project
```

## Requirements

- Python 3.8+
- AWS credentials configured (bedrock profile recommended)
- Required packages:
  ```bash
  pip install strands-agents strands-agents-tools boto3 requests beautifulsoup4
  ```

## Configuration

The agent uses AWS Bedrock by default with the following configuration:
- **Profile**: bedrock (can be overridden with --aws-profile)
- **Region**: us-east-1 (can be overridden with --aws-region)
- **Model**: Uses inference profiles for better availability

## Features

### Asynchronous Process Management
- Spawn agents as background processes
- Track process status and resource usage
- Handle multiple concurrent agent executions
- Retrieve results when tasks complete
- Process lifecycle management with handles

### Autonomous Execution
- Executes Python scripts automatically without user prompts
- Handles file operations without user intervention
- Generates real outputs (PowerPoint, reports, analysis)
- Fully autonomous tool execution with `null_callback_handler`

### Tool Integration
- File read/write operations
- Web content fetching and HTML-to-markdown conversion
- Python code execution (Windows-compatible)
- PowerShell command execution (Windows)
- MCP server connectivity
- HTTP requests for web research

### OLAF Framework Integration
- Memory-map support for directory references (`[id:findings_dir]`)
- Proper timestamp handling (YYYYMMDD-HHMM format)
- Template and prompt loading
- Results saving with OLAF conventions
- Process tracking in `olaf-data/processes/`

## Development

This is part of the research-straf branch for exploring AWS Strands SDK integration with OLAF framework capabilities.