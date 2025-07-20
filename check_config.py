"""Configuration checker and setup utility for the LiteLLM agent.

This script helps verify that the environment is properly configured
for using LiteLLM with the Google ADK agent.
"""

import os
from dotenv import load_dotenv
from multi_tool_agent.litellm_config import litellm_config


def check_configuration():
    """Check and display the current configuration status."""
    print("=== LiteLLM Agent Configuration Check ===\n")
    
    # Load environment variables
    load_dotenv()
    
    # Check .env file exists
    env_file_exists = os.path.exists(".env")
    print(f"✓ .env file exists: {env_file_exists}")
    
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    api_key_set = bool(api_key and api_key.strip())
    print(f"✓ GOOGLE_API_KEY set: {api_key_set}")
    if api_key_set:
        print(f"  Key preview: {api_key[:10]}...")
    else:
        print("  ❌ Please set your GOOGLE_API_KEY in the .env file")
    
    # Check model configuration
    model = os.getenv("LITELLM_MODEL", "gemini/gemini-2.0-flash-exp")
    print(f"✓ Model configured: {model}")
    
    # Check Vertex AI setting
    use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")
    print(f"✓ Use Vertex AI: {use_vertex}")
    
    # Overall status
    print(f"\n=== Overall Status ===")
    is_configured = litellm_config.is_configured()
    print(f"Configuration valid: {'✅ Yes' if is_configured else '❌ No'}")
    
    if not is_configured:
        print("\n=== Setup Instructions ===")
        print("1. Ensure you have a Google API key for Gemini")
        print("2. Set GOOGLE_API_KEY in your .env file")
        print("3. Run this script again to verify configuration")
    
    return is_configured


if __name__ == "__main__":
    check_configuration()
