# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import os

os.environ["OPENAI_API_KEY"] = "sk-...your_openai_api_key_here"

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["main.py"],
    env=None,
)

import asyncio

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Load tools
            tools = await load_mcp_tools(session)

            # Create the agent
            agent = create_react_agent("openai:gpt-4.1", tools)

            # Interactive query loop
            while True:
                query = input("Enter your query (type 'exit' to quit): ")
                if query.lower() == "exit":
                    break
                try:
                    query = f"""
                    You are a note-taking assistant. You can add, retrieve, and delete notes.
                    You can also retrieve all notes for a specific user.
                    
                    here is the query:
                    {query}.
                    using the tools:
                    {tools}.
                    """
                    agent_response = await agent.ainvoke({"messages": query})
                    print(agent_response)
                except Exception as e:
                    print(f"Error: {e}")

# Run the event loop only once
if __name__ == "__main__":
    asyncio.run(main())
