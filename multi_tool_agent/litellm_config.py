"""LiteLLM configuration and integration for the Google ADK agent.

This module provides a simplified interface to use LiteLLM with Gemini models
while maintaining compatibility with the Google ADK framework.
"""

import os
from typing import Dict, Any, Optional
import litellm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class LiteLLMConfig:
    """Configuration class for LiteLLM integration with Gemini models."""
    
    def __init__(self):
        """Initialize LiteLLM configuration."""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = os.getenv("LITELLM_MODEL", "gemini/gemini-2.0-flash-exp")
        self.use_vertex_ai = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() == "TRUE"
        
        # Configure LiteLLM
        self._configure_litellm()
    
    def _configure_litellm(self):
        """Configure LiteLLM settings."""
        if self.api_key:
            # Set API key for Gemini
            os.environ["GEMINI_API_KEY"] = self.api_key
            
        # Configure LiteLLM settings
        litellm.set_verbose = False  # Set to True for debugging
        
    def get_model_name(self) -> str:
        """Get the configured model name for LiteLLM.
        
        Returns:
            str: The model name to use with LiteLLM.
        """
        return self.model
    
    def is_configured(self) -> bool:
        """Check if LiteLLM is properly configured.
        
        Returns:
            bool: True if configuration is valid, False otherwise.
        """
        return bool(self.api_key)


def create_litellm_completion(
    messages: list,
    model: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """Create a completion using LiteLLM.
    
    Args:
        messages (list): List of message objects for the conversation.
        model (str, optional): Model name to use. Defaults to configured model.
        temperature (float): Temperature for response generation. Defaults to 0.7.
        max_tokens (int, optional): Maximum tokens in response.
        **kwargs: Additional arguments to pass to LiteLLM.
    
    Returns:
        Dict[str, Any]: Response from LiteLLM.
    
    Raises:
        ValueError: If LiteLLM is not properly configured.
    """
    config = LiteLLMConfig()
    
    if not config.is_configured():
        raise ValueError(
            "LiteLLM is not properly configured. Please ensure GOOGLE_API_KEY is set."
        )
    
    if model is None:
        model = config.get_model_name()
    
    try:
        response = litellm.completion(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return response
    except Exception as e:
        raise Exception(f"Error calling LiteLLM: {str(e)}")


# Global configuration instance
litellm_config = LiteLLMConfig()
