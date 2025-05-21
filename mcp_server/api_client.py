"""
API Client module for making requests to Cisco APIs defined in the Swagger file
"""

import json
import requests
from typing import Dict, Any, Optional, List
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ApiClientAuthConfig(BaseModel):
    base_url: str
    username: str
    password: str


class ApiClientError(Exception):
    """Exception raised when an API request fails"""

    def __init__(self, status_code: int, message: str, details: Optional[Dict[str, Any]] = None):
        self.status_code = status_code
        self.message = message
        self.details = details or {}
        super().__init__(f"API Error ({status_code}): {message}")


class ApiClient:
    """Client for making requests to Cisco Catalyst Center APIs"""

    def __init__(self, auth_config: ApiClientAuthConfig):
        self.base_url = auth_config.base_url.rstrip('/')
        self.username = auth_config.username
        self.password = auth_config.password
        self.token = None

    def authenticate(self) -> None:
        """Authenticate with the Cisco API and get an access token"""
        auth_url = f"{self.base_url}/dna/system/api/v1/auth/token"
        response = requests.post(
            auth_url,
            auth=(self.username, self.password),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code != 200:
            raise ApiClientError(
                response.status_code,
                "Authentication failed",
                details={"response": response.text}
            )

        token_data = response.json()
        self.token = token_data.get("Token")

        if not self.token:
            raise ApiClientError(
                response.status_code,
                "Token not found in response",
                details={"response": token_data}
            )

    def _ensure_authenticated(self) -> None:
        """Ensure that the client is authenticated"""
        if not self.token:
            self.authenticate()

    def make_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Make a request to the Cisco API"""
        self._ensure_authenticated()

        url = f"{self.base_url}{path}"

        default_headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": self.token
        }

        if headers:
            default_headers.update(headers)

        body = json.dumps(data) if data else None

        logger.debug(f"Making {method} request to {url}")
        logger.debug(f"Parameters: {params}")
        logger.debug(f"Body: {body}")

        response = requests.request(
            method=method,
            url=url,
            params=params,
            data=body,
            headers=default_headers
        )

        if response.status_code >= 400:
            raise ApiClientError(
                response.status_code,
                f"Request failed with status {response.status_code}",
                details={"response": response.text}
            )

        try:
            return response.json()
        except json.JSONDecodeError:
            # Some endpoints might return non-JSON responses
            return {"raw_response": response.text}

    def execute_tool(
        self,
        method: str,
        path: str,
        parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute an API tool with the given parameters"""
        path_params = {}
        query_params = {}
        body_data = parameters.get("body", {})

        # Extract path parameters and replace in the URL
        for param_name, param_value in parameters.items():
            if param_name == "body":
                continue

            # Check if this is a path parameter
            if f"{{{param_name}}}" in path:
                path_params[param_name] = param_value
                path = path.replace(f"{{{param_name}}}", str(param_value))
            else:
                # Assume it's a query parameter
                query_params[param_name] = param_value

        return self.make_request(
            method=method,
            path=path,
            params=query_params,
            data=body_data
        )
