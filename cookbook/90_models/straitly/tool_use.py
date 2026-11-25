"""
Straitly Tool Use
=================
Cookbook example for `straitly/tool_use.py`.
"""

import asyncio

from agno.agent import Agent
from agno.models.straitly import Straitly


def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"The weather in {city} is 21 degrees Celsius and clear."


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(
    model=Straitly(id="deepseek/deepseek-v4-1-flash-1017"),
    tools=[get_weather],
    markdown=True,
)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("What is the weather in Vancouver?")

    # --- Sync + Streaming ---
    agent.print_response("What is the weather in Tokyo?", stream=True)

    # --- Async ---
    asyncio.run(agent.aprint_response("What is the weather in Paris?"))

    # --- Async + Streaming ---
    asyncio.run(agent.aprint_response("What is the weather in London?", stream=True))
