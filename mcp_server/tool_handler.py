"""
MCP Tool Handler module that implements the Model Context Protocol for API tools
"""

import json
import logging
from typing import Dict, Any, List, Optional

from langchain_core.tools import Tool
from langchain_core.pydantic_v1 import BaseModel, Field, create_model

from swagger_parser import ApiTool
from api_client import ApiClient, ApiClientAuthConfig

logger = logging.getLogger(__name__)


class ToolHandler:
    """
    Handler for Model Context Protocol (MCP) tools that wrap API endpoints
    """

    def __init__(self, api_tools: List[ApiTool], api_client: ApiClient):
        self.api_tools = {tool.operation_id: tool for tool in api_tools}
        self.api_client = api_client

    def _create_tool_function(self, api_tool: ApiTool):
        """Create a function that will handle the API tool invocation"""

        def tool_function(**kwargs):
            try:
                logger.info(f"Executing tool {api_tool.operation_id}")
                result = self.api_client.execute_tool(
                    method=api_tool.method,
                    path=api_tool.path,
                    parameters=kwargs
                )
                return json.dumps(result, indent=2)
            except Exception as e:
                logger.error(f"Error executing tool {api_tool.operation_id}: {str(e)}")
                return json.dumps({"error": str(e)})

        return tool_function

    def _create_tool_input_schema(self, api_tool: ApiTool):
        """Create a Pydantic model schema for the tool input"""
        fields = {}

        for param in api_tool.parameters:
            field_type = str
            if param.type == "integer":
                field_type = int
            elif param.type == "number":
                field_type = float
            elif param.type == "boolean":
                field_type = bool

            fields[param.name] = (
                Optional[field_type] if not param.required else field_type,
                Field(description=param.description or "")
            )

        if api_tool.request_body:
            fields["body"] = (Dict[str, Any], Field(description="Request body"))

        # Create and return a dynamic Pydantic model
        model_name = f"{api_tool.operation_id.capitalize()}Input"
        return create_model(model_name, **fields)

    def create_langchain_tools(self) -> List[Tool]:
        """
        Create LangChain Tool objects for each API tool
        These tools are compatible with the Model Context Protocol
        """
        tools = []

        for api_tool in self.api_tools.values():
            input_schema = self._create_tool_input_schema(api_tool)
            tool_func = self._create_tool_function(api_tool)

            tool = Tool(
                name=api_tool.operation_id,
                description=api_tool.description,
                func=tool_func,
                args_schema=input_schema
            )

            tools.append(tool)

        return tools
