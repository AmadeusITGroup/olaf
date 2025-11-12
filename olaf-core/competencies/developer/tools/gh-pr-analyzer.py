#!/usr/bin/env python3
"""
GitHub PR Analyzer using GitHub CLI
Collects comprehensive PR data for code review analysis.

Usage:
    python gh-pr-analyzer.py --pr 123
    python gh-pr-analyzer.py --branch feature/my-branch
    python gh-pr-analyzer.py --latest-open
"""

import subprocess
import json
import sys
import argparse
from typing import Dict, Any, Optional, List
from datetime import datetime

class GitHubPRAnalyzer:
    def __init__(self):
        self._check_auth()
        self.repo_info = self._get_repo_info()
        
    def _check_auth(self):
        """Check GitHub CLI authentication status."""
        print("🔐 Checking GitHub CLI authentication...")
        output, code = self._run_gh_command(['auth', 'status'])
        if code != 0:
            print("❌ ERROR: GitHub CLI is not authenticated!")
            print("Please run: gh auth login")
            print("Then try again.")
            sys.exit(1)
        print("✅ GitHub CLI authentication verified")
        
    def _run_gh_command(self, cmd: List[str]) -> tuple[str, int]:
        """Run GitHub CLI command and return output and exit code."""
        try:
            result = subprocess.run(['gh'] + cmd, 
                                  capture_output=True, 
                                  text=True, 
                                  check=False)
            return result.stdout.strip(), result.returncode
        except FileNotFoundError:
            print("ERROR: GitHub CLI (gh) not found. Please install GitHub CLI.")
            sys.exit(1)
            
    def _get_repo_info(self) -> Dict[str, Any]:
        """Get current repository information."""
        print("🔍 Getting repository information...")
        
        # Get repo name and owner
        output, code = self._run_gh_command(['repo', 'view', '--json', 'name,owner,defaultBranchRef'])
        if code != 0:
            print(f"ERROR: Failed to get repo info: {output}")
            sys.exit(1)
            
        repo_data = json.loads(output)
        
        # Get current branch
        git_result = subprocess.run(['git', 'branch', '--show-current'], 
                                   capture_output=True, text=True)
        current_branch = git_result.stdout.strip() if git_result.returncode == 0 else "unknown"
        
        return {
            'name': repo_data['name'],
            'owner': repo_data['owner']['login'],
            'default_branch': repo_data['defaultBranchRef']['name'],
            'current_branch': current_branch,
            'full_name': f"{repo_data['owner']['login']}/{repo_data['name']}"
        }
        
    def get_pr_by_number(self, pr_number: int) -> Optional[Dict[str, Any]]:
        """Get PR details by PR number."""
        print(f"🔍 Analyzing PR #{pr_number}...")
        
        # Get basic PR details first
        basic_fields = ['title', 'body', 'state', 'number', 'createdAt', 'updatedAt', 'baseRefName', 'headRefName', 'author']
        
        output, code = self._run_gh_command([
            'pr', 'view', str(pr_number), 
            '--json', ','.join(basic_fields)
        ])
        
        if code != 0:
            print(f"ERROR: Failed to get PR #{pr_number}: {output}")
            return None
            
        pr_data = json.loads(output)
        
        # Get additional fields separately to avoid API issues
        try:
            # Get mergeable status
            merge_output, _ = self._run_gh_command([
                'pr', 'view', str(pr_number), '--json', 'mergeable,merged,mergedAt'
            ])
            if merge_output:
                merge_data = json.loads(merge_output)
                pr_data.update(merge_data)
        except:
            pass
            
        try:
            # Get statistics
            stats_output, _ = self._run_gh_command([
                'pr', 'view', str(pr_number), '--json', 'additions,deletions,changedFiles'
            ])
            if stats_output:
                stats_data = json.loads(stats_output)
                pr_data.update(stats_data)
        except:
            pass
        
        # Get PR diff
        print(f"📄 Getting diff for PR #{pr_number}...")
        diff_output, diff_code = self._run_gh_command(['pr', 'diff', str(pr_number)])
        pr_data['diff'] = diff_output if diff_code == 0 else "Failed to get diff"
        
        # Get changed files list
        print(f"📁 Getting changed files for PR #{pr_number}...")
        files_output, files_code = self._run_gh_command([
            'pr', 'view', str(pr_number), 
            '--json', 'files'
        ])
        if files_code == 0:
            files_data = json.loads(files_output)
            pr_data['files'] = files_data.get('files', [])
        
        return pr_data
        
    def get_latest_pr_for_branch(self, branch: str) -> Optional[Dict[str, Any]]:
        """Get the latest PR for a specific branch."""
        print(f"🔍 Finding latest PR for branch '{branch}'...")
        
        # List PRs for the branch (head branch)
        output, code = self._run_gh_command([
            'pr', 'list', 
            '--head', branch,
            '--json', 'number,title,state,createdAt',
            '--limit', '1'
        ])
        
        if code != 0:
            print(f"ERROR: Failed to list PRs for branch '{branch}': {output}")
            return None
            
        prs = json.loads(output)
        if not prs:
            print(f"No PRs found for branch '{branch}'")
            return None
            
        latest_pr = prs[0]
        print(f"Found PR #{latest_pr['number']}: {latest_pr['title']}")
        
        return self.get_pr_by_number(latest_pr['number'])
        
    def get_latest_open_pr(self) -> Optional[Dict[str, Any]]:
        """Get the most recent open PR."""
        print("🔍 Finding latest open PR...")
        
        output, code = self._run_gh_command([
            'pr', 'list',
            '--state', 'open',
            '--json', 'number,title,createdAt',
            '--limit', '1'
        ])
        
        if code != 0:
            print(f"ERROR: Failed to list open PRs: {output}")
            return None
            
        prs = json.loads(output)
        if not prs:
            print("No open PRs found")
            return None
            
        latest_pr = prs[0]
        print(f"Found latest open PR #{latest_pr['number']}: {latest_pr['title']}")
        
        return self.get_pr_by_number(latest_pr['number'])
        
    def format_pr_analysis(self, pr_data: Dict[str, Any]) -> str:
        """Format PR data for analysis."""
        if not pr_data:
            return "No PR data available"
            
        # Header
        analysis = f"""
=== GitHub PR Analysis Report ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Repository: {self.repo_info['full_name']}

=== PR OVERVIEW ===
Number: #{pr_data['number']}
Title: {pr_data['title']}
State: {pr_data['state']}
Author: {pr_data['author']['login']} ({pr_data['author'].get('name', 'N/A')})
Created: {pr_data['createdAt']}
Updated: {pr_data['updatedAt']}

=== BRANCH INFO ===
Base Branch: {pr_data['baseRefName']} 
Head Branch: {pr_data['headRefName']}
Mergeable: {pr_data.get('mergeable', 'Unknown')}
Merged: {pr_data.get('merged', False)}
"""

        if pr_data.get('mergedAt'):
            analysis += f"Merged At: {pr_data['mergedAt']}\n"
            
        # Statistics
        analysis += f"""
=== CHANGE STATISTICS ===
Changed Files: {pr_data.get('changedFiles', 0)}
Additions: +{pr_data.get('additions', 0)}
Deletions: -{pr_data.get('deletions', 0)}
Commits: {len(pr_data.get('commits', []))}
"""

        # Description
        if pr_data.get('body'):
            analysis += f"""
=== DESCRIPTION ===
{pr_data['body']}
"""

        # Files changed
        if pr_data.get('files'):
            analysis += "\n=== CHANGED FILES ===\n"
            for file_info in pr_data['files']:
                additions = file_info.get('additions', 0)
                deletions = file_info.get('deletions', 0)
                analysis += f"📁 {file_info['path']} (+{additions}/-{deletions})\n"
                
        # Reviews
        if pr_data.get('reviews'):
            analysis += "\n=== REVIEWS ===\n"
            for review in pr_data['reviews']:
                analysis += f"👤 {review['author']['login']}: {review['state']} - {review.get('submittedAt', 'N/A')}\n"
                if review.get('body'):
                    analysis += f"   💬 {review['body'][:100]}...\n"
                    
        # Status checks
        if pr_data.get('statusCheckRollup'):
            analysis += "\n=== STATUS CHECKS ===\n"
            for context in pr_data['statusCheckRollup'].get('contexts', []):
                status = context.get('conclusion') or context.get('state', 'Unknown')
                analysis += f"✅ {context.get('context', 'Unknown')}: {status}\n"
                
        # Diff
        if pr_data.get('diff'):
            analysis += f"""
=== DIFF ===
{pr_data['diff']}
"""

        return analysis

def main():
    parser = argparse.ArgumentParser(description='GitHub PR Analyzer using GitHub CLI')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--pr', type=int, help='PR number to analyze')
    group.add_argument('--branch', help='Branch name to find latest PR for')
    group.add_argument('--latest-open', action='store_true', help='Get latest open PR')
    
    args = parser.parse_args()
    
    analyzer = GitHubPRAnalyzer()
    
    print(f"🏛️  Repository: {analyzer.repo_info['full_name']}")
    print(f"🌿 Current Branch: {analyzer.repo_info['current_branch']}")
    print(f"🎯 Default Branch: {analyzer.repo_info['default_branch']}")
    print()
    
    pr_data = None
    
    if args.pr:
        pr_data = analyzer.get_pr_by_number(args.pr)
    elif args.branch:
        pr_data = analyzer.get_latest_pr_for_branch(args.branch)
    elif args.latest_open:
        pr_data = analyzer.get_latest_open_pr()
        
    if pr_data:
        analysis = analyzer.format_pr_analysis(pr_data)
        print(analysis)
    else:
        print("❌ No PR data found")
        sys.exit(1)

if __name__ == '__main__':
    main()