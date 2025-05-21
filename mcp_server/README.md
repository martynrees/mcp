# MCP Server for Cisco Catalyst Center APIs

This project implements a Model Context Protocol (MCP) server that wraps the Cisco Catalyst Center APIs defined in a Swagger JSON file. The MCP server allows you to use these APIs as tools within AI agents built with LangChain or any other framework supporting the Model Context Protocol.

## Features

- Automatically parses Swagger/OpenAPI JSON to extract API endpoints as tools
- Implements the Model Context Protocol for tool discovery and execution
- Provides a FastAPI server to expose the tools via MCP
- Includes authentication with the Cisco Catalyst Center API
- Example client to demonstrate using the MCP server with LangChain

## Prerequisites

- Python 3.9 or higher
- Cisco Catalyst Center with API access
- OpenAI API key

## Setup

1. Clone the repository and navigate to the project directory:

```bash
cd /Users/marrees/Documents/mcp/mcp_server
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the environment variables:

Edit the `.env` file with your configuration details:

```
OPENAI_API_KEY=your_openai_api_key
CISCO_API_BASE_URL=https://your-cisco-catalyst-center-url
CISCO_API_USERNAME=your_username
CISCO_API_PASSWORD=your_password
HOST=0.0.0.0
PORT=8000
SWAGGER_JSON_PATH=../intent_api_2_3_7_9.json
```

## Running the MCP Server

### Option 1: Running Directly

Start the MCP server directly with:

```bash
python server.py
```

### Option 2: Running with Docker (Recommended)

The server can also be run as a Docker container, which ensures consistent environments and easier deployment.

1. Make sure Docker and Docker Compose are installed on your system.

2. Run the Docker container:

```bash
./run_docker.sh
```

This script will build the Docker image and start a container. The server will be available at http://localhost:8000.

## API Endpoints

- `GET /`: Health check endpoint
- `POST /mcp/tools`: Get available tools in MCP format
- `POST /mcp/execute_tool/{tool_name}`: Execute a specific tool with parameters

## Using with LangChain

The project includes an example client (`example_client.py`) that demonstrates how to use the MCP server with LangChain.

Run the example client with:

```bash
python example_client.py
```

The client will fetch the available tools from the MCP server and create a LangChain agent that can use these tools.

## Project Structure

- `server.py`: Main FastAPI server implementing the MCP
- `swagger_parser.py`: Parser for Swagger/OpenAPI JSON files
- `api_client.py`: Client for making requests to Cisco APIs
- `tool_handler.py`: Handler for MCP tools that wrap API endpoints
- `custom_tools.py`: Implementation of custom tools that combine multiple API calls
- `config.py`: Configuration module
- `example_client.py`: Example client using LangChain
- `Dockerfile`: Configuration for building the Docker image
- `docker-compose.yml`: Docker Compose configuration for services
- `run_docker.sh`: Script to build and run the Docker container

## MCP Integration

This server implements the Model Context Protocol (MCP) for AI agents. The MCP defines a standardized way for AI models to discover and use tools.

The key components of MCP integration are:

1. Tool Discovery: The `/mcp/tools` endpoint returns tool schemas in the MCP format.
2. Tool Execution: The `/mcp/execute_tool/{tool_name}` endpoint executes tools and returns results.

## Customization

You can customize the MCP server by:

1. Modifying the `SwaggerParser` to handle different Swagger/OpenAPI formats
2. Extending the `ApiClient` to add authentication methods or error handling
3. Adding new endpoints to the FastAPI server
4. Creating custom tools in the `custom_tools.py` file that combine multiple API calls for advanced functionality

### Custom Tools

The server includes a `custom_tools.py` module that demonstrates how to create custom tools that combine multiple API calls. These tools can provide higher-level functionality that is not directly exposed by the API.

Currently implemented custom tools:

- `network_health_report`: Generates a comprehensive network health report by combining data from multiple API endpoints

## Troubleshooting

- If authentication fails, check your Cisco API credentials in the `.env` file
- If tool execution fails, check the logs for more detailed error messages
- If parsing fails, ensure your Swagger JSON is valid and follows the OpenAPI 3.0.x format

### Docker-specific troubleshooting

- If the Docker container fails to start, check Docker logs: `docker-compose logs -f`
- If the container can't access the Swagger file, ensure the context path in docker-compose.yml is correct
- To rebuild the Docker image completely: `docker-compose down && docker-compose build --no-cache && docker-compose up -d`
- To enter the running container for debugging: `docker exec -it mcp-server bash`

## License

MIT
