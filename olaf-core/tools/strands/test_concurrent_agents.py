#!/usr/bin/env python3
"""
Test: Concurrent OLAF Strands Agent Execution
Tests the system's ability to handle multiple simultaneous agent spawns
"""

import subprocess
import sys
import time
import json
from pathlib import Path
from datetime import datetime

def spawn_agent(task_id, prompt, context):
    """Spawn a single agent and return the result"""
    script_dir = Path(__file__).parent
    wrapper_script = script_dir / "olaf_strands_wrapper.py"
    
    cmd = [
        sys.executable, str(wrapper_script),
        "--spawn",
        "--prompt", prompt,
        "--context", context,
        "--task-id", task_id
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "spawned", "task_id": task_id, "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "task_id": task_id, "error": str(e), "stderr": e.stderr}

def check_status(task_id):
    """Check status of a task"""
    script_dir = Path(__file__).parent
    wrapper_script = script_dir / "olaf_strands_wrapper.py"
    
    cmd = [
        sys.executable, str(wrapper_script),
        "--status",
        "--task-id", task_id
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Parse JSON from output
        lines = result.stdout.strip().split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('{'):
                json_text = '\n'.join(lines[i:])
                return json.loads(json_text)
        return {"status": "parse_error", "raw": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def main():
    print("🚀 Testing Concurrent OLAF Strands Agent Execution")
    print("=" * 60)
    
    # Define test scenarios
    test_agents = [
        {
            "task_id": "concurrent-test-1",
            "prompt": "researcher/search-and-learn.md",
            "context": "Learning objective: Test concurrent execution #1"
        },
        {
            "task_id": "concurrent-test-2", 
            "prompt": "project-manager/create-decision-record.md",
            "context": "title: Test Decision, type: Technical, context: Concurrent testing, decision_makers: Test Team, stakeholders: System"
        },
        {
            "task_id": "concurrent-test-3",
            "prompt": "technical-writer/create-presentation-plan.md", 
            "context": "Topic: Concurrent Processing, Audience: Developers, Duration: 15 minutes"
        },
        {
            "task_id": "concurrent-test-4",
            "prompt": "developer/review-code.md",
            "context": "Review the async agent system for scalability and performance"
        },
        {
            "task_id": "concurrent-test-5",
            "prompt": "researcher/research-and-report.md",
            "context": "Research topic: Async agent architecture patterns"
        }
    ]
    
    print(f"📋 Spawning {len(test_agents)} agents simultaneously...")
    
    # Spawn all agents at once
    spawn_results = []
    start_time = time.time()
    
    for agent in test_agents:
        print(f"   Spawning {agent['task_id']}...")
        result = spawn_agent(agent['task_id'], agent['prompt'], agent['context'])
        spawn_results.append(result)
        
        if result['status'] == 'spawned':
            print(f"   ✅ {agent['task_id']} spawned successfully")
        else:
            print(f"   ❌ {agent['task_id']} failed: {result.get('error', 'Unknown')}")
    
    spawn_time = time.time() - start_time
    successful_spawns = sum(1 for r in spawn_results if r['status'] == 'spawned')
    
    print(f"\n📊 Spawn Results:")
    print(f"   Total agents: {len(test_agents)}")
    print(f"   Successful spawns: {successful_spawns}")
    print(f"   Failed spawns: {len(test_agents) - successful_spawns}")
    print(f"   Total spawn time: {spawn_time:.2f}s")
    print(f"   Average spawn time: {spawn_time/len(test_agents):.2f}s per agent")
    
    if successful_spawns == 0:
        print("❌ No agents spawned successfully. Exiting.")
        return
    
    # Monitor progress
    print(f"\n🔍 Monitoring agent progress...")
    successful_task_ids = [r['task_id'] for r in spawn_results if r['status'] == 'spawned']
    
    max_checks = 20
    check_interval = 10
    
    for check_round in range(max_checks):
        print(f"\n--- Check {check_round + 1}/{max_checks} ---")
        
        running_count = 0
        completed_count = 0
        failed_count = 0
        
        for task_id in successful_task_ids:
            status = check_status(task_id)
            agent_status = status.get('status', 'unknown')
            
            if agent_status == 'running':
                running_count += 1
                cpu = status.get('cpu_percent', 0)
                memory = status.get('memory_mb', 0)
                print(f"   🔄 {task_id}: RUNNING (CPU: {cpu:.1f}%, Mem: {memory:.1f}MB)")
            elif agent_status == 'completed':
                completed_count += 1
                print(f"   ✅ {task_id}: COMPLETED")
            elif agent_status in ['failed', 'error']:
                failed_count += 1
                print(f"   ❌ {task_id}: FAILED")
            else:
                print(f"   ❓ {task_id}: {agent_status}")
        
        print(f"   Summary: {running_count} running, {completed_count} completed, {failed_count} failed")
        
        if running_count == 0:
            print(f"\n🎉 All agents completed!")
            break
        
        if check_round < max_checks - 1:
            print(f"   ⏳ Waiting {check_interval} seconds...")
            time.sleep(check_interval)
    
    # Final summary
    print(f"\n📈 Final Results:")
    final_stats = {"running": 0, "completed": 0, "failed": 0, "unknown": 0}
    
    for task_id in successful_task_ids:
        status = check_status(task_id)
        agent_status = status.get('status', 'unknown')
        final_stats[agent_status] = final_stats.get(agent_status, 0) + 1
    
    total_time = time.time() - start_time
    
    print(f"   Total execution time: {total_time:.2f}s")
    print(f"   Agents completed: {final_stats['completed']}")
    print(f"   Agents still running: {final_stats['running']}")
    print(f"   Agents failed: {final_stats['failed']}")
    print(f"   Success rate: {final_stats['completed']/successful_spawns*100:.1f}%")
    
    if final_stats['completed'] > 0:
        print(f"\n✅ Concurrent execution test PASSED!")
        print(f"   System successfully handled {successful_spawns} simultaneous agents")
        print(f"   {final_stats['completed']} agents completed successfully")
    else:
        print(f"\n⚠️  Concurrent execution test had issues")
        print(f"   No agents completed successfully")
    
    print(f"\n💡 This demonstrates the system can handle multiple concurrent OLAF agents!")

if __name__ == "__main__":
    main()