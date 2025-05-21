#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Set the MCP server URL
export MCP_SERVER_URL="http://localhost:8000"

# Run the example client
echo "Starting example client..."
python example_client.py
