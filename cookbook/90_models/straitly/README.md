# Straitly Cookbook

This cookbook demonstrates how to use [Straitly](https://straitly.ai) with the Agno framework.
Straitly is an AI gateway that provides one OpenAI-compatible API key and base URL for more than
150 models, including Claude, GPT, Gemini, Grok, and DeepSeek.

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `STRAITLY_API_KEY`

Get your API key from: https://straitly.ai/app/keys

```shell
export STRAITLY_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/straitly/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/straitly/tool_use.py
```

## Model IDs

Straitly serves its live model catalog at `GET https://api.straitly.ai/v1/models` and
https://straitly.ai/models. A few example model IDs:

- `deepseek/deepseek-v4-1-flash-1017` (default)
- `claude-sonnet-5-5`
- `gpt-6-astra`
- `gemini-4-carbon`

Read the current catalog from `/v1/models` rather than hardcoding model lists.

## Resources & Support

- [Website](https://straitly.ai)
- [Quickstart Documentation](https://straitly.ai/docs/quickstart)
- [Model List](https://straitly.ai/models)
- [Contact](https://straitly.ai/contact)

### API Reference
- **Base URL**: `https://api.straitly.ai/v1`
- **Models Endpoint**: `https://api.straitly.ai/v1/models`
