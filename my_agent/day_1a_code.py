# Day 1a: From Prompt to Action - Agent and Tool Definition

# 1. Imports
# These imports link your code to the ADK framework and the Gemini types
from google.adk.agents import Agent
from google.genai import types 

# 2. Tool Definition (Function Calling)
# This is the tool the agent "thinks" about and calls to get real-time data.
# The ADK uses the function name and the docstring to understand the tool's purpose.
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.
    
    Args:
        city: The name of the city for which to retrieve the current time.
    """
    # This is a mock/simplified implementation of the function call.
    # When running the agent, the ADK handles the actual time retrieval.
    # The return format mirrors the successful output you saw.
    return {"status": "success", "city": city, "time": "12:30 PM BST on Friday, November 14, 2025"}


# 3. Agent Definition
# This defines the "brain" (the Gemini model) and attaches the tool.
root_agent = Agent(
    model="gemini-2.5-flash",  # The fast, capable model you selected
    name="root_agent",
    description="A helpful assistant that tells the current time in cities.",
    instruction="You are a helpful assistant. When asked about time, use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time] # Attach the function/tool here
)

# You can optionally print the agent definition to confirm its setup
# print(f"Agent '{root_agent.name}' initialized with model {root_agent.model} and tool: {root_agent.tools[0].__name__}")