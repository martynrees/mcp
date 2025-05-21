"""
Example client that demonstrates how to use the MCP server with LangChain
"""

import os
import sys
import json
from typing import List, Dict, Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
from dotenv import load_dotenv

import requests

# Load environment variables
load_dotenv()

# Get API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("ERROR: OPENAI_API_KEY environment variable not set")
    sys.exit(1)

# MCP server URL
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")


def get_mcp_tools() -> List[Dict[str, Any]]:
    """Get available tools from the MCP server"""
    response = requests.post(f"{MCP_SERVER_URL}/mcp/tools")
    response.raise_for_status()
    return response.json()["tools"]


def create_tool_from_schema(tool_schema: Dict[str, Any]) -> Tool:
    """Create a LangChain tool from an MCP tool schema"""
    tool_name = tool_schema["name"]

    def tool_func(params: Dict[str, Any]) -> str:
        """Function that executes the tool via the MCP server"""
        response = requests.post(
            f"{MCP_SERVER_URL}/mcp/execute_tool/{tool_name}",
            json=params
        )
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)

    return Tool(
        name=tool_name,
        description=tool_schema["description"],
        func=tool_func
    )


def main():
    """Main function to demonstrate using the MCP server with LangChain"""
    print("Fetching tools from MCP server...")
    tool_schemas = get_mcp_tools()
    print(f"Found {len(tool_schemas)} tools")

    # Create LangChain tools from MCP tool schemas
    tools = [create_tool_from_schema(schema) for schema in tool_schemas]

    # Initialize LLM
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o", temperature=0)

    # Create an agent with the tools
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that can use various tools to help with network management tasks."),
        ("user", "{input}")
    ])

    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Example usage
    while True:
        user_input = input("\nEnter a task (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        result = agent_executor.invoke({"input": user_input})
        print("\nResult:")
        print(result["output"])


if __name__ == "__main__":
    main()
