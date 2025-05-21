import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cisco API configuration
CISCO_API_BASE_URL = os.getenv("CISCO_API_BASE_URL")
CISCO_API_USERNAME = os.getenv("CISCO_API_USERNAME")
CISCO_API_PASSWORD = os.getenv("CISCO_API_PASSWORD")

# Server configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

# Path to the Swagger JSON file
SWAGGER_JSON_PATH = os.getenv("SWAGGER_JSON_PATH", "../intent_api_2_3_7_9.json")
