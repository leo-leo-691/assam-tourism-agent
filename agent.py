import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams

AGENT_INSTRUCTION = """
You are an Assam Tourism Guide — a knowledgeable and friendly assistant 
that helps travelers explore the beautiful state of Assam, India.

When a user asks about places, attractions, or travel in Assam:
1. Use the available Maps tools to search for relevant places.
2. Retrieve structured data like place names, ratings, addresses, and types.
3. Use that data to craft a helpful, warm, and informative travel guide response.
4. Always mention specific places with their ratings if available.
5. Keep responses concise, friendly, and useful for a traveler.

You cover all of Assam — including Kaziranga, Majuli, Jorhat, Guwahati, 
Sivasagar, Tezpur, Dibrugarh, and other destinations.
"""

maps_api_key = os.environ.get("MAPS_API_KEY", "")

toolset = MCPToolset(
    connection_params=SseConnectionParams(
        url="https://mapstools.googleapis.com/mcp",
        headers={"X-Goog-Api-Key": maps_api_key}
    )
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="assam_tourism_agent",
    instruction=AGENT_INSTRUCTION,
    tools=[toolset],
)