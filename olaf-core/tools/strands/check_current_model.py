#!/usr/bin/env python3
"""
Quick script to check which model you're currently using
"""

import os
import sys
from pathlib import Path

# Add the olaf-core tools to path
sys.path.append(str(Path(__file__).parent / "olaf-core" / "tools" / "strands"))

try:
    from aws_config_manager import AWSConfigManager
    from olaf_strands_agent import StrandsConfig
    
    print("🔍 Checking Current Model Configuration")
    print("=" * 50)
    
    # Check AWS Config Manager default
    aws_manager = AWSConfigManager()
    print(f"AWS Config Manager Default: {aws_manager.DEFAULT_MODEL}")
    
    # Check environment variable
    env_model = os.getenv('AWS_BEDROCK_DEFAULT_MODEL', 'Not set')
    print(f"Environment Variable (AWS_BEDROCK_DEFAULT_MODEL): {env_model}")
    
    # Check Strands Config
    try:
        config = StrandsConfig(Path('.'))
        models = config.get_model_configs()
        print(f"Strands Config Default: {models['aws-bedrock']['default']}")
        print(f"Available Models: {models['aws-bedrock']['available']}")
    except Exception as e:
        print(f"Strands Config: Could not load ({e})")
    
    # Check current configuration summary
    summary = aws_manager.get_configuration_summary()
    print("\n📋 Current Configuration Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Check recommended models
    recommended = aws_manager.get_recommended_models()
    print("\n🎯 Recommended Models:")
    for name, model_id in recommended.items():
        print(f"  {name}: {model_id}")
        
    print("\n✅ Model Check Complete!")
    
except ImportError as e:
    print(f"❌ Could not import required modules: {e}")
    print("Make sure you're running from the correct directory")
except Exception as e:
    print(f"❌ Error checking model configuration: {e}")