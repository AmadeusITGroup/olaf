#!/usr/bin/env python3
"""
Example: Using OLAF Strands API for Async Agent Management
Demonstrates how a calling agent can spawn and manage OLAF Strands agents
"""

import time
from olaf_strands_api import OLAFStrandsAPI

def main():
    print("🚀 OLAF Strands Async Agent Example")
    print("=" * 40)
    
    # Initialize API
    api = OLAFStrandsAPI(project_root="../../../..")
    print(f"📁 Project root: {api.project_root}")
    
    # Example 1: Spawn an agent
    print("\n1️⃣ Spawning background agent...")
    result = api.spawn_agent(
        prompt="developer/review-code.md",
        context="Review the OLAF Strands integration code for improvements and best practices",
        service_provider="aws-bedrock"
    )
    
    if result['status'] == 'spawned':
        task_id = result['task_id']
        print(f"✅ Agent spawned successfully!")
        print(f"📋 Task ID: {task_id}")
        
        # Example 2: Monitor progress
        print(f"\n2️⃣ Monitoring agent progress...")
        max_checks = 10
        check_count = 0
        
        while check_count < max_checks:
            status = api.check_status(task_id)
            print(f"🔍 Check {check_count + 1}: Status = {status.get('status', 'unknown')}")
            
            if status.get('status') == 'running':
                # Show resource usage if available
                if 'cpu_percent' in status:
                    print(f"   💻 CPU: {status['cpu_percent']:.1f}%, Memory: {status.get('memory_mb', 0):.1f}MB")
            
            elif status.get('status') == 'completed':
                print("✅ Agent completed!")
                break
            
            elif status.get('status') in ['failed', 'error']:
                print(f"❌ Agent failed: {status.get('error', 'Unknown error')}")
                return
            
            check_count += 1
            if check_count < max_checks:
                print("   ⏳ Waiting 3 seconds...")
                time.sleep(3)
        
        # Example 3: Get results
        if status.get('status') == 'completed':
            print(f"\n3️⃣ Retrieving results...")
            output = api.get_output(task_id)
            
            if 'main_result' in output:
                print("📄 Main Result Preview:")
                preview = output['main_result'][:300]
                print(f"   {preview}...")
                print(f"\n📁 Results files: {len(output.get('results_files', []))} files")
                for file in output.get('results_files', []):
                    print(f"   - {file}")
            else:
                print("⚠️  No main result found, but process completed")
                print(f"📊 Output: {output}")
        
        else:
            print(f"⏰ Agent still running after {max_checks} checks")
            print("💡 You can check status later with:")
            print(f"   python olaf_strands_wrapper.py --status --task-id {task_id}")
    
    else:
        print(f"❌ Failed to spawn agent: {result.get('error', 'Unknown error')}")
    
    # Example 4: List all processes
    print(f"\n4️⃣ Listing all agent processes...")
    processes = api.list_processes()
    
    if processes:
        print(f"📋 Found {len(processes)} processes:")
        for proc in processes:
            print(f"   {proc.get('task_id', 'unknown')}: {proc.get('status', 'unknown')}")
    else:
        print("📭 No processes found")
    
    print(f"\n🎉 Example completed!")
    print(f"💡 This demonstrates how your calling agent can:")
    print(f"   - Spawn OLAF agents as background processes")
    print(f"   - Monitor their progress without blocking")
    print(f"   - Retrieve results when ready")
    print(f"   - Manage multiple concurrent agents")

if __name__ == "__main__":
    main()