!pip install google-adk

from kaggle_secrets import UserSecretsClient
import os

user_secrets = UserSecretsClient()
os.environ["GEMINI_API_KEY"] = user_secrets.get_secret("GOOGLE_API_KEY")

print("Environment ready.")

def current_time_checker(city: str) -> dict:
    import datetime
    return {"status": "ok", "time": datetime.datetime.now().strftime("%I:%M %p")}

def location_feasibility_check(place_name: str) -> dict:
    name = place_name.lower()
    if "museum" in name:
        return {"location": "Downtown Cultural District", "travel_time": "15 minutes"}
    return {"location": "City Center", "travel_time": "30 minutes"}

print("tools loaded")

from google.adk.agents import Agent

user_profile_data = """
Interests: history, coffee, art.
Start after 12 PM.
Hotel: Central Hotel.
"""

itinerary_agent = Agent(
    model="gemini-2.5-flash",
    name="ItineraryAgent",
    instruction=f"""
You are my itinerary planner.

User profile:
{user_profile_data}

Process:
1. Summarize user context.
2. Create afternoon itinerary starting after 12 PM.
3. Use current_time_checker if helpful.
4. Use location_feasibility_check for locations.
5. Return final refined itinerary only.
""",
    tools=[current_time_checker, location_feasibility_check]
)

print("agent ready")

from google.adk.apps import App

app = App(
    name="itinerary_app",
    root_agent=itinerary_agent
)

from google.adk.runners import (
    Runner,
    InMemorySessionService,
    InMemoryMemoryService,
    InMemoryArtifactService
)

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()
artifact_service = InMemoryArtifactService()

runner = Runner(
    app=app,
    session_service=session_service,
    memory_service=memory_service,
    artifact_service=artifact_service
)

print("runner ready")

from google.adk.runners import types

prompt = "Create a personalized afternoon itinerary for me."

# Create session safely (ignore if exists)
try:
    runner.session_service.create_session_sync(
        app_name="itinerary_app",
        user_id="yash",
        session_id="session1"
    )
except Exception as e:
    if "already exists" in str(e).lower():
        pass
    else:
        raise

# Build request
new_message = types.Content(parts=[types.Part(text=prompt)])

# Run agent
events = runner.run(
    user_id="yash",
    session_id="session1",
    new_message=new_message
)

# Extract clean text ONLY
for ev in events:
    if hasattr(ev, "content") and ev.content:
        for part in ev.content.parts:
            if hasattr(part, "text") and part.text:
                print(part.text)
