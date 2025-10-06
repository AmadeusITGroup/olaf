#!/usr/bin/env python3
"""
Benchmark Setup Script (Python version)
Prepares environment for running AI agent benchmarks
Cross-platform compatible (Windows, Linux, macOS)
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional


class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color
    
    @staticmethod
    def disable_on_windows():
        """Disable colors on Windows if not supported"""
        if sys.platform == 'win32':
            try:
                import colorama
                colorama.init()
            except ImportError:
                Colors.RED = Colors.GREEN = Colors.YELLOW = Colors.BLUE = Colors.NC = ''


class Logger:
    """Simple logging utility"""
    
    @staticmethod
    def info(message: str):
        print(f"{Colors.GREEN}[INFO]{Colors.NC} {message}")
    
    @staticmethod
    def warn(message: str):
        print(f"{Colors.YELLOW}[WARN]{Colors.NC} {message}")
    
    @staticmethod
    def error(message: str):
        print(f"{Colors.RED}[ERROR]{Colors.NC} {message}", file=sys.stderr)
    
    @staticmethod
    def success(message: str):
        print(f"{Colors.BLUE}[SUCCESS]{Colors.NC} {message}")


class BenchmarkSetup:
    """Main benchmark setup class"""
    
    VALID_LANGUAGES = ['java', 'csharp', 'cpp', 'python']
    VALID_SIZES = ['small', 'medium', 'large']
    
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        self.run_id = f"benchmark-{self.timestamp}"
        
        # Setup paths
        script_dir = Path(__file__).parent.resolve()
        self.benchmark_dir = script_dir.parent
        self.test_repos_dir = self.benchmark_dir / 'test-repositories'
        self.results_dir = self.benchmark_dir / 'results'
        self.run_dir = self.results_dir / self.run_id
        
    def validate_inputs(self) -> bool:
        """Validate command line inputs"""
        Logger.info("Validating inputs...")
        
        # Validate language
        if self.args.language not in self.VALID_LANGUAGES:
            Logger.error(f"Invalid language: {self.args.language}")
            Logger.error(f"Must be one of: {', '.join(self.VALID_LANGUAGES)}")
            return False
        
        # Validate size
        if self.args.size not in self.VALID_SIZES:
            Logger.error(f"Invalid size: {self.args.size}")
            Logger.error(f"Must be one of: {', '.join(self.VALID_SIZES)}")
            return False
        
        # Validate agent name
        if not self.args.agent:
            Logger.error("Agent name is required")
            return False
        
        Logger.success("Input validation passed")
        return True
    
    def check_repository_exists(self) -> Optional[Path]:
        """Check if test repository exists"""
        repo_path = self.test_repos_dir / self.args.language / self.args.size
        
        if not repo_path.exists() or not repo_path.is_dir():
            Logger.error(f"Test repository not found: {repo_path}")
            Logger.info("Expected directory structure:")
            Logger.info("  test-repositories/")
            Logger.info(f"    {self.args.language}/")
            Logger.info(f"      {self.args.size}/")
            return None
        
        Logger.success(f"Found test repository: {repo_path}")
        return repo_path
    
    def create_run_directory(self) -> bool:
        """Create results directory for this benchmark run"""
        try:
            self.run_dir.mkdir(parents=True, exist_ok=True)
            Logger.success(f"Created results directory: {self.run_dir}")
            return True
        except Exception as e:
            Logger.error(f"Failed to create results directory: {e}")
            return False
    
    def copy_repository(self, repo_path: Path) -> Optional[Path]:
        """Copy test repository to workspace"""
        workspace_dir = self.run_dir / 'workspace'
        
        try:
            Logger.info("Copying repository to workspace...")
            shutil.copytree(repo_path, workspace_dir)
            Logger.success(f"Repository copied to: {workspace_dir}")
            return workspace_dir
        except Exception as e:
            Logger.error(f"Failed to copy repository: {e}")
            return None
    
    def copy_baseline_metrics(self, repo_path: Path) -> bool:
        """Copy baseline metrics if available"""
        baseline_file = repo_path / 'baseline-metrics.json'
        
        if baseline_file.exists():
            try:
                dest = self.run_dir / 'baseline-metrics.json'
                shutil.copy2(baseline_file, dest)
                Logger.success("Loaded baseline metrics")
                return True
            except Exception as e:
                Logger.warn(f"Failed to copy baseline metrics: {e}")
                return False
        else:
            Logger.warn("Baseline metrics not found")
            return False
    
    def create_session_info(self, workspace_dir: Path) -> bool:
        """Create session info JSON file"""
        session_info = {
            'run_id': self.run_id,
            'timestamp': self.timestamp,
            'timestamp_iso': datetime.now().isoformat(),
            'language': self.args.language,
            'repository_size': self.args.size,
            'agent': self.args.agent,
            'model': self.args.model or '',
            'repository_path': str(self.test_repos_dir / self.args.language / self.args.size),
            'workspace_path': str(workspace_dir),
            'status': 'initialized',
            'timeout_minutes': self.args.timeout,
            'platform': sys.platform,
            'python_version': sys.version,
        }
        
        try:
            session_file = self.run_dir / 'session-info.json'
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session_info, f, indent=2)
            Logger.success("Created session info file")
            return True
        except Exception as e:
            Logger.error(f"Failed to create session info: {e}")
            return False
    
    def create_tasks_file(self) -> bool:
        """Create tasks definition file"""
        tasks = {
            'benchmark_version': '2.0',
            'tasks': [
                {
                    'id': 'task1',
                    'name': 'Repository Comprehension & Documentation Suite',
                    'duration_minutes': 60,
                    'status': 'pending',
                    'deliverables': [
                        'FUNCTIONALITY.md',
                        'ARCHITECTURE.md',
                        'BUILD.md',
                        'TESTING.md',
                        'DEVELOPMENT.md'
                    ]
                },
                {
                    'id': 'task2',
                    'name': 'Build & Test Infrastructure Automation',
                    'duration_minutes': 45,
                    'status': 'pending',
                    'deliverables': [
                        'build-all.sh',
                        'test-all.sh',
                        'metrics-collect.sh',
                        'quality-check.sh'
                    ]
                },
                {
                    'id': 'task3',
                    'name': 'Test Coverage Enhancement & Quality Improvement',
                    'duration_minutes': 90,
                    'status': 'pending',
                    'deliverables': [
                        'coverage-report.html',
                        'new-tests/',
                        'coverage-improvement.json'
                    ]
                },
                {
                    'id': 'task4',
                    'name': 'Language-Specific Refactoring Challenge',
                    'duration_minutes': 90,
                    'status': 'pending',
                    'deliverables': [
                        'refactored-code/',
                        'refactoring-report.md'
                    ]
                },
                {
                    'id': 'task5',
                    'name': 'Advanced Multi-Objective Improvement',
                    'duration_minutes': 120,
                    'status': 'pending',
                    'deliverables': [
                        'performance-improvements/',
                        'security-fixes/',
                        'final-metrics.json',
                        'improvement-report.md'
                    ]
                }
            ]
        }
        
        try:
            tasks_file = self.run_dir / 'tasks.json'
            with open(tasks_file, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, indent=2)
            Logger.success("Created tasks definition file")
            return True
        except Exception as e:
            Logger.error(f"Failed to create tasks file: {e}")
            return False
    
    def create_intervention_log(self) -> bool:
        """Create intervention logging file"""
        log_structure = {
            'run_id': self.run_id,
            'interventions': [],
            'notes': 'Log user interventions during benchmark execution'
        }
        
        try:
            log_file = self.run_dir / 'interventions.json'
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_structure, f, indent=2)
            Logger.success("Created intervention log file")
            return True
        except Exception as e:
            Logger.error(f"Failed to create intervention log: {e}")
            return False
    
    def create_readme(self, workspace_dir: Path) -> bool:
        """Create README with benchmark instructions"""
        readme_content = f"""# Benchmark Run: {self.run_id}

## Configuration

- **Language**: {self.args.language}
- **Repository Size**: {self.args.size}
- **Agent**: {self.args.agent}
- **Model**: {self.args.model or 'N/A'}
- **Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Timeout**: {self.args.timeout} minutes per task

## Directory Structure

```
{self.run_dir.name}/
├── workspace/              # Test repository (work here)
├── session-info.json       # Run configuration
├── tasks.json              # Task definitions and status
├── baseline-metrics.json   # Pre-benchmark metrics
├── interventions.json      # Log user interventions here
└── README.md               # This file
```

## Instructions

1. **Start with Task 1**: Open `tasks.json` to see task details
2. **Work in workspace/**: All code changes should be in the workspace directory
3. **Log interventions**: When you need to help the agent, add an entry to `interventions.json`
4. **Track time**: Note start/end times for each task
5. **Save deliverables**: Place task outputs in workspace/ as specified
6. **Update status**: Mark tasks as completed in `tasks.json`

## Intervention Logging Format

Add entries to `interventions.json`:

```json
{{
  "timestamp": "2025-10-06T01:15:00",
  "task_id": "task1",
  "type": "clarification|correction|guidance|technical_help",
  "description": "What you had to do",
  "time_spent_minutes": 2
}}
```

## Scoring

Run after completion:
```bash
python ../benchmark-scoring.py {self.run_dir}
```

## Task List

See `tasks.json` for detailed task descriptions and deliverables.

Good luck!
"""
        
        try:
            readme_file = self.run_dir / 'README.md'
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            Logger.success("Created README file")
            return True
        except Exception as e:
            Logger.error(f"Failed to create README: {e}")
            return False
    
    def print_summary(self, workspace_dir: Path):
        """Print setup summary"""
        print("\n" + "="*70)
        Logger.success("Benchmark environment setup complete!")
        print("="*70)
        print(f"\n{Colors.BLUE}Configuration:{Colors.NC}")
        print(f"  Language:     {self.args.language}")
        print(f"  Size:         {self.args.size}")
        print(f"  Agent:        {self.args.agent}")
        print(f"  Model:        {self.args.model or 'N/A'}")
        print(f"  Timeout:      {self.args.timeout} minutes/task")
        print(f"\n{Colors.BLUE}Paths:{Colors.NC}")
        print(f"  Run ID:       {self.run_id}")
        print(f"  Results:      {self.run_dir}")
        print(f"  Workspace:    {workspace_dir}")
        print(f"\n{Colors.BLUE}Next Steps:{Colors.NC}")
        print(f"  1. cd {workspace_dir}")
        print(f"  2. Open tasks.json to see task details")
        print(f"  3. Start with Task 1")
        print(f"  4. Log any interventions in interventions.json")
        print(f"  5. Run scoring when complete:")
        print(f"     python benchmark-scoring.py {self.run_dir}")
        print("\n" + "="*70 + "\n")
    
    def run(self) -> int:
        """Main execution flow"""
        Colors.disable_on_windows()
        
        Logger.info(f"Setting up benchmark environment")
        Logger.info(f"Run ID: {self.run_id}")
        
        # Step 1: Validate inputs
        if not self.validate_inputs():
            return 1
        
        # Step 2: Check repository exists
        repo_path = self.check_repository_exists()
        if not repo_path:
            return 1
        
        # Step 3: Create run directory
        if not self.create_run_directory():
            return 1
        
        # Step 4: Copy repository to workspace
        workspace_dir = self.copy_repository(repo_path)
        if not workspace_dir:
            return 1
        
        # Step 5: Copy baseline metrics
        self.copy_baseline_metrics(repo_path)
        
        # Step 6: Create session info
        if not self.create_session_info(workspace_dir):
            return 1
        
        # Step 7: Create tasks file
        if not self.create_tasks_file():
            return 1
        
        # Step 8: Create intervention log
        if not self.create_intervention_log():
            return 1
        
        # Step 9: Create README
        if not self.create_readme(workspace_dir):
            return 1
        
        # Step 10: Print summary
        self.print_summary(workspace_dir)
        
        return 0


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Setup AI Agent Benchmark Environment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -l java -s small -a copilot
  %(prog)s -l python -s medium -a cursor -m gpt-4
  %(prog)s --language csharp --size large --agent aider --timeout 120
        """
    )
    
    parser.add_argument(
        '-l', '--language',
        required=True,
        choices=['java', 'csharp', 'cpp', 'python'],
        help='Programming language'
    )
    
    parser.add_argument(
        '-s', '--size',
        required=True,
        choices=['small', 'medium', 'large'],
        help='Repository size'
    )
    
    parser.add_argument(
        '-a', '--agent',
        required=True,
        help='Agent name (e.g., copilot, cursor, aider, windsurf)'
    )
    
    parser.add_argument(
        '-m', '--model',
        help='Model name (e.g., gpt-4, claude-sonnet-3.5)'
    )
    
    parser.add_argument(
        '-t', '--timeout',
        type=int,
        default=60,
        help='Timeout in minutes per task (default: 60)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 2.0'
    )
    
    return parser.parse_args()


def main():
    """Main entry point"""
    try:
        args = parse_arguments()
        setup = BenchmarkSetup(args)
        return setup.run()
    except KeyboardInterrupt:
        Logger.warn("\nBenchmark setup interrupted by user")
        return 130
    except Exception as e:
        Logger.error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
