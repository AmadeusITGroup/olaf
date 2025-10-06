# Benchmark Framework Improvements - Detailed Explanation

This document explains three suggested enhancements to your benchmark framework with concrete examples and implementation guidance.

---

## 1. Add Explicit Timeout Handling in Scripts

### **The Problem**

Currently, your benchmark protocol mentions time budgets (e.g., "60 minutes for Task 1"), but there's no automated enforcement. This means:

- An agent could run indefinitely if it gets stuck
- Human observers must manually track time and interrupt
- Results are inconsistent (some runs stopped early, others allowed to continue)
- Scoring doesn't account for incomplete work due to timeout

### **Why This Matters**

In real-world development:
- Developers have deadlines
- Stuck processes waste resources
- Time efficiency is a key metric
- Automated CI/CD pipelines need hard limits

### **Concrete Example**

**Current Situation:**
```python
# benchmark-scoring.py currently has no timeout logic
def score_task1(self, task_data: Dict) -> Dict[str, Any]:
    # Assumes task completed, no timeout check
    if interventions == 0:
        score_breakdown['autonomy'] = 10
```

**Problem Scenario:**
- Task 1 has 60-minute budget
- Agent gets stuck analyzing a large dependency tree at minute 45
- Human must decide: wait longer? interrupt? how to score?
- Inconsistent across different benchmark runs

### **Proposed Solution**

#### A. Add timeout wrapper to execution scripts

**New file: `benchmark-timeout-wrapper.py`**
```python
import subprocess
import signal
from datetime import datetime, timedelta

class TimeoutExecutor:
    """Execute benchmark task with hard timeout"""
    
    def run_with_timeout(self, task_id: str, timeout_minutes: int):
        """
        Run task with automatic timeout
        Returns: (completed: bool, duration_seconds: float, timed_out: bool)
        """
        start_time = datetime.now()
        deadline = start_time + timedelta(minutes=timeout_minutes)
        
        try:
            # Start monitoring (agent works in workspace)
            while datetime.now() < deadline:
                time.sleep(10)  # Check every 10 seconds
                
                # Check if agent marked task as complete
                if self.check_task_completion(task_id):
                    duration = (datetime.now() - start_time).total_seconds()
                    return True, duration, False
            
            # Timeout reached
            duration = (datetime.now() - start_time).total_seconds()
            self.log_timeout(task_id, timeout_minutes)
            return False, duration, True
            
        except KeyboardInterrupt:
            # Manual intervention
            duration = (datetime.now() - start_time).total_seconds()
            return False, duration, False
    
    def check_task_completion(self, task_id: str) -> bool:
        """Check if agent completed task (marked in tasks.json)"""
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
        
        for task in tasks['tasks']:
            if task['id'] == task_id:
                return task.get('status') == 'completed'
        
        return False
    
    def log_timeout(self, task_id: str, minutes: int):
        """Log timeout event"""
        with open('interventions.json', 'r+') as f:
            data = json.load(f)
            data['interventions'].append({
                'timestamp': datetime.now().isoformat(),
                'task_id': task_id,
                'type': 'timeout',
                'description': f'Task exceeded {minutes} minute timeout',
                'auto_generated': True
            })
            f.seek(0)
            json.dump(data, f, indent=2)
```

#### B. Update scoring to handle timeouts

```python
def score_task1(self, task_data: Dict) -> Dict[str, Any]:
    """Score Task 1 with timeout handling"""
    score_breakdown = {
        'completeness': 0,
        'accuracy': 0,
        'quality': 0,
        'autonomy': 0
    }
    
    # NEW: Check if task timed out
    timed_out = task_data.get('timed_out', False)
    duration_minutes = task_data.get('duration_seconds', 0) / 60
    
    if timed_out:
        # Partial credit based on what was completed
        completeness_ratio = self.calculate_partial_completion(task_data)
        score_breakdown['completeness'] = completeness_ratio * 40
        
        # Penalize quality scores for incomplete work
        score_breakdown['accuracy'] = completeness_ratio * 30 * 0.7  # 30% penalty
        score_breakdown['quality'] = completeness_ratio * 20 * 0.7
        
        # Zero autonomy points for timeout
        score_breakdown['autonomy'] = 0
    else:
        # Existing scoring logic
        # ...
    
    return {
        'score': sum(score_breakdown.values()),
        'breakdown': score_breakdown,
        'max_score': 100,
        'timed_out': timed_out,
        'duration_minutes': duration_minutes
    }
```

#### C. Add timeout config to session

```json
{
  "run_id": "benchmark-20251006-0115",
  "timeouts": {
    "task1": 60,
    "task2": 45,
    "task3": 90,
    "task4": 90,
    "task5": 120,
    "enforcement": "hard",  // or "soft" (warning only)
    "grace_period_seconds": 60  // 1 minute warning before kill
  }
}
```

### **Benefits**

✅ Consistent measurement across all benchmark runs  
✅ Automated execution without human monitoring  
✅ Fair comparison (all agents get same time)  
✅ Realistic simulation of time-constrained work  
✅ CI/CD integration possible  

---

## 2. Consider Adding a "Partial Success" Scoring Dimension

### **The Problem**

Your current scoring is binary or completion-based:
- Task 1: "All 5 documents created: 20 points" (all or nothing)
- This doesn't capture nuanced performance
- An agent that creates 4 perfect documents gets same score as one that creates 0

### **Why This Matters**

In real-world development:
- Partial progress has value
- Developers prioritize work (complete critical parts first)
- 80% correct is better than 0% complete
- Ability to deliver under constraints matters

### **Concrete Example**

**Current Scoring (Task 1 Completeness):**
```python
# All or nothing approach
docs_present = 0
for doc in required_docs:
    if (workspace / doc).exists():
        docs_present += 1

score_breakdown['completeness'] = (docs_present / len(required_docs)) * 40
```

**Problem Scenario:**
- Agent A: Creates all 5 docs, but each is 50% incomplete (many sections missing)
  - Score: 40 points (5/5 docs present)
- Agent B: Creates 3 docs, each is 100% complete and excellent
  - Score: 24 points (3/5 docs present)
- Agent B performed better but scored lower!

### **Proposed Solution**

#### Add multi-level completeness scoring

```python
def score_task1_enhanced(self, task_data: Dict) -> Dict[str, Any]:
    """Enhanced scoring with partial success dimensions"""
    
    # DIMENSION 1: Deliverable presence (20 points)
    presence_score = self.score_deliverable_presence()
    
    # DIMENSION 2: Deliverable completeness (20 points)
    completeness_score = self.score_deliverable_completeness()
    
    # DIMENSION 3: Content accuracy (30 points)
    accuracy_score = self.score_content_accuracy()
    
    # DIMENSION 4: Content quality (20 points)
    quality_score = self.score_content_quality()
    
    # DIMENSION 5: Autonomy (10 points)
    autonomy_score = self.score_autonomy()
    
    score_breakdown = {
        'presence': presence_score,        # File exists
        'completeness': completeness_score, # All sections present
        'accuracy': accuracy_score,         # Information correct
        'quality': quality_score,           # Well-written, useful
        'autonomy': autonomy_score         # No intervention needed
    }
    
    return {
        'score': sum(score_breakdown.values()),
        'breakdown': score_breakdown,
        'max_score': 100
    }
```

#### Detailed completeness checking

```python
def score_deliverable_completeness(self) -> float:
    """Check if deliverables have all required sections"""
    
    required_sections = {
        'FUNCTIONALITY.md': [
            'Purpose and objectives',
            'Key features',
            'Main components',
            'Technology stack',
            'Entry points',
            'Usage examples'
        ],
        'ARCHITECTURE.md': [
            'Project structure',
            'Module relationships',
            'Design patterns',
            'Data flow',
            'Configuration',
            'Key abstractions',
            'Architectural diagrams'
        ],
        # ... other documents
    }
    
    total_sections = 0
    present_sections = 0
    
    for doc_name, sections in required_sections.items():
        doc_path = self.workspace / doc_name
        
        if not doc_path.exists():
            total_sections += len(sections)
            continue
        
        content = doc_path.read_text()
        
        for section in sections:
            total_sections += 1
            # Check if section exists (heading or keywords)
            if self.section_exists(content, section):
                present_sections += 1
    
    return (present_sections / total_sections) * 20 if total_sections > 0 else 0
```

#### Priority-based scoring

```python
def score_with_priorities(self) -> Dict:
    """Score with prioritized deliverables"""
    
    # Define criticality levels
    deliverables_priority = {
        'FUNCTIONALITY.md': 'critical',    # Must have (3x weight)
        'ARCHITECTURE.md': 'critical',     # Must have (3x weight)
        'BUILD.md': 'important',           # Should have (2x weight)
        'TESTING.md': 'important',         # Should have (2x weight)
        'DEVELOPMENT.md': 'nice-to-have'   # Could have (1x weight)
    }
    
    weights = {'critical': 3, 'important': 2, 'nice-to-have': 1}
    
    weighted_score = 0
    max_possible = 0
    
    for doc, priority in deliverables_priority.items():
        weight = weights[priority]
        doc_score = self.score_document(doc)  # 0-100
        
        weighted_score += doc_score * weight
        max_possible += 100 * weight
    
    return {
        'weighted_score': (weighted_score / max_possible) * 40,
        'prioritization_quality': self.assess_agent_prioritization()
    }
```

### **Benefits**

✅ More nuanced agent comparison  
✅ Rewards partial progress appropriately  
✅ Identifies agents that prioritize well  
✅ Better reflects real-world development  
✅ Encourages "fail gracefully" behavior  

---

## 3. Include Memory/Resource Consumption Metrics for Agents

### **The Problem**

Your benchmark measures:
- ✅ Time taken
- ✅ Code quality
- ✅ Task completion
- ❌ Resource usage

But not:
- How much memory did the agent use?
- How many API calls were made?
- How much did this cost?
- Is the agent efficient or wasteful?

### **Why This Matters**

In real-world scenarios:
- API costs money (GPT-4 tokens are expensive)
- Memory limits exist (especially in containers)
- Network usage matters (bandwidth, latency)
- Efficiency affects scalability

### **Concrete Example**

**Scenario: Two agents complete Task 1 in 50 minutes**

**Agent A:**
- Reads each file once
- Generates documentation in single pass
- Uses 500MB RAM
- Makes 30 API calls
- Total tokens: 50,000
- Estimated cost: $0.75

**Agent B:**
- Re-reads files multiple times
- Regenerates sections repeatedly
- Uses 2GB RAM
- Makes 300 API calls
- Total tokens: 500,000
- Estimated cost: $7.50

**Current benchmark: Both score equally** (same time, same output quality)  
**Real-world: Agent A is 10x more efficient and cost-effective**

### **Proposed Solution**

#### A. Add resource monitoring wrapper

**New file: `benchmark-resource-monitor.py`**
```python
import psutil
import time
from dataclasses import dataclass
from typing import List

@dataclass
class ResourceSnapshot:
    """Resource usage at a point in time"""
    timestamp: float
    memory_mb: float
    cpu_percent: float
    disk_io_mb: float
    network_io_mb: float

class ResourceMonitor:
    """Monitor resource usage during benchmark execution"""
    
    def __init__(self, process_name: str, interval_seconds: int = 10):
        self.process_name = process_name
        self.interval = interval_seconds
        self.snapshots: List[ResourceSnapshot] = []
        self.running = False
    
    def start(self):
        """Start monitoring in background thread"""
        self.running = True
        import threading
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def stop(self) -> Dict:
        """Stop monitoring and return statistics"""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join(timeout=5)
        
        return self.calculate_statistics()
    
    def _monitor_loop(self):
        """Background monitoring loop"""
        process = self._find_process()
        if not process:
            return
        
        while self.running:
            try:
                snapshot = ResourceSnapshot(
                    timestamp=time.time(),
                    memory_mb=process.memory_info().rss / 1024 / 1024,
                    cpu_percent=process.cpu_percent(interval=1),
                    disk_io_mb=self._get_io_counters(process, 'disk'),
                    network_io_mb=self._get_io_counters(process, 'network')
                )
                self.snapshots.append(snapshot)
                time.sleep(self.interval)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                break
    
    def calculate_statistics(self) -> Dict:
        """Calculate resource usage statistics"""
        if not self.snapshots:
            return self._empty_stats()
        
        memory_values = [s.memory_mb for s in self.snapshots]
        cpu_values = [s.cpu_percent for s in self.snapshots]
        
        return {
            'memory_mb': {
                'min': min(memory_values),
                'max': max(memory_values),
                'avg': sum(memory_values) / len(memory_values),
                'peak': max(memory_values)
            },
            'cpu_percent': {
                'min': min(cpu_values),
                'max': max(cpu_values),
                'avg': sum(cpu_values) / len(cpu_values)
            },
            'duration_seconds': self.snapshots[-1].timestamp - self.snapshots[0].timestamp,
            'samples_collected': len(self.snapshots)
        }
```

#### B. Add API call tracking

**Modify session-info.json to track API metrics:**
```json
{
  "run_id": "benchmark-20251006-0115",
  "agent": "cursor",
  "model": "gpt-4",
  "resource_metrics": {
    "api_calls": {
      "total_requests": 45,
      "by_task": {
        "task1": 30,
        "task2": 15
      },
      "by_type": {
        "code_completion": 20,
        "chat": 15,
        "edit": 10
      }
    },
    "tokens": {
      "total_input": 125000,
      "total_output": 35000,
      "total_combined": 160000,
      "by_task": {
        "task1": {"input": 80000, "output": 20000},
        "task2": {"input": 45000, "output": 15000}
      }
    },
    "cost_estimates": {
      "total_usd": 2.40,
      "by_task": {
        "task1": 1.50,
        "task2": 0.90
      },
      "rate_card": {
        "input_per_1k": 0.01,
        "output_per_1k": 0.03
      }
    }
  }
}
```

#### C. Add efficiency scoring dimension

```python
def score_efficiency(self, task_data: Dict) -> Dict:
    """Score resource efficiency"""
    
    resources = task_data.get('resource_metrics', {})
    
    # Memory efficiency (10 points)
    # Penalize if using more than reasonable threshold
    memory_score = 10
    peak_memory_mb = resources.get('memory_mb', {}).get('peak', 0)
    if peak_memory_mb > 1000:  # 1GB threshold
        memory_score = max(0, 10 - (peak_memory_mb - 1000) / 200)
    
    # API call efficiency (10 points)
    # Fewer calls = better (for same quality)
    api_calls = resources.get('api_calls', {}).get('total_requests', 0)
    api_score = 10
    if api_calls > 50:  # 50 calls threshold for Task 1
        api_score = max(0, 10 - (api_calls - 50) / 10)
    
    # Token efficiency (10 points)
    # Measure tokens per output quality
    tokens = resources.get('tokens', {}).get('total_combined', 0)
    quality_score = task_data.get('score', 0)  # Base quality score
    
    if quality_score > 0 and tokens > 0:
        tokens_per_quality_point = tokens / quality_score
        # Lower is better
        if tokens_per_quality_point < 1000:
            token_score = 10
        elif tokens_per_quality_point < 2000:
            token_score = 7
        elif tokens_per_quality_point < 3000:
            token_score = 4
        else:
            token_score = 0
    else:
        token_score = 0
    
    # Cost efficiency (10 points)
    cost = resources.get('cost_estimates', {}).get('total_usd', 0)
    cost_score = 10
    if cost > 1.0:  # $1 threshold
        cost_score = max(0, 10 - (cost - 1.0) * 5)
    
    return {
        'memory_efficiency': memory_score,
        'api_efficiency': api_score,
        'token_efficiency': token_score,
        'cost_efficiency': cost_score,
        'total_efficiency_score': memory_score + api_score + token_score + cost_score,
        'max_efficiency_score': 40
    }
```

#### D. Add efficiency comparison in reports

```python
def generate_comparison_report(self, run_dirs: List[Path]):
    """Generate cross-agent comparison with efficiency metrics"""
    
    agents_data = []
    
    for run_dir in run_dirs:
        session_info = self.load_json(run_dir / 'session-info.json')
        scores = self.load_json(run_dir / 'scores.json')
        
        agents_data.append({
            'agent': session_info['agent'],
            'model': session_info['model'],
            'quality_score': scores['overall_score'],
            'efficiency_score': scores.get('efficiency_score', 0),
            'total_cost': session_info['resource_metrics']['cost_estimates']['total_usd'],
            'api_calls': session_info['resource_metrics']['api_calls']['total_requests'],
            'tokens': session_info['resource_metrics']['tokens']['total_combined']
        })
    
    # Generate comparison table
    print("\n" + "="*100)
    print(f"{'Agent':<15} {'Model':<20} {'Quality':<10} {'Efficiency':<12} {'Cost':<10} {'API Calls':<12} {'Tokens':<12}")
    print("="*100)
    
    for data in sorted(agents_data, key=lambda x: x['quality_score'], reverse=True):
        print(f"{data['agent']:<15} "
              f"{data['model']:<20} "
              f"{data['quality_score']:<10.1f} "
              f"{data['efficiency_score']:<12.1f} "
              f"${data['total_cost']:<9.2f} "
              f"{data['api_calls']:<12} "
              f"{data['tokens']:<12}")
    
    print("="*100)
    
    # Calculate value score (quality per dollar)
    print("\n" + "Value Rankings (Quality Score / Cost):")
    for data in sorted(agents_data, key=lambda x: x['quality_score']/max(x['total_cost'], 0.01), reverse=True):
        value = data['quality_score'] / max(data['total_cost'], 0.01)
        print(f"  {data['agent']}: {value:.1f} points per dollar")
```

### **Benefits**

✅ Identifies resource-efficient agents  
✅ Tracks actual costs for comparison  
✅ Prevents memory leaks/resource abuse  
✅ Enables cost-benefit analysis  
✅ Real-world operational concerns addressed  
✅ Helps choose agent for production use  

---

## Summary

These three improvements transform your benchmark from "does it work?" to "how efficiently does it work in real-world conditions?"

| Enhancement | Impact | Complexity | Priority |
|------------|--------|------------|----------|
| **Timeout Handling** | High - ensures fair comparison | Medium | **High** |
| **Partial Success Scoring** | High - more nuanced insights | Low-Medium | **High** |
| **Resource Metrics** | Medium-High - operational concerns | Medium-High | **Medium** |

### Implementation Order

1. **Phase 1**: Timeout handling (foundational)
2. **Phase 2**: Partial success scoring (improves insights)
3. **Phase 3**: Resource metrics (operational excellence)

### Quick Wins

- Add timeout wrapper first (can be done in 1-2 hours)
- Start tracking API calls manually in interventions.json
- Add "sections present" check to scoring script

---

**Last Updated**: 2025-10-06  
**Version**: 1.0
