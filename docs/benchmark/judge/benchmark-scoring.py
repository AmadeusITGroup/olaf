#!/usr/bin/env python3
"""
Benchmark Scoring Script
Calculates scores for completed benchmark tasks
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class BenchmarkScorer:
    """Scores benchmark task results"""
    
    # Task weights for overall score
    TASK_WEIGHTS = {
        'task1': 0.15,  # Documentation
        'task2': 0.15,  # Automation
        'task3': 0.25,  # Testing
        'task4': 0.20,  # Language-specific
        'task5': 0.25,  # Advanced multi-objective
    }
    
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.session_info = self.load_json('session-info.json')
        self.tasks = self.load_json('tasks.json')
        self.baseline = self.load_json('baseline-metrics.json')
        
    def load_json(self, filename: str) -> Dict:
        """Load JSON file from run directory"""
        filepath = self.run_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Required file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def score_task1(self, task_data: Dict) -> Dict[str, Any]:
        """Score Task 1: Documentation Suite"""
        score_breakdown = {
            'completeness': 0,
            'accuracy': 0,
            'quality': 0,
            'autonomy': 0
        }
        
        # Check deliverables (40 points for completeness)
        required_docs = [
            'FUNCTIONALITY.md',
            'ARCHITECTURE.md',
            'BUILD.md',
            'TESTING.md',
            'DEVELOPMENT.md'
        ]
        
        docs_present = 0
        workspace = self.run_dir / 'workspace'
        for doc in required_docs:
            if (workspace / doc).exists():
                docs_present += 1
        
        score_breakdown['completeness'] = (docs_present / len(required_docs)) * 40
        
        # Accuracy (30 points) - would require manual review
        # For automation, check if docs have minimum content
        score_breakdown['accuracy'] = 30  # Placeholder - needs manual review
        
        # Quality (20 points) - would require manual review
        score_breakdown['quality'] = 20  # Placeholder - needs manual review
        
        # Autonomy (10 points)
        interventions = len(task_data.get('interventions', []))
        if interventions == 0:
            score_breakdown['autonomy'] = 10
        elif interventions <= 2:
            score_breakdown['autonomy'] = 7
        elif interventions <= 4:
            score_breakdown['autonomy'] = 4
        else:
            score_breakdown['autonomy'] = 0
        
        total_score = sum(score_breakdown.values())
        
        return {
            'score': total_score,
            'breakdown': score_breakdown,
            'max_score': 100
        }
    
    def score_task2(self, task_data: Dict) -> Dict[str, Any]:
        """Score Task 2: Automation Scripts"""
        score_breakdown = {
            'functionality': 0,
            'quality': 0,
            'integration': 0,
            'autonomy': 0
        }
        
        # Check deliverables (50 points for functionality)
        required_scripts = [
            'build-all.sh',
            'test-all.sh',
            'metrics-collect.sh',
            'quality-check.sh'
        ]
        
        scripts_present = 0
        workspace = self.run_dir / 'workspace'
        for script in required_scripts:
            script_path = workspace / script
            if script_path.exists() and script_path.stat().st_mode & 0o111:
                scripts_present += 1
        
        score_breakdown['functionality'] = (scripts_present / len(required_scripts)) * 50
        
        # Quality (30 points) - placeholder
        score_breakdown['quality'] = 30
        
        # Integration (10 points) - placeholder
        score_breakdown['integration'] = 10
        
        # Autonomy (10 points)
        interventions = len(task_data.get('interventions', []))
        if interventions == 0:
            score_breakdown['autonomy'] = 10
        elif interventions <= 2:
            score_breakdown['autonomy'] = 7
        elif interventions <= 4:
            score_breakdown['autonomy'] = 4
        else:
            score_breakdown['autonomy'] = 0
        
        total_score = sum(score_breakdown.values())
        
        return {
            'score': total_score,
            'breakdown': score_breakdown,
            'max_score': 100
        }
    
    def calculate_overall_score(self) -> Dict[str, Any]:
        """Calculate overall benchmark score"""
        task_scores = {}
        weighted_sum = 0
        total_weight = 0
        
        for task in self.tasks['tasks']:
            task_id = task['id']
            if task['status'] == 'completed' and task['score'] is not None:
                task_scores[task_id] = task['score']
                weight = self.TASK_WEIGHTS.get(task_id, 0)
                weighted_sum += task['score'] * weight
                total_weight += weight
        
        overall_score = weighted_sum / total_weight if total_weight > 0 else 0
        
        # Determine tier
        if overall_score >= 90:
            tier = "Elite"
        elif overall_score >= 80:
            tier = "Advanced"
        elif overall_score >= 70:
            tier = "Proficient"
        elif overall_score >= 60:
            tier = "Intermediate"
        elif overall_score >= 50:
            tier = "Basic"
        else:
            tier = "Novice"
        
        return {
            'overall_score': round(overall_score, 2),
            'tier': tier,
            'task_scores': task_scores,
            'tasks_completed': len(task_scores),
            'total_tasks': len(self.tasks['tasks'])
        }
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive scoring report"""
        overall = self.calculate_overall_score()
        
        report = {
            'run_id': self.session_info['run_id'],
            'timestamp': datetime.now().isoformat(),
            'session': self.session_info,
            'overall': overall,
            'tasks': []
        }
        
        for task in self.tasks['tasks']:
            task_report = {
                'id': task['id'],
                'name': task['name'],
                'status': task['status'],
                'score': task.get('score'),
                'duration_seconds': task.get('duration_seconds'),
                'interventions': len(task.get('interventions', []))
            }
            report['tasks'].append(task_report)
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """Print formatted report"""
        print("=" * 60)
        print("BENCHMARK SCORING REPORT")
        print("=" * 60)
        print(f"\nRun ID: {report['run_id']}")
        print(f"Agent: {report['session']['agent']}")
        print(f"Model: {report['session'].get('model', 'N/A')}")
        print(f"Language: {report['session']['language']}")
        print(f"Repository Size: {report['session']['repository_size']}")
        
        print(f"\n{'OVERALL SCORE':>30}: {report['overall']['overall_score']:.2f}/100")
        print(f"{'TIER':>30}: {report['overall']['tier']}")
        print(f"{'TASKS COMPLETED':>30}: {report['overall']['tasks_completed']}/{report['overall']['total_tasks']}")
        
        print("\n" + "-" * 60)
        print("TASK SCORES")
        print("-" * 60)
        
        for task in report['tasks']:
            print(f"\n{task['name']}")
            print(f"  Status: {task['status']}")
            if task['score'] is not None:
                print(f"  Score: {task['score']:.2f}/100")
            if task['duration_seconds'] is not None:
                minutes = task['duration_seconds'] // 60
                seconds = task['duration_seconds'] % 60
                print(f"  Duration: {minutes}m {seconds}s")
            print(f"  Interventions: {task['interventions']}")
        
        print("\n" + "=" * 60)

def main():
    if len(sys.argv) < 2:
        print("Usage: benchmark-score.py <run_directory>")
        sys.exit(1)
    
    run_dir = Path(sys.argv[1])
    if not run_dir.exists():
        print(f"Error: Run directory not found: {run_dir}")
        sys.exit(1)
    
    scorer = BenchmarkScorer(run_dir)
    report = scorer.generate_report()
    scorer.print_report(report)
    
    # Save report
    report_file = run_dir / 'scoring-report.json'
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: {report_file}")

if __name__ == '__main__':
    main()