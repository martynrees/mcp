"""
Swagger API Parser module for extracting API tools from Swagger JSON definitions
"""

import json
import os
import re
from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field


class ParameterSchema(BaseModel):
    name: str
    description: Optional[str] = None
    required: bool = False
    type: str
    default: Optional[Any] = None
    enum: Optional[List[Any]] = None

    @classmethod
    def from_swagger(cls, param_data: Dict[str, Any]):
        schema = param_data.get("schema", {})
        return cls(
            name=param_data.get("name", ""),
            description=param_data.get("description", ""),
            required=param_data.get("required", False),
            type=schema.get("type", "string"),
            default=schema.get("default"),
            enum=schema.get("enum")
        )


class ApiTool(BaseModel):
    """Represents an API endpoint as a tool that can be used by language models"""
    name: str
    description: str
    operation_id: str
    method: str
    path: str
    parameters: List[ParameterSchema] = []
    request_body: Optional[Dict[str, Any]] = None
    tags: List[str] = []

    def to_tool_schema(self) -> Dict[str, Any]:
        """Convert the API endpoint to a tool schema for MCP"""
        properties = {}
        required = []

        for param in self.parameters:
            param_type = param.type
            param_properties = {"type": param_type, "description": param.description or ""}

            if param.enum:
                param_properties["enum"] = param.enum

            if param.default is not None:
                param_properties["default"] = param.default

            properties[param.name] = param_properties

            if param.required:
                required.append(param.name)

        if self.request_body:
            properties["body"] = {
                "type": "object",
                "description": "Request body for the API call"
            }
            required.append("body")

        return {
            "name": self.operation_id,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required
            }
        }


class SwaggerParser:
    """Parser for Swagger/OpenAPI JSON files to extract API endpoints as tools"""

    def __init__(self, swagger_json_path: str):
        self.swagger_json_path = swagger_json_path
        self.swagger_data = self._load_swagger_json()

    def _load_swagger_json(self) -> Dict[str, Any]:
        """Load and parse the Swagger JSON file"""
        try:
            print(f"Loading Swagger JSON from: {self.swagger_json_path}")
            with open(self.swagger_json_path, 'r') as file:
                data = json.load(file)
                print(f"Successfully loaded JSON with {len(data)} top-level keys")
                return data
        except FileNotFoundError:
            print(f"ERROR: Swagger JSON file not found at: {self.swagger_json_path}")
            print(f"Current working directory: {os.getcwd()}")
            raise
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in file: {str(e)}")
            raise

    def _sanitize_operation_id(self, operation_id: str) -> str:
        """Sanitize the operation ID to be a valid function name"""
        # Replace non-alphanumeric characters with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', operation_id)
        # Ensure it starts with a letter
        if not sanitized[0].isalpha():
            sanitized = 'op_' + sanitized
        return sanitized

    def extract_api_tools(self) -> List[ApiTool]:
        """Extract API endpoints as tools from the Swagger JSON"""
        tools = []

        # Check if we're working with the new format (structured by categories)
        if not self.swagger_data.get("paths") and isinstance(self.swagger_data, dict):
            # Process new format where json is organized by categories
            for category, endpoints_list in self.swagger_data.items():
                if isinstance(endpoints_list, list):
                    # Handle direct list of endpoints
                    for endpoint in endpoints_list:
                        self._process_endpoint(endpoint, tools, category)
                elif isinstance(endpoints_list, dict):
                    # Handle subcategories
                    for subcategory, endpoints in endpoints_list.items():
                        if isinstance(endpoints, list):
                            for endpoint in endpoints:
                                self._process_endpoint(endpoint, tools, f"{category}/{subcategory}")
            return tools

        # Original format processing
        for path, path_item in self.swagger_data.get("paths", {}).items():
            for method, operation in path_item.items():
                if method not in ["get", "post", "put", "delete", "patch"]:
                    continue

                operation_id = operation.get("operationId")
                if not operation_id:
                    continue

                sanitized_op_id = self._sanitize_operation_id(operation_id)
                description = operation.get("description") or operation.get("summary", "")

                parameters = []
                for param in operation.get("parameters", []):
                    parameters.append(ParameterSchema.from_swagger(param))

                request_body = operation.get("requestBody")

                tags = operation.get("tags", [])

                tool = ApiTool(
                    name=sanitized_op_id,
                    description=description,
                    operation_id=sanitized_op_id,
                    method=method,
                    path=path,
                    parameters=parameters,
                    request_body=request_body,
                    tags=tags
                )

                tools.append(tool)

        return tools

    def _process_endpoint(self, endpoint: Dict[str, Any], tools: List[ApiTool], category: str) -> None:
        """Process a single endpoint from the new format JSON and add it to tools list"""
        path = endpoint.get("path")
        method = endpoint.get("method", "").lower()
        operation_id = endpoint.get("operationId")

        if not path or not method or not operation_id or method not in ["get", "post", "put", "delete", "patch"]:
            return

        sanitized_op_id = self._sanitize_operation_id(operation_id)
        description = endpoint.get("description") or endpoint.get("summary", "")

        # Process parameters
        parameters = []
        for param_name in endpoint.get("parameters", []):
            # Create a simple parameter schema for path parameters
            param = ParameterSchema(
                name=param_name,
                description=f"Path parameter: {param_name}",
                required=True,
                type="string"
            )
            parameters.append(param)

        # Process query parameters
        for param_name in endpoint.get("query_parameters", []):
            # Create a simple parameter schema for query parameters
            param = ParameterSchema(
                name=param_name,
                description=f"Query parameter: {param_name}",
                required=False,
                type="string"
            )
            parameters.append(param)

        # Create the tool
        tool = ApiTool(
            name=sanitized_op_id,
            description=description,
            operation_id=sanitized_op_id,
            method=method,
            path=path,
            parameters=parameters,
            tags=[category]
        )

        tools.append(tool)
