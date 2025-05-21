"""
MCP Server module that implements the Model Context Protocol server
"""

import json
import logging
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, Field
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

import config
from swagger_parser import SwaggerParser, ApiTool
from api_client import ApiClient, ApiClientAuthConfig
from tool_handler import ToolHandler
from custom_tools import CustomTools

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="MCP API Gateway",
    description="Model Context Protocol server for Cisco Catalyst Center APIs",
    version="1.0.0"
)

# Global variables to store tools
api_tools: List[ApiTool] = []
langchain_tools: List[Tool] = []
llm = None
tool_handler = None
custom_tools = None


class MCPToolsRequest(BaseModel):
    input: str = Field(..., description="The input for the LLM")
    config: Optional[Dict[str, Any]] = Field(default={}, description="Configuration for the LLM")


class MCPToolsResponse(BaseModel):
    response: str = Field(..., description="The response from the LLM")
    tools: List[Dict[str, Any]] = Field(..., description="The available tools")


async def setup_tools():
    """Set up the tools for the MCP server"""
    global api_tools, langchain_tools, llm, tool_handler, custom_tools

    # Parse Swagger file to extract API tools
    parser = SwaggerParser(config.SWAGGER_JSON_PATH)
    api_tools = parser.extract_api_tools()

    logger.info(f"Extracted {len(api_tools)} API tools from Swagger file")

    # Initialize API client
    api_client = ApiClient(
        auth_config=ApiClientAuthConfig(
            base_url=config.CISCO_API_BASE_URL,
            username=config.CISCO_API_USERNAME,
            password=config.CISCO_API_PASSWORD
        )
    )

    # Initialize tool handler
    tool_handler = ToolHandler(api_tools, api_client)
    langchain_tools = tool_handler.create_langchain_tools()

    # Initialize custom tools
    custom_tools = CustomTools(api_client)

    # Initialize OpenAI LLM
    llm = ChatOpenAI(
        api_key=config.OPENAI_API_KEY,
        model="gpt-4.1-mini",
        temperature=0
    )


@app.on_event("startup")
async def startup_event():
    """Startup event for the FastAPI app"""
    await setup_tools()


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "MCP Server is running"}


@app.post("/mcp/tools")
async def get_tools():
    """Get available tools for the MCP server"""
    global langchain_tools, custom_tools

    if not langchain_tools:
        await setup_tools()

    # Format tools in MCP format
    mcp_tools = []
    for api_tool in api_tools:
        mcp_tools.append(api_tool.to_tool_schema())

    # Add custom tools
    if custom_tools:
        mcp_tools.extend(custom_tools.get_custom_tool_schemas())

    return {"tools": mcp_tools}


@app.post("/mcp/execute_tool/{tool_name}")
async def execute_tool(tool_name: str, request: Request):
    """Execute a tool by name with parameters"""
    global tool_handler, custom_tools

    if not tool_handler:
        await setup_tools()

    # Check if it's a custom tool
    if tool_name == "network_health_report":
        try:
            result = custom_tools.network_health_report()
            return result
        except Exception as e:
            logger.error(f"Error executing custom tool {tool_name}: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    # Get the tool
    api_tool = None
    for tool in api_tools:
        if tool.operation_id == tool_name:
            api_tool = tool
            break

    if not api_tool:
        raise HTTPException(status_code=404, detail=f"Tool {tool_name} not found")

    # Parse request body
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON in request body")

    # Execute tool
    try:
        for tool in langchain_tools:
            if tool.name == tool_name:
                result = tool.invoke(body)
                return json.loads(result)

        raise HTTPException(status_code=404, detail=f"Tool {tool_name} implementation not found")
    except Exception as e:
        logger.error(f"Error executing tool {tool_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host=config.HOST,
        port=config.PORT,
        reload=True
    )
