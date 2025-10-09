#!/usr/bin/env python3
"""
OLAF Strands API - Programmatic Interface
Simple Python API for spawning and managing OLAF Strands agents
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

class OLAFStrandsAPI:
    """Programmatic interface for OLAF Strands agents"""
    
    def __init__(self, project_root: str = ".", aws_profile: str = "bedrock"):
        self.project_root = Path(project_root).resolve()
        self.aws_profile = aws_profile
        
        # Find wrapper script
        self.wrapper_script = self._find_wrapper_script()
        
        # Find project root with olaf-core
        if not (self.project_root / "olaf-core").exists():
            # Try current directory first
            current_dir = Path(__file__).parent
            test_paths = [
                current_dir / "../../../..",  # From tools/strands to project root
                current_dir.parent.parent.parent.parent,  # Same but resolved
                self.project_root,
            ]
            
            # Add parent directories
            for parent in self.project_root.parents:
                test_paths.extend([
                    parent,
                    parent / "olaf"
                ])
            
            for test_path in test_paths:
                test_path = test_path.resolve()
                if (test_path / "olaf-core").exists():
                    self.project_root = test_path
                    break
    
    def _find_wrapper_script(self) -> Path:
        """Find the wrapper script"""
        script_dir = Path(__file__).parent
        wrapper_script = script_dir / 'olaf_strands_wrapper.py'
        
        if not wrapper_script.exists():
            raise FileNotFoundError(f"Wrapper script not found at {wrapper_script}")
        
        return wrapper_script
    
    def spawn_agent(self, 
                   prompt: str,
                   service_provider: str = "aws-bedrock",
                   model_name: Optional[str] = None,
                   context: str = "",
                   task_id: Optional[str] = None,
                   timestamp: Optional[str] = None) -> Dict[str, Any]:
        """
        Spawn an agent as a background process
        
        Args:
            prompt: Prompt file path (relative to olaf-core/prompts/)
            service_provider: AI service provider ('aws-bedrock' or 'openai')
            model_name: Model name (uses default if not specified)
            context: Additional context data
            task_id: Custom task ID (auto-generated if not provided)
            timestamp: Custom timestamp (YYYYMMDD-HHMM format)
        
        Returns:
            Dict with task_id, status, and process information
        """
        # Generate timestamp if not provided
        if not timestamp:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        
        # Generate task ID if not provided
        if not task_id:
            prompt_name = Path(prompt).stem
            task_id = f"{timestamp}-{prompt_name}"
        
        # Build command
        cmd = [
            sys.executable, str(self.wrapper_script),
            '--spawn',
            '--prompt', prompt,
            '--service', service_provider,
            '--project-root', str(self.project_root),
            '--aws-profile', self.aws_profile,
            '--task-id', task_id,
            '--timestamp', timestamp
        ]
        
        if model_name:
            cmd.extend(['--model', model_name])
        
        if context:
            cmd.extend(['--context', context])
        
        try:
            # Execute wrapper
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            return {
                'status': 'spawned',
                'task_id': task_id,
                'timestamp': timestamp,
                'message': 'Agent spawned successfully',
                'stdout': result.stdout
            }
            
        except subprocess.CalledProcessError as e:
            return {
                'status': 'error',
                'task_id': task_id,
                'error': f"Failed to spawn agent: {e}",
                'stderr': e.stderr,
                'stdout': e.stdout
            }
    
    def check_status(self, task_id: str) -> Dict[str, Any]:
        """
        Check status of a background agent process
        
        Args:
            task_id: Task ID to check
        
        Returns:
            Dict with status information
        """
        cmd = [
            sys.executable, str(self.wrapper_script),
            '--status',
            '--task-id', task_id,
            '--project-root', str(self.project_root)
        ]
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            # Parse JSON output
            output_lines = result.stdout.strip().split('\n')
            json_start = -1
            for i, line in enumerate(output_lines):
                if line.strip().startswith('{'):
                    json_start = i
                    break
            
            if json_start >= 0:
                json_text = '\n'.join(output_lines[json_start:])
                return json.loads(json_text)
            else:
                return {
                    'status': 'unknown',
                    'task_id': task_id,
                    'raw_output': result.stdout
                }
                
        except subprocess.CalledProcessError as e:
            return {
                'status': 'error',
                'task_id': task_id,
                'error': f"Failed to check status: {e}",
                'stderr': e.stderr
            }
        except json.JSONDecodeError as e:
            return {
                'status': 'parse_error',
                'task_id': task_id,
                'error': f"Failed to parse status: {e}",
                'raw_output': result.stdout
            }
    
    def get_output(self, task_id: str) -> Dict[str, Any]:
        """
        Get output from a completed agent process
        
        Args:
            task_id: Task ID to get output for
        
        Returns:
            Dict with output and results
        """
        cmd = [
            sys.executable, str(self.wrapper_script),
            '--get-output',
            '--task-id', task_id,
            '--project-root', str(self.project_root)
        ]
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            # Parse JSON output
            output_lines = result.stdout.strip().split('\n')
            json_start = -1
            for i, line in enumerate(output_lines):
                if line.strip().startswith('{'):
                    json_start = i
                    break
            
            if json_start >= 0:
                json_text = '\n'.join(output_lines[json_start:])
                return json.loads(json_text)
            else:
                return {
                    'status': 'unknown',
                    'task_id': task_id,
                    'raw_output': result.stdout
                }
                
        except subprocess.CalledProcessError as e:
            return {
                'status': 'error',
                'task_id': task_id,
                'error': f"Failed to get output: {e}",
                'stderr': e.stderr
            }
        except json.JSONDecodeError as e:
            return {
                'status': 'parse_error',
                'task_id': task_id,
                'error': f"Failed to parse output: {e}",
                'raw_output': result.stdout
            }
    
    def list_processes(self) -> List[Dict[str, Any]]:
        """
        List all agent processes
        
        Returns:
            List of process status dictionaries
        """
        cmd = [
            sys.executable, str(self.wrapper_script),
            '--list-processes',
            '--project-root', str(self.project_root)
        ]
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            # Parse output - look for process list
            processes = []
            lines = result.stdout.strip().split('\n')
            
            for line in lines:
                if ':' in line and ('running' in line or 'completed' in line or 'failed' in line):
                    parts = line.strip().split(':', 1)
                    if len(parts) == 2:
                        task_id = parts[0].strip()
                        status = parts[1].strip()
                        processes.append({
                            'task_id': task_id,
                            'status': status
                        })
            
            return processes
                
        except subprocess.CalledProcessError as e:
            return [{
                'status': 'error',
                'error': f"Failed to list processes: {e}",
                'stderr': e.stderr
            }]
    
    def wait_for_completion(self, task_id: str, 
                          check_interval: int = 5, 
                          max_wait: int = 300) -> Dict[str, Any]:
        """
        Wait for an agent process to complete
        
        Args:
            task_id: Task ID to wait for
            check_interval: Seconds between status checks
            max_wait: Maximum seconds to wait
        
        Returns:
            Final status and output
        """
        import time
        
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            status = self.check_status(task_id)
            
            if status.get('status') in ['completed', 'failed', 'error']:
                # Get final output
                output = self.get_output(task_id)
                return {
                    'final_status': status,
                    'output': output,
                    'wait_time': time.time() - start_time
                }
            
            time.sleep(check_interval)
        
        return {
            'status': 'timeout',
            'task_id': task_id,
            'wait_time': max_wait,
            'last_status': self.check_status(task_id)
        }


# Convenience functions for quick usage
def spawn_agent(prompt: str, **kwargs) -> Dict[str, Any]:
    """Quick spawn function"""
    api = OLAFStrandsAPI()
    return api.spawn_agent(prompt, **kwargs)

def check_status(task_id: str) -> Dict[str, Any]:
    """Quick status check function"""
    api = OLAFStrandsAPI()
    return api.check_status(task_id)

def get_output(task_id: str) -> Dict[str, Any]:
    """Quick output retrieval function"""
    api = OLAFStrandsAPI()
    return api.get_output(task_id)

def list_processes() -> List[Dict[str, Any]]:
    """Quick process listing function"""
    api = OLAFStrandsAPI()
    return api.list_processes()


if __name__ == "__main__":
    # Example usage
    print("OLAF Strands API - Example Usage")
    print("================================")
    
    # Initialize API
    api = OLAFStrandsAPI()
    
    # Example: Spawn an agent
    print("\n1. Spawning agent...")
    result = api.spawn_agent(
        prompt="developer/review-code.md",
        context="Review the current codebase for improvements"
    )
    print(f"Spawn result: {result}")
    
    if result['status'] == 'spawned':
        task_id = result['task_id']
        
        # Example: Check status
        print(f"\n2. Checking status for {task_id}...")
        status = api.check_status(task_id)
        print(f"Status: {status}")
        
        # Example: List all processes
        print("\n3. Listing all processes...")
        processes = api.list_processes()
        for proc in processes:
            print(f"  {proc}")