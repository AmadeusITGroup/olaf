#!/usr/bin/env python3
"""
Demo: Complete OLAF Strands Async Workflow
Shows how a calling agent can spawn, monitor, and retrieve results from OLAF agents
"""

import subprocess
import sys
import time
from pathlib import Path


def run_command(cmd, description):
    """Run a command and show the output"""
    print(f"\n🔧 {description}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print(f"Stderr: {e.stderr}")
        return False

def main():
    print("🚀 OLAF Strands Async Workflow Demo")
    print("=" * 50)
    
    # Change to the strands directory
    script_dir = Path(__file__).parent
    wrapper_script = script_dir / "olaf_strands_wrapper.py"
    
    if not wrapper_script.exists():
        print(f"❌ Wrapper script not found: {wrapper_script}")
        return
    
    # Demo task ID
    task_id = "demo-workflow-test"
    
    # Step 1: Spawn an agent
    spawn_cmd = [
        sys.executable, str(wrapper_script),
        "--spawn",
        "--prompt", "researcher/search-and-learn.md",
        "--context", "Learning objective: Demonstrate async OLAF agent workflow",
        "--task-id", task_id
    ]
    
    if not run_command(spawn_cmd, "Step 1: Spawning OLAF Agent"):
        return
    
    # Step 2: Check status immediately (should be running)
    status_cmd = [
        sys.executable, str(wrapper_script),
        "--status",
        "--task-id", task_id
    ]
    
    run_command(status_cmd, "Step 2: Checking Initial Status")
    
    # Step 3: Wait and check again
    print(f"\n⏳ Waiting 15 seconds for agent to complete...")
    time.sleep(15)
    
    run_command(status_cmd, "Step 3: Checking Status After Wait")
    
    # Step 4: Get output
    output_cmd = [
        sys.executable, str(wrapper_script),
        "--get-output",
        "--task-id", task_id
    ]
    
    run_command(output_cmd, "Step 4: Retrieving Agent Output")
    
    # Step 5: List all processes
    list_cmd = [
        sys.executable, str(wrapper_script),
        "--list-processes"
    ]
    
    run_command(list_cmd, "Step 5: Listing All Agent Processes")
    
    print(f"\n🎉 Demo completed!")
    print(f"💡 This demonstrates the complete async workflow:")
    print(f"   ✅ Spawn agent as background process")
    print(f"   ✅ Monitor status without blocking")
    print(f"   ✅ Retrieve results when ready")
    print(f"   ✅ Manage multiple concurrent agents")
    print(f"\n🔗 Your calling agent can use the same pattern!")

if __name__ == "__main__":
    main()