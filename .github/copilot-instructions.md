# GitHub Copilot Instructions for Google ADK Agent Sample

## Project Overview

This is a sample multi-tool agent built using Google's Agent Development Kit (ADK) that demonstrates weather and time query capabilities. The project showcases how to create, configure, and deploy an AI agent with custom tools using the Google ADK framework.

## Technical Stack

### Core Framework
- **Google ADK (Agent Development Kit) v1.6.1**: Primary framework for building AI agents
- **Python 3.9+**: Core programming language
- **Google Gemini 2.0 Flash**: Large Language Model for natural language processing

### Web Interface
- **FastAPI**: Web framework for the development UI (provided by ADK)
- **Uvicorn**: ASGI server for running the web interface (provided by ADK)

### Dependencies
- **zoneinfo**: Python standard library for timezone handling
- **datetime**: Python standard library for date/time operations

### Development Tools
- **ADK CLI**: Command-line interface for running and managing agents
- **Environment Variables**: Configuration management via `.env` files

## Project Structure

```
google-adk-agent-sample/
├── multi_tool_agent/           # Main agent package
│   ├── __init__.py            # Package initialization
│   ├── agent.py               # Agent definition with tools
│   └── .env                   # Environment configuration (not in git)
├── .github/                   # GitHub configuration
│   └── copilot-instructions.md # This file
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── LICENSE                    # License file
└── README.md                  # Project documentation
```

## Code Flow and Architecture

### 1. Agent Initialization (`multi_tool_agent/agent.py`)

The application follows this flow:

1. **Tool Definition**: Individual functions are defined with specific capabilities
   - `get_weather(city: str)`: Retrieves weather information for supported cities
   - `get_current_time(city: str)`: Gets current time for supported cities

2. **Agent Creation**: A root agent is instantiated with:
   - Model specification (gemini-2.0-flash)
   - Agent name and description
   - Instruction set for behavior
   - List of available tools

3. **Tool Registration**: Functions are registered as tools in the agent's toolkit

### 2. Execution Flow

```
User Query → ADK Web Interface → Gemini Model → Tool Selection → Tool Execution → Response Generation → User Interface
```

#### Detailed Flow:
1. **User Input**: User submits query via web interface
2. **Model Processing**: Gemini 2.0 Flash processes the natural language input
3. **Tool Selection**: Model determines which tool(s) to use based on query intent
4. **Tool Execution**: Selected tools are executed with extracted parameters
5. **Response Synthesis**: Model generates natural language response based on tool results
6. **Output Delivery**: Response is delivered to user via web interface

### 3. Tool Architecture

Each tool follows a consistent pattern:

```python
def tool_name(parameter: type) -> dict:
    """Tool description for AI model understanding.
    
    Args:
        parameter (type): Parameter description.
        
    Returns:
        dict: Standardized response with status and result/error.
    """
    # Validation logic
    if valid_condition:
        return {
            "status": "success",
            "result": "successful_result"
        }
    else:
        return {
            "status": "error",
            "error_message": "descriptive_error_message"
        }
```

### 4. Error Handling

- **Graceful Degradation**: Tools return structured error responses for unsupported queries
- **Status Indicators**: All responses include status fields for success/error states
- **Descriptive Messages**: Error messages provide clear feedback to users

## Configuration Management

### Environment Variables
- `GOOGLE_GENAI_USE_VERTEXAI`: Boolean flag for Vertex AI usage (default: FALSE)
- `GOOGLE_API_KEY`: Google API key for Gemini access

### Security Considerations
- API keys stored in `.env` files (excluded from version control)
- Environment-based configuration for production deployments

## Development Guidelines

### Adding New Tools
1. Define function with appropriate type hints and docstrings
2. Implement validation logic for parameters
3. Return standardized response format (`status`, `result`/`error_message`)
4. Add function to the `tools` list in `root_agent`

### Code Style
- Use descriptive function names that clearly indicate purpose
- Include comprehensive docstrings with Args and Returns sections
- Follow Python type hints for all function parameters and returns
- Maintain consistent error response format across all tools

### Testing Approach
- Test via ADK web interface at `http://localhost:8000`
- Verify both successful and error scenarios
- Monitor execution flow via Events tab in web interface
- Use Trace Logs for performance analysis

## Supported Operations

### Current Capabilities
- **Weather Queries**: New York only (mocked data for demonstration)
- **Time Queries**: New York timezone (America/New_York)

### Extension Points
- Add support for additional cities by extending conditional logic
- Integrate real weather APIs for live data
- Implement additional timezone support
- Add new tool types (calendar, news, etc.)

## Deployment Patterns

### Local Development
```bash
adk web  # Starts development server on localhost:8000
```

### Production Options
- Google Cloud Run
- Vertex AI Agent Engine
- Google Kubernetes Engine (GKE)

## Key Design Principles

1. **Modularity**: Each tool is self-contained with clear responsibilities
2. **Consistency**: Standardized response format across all tools
3. **Extensibility**: Easy to add new tools and capabilities
4. **Error Resilience**: Graceful handling of unsupported requests
5. **Documentation**: Comprehensive docstrings for AI model understanding

## Integration Points

- **Google ADK Framework**: Core agent functionality and web interface
- **Gemini API**: Natural language processing and tool selection
- **Python Standard Library**: Datetime and timezone operations
- **Environment Configuration**: Secure API key management

This architecture provides a solid foundation for building multi-tool AI agents with Google ADK, emphasizing maintainability, extensibility, and robust error handling.

## GitHub Copilot Instructions
---
mode: agent
---
- always ask for confimration before adding any new pip packages.
- always ask for confirmation before making any changes to the codebase.
- always explain the changes in detail step by step and the rationale behind them.
- always provide a summary of the changes made.
- always ensure that the code is well-documented and follows best practices.
- always generate a .env file with the below keys if one doesnt exist.
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=
- always ask user for the GOOGLE_API_KEY if there is no value assigned for the key.
