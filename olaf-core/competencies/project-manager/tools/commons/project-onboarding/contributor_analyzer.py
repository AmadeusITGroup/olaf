#!/usr/bin/env python3
"""
Generic Git Contributor Analysis Tool
Analyzes contributor patterns, bus factor, and knowledge distribution risks for any Git repository.
"""

import argparse
import subprocess
import json
import logging
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from pathlib import Path
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContributorAnalyzer:
    def __init__(self, repo_path, analysis_period_months=12, output_file=None):
        self.repo_path = Path(repo_path).resolve()
        self.analysis_period_months = analysis_period_months
        self.output_file = output_file
        self.since_date = (datetime.now() - timedelta(days=30 * analysis_period_months)).strftime('%Y-%m-%d')
        
        # Verify repository exists and is a git repo
        if not self.repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")
        
        git_dir = self.repo_path / '.git'
        if not git_dir.exists():
            raise ValueError(f"Not a git repository: {repo_path}")
    
    def run_git_command(self, cmd):
        """Execute git command and return output"""
        try:
            result = subprocess.run(
                cmd, 
                cwd=self.repo_path, 
                capture_output=True, 
                text=True, 
                encoding='utf-8',
                errors='replace',
                check=True
            )
            return result.stdout.strip() if result.stdout else ""
        except subprocess.CalledProcessError as e:
            logger.error(f"Git command failed: {' '.join(cmd)}")
            logger.error(f"Error: {e.stderr}")
            return ""
    
    def get_contributor_stats(self):
        """Get basic contributor statistics"""
        logger.info("Analyzing contributor statistics...")
        
        # Get all commits since analysis period
        total_commits_cmd = ['git', 'log', '--oneline', f'--since={self.since_date}']
        total_commits = len(self.run_git_command(total_commits_cmd).split('\n')) if self.run_git_command(total_commits_cmd) else 0
        
        # Get contributor commit counts
        contributors_cmd = ['git', 'log', '--pretty=format:%an', f'--since={self.since_date}']
        contributors_output = self.run_git_command(contributors_cmd)
        
        if not contributors_output:
            return {}, 0, {}
        
        contributor_commits = Counter(contributors_output.split('\n'))
        
        # Get contributor emails for identification
        contributors_with_email_cmd = ['git', 'log', '--pretty=format:%an|%ae', f'--since={self.since_date}']
        contributors_with_email = self.run_git_command(contributors_with_email_cmd)
        
        contributor_emails = {}
        for line in contributors_with_email.split('\n'):
            if '|' in line:
                name, email = line.split('|', 1)
                contributor_emails[name] = email
        
        return contributor_commits, total_commits, contributor_emails
    
    def identify_bots_and_automation(self, contributor_commits, contributor_emails):
        """Identify automated contributors (bots, CI/CD)"""
        bot_patterns = [
            r'.*\[bot\].*',
            r'.*bot.*',
            r'github-actions.*',
            r'renovate.*',
            r'dependabot.*',
            r'.*automation.*',
            r'.*ci.*',
            r'.*deploy.*'
        ]
        
        bots = {}
        humans = {}
        
        for contributor, commits in contributor_commits.items():
            email = contributor_emails.get(contributor, '')
            is_bot = any(re.match(pattern, contributor.lower()) or re.match(pattern, email.lower()) 
                        for pattern in bot_patterns)
            
            if is_bot:
                bots[contributor] = commits
            else:
                humans[contributor] = commits
        
        return humans, bots
    
    def calculate_bus_factor(self, human_commits, total_human_commits):
        """Calculate bus factor - minimum contributors needed for 50% of commits"""
        if not human_commits:
            return 0, []
        
        sorted_contributors = sorted(human_commits.items(), key=lambda x: x[1], reverse=True)
        cumulative_commits = 0
        bus_factor = 0
        critical_contributors = []
        
        for contributor, commits in sorted_contributors:
            cumulative_commits += commits
            bus_factor += 1
            critical_contributors.append((contributor, commits, commits/total_human_commits))
            
            if cumulative_commits >= total_human_commits * 0.5:
                break
        
        return bus_factor, critical_contributors
    
    def analyze_file_ownership(self):
        """Analyze file ownership patterns using git blame"""
        logger.info("Analyzing file ownership patterns...")
        
        # Get list of files in repository
        files_cmd = ['git', 'ls-files', '--', '*.py', '*.js', '*.ts', '*.tsx', '*.java', '*.cpp', '*.c', '*.h']
        files_output = self.run_git_command(files_cmd)
        
        if not files_output:
            return {}
        
        files = [f for f in files_output.split('\n') if f.strip()]
        file_ownership = {}
        
        # Analyze ownership for a sample of files (limit to avoid performance issues)
        sample_files = files[:50] if len(files) > 50 else files
        
        for file_path in sample_files:
            try:
                blame_cmd = ['git', 'blame', '--line-porcelain', file_path]
                blame_output = self.run_git_command(blame_cmd)
                
                if blame_output:
                    authors = []
                    for line in blame_output.split('\n'):
                        if line.startswith('author '):
                            author = line[7:]  # Remove 'author ' prefix
                            authors.append(author)
                    
                    if authors:
                        author_counts = Counter(authors)
                        total_lines = len(authors)
                        file_ownership[file_path] = {
                            'total_lines': total_lines,
                            'authors': dict(author_counts),
                            'primary_author': author_counts.most_common(1)[0] if author_counts else None
                        }
            except Exception as e:
                logger.warning(f"Could not analyze ownership for {file_path}: {e}")
                continue
        
        return file_ownership
    
    def analyze_commit_patterns(self, human_commits):
        """Analyze commit patterns over time"""
        logger.info("Analyzing commit patterns...")
        
        # Get commit dates for top contributors
        top_contributors = sorted(human_commits.items(), key=lambda x: x[1], reverse=True)[:10]
        
        commit_patterns = {}
        for contributor, _ in top_contributors:
            dates_cmd = ['git', 'log', '--author=' + contributor, '--pretty=format:%ad', '--date=short', f'--since={self.since_date}']
            dates_output = self.run_git_command(dates_cmd)
            
            if dates_output:
                dates = dates_output.split('\n')
                commit_patterns[contributor] = {
                    'total_commits': len(dates),
                    'first_commit': min(dates) if dates else None,
                    'last_commit': max(dates) if dates else None,
                    'commit_dates': dates
                }
        
        return commit_patterns
    
    def generate_risk_assessment(self, bus_factor, critical_contributors, total_human_commits, file_ownership):
        """Generate risk assessment based on analysis"""
        risk_level = "LOW"
        recommendations = []
        
        if bus_factor == 1:
            risk_level = "CRITICAL"
            recommendations.extend([
                "Immediate knowledge documentation required",
                "Emergency succession planning needed",
                "Cross-training program implementation"
            ])
        elif bus_factor <= 2:
            risk_level = "HIGH"
            recommendations.extend([
                "Knowledge transfer sessions required",
                "Distributed code review implementation",
                "Backup contributor identification"
            ])
        elif bus_factor <= 3:
            risk_level = "MEDIUM"
            recommendations.extend([
                "Regular knowledge sharing sessions",
                "Documentation improvement",
                "Contributor development program"
            ])
        
        # Check for single-owner files
        single_owner_files = []
        for file_path, ownership in file_ownership.items():
            if ownership['primary_author']:
                primary_author, primary_lines = ownership['primary_author']
                ownership_percentage = primary_lines / ownership['total_lines']
                if ownership_percentage > 0.8:  # 80% ownership threshold
                    single_owner_files.append({
                        'file': file_path,
                        'owner': primary_author,
                        'ownership_percentage': ownership_percentage
                    })
        
        if single_owner_files:
            recommendations.append("Address single-owner files with high ownership concentration")
        
        return {
            'risk_level': risk_level,
            'bus_factor': bus_factor,
            'recommendations': recommendations,
            'single_owner_files': single_owner_files[:10]  # Limit to top 10
        }
    
    def generate_report(self):
        """Generate comprehensive contributor analysis report"""
        logger.info(f"Starting contributor analysis for: {self.repo_path}")
        logger.info(f"Analysis period: {self.analysis_period_months} months (since {self.since_date})")
        
        # Get basic statistics
        contributor_commits, total_commits, contributor_emails = self.get_contributor_stats()
        
        if not contributor_commits:
            logger.warning("No commits found in the specified period")
            return
        
        # Separate humans from bots
        human_commits, bot_commits = self.identify_bots_and_automation(contributor_commits, contributor_emails)
        total_human_commits = sum(human_commits.values())
        total_bot_commits = sum(bot_commits.values())
        
        # Calculate bus factor
        bus_factor, critical_contributors = self.calculate_bus_factor(human_commits, total_human_commits)
        
        # Analyze file ownership
        file_ownership = self.analyze_file_ownership()
        
        # Analyze commit patterns
        commit_patterns = self.analyze_commit_patterns(human_commits)
        
        # Generate risk assessment
        risk_assessment = self.generate_risk_assessment(bus_factor, critical_contributors, total_human_commits, file_ownership)
        
        # Generate report
        report = self.create_markdown_report(
            total_commits, total_human_commits, total_bot_commits,
            human_commits, bot_commits, contributor_emails,
            bus_factor, critical_contributors, file_ownership,
            commit_patterns, risk_assessment
        )
        
        # Save report
        if self.output_file:
            output_path = Path(self.output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Report saved to: {output_path}")
        else:
            print(report)
    
    def create_markdown_report(self, total_commits, total_human_commits, total_bot_commits,
                             human_commits, bot_commits, contributor_emails,
                             bus_factor, critical_contributors, file_ownership,
                             commit_patterns, risk_assessment):
        """Create formatted markdown report"""
        
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        
        report = f"""# Critical Contributors Analysis

Analysis performed on: {timestamp}  
Repository: {self.repo_path}  
Period analyzed: {self.analysis_period_months} months (since {self.since_date})

## Executive Summary

This analysis identified contributor concentration risks by analyzing:
- **Commit Distribution**: How commits are distributed among contributors
- **Bus Factor**: Minimum contributors needed for 50% of development work
- **File Ownership**: Code ownership patterns and concentration risks
- **Risk Assessment**: Overall project sustainability assessment

## Contributor Statistics

- **Total Commits**: {total_commits:,}
- **Human Commits**: {total_human_commits:,} ({total_human_commits/total_commits*100:.1f}%)
- **Automated Commits**: {total_bot_commits:,} ({total_bot_commits/total_commits*100:.1f}%)
- **Unique Human Contributors**: {len(human_commits)}
- **Bus Factor**: {bus_factor}

## Top Human Contributors

| Rank | Contributor | Commits | Percentage | Email | Risk Level |
|------|-------------|---------|------------|-------|------------|
"""
        
        # Add top contributors table
        sorted_humans = sorted(human_commits.items(), key=lambda x: x[1], reverse=True)
        for i, (contributor, commits) in enumerate(sorted_humans[:15], 1):
            percentage = commits / total_human_commits * 100
            email = contributor_emails.get(contributor, 'N/A')
            
            if percentage > 30:
                risk = "CRITICAL"
            elif percentage > 15:
                risk = "HIGH"
            elif percentage > 10:
                risk = "MEDIUM"
            else:
                risk = "LOW"
            
            report += f"| {i} | {contributor} | {commits} | {percentage:.1f}% | {email} | {risk} |\n"
        
        report += f"""

## Bus Factor Analysis

**Bus Factor: {bus_factor}** - Minimum contributors representing 50% of commits

### Critical Contributors (50% of commits)
"""
        
        for i, (contributor, commits, percentage) in enumerate(critical_contributors, 1):
            report += f"{i}. **{contributor}**: {commits} commits ({percentage*100:.1f}%)\n"
        
        report += f"""

## Automated Contributors

| Bot/Service | Commits | Purpose |
|-------------|---------|---------|
"""
        
        sorted_bots = sorted(bot_commits.items(), key=lambda x: x[1], reverse=True)
        for bot, commits in sorted_bots[:10]:
            purpose = "Automation"
            if "github-actions" in bot.lower():
                purpose = "CI/CD"
            elif "renovate" in bot.lower() or "dependabot" in bot.lower():
                purpose = "Dependencies"
            elif "deploy" in bot.lower():
                purpose = "Deployment"
            
            report += f"| {bot} | {commits} | {purpose} |\n"
        
        report += f"""

## File Ownership Analysis

Analyzed {len(file_ownership)} files for ownership concentration:

### High Ownership Concentration Files
"""
        
        high_concentration_files = []
        for file_path, ownership in file_ownership.items():
            if ownership['primary_author']:
                primary_author, primary_lines = ownership['primary_author']
                ownership_percentage = primary_lines / ownership['total_lines']
                if ownership_percentage > 0.7:  # 70% threshold
                    high_concentration_files.append((file_path, primary_author, ownership_percentage))
        
        high_concentration_files.sort(key=lambda x: x[2], reverse=True)
        
        if high_concentration_files:
            report += "| File | Primary Owner | Ownership % |\n|------|---------------|-------------|\n"
            for file_path, owner, percentage in high_concentration_files[:10]:
                report += f"| {file_path} | {owner} | {percentage*100:.1f}% |\n"
        else:
            report += "No files with high ownership concentration found.\n"
        
        report += f"""

## Risk Assessment

**Overall Risk Level: {risk_assessment['risk_level']}**

### Risk Factors
- Bus Factor: {risk_assessment['bus_factor']}
- Single-owner files: {len(risk_assessment['single_owner_files'])}

### Recommendations
"""
        
        for i, recommendation in enumerate(risk_assessment['recommendations'], 1):
            report += f"{i}. {recommendation}\n"
        
        if risk_assessment['single_owner_files']:
            report += "\n### Files Requiring Attention\n"
            for file_info in risk_assessment['single_owner_files']:
                report += f"- **{file_info['file']}**: {file_info['ownership_percentage']*100:.1f}% owned by {file_info['owner']}\n"
        
        report += f"""

## Commit Pattern Analysis

### Activity Patterns for Top Contributors
"""
        
        for contributor, pattern in list(commit_patterns.items())[:5]:
            if pattern['first_commit'] and pattern['last_commit']:
                report += f"""
**{contributor}**:
- Total commits: {pattern['total_commits']}
- First commit: {pattern['first_commit']}
- Last commit: {pattern['last_commit']}
- Average commits per month: {pattern['total_commits'] / self.analysis_period_months:.1f}
"""
        
        report += f"""

## Recommendations for Risk Mitigation

### Immediate Actions (0-30 days)
1. **Knowledge Documentation**: Document critical knowledge from top contributors
2. **Cross-training**: Implement knowledge sharing sessions
3. **Code Review Distribution**: Distribute review responsibilities

### Medium-term Actions (1-3 months)
1. **Mentorship Program**: Pair experienced contributors with newcomers
2. **Documentation Standards**: Establish comprehensive documentation practices
3. **Succession Planning**: Identify and train backup contributors

### Long-term Strategy (3-12 months)
1. **Contributor Development**: Establish contributor growth pipeline
2. **Knowledge Management**: Implement systematic knowledge capture
3. **Risk Monitoring**: Regular bus factor and risk assessments

## Methodology

This analysis uses the following approach:
1. **Commit Analysis**: Examines commit history over {self.analysis_period_months} months
2. **Bot Detection**: Identifies automated contributors using pattern matching
3. **Bus Factor Calculation**: Determines minimum contributors for 50% of work
4. **File Ownership**: Analyzes code ownership using git blame
5. **Risk Assessment**: Combines metrics to assess overall project risk

---
*Generated by OLAF Contributor Analyzer*
"""
        
        return report

def main():
    parser = argparse.ArgumentParser(description='Analyze Git repository contributor patterns and risks')
    parser.add_argument('repo_path', help='Path to the Git repository')
    parser.add_argument('-m', '--months', type=int, default=12, 
                       help='Analysis period in months (default: 12)')
    parser.add_argument('-o', '--output', help='Output file path (default: stdout)')
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        analyzer = ContributorAnalyzer(args.repo_path, args.months, args.output)
        analyzer.generate_report()
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
