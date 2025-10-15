#!/usr/bin/env python3
"""
OLAF Strands Agent - Simplified Implementation
A lightweight OLAF-compatible agent using AWS Strands SDK built-in tools
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import logging

def show_banner():
    """Display ASCII art banner"""
    banner = r"""
 _____ _        ___   _____ 
/  ___| |      / _ \ |  ___|
\ `--.| |_ _ __/ /_\ \| |_   
 `--. \ __| '__|  _  ||  _|  
/\__/ / |_| |  | | | || |    
\____/ \__|_|  \_| |_/\_|    
                             
"""
    print(f"\033[96m{banner}\033[0m")
    print("\033[96mOLAF Strands Agent - Simplified SDK Implementation\033[0m")
    print("\033[96m=================================================\033[0m")

class StrandsConfig:
    """Configuration management for OLAF Strands Agent"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        
    @property
    def models(self) -> Dict[str, Dict[str, Any]]:
        """Get model configurations"""
        return {
            'aws-bedrock': {
                'default': os.getenv('AWS_BEDROCK_DEFAULT_MODEL', 'anthropic.claude-3-5-sonnet-20241022-v1:0'),
                'available': [
                    'anthropic.claude-3-5-sonnet-20241022-v1:0',
                    'anthropic.claude-3-haiku-20240307-v1:0',
                    'anthropic.claude-3-opus-20240229-v1:0',
                    'us.amazon.nova-pro-v1:0',
                    'us.amazon.nova-lite-v1:0'
                ]
            },
            'openai': {
                'default': os.getenv('OPENAI_DEFAULT_MODEL', 'gpt-4-turbo'),
                'available': ['gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo']
            }
        }
    
    @property
    def paths(self) -> Dict[str, Path]:
        """Get OLAF directory paths"""
        return {
            'findings_dir': self.project_root / 'olaf-data' / 'findings',
            'prompts_dir': self.project_root / 'olaf-core' / 'prompts',
            'templates_dir': self.project_root / 'olaf-core' / 'templates',
            'tools_dir': self.project_root / 'olaf-core' / 'tools',
            'project_root': self.project_root
        }
    
    @property
    def aws_config(self) -> Dict[str, Any]:
        """Get AWS configuration"""
        return {
            'region': os.getenv('AWS_REGION', 'us-east-1'),
            'max_tokens': int(os.getenv('MAX_TOKENS', '4000')),
            'temperature': float(os.getenv('TEMPERATURE', '0.7'))
        }

def setup_logging(log_file: str) -> logging.Logger:
    """Setup logging configuration"""
    logger = logging.getLogger('olaf_strands_agent')
    logger.setLevel(logging.INFO)
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def resolve_olaf_paths(content: str, config: StrandsConfig) -> str:
    """Resolve OLAF memory map references in content"""
    replacements = {
        '[id:findings_dir]': str(config.paths['findings_dir']),
        '[id:prompts_dir]': str(config.paths['prompts_dir']),
        '[id:templates_dir]': str(config.paths['templates_dir']),
        '[id:tools_dir]': str(config.paths['tools_dir']),
        '[id:project_root]': str(config.paths['project_root'])
    }
    
    for placeholder, path in replacements.items():
        content = content.replace(placeholder, path)
    
    return content

def load_prompt_file(prompt_path: Path, logger: logging.Logger) -> Optional[Dict[str, Any]]:
    """Load and parse a prompt file"""
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata if present (YAML front matter)
        metadata = {}
        prompt_content = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # Parse YAML front matter (simple key-value parsing)
                front_matter = parts[1].strip()
                for line in front_matter.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()
                prompt_content = parts[2].strip()
        
        logger.info(f"Loaded prompt: {prompt_path.name}")
        return {
            'metadata': metadata,
            'content': prompt_content,
            'path': str(prompt_path)
        }
    
    except Exception as e:
        logger.error(f"Failed to load prompt {prompt_path}: {e}")
        return None

class OLAFStrandsAgent:
    """OLAF-compatible Strands Agent using SDK tools"""
    
    def __init__(self, project_root: Path, service_provider: str = 'aws-bedrock', 
                 model_name: str = None, aws_profile: str = None, logger: logging.Logger = None):
        self.config = StrandsConfig(project_root)
        self.service_provider = service_provider
        self.model_name = model_name or self.config.models[service_provider]['default']
        self.aws_profile = aws_profile or 'bedrock'  # Default to bedrock profile
        self.logger = logger or logging.getLogger(__name__)
        self.agent = self._create_agent()
    
    def _create_windows_execution_tools(self):
        """Create Windows-compatible execution tools"""
        try:
            # Import our custom Windows tools
            from windows_execution_tools import (
                create_python_executor_tool,
                create_powershell_executor_tool,
                create_python_code_executor_tool
            )
            
            tools = []
            
            # Add Python script executor
            try:
                python_script_tool = create_python_executor_tool()
                tools.append(python_script_tool)
                self.logger.info("Added Windows Python script executor tool")
            except Exception as e:
                self.logger.warning(f"Failed to create Python script executor: {e}")
            
            # Add PowerShell executor
            try:
                powershell_tool = create_powershell_executor_tool()
                tools.append(powershell_tool)
                self.logger.info("Added Windows PowerShell executor tool")
            except Exception as e:
                self.logger.warning(f"Failed to create PowerShell executor: {e}")
            
            # Add Python code executor
            try:
                python_code_tool = create_python_code_executor_tool()
                tools.append(python_code_tool)
                self.logger.info("Added Windows Python code executor tool")
            except Exception as e:
                self.logger.warning(f"Failed to create Python code executor: {e}")
            
            return tools
            
        except ImportError as e:
            self.logger.warning(f"Failed to import Windows execution tools: {e}")
            return []
    
    def _create_agent(self):
        """Create Strands agent with appropriate model and tools"""
        try:
            from strands import Agent
            # Import core tools
            from strands_tools import file_read, file_write, editor, http_request
            core_tools = [file_read, file_write, editor, http_request]
            self.logger.info("Loaded core tools: file_read, file_write, editor, http_request")
            
            # Import execution tools (Windows-compatible)
            additional_tools = []
            
            # Add Windows-compatible execution tools
            windows_tools = self._create_windows_execution_tools()
            additional_tools.extend(windows_tools)
            
            # Try code_interpreter (works on Windows) - as backup
            try:
                from strands_tools.code_interpreter.code_interpreter import tool as code_interpreter_tool
                additional_tools.append(code_interpreter_tool)
                self.logger.info("Added code_interpreter tool for Python execution")
            except ImportError as e:
                self.logger.warning(f"code_interpreter not available: {e}")
            
            # Try python_repl and shell (Unix-only) - fallback for non-Windows
            try:
                from strands_tools import python_repl, shell
                additional_tools.extend([python_repl, shell])
                self.logger.info("Added python_repl and shell tools for script execution")
            except ImportError as e:
                self.logger.warning(f"Unix execution tools not available (expected on Windows): {e}")
            
            # Import model based on service provider
            if self.service_provider == 'aws-bedrock':
                from strands.models import BedrockModel
                import boto3
                
                # Create session with specific profile
                session = boto3.Session(profile_name=self.aws_profile)
                self.logger.info(f"Using AWS profile: {self.aws_profile}")
                
                # Disable streaming for models that don't support tools
                streaming = not ('titan' in self.model_name.lower())
                
                model = BedrockModel(
                    model_id=self.model_name,
                    temperature=self.config.aws_config['temperature'],
                    streaming=streaming,
                    region=self.config.aws_config['region'],
                    session=session  # Pass the session with bedrock profile
                )
            elif self.service_provider == 'openai':
                from strands.models import OpenAIModel
                model = OpenAIModel(
                    model_id=self.model_name,
                    temperature=self.config.aws_config['temperature']
                )
            else:
                raise ValueError(f"Unsupported service provider: {self.service_provider}")
            
            # Combine all tools
            tools = core_tools + additional_tools
            
            # Try to add MCP client if available
            try:
                from strands_tools import mcp_client
                tools.append(mcp_client)
                self.logger.info("Added MCP client tool")
            except ImportError:
                self.logger.warning("MCP client not available")
            
            # Note: Tavily tools intentionally excluded - using only internal SDK tools
            
            # Create agent with autonomous execution (no user prompts)
            from strands.handlers import null_callback_handler
            
            agent = Agent(
                model=model, 
                tools=tools,
                callback_handler=null_callback_handler  # Disable user prompts for tool execution
            )
            self.logger.info(f"Created Strands agent with {len(tools)} tools (autonomous mode)")
            return agent
            
        except ImportError as e:
            self.logger.error(f"Failed to import Strands SDK: {e}")
            self.logger.error("Please install: pip install strands-agents strands-agents-tools")
            raise
        except Exception as e:
            self.logger.error(f"Failed to create agent: {e}")
            raise
    
    def execute_prompt(self, prompt_path: str, context: str = "", 
                      templates: list = None) -> Dict[str, Any]:
        """Execute OLAF prompt with Strands agent"""
        start_time = datetime.now()
        
        try:
            # Load prompt
            prompt_file = self.config.paths['prompts_dir'] / prompt_path
            prompt_data = load_prompt_file(prompt_file, self.logger)
            
            if not prompt_data:
                raise ValueError(f"Failed to load prompt: {prompt_path}")
            
            # Resolve OLAF memory map references
            resolved_prompt = resolve_olaf_paths(prompt_data['content'], self.config)
            
            # Add OLAF context information with timestamp
            olaf_context = self._generate_olaf_context(getattr(self, 'timestamp', None))
            
            # Combine prompt with context
            full_prompt = f"{resolved_prompt}\n\n{olaf_context}"
            if context:
                full_prompt += f"\n\nAdditional Context:\n{context}"
            
            self.logger.info(f"Executing prompt with Strands agent: {prompt_path}")
            
            # Execute with Strands agent
            response = self.agent(full_prompt)
            
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # Format response
            result = {
                'service_provider': self.service_provider,
                'model_name': self.model_name,
                'prompt_path': prompt_path,
                'response_text': response,
                'metadata': {
                    'timestamp': end_time.isoformat(),
                    'execution_time_seconds': execution_time,
                    'prompt_metadata': prompt_data['metadata']
                }
            }
            
            self.logger.info(f"Prompt execution completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            self.logger.error(f"Failed to execute prompt: {e}")
            raise
    
    def _generate_olaf_context(self, timestamp: str = None) -> str:
        """Generate OLAF-specific context for the agent"""
        # Use provided timestamp or generate fresh local timestamp
        if not timestamp:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        
        context = f"""
## OLAF Framework Context

**Current Local Time**: {timestamp} (YYYYMMDD-HHmm format)
**Note**: Always use current local time when creating timestamps for file names

## Available OLAF Directories
- **Findings**: {self.config.paths['findings_dir']}
- **Prompts**: {self.config.paths['prompts_dir']}
- **Templates**: {self.config.paths['templates_dir']}
- **Tools**: {self.config.paths['tools_dir']}
- **Project Root**: {self.config.paths['project_root']}

## Available Tools
You have access to the following Strands SDK tools:
- **file_read**: Read files, search patterns, get statistics
- **file_write**: Create, append, overwrite files
- **editor**: Advanced editing with syntax highlighting, find/replace
- **http_request**: Make HTTP requests, convert HTML to markdown - USE THIS for web research
- **execute_python_script**: Execute Python scripts with arguments (Windows-compatible)
- **execute_powershell_command**: Execute PowerShell commands (Windows-compatible)
- **execute_python_code**: Execute Python code snippets directly (Windows-compatible)
- **python_repl**: Execute Python code directly (if available on Unix)
- **shell**: Execute shell commands and scripts (if available on Unix)
- **mcp_client**: Connect to MCP servers (if available)

## Script Execution (Windows-Compatible)
You can execute OLAF scripts and tools using:
- **execute_python_script**: For running Python scripts like `tools/generate_dynamic_pptx.py`
- **execute_python_code**: For executing Python code snippets directly
- **execute_powershell_command**: For PowerShell commands and Windows system operations
- **file_read**: To read script outputs and results
- **file_write**: To create reports and summaries

## OLAF Conventions
- Use US English
- Follow `verb-entity-complement.md` naming pattern
- Use `YYYYMMDD-HHmm` timestamp format
- Save results to findings directory when appropriate
"""
        return context

def save_results(results: Dict[str, Any], output_location: str, 
                timestamp: str, logger: logging.Logger) -> Dict[str, str]:
    """Save results to files"""
    output_files = {}
    output_dir = Path(output_location).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Save main results
        results_file = output_dir / f"olaf-strands-results-{timestamp}.md"
        with open(results_file, 'w', encoding='utf-8') as f:
            f.write(f"# OLAF Strands Agent Results\n\n")
            f.write(f"**Timestamp**: {results['metadata']['timestamp']}\n")
            f.write(f"**Service**: {results['service_provider']}\n")
            f.write(f"**Model**: {results['model_name']}\n")
            f.write(f"**Prompt**: {results['prompt_path']}\n")
            f.write(f"**Execution Time**: {results['metadata']['execution_time_seconds']:.2f}s\n\n")
            f.write(f"## Response\n\n{results['response_text']}\n\n")
        
        output_files['results'] = str(results_file)
        
        # Save metadata
        metadata_file = output_dir / f"olaf-strands-metadata-{timestamp}.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(results['metadata'], f, indent=2)
        
        output_files['metadata'] = str(metadata_file)
        
        logger.info(f"Results saved to {len(output_files)} files")
        
    except Exception as e:
        logger.error(f"Failed to save results: {e}")
    
    return output_files

def main():
    parser = argparse.ArgumentParser(
        description='OLAF Strands Agent - Simplified SDK Implementation'
    )
    parser.add_argument('--service-provider', default='aws-bedrock',
                       choices=['aws-bedrock', 'openai'],
                       help='AI service provider to use')
    parser.add_argument('--model-name',
                       help='Model name (uses default if not specified)')
    parser.add_argument('--prompt', required=True,
                       help='Path to prompt file (relative to prompts directory)')
    parser.add_argument('--context', default='',
                       help='Additional context data for the agent')
    parser.add_argument('--output-location',
                       help='Custom output location (default: auto-generated in findings)')
    parser.add_argument('--project-root', default='.',
                       help='Path to the project root containing olaf-core')
    parser.add_argument('--aws-profile', default='bedrock',
                       help='AWS profile name to use (default: bedrock)')
    parser.add_argument('--timestamp',
                       help='Timestamp to use for file operations (YYYYMMDD-HHMM format)')
    
    args = parser.parse_args()
    
    try:
        show_banner()
        
        # Use provided timestamp or generate new one
        timestamp = args.timestamp or datetime.now().strftime("%Y%m%d-%H%M")
        
        # Find project root
        project_root = Path(args.project_root).resolve()
        
        # Look for olaf-core directory
        if not (project_root / "olaf-core").exists():
            # Try parent directories
            for parent in project_root.parents:
                if (parent / "olaf-core").exists():
                    project_root = parent
                    break
                elif (parent / "olaf" / "olaf-core").exists():
                    project_root = parent / "olaf"
                    break
        
        print(f"Project root: {project_root}")
        
        # Setup paths
        config = StrandsConfig(project_root)
        findings_dir = config.paths['findings_dir']
        findings_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        log_file = findings_dir / f"olaf-strands-execution-{timestamp}.log"
        logger = setup_logging(str(log_file))
        
        logger.info("Starting OLAF Strands Agent execution")
        logger.info(f"Service Provider: {args.service_provider}")
        logger.info(f"Model: {args.model_name or 'default'}")
        logger.info(f"Prompt: {args.prompt}")
        
        # Create agent
        agent = OLAFStrandsAgent(
            project_root=project_root,
            service_provider=args.service_provider,
            model_name=args.model_name,
            aws_profile=args.aws_profile,
            logger=logger
        )
        # Store timestamp for context generation
        agent.timestamp = timestamp
        
        # Execute prompt
        results = agent.execute_prompt(
            prompt_path=args.prompt,
            context=args.context
        )
        
        # Determine output location
        if not args.output_location:
            args.output_location = str(findings_dir / f"olaf-strands-results-{timestamp}.md")
        
        # Save results
        output_files = save_results(results, args.output_location, timestamp, logger)
        
        # Print summary
        print(f"\n\033[92m=== Execution Summary ===\033[0m")
        print(f"Service Provider: {args.service_provider}")
        print(f"Model: {results['model_name']}")
        print(f"Prompt: {args.prompt}")
        print(f"Execution Time: {results['metadata']['execution_time_seconds']:.2f}s")
        print(f"Output Files: {list(output_files.values())}")
        print(f"Execution Log: {log_file}")
        
        logger.info("OLAF Strands Agent execution completed successfully")
        
    except Exception as e:
        print(f"Error during execution: {e}")
        if 'logger' in locals():
            logger.error(f"Execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
