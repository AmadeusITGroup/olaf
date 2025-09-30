#!/usr/bin/env python3
"""
Test Bedrock Model - Verify which model you're actually using
"""

import boto3
import json
import sys
from pathlib import Path

def test_bedrock_model(model_id: str, profile: str = 'bedrock', region: str = 'us-east-1'):
    """
    Test a Bedrock model by making an actual inference call
    
    Args:
        model_id: The model ID to test
        profile: AWS profile name
        region: AWS region
    """
    
    print(f"🧪 Testing Bedrock Model: {model_id}")
    print(f"📍 Profile: {profile}, Region: {region}")
    print("=" * 60)
    
    try:
        # Create session and client
        session = boto3.Session(profile_name=profile)
        bedrock_runtime = session.client('bedrock-runtime', region_name=region)
        
        # Prepare the request
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "messages": [
                {
                    "role": "user", 
                    "content": "What model are you? Please tell me your exact name and version. Also, are you Claude Sonnet 4 or Claude 3.5 Sonnet?"
                }
            ]
        }
        
        print("📤 Sending request to model...")
        
        # Make the inference call
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body),
            contentType='application/json',
            accept='application/json'
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        model_response = response_body['content'][0]['text']
        
        print("✅ Model Response:")
        print("-" * 40)
        print(model_response)
        print("-" * 40)
        
        # Show metadata
        print(f"\n📊 Response Metadata:")
        print(f"  Input Tokens: {response_body.get('usage', {}).get('input_tokens', 'N/A')}")
        print(f"  Output Tokens: {response_body.get('usage', {}).get('output_tokens', 'N/A')}")
        print(f"  Model ID Used: {model_id}")
        
        return True, model_response
        
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False, str(e)

def test_multiple_models(region: str = 'us-east-1'):
    """Test multiple model configurations"""
    
    # Models to test - adjust inference profiles based on region
    if region == 'eu-central-1':  # Frankfurt
        models_to_test = [
            {
                'name': 'Sonnet 4 Inference Profile (EU)',
                'id': 'eu.anthropic.claude-sonnet-4-20250514-v1:0'
            },
            {
                'name': 'Sonnet 3.5 Direct Model', 
                'id': 'anthropic.claude-3-5-sonnet-20241022-v1:0'
            },
            {
                'name': 'Sonnet 3.5 Inference Profile (EU)',
                'id': 'eu.anthropic.claude-3-5-sonnet-20241022-v2:0'
            }
        ]
    else:  # US regions
        models_to_test = [
            {
                'name': 'Sonnet 4 Inference Profile (US)',
                'id': 'us.anthropic.claude-sonnet-4-20250514-v1:0'
            },
            {
                'name': 'Sonnet 3.5 Direct Model', 
                'id': 'anthropic.claude-3-5-sonnet-20241022-v1:0'
            },
            {
                'name': 'Sonnet 3.5 Inference Profile (US)',
                'id': 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
            }
        ]
    
    print(f"🔍 Testing Multiple Models in Region: {region}")
    print("=" * 60)
    
    results = []
    
    for model in models_to_test:
        print(f"\n🎯 Testing: {model['name']}")
        success, response = test_bedrock_model(model['id'], region=region)
        
        results.append({
            'name': model['name'],
            'id': model['id'],
            'success': success,
            'response': response[:100] + "..." if len(response) > 100 else response
        })
        
        if not success:
            print(f"⚠️  Model {model['name']} failed: {response}")
        
        print("\n" + "="*60)
    
    # Summary
    print("\n📋 Test Summary:")
    for result in results:
        status = "✅ SUCCESS" if result['success'] else "❌ FAILED"
        print(f"  {result['name']}: {status}")
        if result['success']:
            print(f"    Response preview: {result['response']}")
    
    return results

def check_current_configuration():
    """Check what model configuration is currently set"""
    
    print("🔧 Current Configuration Check")
    print("=" * 40)
    
    # Check environment variables
    import os
    aws_profile = os.getenv('AWS_PROFILE', 'Not set')
    aws_region = os.getenv('AWS_REGION', 'Not set') 
    bedrock_model = os.getenv('AWS_BEDROCK_DEFAULT_MODEL', 'Not set')
    
    print(f"Environment Variables:")
    print(f"  AWS_PROFILE: {aws_profile}")
    print(f"  AWS_REGION: {aws_region}")
    print(f"  AWS_BEDROCK_DEFAULT_MODEL: {bedrock_model}")
    
    # Try to load OLAF configuration
    try:
        sys.path.append(str(Path(__file__).parent / "olaf-core" / "tools" / "strands"))
        from aws_config_manager import AWSConfigManager
        
        manager = AWSConfigManager()
        summary = manager.get_configuration_summary()
        
        print(f"\nOLAF Configuration:")
        for key, value in summary.items():
            print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"\nOLAF Configuration: Could not load ({e})")

if __name__ == "__main__":
    print("🚀 Bedrock Model Tester")
    print("=" * 60)
    
    # Check current configuration
    check_current_configuration()
    
    print("\n")
    
    # Test specific model or run full test
    if len(sys.argv) > 1:
        if sys.argv[1] == '--region' and len(sys.argv) > 2:
            # Test all models in specific region
            region = sys.argv[2]
            test_multiple_models(region)
        else:
            # Test specific model
            model_id = sys.argv[1]
            profile = sys.argv[2] if len(sys.argv) > 2 else 'bedrock'
            region = sys.argv[3] if len(sys.argv) > 3 else 'us-east-1'
            
            test_bedrock_model(model_id, profile, region)
    else:
        # Test multiple models in default region
        test_multiple_models()
    
    print("\n🎉 Testing Complete!")
    print("\nUsage:")
    print("  python test_bedrock_model.py                                    # Test all models (US East)")
    print("  python test_bedrock_model.py --region eu-central-1             # Test all models (Frankfurt)")
    print("  python test_bedrock_model.py <model-id>                        # Test specific model")
    print("  python test_bedrock_model.py <model-id> <profile> <region>     # Test with custom settings")
    print("\nRegion Examples:")
    print("  us-east-1      # US East (N. Virginia)")
    print("  eu-central-1   # Europe (Frankfurt)")
    print("  us-west-2      # US West (Oregon)")