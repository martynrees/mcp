#!/bin/bash

# Stop and remove existing container if running
docker-compose down

# Build and start the container
docker-compose up --build -d

# Show logs
echo "MCP server is starting. View logs with:"
echo "docker-compose logs -f"
echo ""
echo "Server will be available at http://localhost:8000"