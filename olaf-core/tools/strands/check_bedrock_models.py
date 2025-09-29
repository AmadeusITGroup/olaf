#!/usr/bin/env python3
"""
Check available Bedrock models
"""
import boto3
import os
import json

def check_bedrock_models():
    try:
        # Set the profile
        os.environ['AWS_PROFILE'] = 'bedrock'
        
        # Create Bedrock client
        session = boto3.Session(profile_name='bedrock')
        bedrock = session.client('bedrock', region_name='us-east-1')
        
        print("🔍 Checking available Bedrock models...")
        print(f"📍 Region: us-east-1")
        print(f"👤 Profile: bedrock")
        print()
        
        # List foundation models
        response = bedrock.list_foundation_models()
        
        print("📋 Available Foundation Models:")
        print("=" * 80)
        
        # Group by provider
        providers = {}
        for model in response['modelSummaries']:
            provider = model['providerName']
            if provider not in providers:
                providers[provider] = []
            providers[provider].append(model)
        
        for provider, models in providers.items():
            print(f"\n🏢 {provider}:")
            for model in models:
                status = model.get('modelLifecycle', {}).get('status', 'ACTIVE')
                supports_streaming = 'responseStreamingSupported' in model and model['responseStreamingSupported']
                
                print(f"  ✅ {model['modelId']}")
                print(f"     Name: {model['modelName']}")
                print(f"     Status: {status}")
                print(f"     Streaming: {'Yes' if supports_streaming else 'No'}")
                
                # Check input/output modalities
                input_modalities = model.get('inputModalities', [])
                output_modalities = model.get('outputModalities', [])
                print(f"     Input: {', '.join(input_modalities)}")
                print(f"     Output: {', '.join(output_modalities)}")
                print()
        
        # Also check model access (this might show which models you can actually use)
        print("\n🔐 Checking model access...")
        
        # Try a few common models to see which ones work
        test_models = [
            "anthropic.claude-3-sonnet-20240229-v1:0",
            "anthropic.claude-3-haiku-20240307-v1:0", 
            "anthropic.claude-v2",
            "amazon.titan-text-express-v1"
        ]
        
        bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')
        
        for model_id in test_models:
            try:
                # Try to get model info (this will fail if no access)
                test_body = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 10,
                    "messages": [{"role": "user", "content": "test"}]
                } if 'anthropic' in model_id else {
                    "inputText": "test",
                    "textGenerationConfig": {"maxTokenCount": 10}
                }
                
                # This will throw an exception if we don't have access
                response = bedrock_runtime.invoke_model(
                    modelId=model_id,
                    body=json.dumps(test_body),
                    contentType='application/json'
                )
                print(f"  ✅ {model_id} - ACCESS GRANTED")
                
            except Exception as e:
                error_msg = str(e)
                if "AccessDeniedException" in error_msg:
                    print(f"  ❌ {model_id} - NO ACCESS")
                elif "ValidationException" in error_msg and "model identifier is invalid" in error_msg:
                    print(f"  ❓ {model_id} - MODEL NOT AVAILABLE")
                else:
                    print(f"  ⚠️  {model_id} - ERROR: {error_msg}")
        
    except Exception as e:
        print(f"❌ Error checking Bedrock models: {e}")
        print(f"   Make sure your 'bedrock' AWS profile is configured correctly")

if __name__ == "__main__":
    check_bedrock_models()
