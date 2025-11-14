# Day 1b: Multi-Agent System for Collaborative Writing

from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import Tool
from google.genai import types

# --- 1. Tool Definition (The Exit Condition) ---

# The Refiner Agent will use this tool to signal when the story is finished.
def exit_loop():
  """Exits the current agent collaboration loop. The refiner uses this when
  the story quality is satisfactory."""
  # In a real system, this function terminates the workflow.
  return "Exit signal sent. Story is complete."

# --- 2. Specialized Agent Definitions (The Team) ---

# Agent 1: Story Drafting
story_draft_agent = Agent(
    model="gemini-2.5-flash",
    name="Story_Draft_Agent",
    description="An agent that creates the initial story draft.",
    instruction="Your only task is to write a compelling first draft of the story based on the user prompt.",
)

# Agent 2: Critique (Refiner is the Critique Agent in the notebook)
# Note: Based on the screenshot, the "Refiner" agent serves the dual role of 
# critiquing AND refining, and also manages the exit loop.
refiner_agent = Agent(
    model="gemini-2.5-flash",
    name="Refiner_Agent",
    description="A critical story editor and refiner. You have a story craft and critique function.",
    instruction="Your task is to analyze the current story draft. Provide detailed critique for improvement. If the story is excellent, you MUST call the 'exit_loop' function.",
    tools=[exit_loop] # Only the Refiner gets the exit tool
)

# Agent 3: Critique (This agent provides the detailed critique in the loop)
critique_agent = Agent(
    model="gemini-2.5-flash",
    name="Critique_Agent",
    description="A senior editor that provides highly structured and objective feedback.",
    instruction="Provide a highly detailed critique of the current story, focusing on character development and plot holes. Do NOT modify the story.",
)


# --- 3. Orchestrator Definition (The Workflow) ---

# The SequentialAgent runs the specified agents in a loop until the exit_loop tool is called.
story_refinement_loop = SequentialAgent(
    # The initial writer is executed first
    initial_writer=story_draft_agent,
    # The loop alternates between critique and refinement
    loop=[
        critique_agent, 
        refiner_agent
    ],
    name="Story_Refinement_Loop"
)

print("✅ Multi-Agent Refinement Loop created and ready to run.")