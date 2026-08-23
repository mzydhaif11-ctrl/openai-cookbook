# Build a simple starter agent with the OpenAI Agents SDK

This example shows a minimal agent that uses a custom tool to answer weather questions. It is intentionally small so you can use it as a starting point for more capable agent workflows.

## What it does

- Creates a single agent with a concise system prompt.
- Adds a custom weather lookup tool.
- Runs the agent from the command line so you can try prompts interactively.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r examples/agents_sdk/simple_agent/requirements.txt
export OPENAI_API_KEY="your-api-key"
```

## Run the example

```bash
python examples/agents_sdk/simple_agent/main.py
```

Try prompts such as:

- "What's the weather in Seattle?"
- "Give me a short forecast for London."
- "How is the weather in New York today?"

The agent will use the built-in weather tool for these requests.
