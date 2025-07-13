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