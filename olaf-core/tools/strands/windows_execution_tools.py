#!/usr/bin/env python3
"""
Windows Execution Tools for OLAF Strands Agent
Provides Python script execution and PowerShell command execution tools for Windows environments
"""

import subprocess
import sys
import os
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any
import json


def create_python_executor_tool():
    """Create a Python script execution tool for Windows"""
    from strands import tool
    
    @tool
    def execute_python_script(script_path: str, *args: str, working_directory: Optional[str] = None) -> str:
        """
        Execute a Python script with arguments on Windows.
        
        Args:
            script_path: Path to the Python script to execute (absolute or relative)
            *args: Arguments to pass to the script
            working_directory: Optional working directory for script execution
        
        Returns:
            JSON string containing execution results with stdout, stderr, and return code
        """
        try:
            # Resolve script path
            script_path = Path(script_path).resolve()
            if not script_path.exists():
                return json.dumps({
                    "success": False,
                    "error": f"Script not found: {script_path}",
                    "stdout": "",
                    "stderr": "",
                    "return_code": -1
                })
            
            # Build command
            cmd = [sys.executable, str(script_path)] + list(args)
            
            # Set working directory
            cwd = working_directory if working_directory else script_path.parent
            
            # Execute script
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                cwd=cwd,
                shell=False
            )
            
            return json.dumps({
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
                "command": " ".join(cmd),
                "working_directory": str(cwd)
            }, indent=2)
                    
        except subprocess.TimeoutExpired:
            return json.dumps({
                "success": False,
                "error": "Script execution timed out after 5 minutes",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": f"Failed to execute script: {str(e)}",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
    
    return execute_python_script


def create_powershell_executor_tool():
    """Create a PowerShell command execution tool for Windows"""
    from strands import tool
    
    @tool
    def execute_powershell_command(command: str, working_directory: Optional[str] = None, 
                                 execution_policy: str = "Bypass") -> str:
        """
        Execute a PowerShell command on Windows.
        
        Args:
            command: PowerShell command or script block to execute
            working_directory: Optional working directory for command execution
            execution_policy: PowerShell execution policy (default: Bypass)
        
        Returns:
            JSON string containing execution results with stdout, stderr, and return code
        """
        try:
            # Build PowerShell command
            ps_cmd = [
                "powershell.exe",
                "-ExecutionPolicy", execution_policy,
                "-NoProfile",
                "-NonInteractive",
                "-Command", command
            ]
            
            # Set working directory
            cwd = working_directory if working_directory else os.getcwd()
            
            # Execute command
            result = subprocess.run(
                ps_cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                cwd=cwd,
                shell=False
            )
            
            return json.dumps({
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
                "command": command,
                "working_directory": str(cwd)
            }, indent=2)
                    
        except subprocess.TimeoutExpired:
            return json.dumps({
                "success": False,
                "error": "PowerShell command timed out after 5 minutes",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": f"Failed to execute PowerShell command: {str(e)}",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
    
    return execute_powershell_command


def create_python_code_executor_tool():
    """Create a Python code execution tool (for code snippets, not files)"""
    from strands import tool
    
    @tool
    def execute_python_code(code: str, working_directory: Optional[str] = None) -> str:
        """
        Execute Python code directly (not from a file).
        
        Args:
            code: Python code to execute
            working_directory: Optional working directory for code execution
        
        Returns:
            JSON string containing execution results with stdout, stderr, and return code
        """
        try:
            # Create temporary file for the code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
                temp_file.write(code)
                temp_file_path = temp_file.name
            
            try:
                # Build command
                cmd = [sys.executable, temp_file_path]
                
                # Set working directory
                cwd = working_directory if working_directory else os.getcwd()
                
                # Execute code
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=300,  # 5 minute timeout
                    cwd=cwd,
                    shell=False
                )
                
                return json.dumps({
                    "success": result.returncode == 0,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "return_code": result.returncode,
                    "code_preview": code[:200] + "..." if len(code) > 200 else code,
                    "working_directory": str(cwd)
                }, indent=2)
                        
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file_path)
                except:
                    pass
                    
        except subprocess.TimeoutExpired:
            return json.dumps({
                "success": False,
                "error": "Python code execution timed out after 5 minutes",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": f"Failed to execute Python code: {str(e)}",
                "stdout": "",
                "stderr": "",
                "return_code": -1
            })
    
    return execute_python_code


# Export the tool creation functions
__all__ = [
    'create_python_executor_tool',
    'create_powershell_executor_tool', 
    'create_python_code_executor_tool'
]


if __name__ == "__main__":
    # Test the tools
    print("Testing Windows Execution Tools...")
    
    # Test Python executor
    python_tool = create_python_executor_tool()
    print("\n1. Testing Python script execution:")
    result = python_tool("python", "-c", "print('Hello from Python!')")
    print(result)
    
    # Test PowerShell executor
    ps_tool = create_powershell_executor_tool()
    print("\n2. Testing PowerShell command execution:")
    result = ps_tool("Write-Host 'Hello from PowerShell!'")
    print(result)
    
    # Test Python code executor
    code_tool = create_python_code_executor_tool()
    print("\n3. Testing Python code execution:")
    result = code_tool("import sys\nprint(f'Python version: {sys.version}')")
    print(result)
