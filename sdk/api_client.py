import requests
from typing import Dict, Any

class HunterAPIClient:
    BASE_URL = "https://api.hunter.io/v2"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def validate_email(self, email: str) -> bool:
        response = requests.get(f"{self.BASE_URL}/email-verifier", params={"email": email, "api_key": self.api_key})
        response.raise_for_status()
        data = response.json()
        
        return data["data"]["status"] == "valid"
