"""Multi-tool agent package with LiteLLM integration.

This package provides a Google ADK agent that uses LiteLLM for unified access
to language models, specifically configured for Gemini models.
"""

from . import agent
from .agent import root_agent
from .litellm_config import litellm_config
from .litellm_agent import LiteLLMAgent, create_litellm_agent

__all__ = [
    "agent",
    "root_agent", 
    "litellm_config",
    "LiteLLMAgent",
    "create_litellm_agent",
]
