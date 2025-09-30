#!/usr/bin/env python3
"""
OLAF Strands Agent Wrapper - Async Process Manager
A wrapper that spawns OLAF Strands agents as background processes
"""


import argparse
import subprocess
import sys
import json
import time
import psutil
from datetime import datetime
from pathlib import Path
import logging
from typing import Dict, Any, Optional
from aws_config_manager import AWSConfigManager

class AgentProcessManager:
    """Manages background agent processes"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.processes_dir = project_root / 'olaf-data' / 'processes'
        self.processes_dir.mkdir(parents=True, exist_ok=True)
    
    def spawn_agent(self, cmd: list, task_id: str) -> Dict[str, Any]:
        """Spawn agent as background process and return handle"""
        try:
            # Create process info file
            process_file = self.processes_dir / f"{task_id}.json"
            
            # Start process
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if sys.platform == 'win32' else 0
            )
            
            # Create process handle
            handle = {
                'task_id': task_id,
                'pid': process.pid,
                'status': 'running',
                'started_at': datetime.now().isoformat(),
                'command': cmd,
                'process_file': str(process_file),
                'stdout_file': str(self.processes_dir / f"{task_id}_stdout.log"),
                'stderr_file': str(self.processes_dir / f"{task_id}_stderr.log")
            }
            
            # Save handle to file
            with open(process_file, 'w') as f:
                json.dump(handle, f, indent=2)
            
            print(f"Agent spawned as background process")
            print(f"Task ID: {task_id}")
            print(f"Process ID: {process.pid}")
            print(f"Handle file: {process_file}")
            
            return handle
            
        except Exception as e:
            return {
                'task_id': task_id,
                'status': 'failed',
                'error': str(e),
                'started_at': datetime.now().isoformat()
            }
    
    def check_status(self, task_id: str) -> Dict[str, Any]:
        """Check status of a background agent process"""
        process_file = self.processes_dir / f"{task_id}.json"
        
        if not process_file.exists():
            return {'status': 'not_found', 'task_id': task_id}
        
        try:
            with open(process_file, 'r') as f:
                handle = json.load(f)
            
            pid = handle.get('pid')
            if not pid:
                return {'status': 'invalid_handle', 'task_id': task_id}
            
            # Check if process is still running
            try:
                process = psutil.Process(pid)
                if process.is_running():
                    handle['status'] = 'running'
                    handle['cpu_percent'] = process.cpu_percent()
                    handle['memory_mb'] = process.memory_info().rss / 1024 / 1024
                else:
                    handle['status'] = 'completed'
                    handle['completed_at'] = datetime.now().isoformat()
            except psutil.NoSuchProcess:
                handle['status'] = 'completed'
                handle['completed_at'] = datetime.now().isoformat()
            
            # Update handle file
            with open(process_file, 'w') as f:
                json.dump(handle, f, indent=2)
            
            return handle
            
        except Exception as e:
            return {
                'status': 'error',
                'task_id': task_id,
                'error': str(e)
            }
    
    def get_output(self, task_id: str) -> Dict[str, Any]:
        """Get output from completed agent process"""
        handle = self.check_status(task_id)
        
        if handle['status'] == 'running':
            return {'status': 'still_running', 'task_id': task_id}
        
        try:
            # Look for results files
            findings_dir = self.project_root / 'olaf-data' / 'findings'
            results_pattern = f"*{task_id}*"
            
            results_files = list(findings_dir.glob(results_pattern))
            
            output = {
                'task_id': task_id,
                'status': handle['status'],
                'results_files': [str(f) for f in results_files],
                'handle': handle
            }
            
            # Read main results if available
            for file in results_files:
                if 'results' in file.name and file.suffix == '.md':
                    with open(file, 'r', encoding='utf-8') as f:
                        output['main_result'] = f.read()
                    break
            
            return output
            
        except Exception as e:
            return {
                'status': 'error',
                'task_id': task_id,
                'error': str(e)
            }
    
    def list_processes(self) -> list:
        """List all agent processes"""
        processes = []
        
        for process_file in self.processes_dir.glob("*.json"):
            if not process_file.name.endswith('_stdout.log') and not process_file.name.endswith('_stderr.log'):
                task_id = process_file.stem
                status = self.check_status(task_id)
                processes.append(status)
        
        return processes

def show_usage_examples():
    """Show common usage examples"""
    examples = """
OLAF Strands Agent Wrapper - Async Process Manager

SPAWN MODE (Background execution):
1. Spawn agent and get handle:
   python olaf_strands_wrapper.py --spawn --prompt developer/review-code.md

2. Spawn with custom task ID:
   python olaf_strands_wrapper.py --spawn --task-id my-analysis --prompt researcher/research-and-report.md

STATUS CHECKING:
3. Check status of running task:
   python olaf_strands_wrapper.py --status --task-id 20241229-1430-review-code

4. Get results from completed task:
   python olaf_strands_wrapper.py --get-output --task-id 20241229-1430-review-code

5. List all processes:
   python olaf_strands_wrapper.py --list-processes

SYNCHRONOUS MODE (Wait for completion):
6. Run and wait (original behavior):
   python olaf_strands_wrapper.py --prompt developer/review-code.md --wait

Environment Variables:
- AWS Bedrock: AWS_PROFILE, AWS_REGION, AWS_BEDROCK_DEFAULT_MODEL
- OpenAI: OPENAI_API_KEY, OPENAI_DEFAULT_MODEL
- General: MAX_TOKENS, TEMPERATURE

Installation Requirements:
pip install strands-agents strands-agents-tools boto3 psutil
"""
    print(examples)

def main():
    parser = argparse.ArgumentParser(
        description='OLAF Strands Agent Wrapper - Async Process Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Mode selection
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--spawn', action='store_true',
                           help='Spawn agent as background process (default behavior)')
    mode_group.add_argument('--status', action='store_true',
                           help='Check status of a task')
    mode_group.add_argument('--get-output', action='store_true',
                           help='Get output from completed task')
    mode_group.add_argument('--list-processes', action='store_true',
                           help='List all agent processes')
    mode_group.add_argument('--wait', action='store_true',
                           help='Run synchronously and wait for completion')
    
    # Task management
    parser.add_argument('--task-id',
                       help='Task ID for status/output operations (auto-generated if not provided)')
    
    # Agent configuration
    parser.add_argument('--prompt',
                       help='Prompt file path (relative to olaf-core/prompts/)')
    parser.add_argument('--service', '--service-provider', dest='service_provider', 
                       default='aws-bedrock', choices=['aws-bedrock', 'openai'],
                       help='AI service provider (default: aws-bedrock)')
    parser.add_argument('--model', '--model-name', dest='model_name',
                       help='Model name (uses service default if not specified)')
    parser.add_argument('--context', default='',
                       help='Additional context data')
    parser.add_argument('--timestamp',
                       help='Override timestamp (YYYYMMDD-HHMM format, uses current local time if not provided)')
    parser.add_argument('--output', '--output-location', dest='output_location',
                       help='Custom output location')
    parser.add_argument('--project-root', default='.',
                       help='Path to project root containing olaf-core')
    parser.add_argument('--aws-profile', default='bedrock',
                       help='AWS profile name to use (default: bedrock)')
    parser.add_argument('--examples', action='store_true',
                       help='Show usage examples and exit')
    
    args = parser.parse_args()
    
    if args.examples:
        show_usage_examples()
        return
    
    # Find project root
    project_root = Path(args.project_root).resolve()
    
    # Look for olaf-core directory
    if not (project_root / "olaf-core").exists():
        # Try parent directories
        for parent in project_root.parents:
            if (parent / "olaf-core").exists():
                project_root = parent
                break
            elif (parent / "olaf" / "olaf-core").exists():
                project_root = parent / "olaf"
                break
    
    # Initialize process manager
    manager = AgentProcessManager(project_root)
    
    # Handle different modes
    if args.status:
        if not args.task_id:
            print("Task ID required for status check")
            sys.exit(1)
        
        status = manager.check_status(args.task_id)
        print(f"Task Status: {args.task_id}")
        print(json.dumps(status, indent=2))
        return
    
    elif args.get_output:
        if not args.task_id:
            print("Task ID required for output retrieval")
            sys.exit(1)
        
        output = manager.get_output(args.task_id)
        print(f"Task Output: {args.task_id}")
        print(json.dumps(output, indent=2))
        return
    
    elif args.list_processes:
        processes = manager.list_processes()
        print(f"Agent Processes ({len(processes)} total):")
        for proc in processes:
            print(f"  {proc['task_id']}: {proc['status']}")
        return
    
    # For spawn or wait modes, we need a prompt
    if not args.prompt:
        print("❌ Prompt required for agent execution")
        sys.exit(1)
    
    # Generate local timestamp if not provided
    if not args.timestamp:
        args.timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    
    # Generate task ID if not provided
    if not args.task_id:
        prompt_name = Path(args.prompt).stem
        args.task_id = f"{args.timestamp}-{prompt_name}"
    
    # Setup AWS configuration if using Bedrock
    if args.service_provider == 'aws-bedrock':
        # Setup logging for configuration
        config_logger = logging.getLogger('aws_config')
        config_logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        config_logger.addHandler(handler)
        
        # Initialize AWS configuration manager
        aws_manager = AWSConfigManager(config_logger)
        
        # Set default model if not provided
        if not args.model_name:
            args.model_name = aws_manager.DEFAULT_MODEL  # Sonnet 4 inference profile
        
        # Setup AWS environment
        print("Configuring AWS Bedrock environment...")
        config_result = aws_manager.setup_aws_environment(
            profile=args.aws_profile,
            region='us-east-1',  # Default region
            model=args.model_name
        )
        
        if config_result['status'] == 'success':
            print(f"AWS Configuration: {config_result['message']}")
        else:
            print(f"AWS Configuration Warning: {config_result['message']}")
            print("   Proceeding anyway - check your AWS credentials if execution fails")
        
        # Show configuration summary
        summary = aws_manager.get_configuration_summary()
        print(f"   Profile: {summary['aws_profile']}, Region: {summary['aws_region']}")
        print(f"   Model: {args.model_name}")
        
    else:
        # Set default models for other services
        if not args.model_name:
            model_defaults = {
                'openai': 'gpt-4-turbo'
            }
            args.model_name = model_defaults.get(args.service_provider, 'default')
    
    # Find the main agent script (in same directory)
    script_dir = Path(__file__).parent
    agent_script = script_dir / 'olaf_strands_agent.py'
    
    if not agent_script.exists():
        print(f"❌ OLAF Strands agent script not found at {agent_script}")
        sys.exit(1)
    
    # Build command
    cmd = [
        sys.executable, str(agent_script),
        '--service-provider', args.service_provider,
        '--prompt', args.prompt,
        '--project-root', str(project_root)
    ]
    
    if args.model_name:
        cmd.extend(['--model-name', args.model_name])
    
    if args.context:
        cmd.extend(['--context', args.context])
    
    if args.output_location:
        cmd.extend(['--output-location', args.output_location])
    
    if args.aws_profile:
        cmd.extend(['--aws-profile', args.aws_profile])
    
    # Always pass the timestamp to the agent
    cmd.extend(['--timestamp', args.timestamp])
    
    # Execute based on mode
    if args.wait:
        # Synchronous execution (original behavior)
        try:
            print(f"Executing OLAF Strands Agent (synchronous)...")
            print(f"Service: {args.service_provider}")
            print(f"Model: {args.model_name or 'default'}")
            print(f"Prompt: {args.prompt}")
            print(f"Timestamp: {args.timestamp}")
            if args.context:
                print(f"Context: {args.context[:50]}{'...' if len(args.context) > 50 else ''}")
            print()
            
            result = subprocess.run(cmd, check=True)
            print(f"\nAgent execution completed successfully!")
            
        except subprocess.CalledProcessError as e:
            print(f"\nAgent execution failed with exit code {e.returncode}")
            sys.exit(e.returncode)
        except Exception as e:
            print(f"\nError executing agent: {e}")
            sys.exit(1)
    
    else:
        # Asynchronous execution (spawn mode - default)
        print(f"Spawning OLAF Strands Agent (background)...")
        print(f"Service: {args.service_provider}")
        print(f"Model: {args.model_name or 'default'}")
        print(f"Prompt: {args.prompt}")
        print(f"Timestamp: {args.timestamp}")
        if args.context:
            print(f"Context: {args.context[:50]}{'...' if len(args.context) > 50 else ''}")
        print()
        
        handle = manager.spawn_agent(cmd, args.task_id)
        
        if handle['status'] == 'running':
            print(f"\nAgent spawned successfully!")
            print(f"Use this task ID to check status: {args.task_id}")
            print(f"Check status: python {Path(__file__).name} --status --task-id {args.task_id}")
            print(f"Get results: python {Path(__file__).name} --get-output --task-id {args.task_id}")
        else:
            print(f"\nFailed to spawn agent: {handle.get('error', 'Unknown error')}")
            sys.exit(1)

if __name__ == "__main__":
    main()
