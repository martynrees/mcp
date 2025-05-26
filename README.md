# MCP Server for Cisco Catalyst Center APIs

This server implements the Model Context Protocol (MCP) for Cisco Catalyst Center APIs. It is designed to run exclusively as a Docker container.

## Usage

1. Build and run the Docker container:

```sh
docker build -t mcp-server .
docker run -d -p 8000:8000 --env-file .env mcp-server
```

2. The server will be available at `http://<host>:8000` (replace `<host>` with your Docker host IP).

## Endpoints

- `POST /mcp/tools`: Get available tools in MCP format
- `POST /mcp/execute_tool/{tool_name}`: Execute a specific tool with parameters

## Environment Variables

See `.env` for configuration options. The server expects the API definition file at the path specified by `SWAGGER_JSON_PATH`.

## Development

- All development and testing should use a Python virtual environment (`python -m venv venv`).
- The server is not intended to be run directly on the host.

---

*Client scripts and instructions have been removed. This server is for containerized use only.*
