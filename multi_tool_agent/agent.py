"""Main agent configuration using LiteLLM with Gemini model.

This module defines the root agent that uses LiteLLM for unified LLM access
while maintaining compatibility with the Google ADK framework.
"""

from .tools import get_weather, get_current_time
from .litellm_agent import create_litellm_agent


# Create the root agent using LiteLLM
root_agent = create_litellm_agent(
    name="weather_time_agent",
    description=(
        "Agent to answer questions about the time and weather in a city using LiteLLM with Gemini."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city. "
        "Use the available tools to provide accurate information. Always be polite and helpful."
    ),
    tools=[get_weather, get_current_time],
    temperature=0.7,  # Slightly creative but focused responses
    max_tokens=1000,  # Reasonable response length
)
