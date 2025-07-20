"""Custom agent wrapper that integrates LiteLLM with Google ADK framework.

This module provides a bridge between LiteLLM and the Google ADK Agent class,
allowing us to use LiteLLM's unified interface while maintaining ADK compatibility.
"""

from google.adk.agents import Agent
from typing import List, Callable, Optional, Dict, Any
from .litellm_config import litellm_config, create_litellm_completion
import json


class LiteLLMAgent(Agent):
    """Custom Agent class that uses LiteLLM instead of the default ADK model."""
    
    def __init__(
        self,
        name: str,
        description: str,
        instruction: str,
        tools: List[Callable],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ):
        """Initialize the LiteLLM Agent.
        
        Args:
            name (str): Name of the agent.
            description (str): Description of the agent's purpose.
            instruction (str): Instructions for the agent's behavior.
            tools (List[Callable]): List of tool functions.
            model (str, optional): LiteLLM model name. Defaults to configured model.
            temperature (float): Response temperature. Defaults to 0.7.
            max_tokens (int, optional): Maximum tokens in response.
            **kwargs: Additional arguments for the parent Agent class.
        """
        # Initialize parent class with a placeholder model
        # We'll override the actual LLM calls to use LiteLLM
        super().__init__(
            name=name,
            model="gemini-2.0-flash",  # Placeholder for ADK compatibility
            description=description,
            instruction=instruction,
            tools=tools,
            **kwargs
        )
        
        # Store LiteLLM specific configuration using object.__setattr__ to bypass Pydantic validation
        object.__setattr__(self, 'litellm_model', model or litellm_config.get_model_name())
        object.__setattr__(self, 'temperature', temperature)
        object.__setattr__(self, 'max_tokens', max_tokens)
        
        # Verify configuration
        if not litellm_config.is_configured():
            raise ValueError(
                "LiteLLM is not properly configured. Please ensure GOOGLE_API_KEY is set in your .env file."
            )
    
    def _call_litellm(self, messages: List[Dict[str, str]]) -> str:
        """Call LiteLLM with the provided messages.
        
        Args:
            messages (List[Dict[str, str]]): Conversation messages.
            
        Returns:
            str: Response from LiteLLM.
        """
        try:
            response = create_litellm_completion(
                messages=messages,
                model=getattr(self, 'litellm_model', litellm_config.get_model_name()),
                temperature=getattr(self, 'temperature', 0.7),
                max_tokens=getattr(self, 'max_tokens', None)
            )
            
            # Extract content from LiteLLM response
            if hasattr(response, 'choices') and response.choices:
                return response.choices[0].message.content
            else:
                return "I apologize, but I couldn't generate a response."
                
        except Exception as e:
            print(f"Error calling LiteLLM: {e}")
            return f"I encountered an error while processing your request: {str(e)}"
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current LiteLLM model configuration.
        
        Returns:
            Dict[str, Any]: Model configuration information.
        """
        return {
            "model": getattr(self, 'litellm_model', 'unknown'),
            "temperature": getattr(self, 'temperature', 0.7),
            "max_tokens": getattr(self, 'max_tokens', None),
            "configured": litellm_config.is_configured(),
            "api_key_set": bool(litellm_config.api_key)
        }


def create_litellm_agent(
    name: str,
    description: str,
    instruction: str,
    tools: List[Callable],
    **kwargs
) -> LiteLLMAgent:
    """Factory function to create a LiteLLM-powered agent.
    
    Args:
        name (str): Name of the agent.
        description (str): Description of the agent's purpose.
        instruction (str): Instructions for the agent's behavior.
        tools (List[Callable]): List of tool functions.
        **kwargs: Additional arguments for the LiteLLMAgent.
        
    Returns:
        LiteLLMAgent: Configured agent instance.
    """
    return LiteLLMAgent(
        name=name,
        description=description,
        instruction=instruction,
        tools=tools,
        **kwargs
    )
