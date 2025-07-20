# Google ADK Agent Sample with LiteLLM Integration

A simple multi-tool agent built using Google's Agent Development Kit (ADK) integrated with LiteLLM for unified language model access. This project demonstrates weather and time query capabilities while showcasing how to integrate LiteLLM with the Google ADK framework for enhanced flexibility and model management.

## 🚀 Features

- **LiteLLM Integration**: Unified interface for accessing Gemini models through LiteLLM
- **Weather Information**: Get current weather reports for supported cities (New York)
- **Time Queries**: Retrieve current time for specified cities (New York)
- **Interactive Web UI**: Browser-based interface for testing and interaction
- **Event Tracing**: Monitor function calls, responses, and execution flow
- **Voice Support**: Optional voice interaction capabilities
- **Gemini Integration**: Powered by Google's Gemini 2.0 Flash model via LiteLLM
- **Flexible Model Configuration**: Easy model switching and configuration management

## 🛠️ Technology Stack

- **Google ADK**: Agent Development Kit for building AI agents
- **LiteLLM**: Unified interface for multiple LLM providers
- **Python 3.9+**: Core programming language
- **Google Gemini API**: Large Language Model for natural language processing
- **FastAPI**: Web framework for the development UI
- **Uvicorn**: ASGI server for running the web interface

## 📋 Prerequisites

- Python 3.9 or higher
- Google API key for Gemini access
- Windows PowerShell (for the provided commands)

## ⚙️ Setup & Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd google-adk-agent-sample
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   # or for Command Prompt: .venv\Scripts\activate.bat
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Check if configuration is properly set up
   python check_config.py
   ```

5. **Set up your Google API key**
   - The `.env` file has been created with the required variables
   - You need to add your Google API key to the `.env` file

## 🔧 Configuration

The agent uses environment variables for configuration. The `.env` file in the root directory contains:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=
LITELLM_MODEL=gemini/gemini-2.0-flash-exp
```

**Configuration Steps:**
1. Get your Google API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Open the `.env` file and add your API key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
3. Run the configuration checker:
   ```bash
   python check_config.py
   ```

**Configuration Options:**
- `GOOGLE_API_KEY`: Your Google API key for Gemini access (required)
- `LITELLM_MODEL`: LiteLLM model identifier (default: gemini/gemini-2.0-flash-exp)
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to TRUE to use Vertex AI instead of standard API

**Security Best Practices:**
- Never commit API keys to version control
- Use environment variables in production
- Consider using Google Cloud Secret Manager for production deployments
- The `.env` file is included in `.gitignore` to prevent accidental commits

## 📁 Project Structure

```
google-adk-agent-sample/
├── multi_tool_agent/           # Main agent package
│   ├── __init__.py            # Package initialization and exports
│   ├── agent.py               # Main agent definition using LiteLLM
│   ├── litellm_config.py      # LiteLLM configuration and setup
│   ├── litellm_agent.py       # Custom agent wrapper for LiteLLM integration
│   └── tools/                 # Tool implementations
│       ├── __init__.py        # Tools package initialization  
│       ├── weather_tool.py    # Weather information tool
│       └── time_tool.py       # Time information tool
├── .env                       # Environment configuration (not in git)
├── .gitignore                 # Git ignore rules
├── check_config.py            # Configuration validation utility
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🔍 LiteLLM Integration Details

**Why LiteLLM?**
- **Unified Interface**: Single API for multiple LLM providers
- **Easy Model Switching**: Change models without rewriting code
- **Better Error Handling**: Standardized error responses across providers
- **Future-Proof**: Easy to add support for other LLM providers

**Architecture:**
1. **LiteLLMConfig**: Manages configuration and API key setup
2. **LiteLLMAgent**: Custom agent wrapper that inherits from Google ADK Agent
3. **Integration Layer**: Bridges LiteLLM calls with ADK framework

## 🚀 Running the Agent

1. **Ensure virtual environment is activated**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Start the development server**
   ```bash
   .venv\Scripts\adk.exe web
   # or alternatively: adk web (if PATH is configured)
   ```

3. **Access the web interface**
   - Open your browser to `http://localhost:8000`
   - Select "multi_tool_agent" from the dropdown in the top-left corner
   - Start chatting with your agent!

## 💬 Example Interactions

Try these prompts with your agent:

**Successful queries:**
- "What is the weather in New York?"
- "What is the time in New York?"
- "Can you tell me both the weather and time in New York?"

**Error handling examples:**
- "What is the weather in Paris?" (demonstrates error handling for unsupported cities)
- "What is the time in London?" (shows graceful error responses)

## 🔍 Exploring the Interface

**Chat Tab:**
- Text-based conversation with your agent
- Real-time responses from the Gemini model
- Voice input support (enable microphone)

**Events Tab:**
- View detailed function call logs
- Monitor tool execution and responses
- Analyze model reasoning and decision-making

**Trace Logs:**
- Performance metrics and latency information
- Execution flow visualization
- Debugging and optimization insights

## 🛠️ Development

**Adding New Tools:**
1. Define new functions in `multi_tool_agent/agent.py`
2. Add proper docstrings for tool descriptions
3. Include the function in the `tools` list of the `root_agent`

**Example tool structure:**
```python
def your_new_tool(parameter: str) -> dict:
    """Tool description for the AI model.
    
    Args:
        parameter (str): Description of the parameter.
        
    Returns:
        dict: Status and result or error message.
    """
    # Your tool logic here
    return {"status": "success", "result": "Your result"}
```

**Supported Cities (Current Implementation):**
- New York (weather and time)

**To extend city support:**
- Add more city conditions in `get_weather()` and `get_current_time()` functions
- Include appropriate timezone identifiers for time queries
- Consider integrating real weather APIs for live data

## 🚀 Deployment Options

**Local Development:**
- Use `adk web` for testing and development
- Ideal for rapid prototyping and debugging

**Production Deployment:**
- Deploy to Google Cloud Run
- Use Vertex AI Agent Engine
- Deploy to Google Kubernetes Engine (GKE)
- Refer to [ADK Deployment Guide](https://google.github.io/adk-docs/deploy/)

## 📚 Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python Repository](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with the ADK web interface
5. Submit a pull request

## 📄 License

This project is provided as a sample implementation for educational purposes.

## ⚠️ Important Notes

- This is a sample project for learning Google ADK
- The weather data is mocked for demonstration
- For production use, integrate with real weather APIs
- Always follow security best practices for API key management
