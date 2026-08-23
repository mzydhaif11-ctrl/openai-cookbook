import asyncio
import os

from agents import Agent, Runner, function_tool


@function_tool
def get_weather(city: str) -> str:
    """Return a short weather summary for a city."""
    weather_map = {
        "seattle": "Cloudy with light rain and temperatures around 18°C.",
        "new york": "Sunny with a cool breeze and temperatures around 24°C.",
        "london": "Overcast with a chance of drizzle and temperatures around 16°C.",
    }

    normalized_city = city.strip().lower()
    if normalized_city in weather_map:
        return weather_map[normalized_city]

    return f"I don't have a forecast for {city}."


agent = Agent(
    name="starter_assistant",
    instructions=(
        "You are a concise travel assistant. "
        "Use the weather tool when the user asks about a city forecast. "
        "Answer in two or three sentences and keep the tone helpful and professional."
    ),
    tools=[get_weather],
)


async def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY before running this example.")

    print("Type a prompt to chat with the agent. Enter /exit to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"/exit", "quit"}:
            break

        result = await Runner.run(agent, user_input)
        print(f"Assistant: {result.final_output}\n")


if __name__ == "__main__":
    asyncio.run(main())
