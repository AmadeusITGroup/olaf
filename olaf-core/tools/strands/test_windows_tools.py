#!/usr/bin/env python3
"""
Test script for Windows execution tools
"""

import sys
import json
from pathlib import Path

def test_windows_tools():
    """Test the Windows execution tools"""
    print("Testing Windows Execution Tools for OLAF Strands Agent")
    print("=" * 60)
    
    try:
        # Import the tools
        from windows_execution_tools import (
            create_python_executor_tool,
            create_powershell_executor_tool,
            create_python_code_executor_tool
        )
        
        # Create tool instances
        python_script_tool = create_python_executor_tool()
        powershell_tool = create_powershell_executor_tool()
        python_code_tool = create_python_code_executor_tool()
        
        print("✓ Successfully imported and created all Windows tools")
        
        # Test 1: Python code execution
        print("\n1. Testing Python code execution:")
        test_code = """
import sys
import os
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print("Hello from Python code executor!")
"""
        result = python_code_tool(test_code)
        result_data = json.loads(result)
        print(f"Success: {result_data['success']}")
        if result_data['success']:
            print(f"Output: {result_data['stdout']}")
        else:
            print(f"Error: {result_data['error']}")
        
        # Test 2: PowerShell command execution
        print("\n2. Testing PowerShell command execution:")
        ps_command = "Get-Location; Write-Host 'Hello from PowerShell!'; $PSVersionTable.PSVersion"
        result = powershell_tool(ps_command)
        result_data = json.loads(result)
        print(f"Success: {result_data['success']}")
        if result_data['success']:
            print(f"Output: {result_data['stdout']}")
        else:
            print(f"Error: {result_data['error']}")
        
        # Test 3: Python script execution (create a temp script)
        print("\n3. Testing Python script execution:")
        temp_script = Path("temp_test_script.py")
        temp_script.write_text("""
import sys
print("Hello from Python script!")
print(f"Arguments received: {sys.argv[1:]}")
""")
        
        try:
            result = python_script_tool(str(temp_script), "arg1", "arg2", "arg3")
            result_data = json.loads(result)
            print(f"Success: {result_data['success']}")
            if result_data['success']:
                print(f"Output: {result_data['stdout']}")
            else:
                print(f"Error: {result_data['error']}")
        finally:
            # Clean up
            if temp_script.exists():
                temp_script.unlink()
        
        print("\n✓ All tests completed!")
        
    except ImportError as e:
        print(f"✗ Failed to import tools: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_windows_tools()
    sys.exit(0 if success else 1)
