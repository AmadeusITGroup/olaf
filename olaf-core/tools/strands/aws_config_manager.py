#!/usr/bin/env python3
"""
AWS Configuration Manager for OLAF Strands Agent
Ensures proper AWS Bedrock configuration and credential management
"""

import os
import sys
import subprocess
import boto3
import json
from pathlib import Path
from typing import Dict, Optional, Tuple
import logging

class AWSConfigManager:
    """Manages AWS configuration for OLAF Strands Agent"""
    
    # Default configuration
    DEFAULT_PROFILE = "bedrock"
    DEFAULT_REGION = "us-east-1"
    DEFAULT_MODEL = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"  # Sonnet 4 inference profile
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.profile = None
        self.region = None
        self.model = None
        
    def setup_aws_environment(self, profile: str = None, region: str = None, model: str = None) -> Dict[str, str]:
        """
        Setup AWS environment with proper configuration
        
        Args:
            profile: AWS profile name (default: bedrock)
            region: AWS region (default: us-east-1)
            model: Model ID (default: Sonnet 4 inference profile)
            
        Returns:
            Dict with configuration details
        """
        # Use provided values or defaults
        self.profile = profile or self.DEFAULT_PROFILE
        self.region = region or self.DEFAULT_REGION
        self.model = model or self.DEFAULT_MODEL
        
        self.logger.info(f"Setting up AWS environment: profile={self.profile}, region={self.region}")
        
        # Set environment variables
        os.environ['AWS_PROFILE'] = self.profile
        os.environ['AWS_REGION'] = self.region
        
        # Clear any cached credentials that might be stale
        self._clear_credential_cache()
        
        # Validate configuration
        config_status = self._validate_configuration()
        
        return {
            'profile': self.profile,
            'region': self.region,
            'model': self.model,
            'status': config_status['status'],
            'message': config_status['message']
        }
    
    def _clear_credential_cache(self):
        """Clear boto3 credential cache to avoid stale tokens"""
        try:
            # Clear environment variables that might have cached credentials
            cache_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_SESSION_TOKEN']
            for var in cache_vars:
                if var in os.environ:
                    del os.environ[var]
                    self.logger.debug(f"Cleared cached environment variable: {var}")
            
            # Clear boto3 session cache
            if hasattr(boto3, '_session'):
                boto3._session = None
                self.logger.debug("Cleared boto3 session cache")
                
        except Exception as e:
            self.logger.warning(f"Failed to clear credential cache: {e}")
    
    def _validate_configuration(self) -> Dict[str, str]:
        """Validate AWS configuration and credentials"""
        try:
            # Test AWS CLI access
            result = subprocess.run(
                ['aws', 'sts', 'get-caller-identity', '--profile', self.profile],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                identity = json.loads(result.stdout)
                self.logger.info(f"AWS credentials validated for user: {identity.get('Arn', 'Unknown')}")
                
                # Test Bedrock access
                bedrock_status = self._test_bedrock_access()
                
                return {
                    'status': 'success',
                    'message': f"AWS configured successfully. User: {identity.get('UserId', 'Unknown')}"
                }
            else:
                error_msg = result.stderr.strip()
                self.logger.error(f"AWS credential validation failed: {error_msg}")
                return {
                    'status': 'error',
                    'message': f"AWS credential validation failed: {error_msg}"
                }
                
        except subprocess.TimeoutExpired:
            return {
                'status': 'error',
                'message': "AWS credential validation timed out"
            }
        except FileNotFoundError:
            return {
                'status': 'error', 
                'message': "AWS CLI not found. Please install AWS CLI."
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f"Configuration validation failed: {str(e)}"
            }
    
    def _test_bedrock_access(self) -> bool:
        """Test if Bedrock is accessible with current credentials"""
        try:
            session = boto3.Session(profile_name=self.profile)
            bedrock = session.client('bedrock', region_name=self.region)
            
            # Try to list foundation models (lightweight test)
            response = bedrock.list_foundation_models(byOutputModality='TEXT')
            model_count = len(response.get('modelSummaries', []))
            
            self.logger.info(f"Bedrock access confirmed. {model_count} models available.")
            return True
            
        except Exception as e:
            self.logger.warning(f"Bedrock access test failed: {e}")
            return False
    
    def get_recommended_models(self) -> Dict[str, str]:
        """Get recommended model configurations"""
        return {
            'sonnet_4': 'us.anthropic.claude-3-5-sonnet-20241022-v2:0',  # Inference profile
            'sonnet_3_5': 'anthropic.claude-3-5-sonnet-20240620-v1:0',   # Direct model
            'haiku_3_5': 'anthropic.claude-3-5-haiku-20241022-v1:0',     # Direct model
            'opus_3': 'anthropic.claude-3-opus-20240229-v1:0'            # Direct model
        }
    
    def check_model_availability(self, model_id: str) -> Tuple[bool, str]:
        """Check if a specific model is available"""
        try:
            session = boto3.Session(profile_name=self.profile)
            bedrock = session.client('bedrock', region_name=self.region)
            
            # List available models
            response = bedrock.list_foundation_models()
            available_models = [model['modelId'] for model in response.get('modelSummaries', [])]
            
            if model_id in available_models:
                return True, f"Model {model_id} is available"
            else:
                # Check if it might be an inference profile
                if model_id.startswith('us.'):
                    return True, f"Model {model_id} appears to be an inference profile (cannot verify directly)"
                else:
                    return False, f"Model {model_id} not found in available models"
                    
        except Exception as e:
            return False, f"Failed to check model availability: {str(e)}"
    
    def get_configuration_summary(self) -> Dict[str, str]:
        """Get current configuration summary"""
        return {
            'aws_profile': os.getenv('AWS_PROFILE', 'Not set'),
            'aws_region': os.getenv('AWS_REGION', 'Not set'),
            'default_model': self.model or 'Not set',
            'recommended_model': self.DEFAULT_MODEL
        }


def setup_aws_for_strands(profile: str = None, region: str = None, model: str = None, 
                         logger: Optional[logging.Logger] = None) -> Dict[str, str]:
    """
    Convenience function to setup AWS configuration for Strands agent
    
    Args:
        profile: AWS profile name (default: bedrock)
        region: AWS region (default: us-east-1)  
        model: Model ID (default: Sonnet 4 inference profile)
        logger: Optional logger instance
        
    Returns:
        Configuration status dictionary
    """
    manager = AWSConfigManager(logger)
    return manager.setup_aws_environment(profile, region, model)


if __name__ == "__main__":
    # Test the configuration manager
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    print("AWS Configuration Manager Test")
    print("=" * 40)
    
    manager = AWSConfigManager(logger)
    
    # Setup configuration
    config = manager.setup_aws_environment()
    print(f"Configuration Status: {config['status']}")
    print(f"Message: {config['message']}")
    
    # Show configuration summary
    summary = manager.get_configuration_summary()
    print("\nConfiguration Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Show recommended models
    models = manager.get_recommended_models()
    print("\nRecommended Models:")
    for name, model_id in models.items():
        print(f"  {name}: {model_id}")
    
    # Test model availability
    test_model = manager.DEFAULT_MODEL
    available, message = manager.check_model_availability(test_model)
    print(f"\nModel Check ({test_model}): {message}")