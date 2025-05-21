"""
Custom tool implementations that combine multiple API calls
"""

import json
import logging
from typing import Dict, Any, List

from api_client import ApiClient

logger = logging.getLogger(__name__)


class CustomTools:
    """
    Custom tool implementations that combine multiple API calls
    to provide higher-level functionality
    """

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def network_health_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive network health report
        by combining data from multiple API endpoints
        """
        try:
            # Get overall network health
            network_health = self.api_client.make_request(
                method="GET",
                path="/dna/intent/api/v1/network-health"
            )

            # Get site health
            site_health = self.api_client.make_request(
                method="GET",
                path="/dna/intent/api/v1/site-health"
            )

            # Get device health
            device_health = self.api_client.make_request(
                method="GET",
                path="/dna/intent/api/v1/device-health"
            )

            # Get client health
            client_health = self.api_client.make_request(
                method="GET",
                path="/dna/intent/api/v1/client-health"
            )

            # Get issues
            issues = self.api_client.make_request(
                method="GET",
                path="/dna/intent/api/v1/issues"
            )

            # Combine the data into a comprehensive report
            report = {
                "network_health": network_health,
                "site_health": site_health,
                "device_health": device_health,
                "client_health": client_health,
                "issues": issues,
                "summary": {
                    "total_sites": len(site_health.get("response", [])),
                    "total_devices": len(device_health.get("response", [])),
                    "total_clients": len(client_health.get("response", [])),
                    "total_issues": len(issues.get("response", [])),
                    "overall_health_score": network_health.get("healthScore", 0)
                }
            }

            return report
        except Exception as e:
            logger.error(f"Error generating network health report: {str(e)}")
            return {"error": str(e)}

    def get_custom_tool_schemas(self) -> List[Dict[str, Any]]:
        """Get the custom tool schemas in MCP format"""
        return [
            {
                "name": "network_health_report",
                "description": "Generate a comprehensive network health report that combines data from multiple APIs",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        ]
