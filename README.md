# Travel Agent

An AI-powered travel agent built with LangChain and LangGraph.

## Setup

**Requirements:** Python 3.13+

1. Clone the repo
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file with your API keys (e.g. `OPENAI_API_KEY`)

## Usage

```bash
uv run main.py
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - LLM framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Agent orchestration
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
