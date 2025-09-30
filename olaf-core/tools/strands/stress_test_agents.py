#!/usr/bin/env python3
"""
Stress Test: High-Volume OLAF Strands Agent Execution
Tests system limits with many simultaneous agents
"""


import subprocess
import sys
import time
import json
from pathlib import Path
from datetime import datetime

def spawn_agent_batch(batch_id, count):
    """Spawn a batch of agents quickly"""
    script_dir = Path(__file__).parent
    wrapper_script = script_dir / "olaf_strands_wrapper.py"
    
    results = []
    
    for i in range(count):
        task_id = f"stress-{batch_id}-{i+1:02d}"
        
        # Vary the prompts to test different workloads
        prompts = [
            ("researcher/search-and-learn.md", f"Learning objective: Stress test batch {batch_id} agent {i+1}"),
            ("project-manager/create-decision-record.md", f"title: Stress Test {i+1}, type: Technical, context: Load testing, decision_makers: System, stakeholders: Test"),
            ("technical-writer/create-presentation-plan.md", f"Topic: Stress Test {i+1}, Audience: System, Duration: 10 minutes"),
        ]
        
        prompt, context = prompts[i % len(prompts)]
        
        cmd = [
            sys.executable, str(wrapper_script),
            "--spawn",
            "--prompt", prompt,
            "--context", context,
            "--task-id", task_id
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
            results.append({"status": "spawned", "task_id": task_id})
            print(f"   ✅ {task_id}")
        except subprocess.TimeoutExpired:
            results.append({"status": "timeout", "task_id": task_id})
            print(f"   ⏰ {task_id} (timeout)")
        except subprocess.CalledProcessError as e:
            results.append({"status": "error", "task_id": task_id, "error": str(e)})
            print(f"   ❌ {task_id} (error)")
    
    return results

def check_system_status():
    """Check overall system status"""
    script_dir = Path(__file__).parent
    wrapper_script = script_dir / "olaf_strands_wrapper.py"
    
    cmd = [sys.executable, str(wrapper_script), "--list-processes"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Count processes from output
        lines = result.stdout.strip().split('\n')
        process_count = 0
        for line in lines:
            if ':' in line and ('running' in line or 'completed' in line):
                process_count += 1
        return process_count
    except Exception:
        return -1

def main():
    print("🔥 OLAF Strands Agent Stress Test")
    print("=" * 50)
    
    # Test parameters
    batches = [
        {"id": "A", "count": 10, "description": "10 agents (moderate load)"},
        {"id": "B", "count": 15, "description": "15 agents (high load)"},
        {"id": "C", "count": 20, "description": "20 agents (stress load)"},
    ]
    
    all_results = []
    
    for batch in batches:
        print(f"\n🚀 Batch {batch['id']}: {batch['description']}")
        print("-" * 40)
        
        start_time = time.time()
        
        # Check system before batch
        initial_processes = check_system_status()
        print(f"   Initial processes: {initial_processes}")
        
        # Spawn batch
        print(f"   Spawning {batch['count']} agents...")
        batch_results = spawn_agent_batch(batch['id'], batch['count'])
        
        spawn_time = time.time() - start_time
        successful = sum(1 for r in batch_results if r['status'] == 'spawned')
        
        print(f"\n   📊 Batch {batch['id']} Results:")
        print(f"      Spawn time: {spawn_time:.2f}s")
        print(f"      Success rate: {successful}/{batch['count']} ({successful/batch['count']*100:.1f}%)")
        print(f"      Avg spawn time: {spawn_time/batch['count']:.2f}s per agent")
        
        # Check system after batch
        final_processes = check_system_status()
        print(f"      Total processes: {final_processes}")
        
        all_results.extend(batch_results)
        
        # Wait between batches to let system stabilize
        if batch != batches[-1]:  # Don't wait after last batch
            print(f"   ⏳ Waiting 30 seconds before next batch...")
            time.sleep(30)
    
    # Overall summary
    print(f"\n📈 Overall Stress Test Results:")
    print("=" * 50)
    
    total_agents = sum(batch['count'] for batch in batches)
    total_successful = sum(1 for r in all_results if r['status'] == 'spawned')
    total_timeouts = sum(1 for r in all_results if r['status'] == 'timeout')
    total_errors = sum(1 for r in all_results if r['status'] == 'error')
    
    print(f"   Total agents attempted: {total_agents}")
    print(f"   Successfully spawned: {total_successful}")
    print(f"   Timeouts: {total_timeouts}")
    print(f"   Errors: {total_errors}")
    print(f"   Overall success rate: {total_successful/total_agents*100:.1f}%")
    
    # System capacity assessment
    if total_successful >= 40:
        print(f"\n🏆 EXCELLENT: System handled {total_successful}+ concurrent agents!")
    elif total_successful >= 25:
        print(f"\n✅ GOOD: System handled {total_successful} concurrent agents well")
    elif total_successful >= 15:
        print(f"\n👍 FAIR: System handled {total_successful} concurrent agents adequately")
    else:
        print(f"\n⚠️  LIMITED: System struggled with high concurrency ({total_successful} successful)")
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    if total_successful >= 30:
        print(f"   - System is ready for production with high concurrency")
        print(f"   - Can handle burst loads effectively")
    elif total_successful >= 20:
        print(f"   - System handles moderate concurrent loads well")
        print(f"   - Consider rate limiting for very high loads")
    else:
        print(f"   - System may need optimization for high concurrency")
        print(f"   - Consider implementing queue management")
    
    print(f"\n🎯 Stress test completed!")

if __name__ == "__main__":
    main()