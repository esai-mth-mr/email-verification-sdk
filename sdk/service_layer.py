from .api_client import HunterAPIClient
from .data_storage import InMemoryDataStorage
from typing import Optional

class EmailValidationService:
    def __init__(self, api_key: str) -> None:
        self.api_client = HunterAPIClient(api_key)
        self.data_storage = InMemoryDataStorage()

    def validate_and_store(self, email: str) -> bool:
        is_verified = self.api_client.validate_email(email)
        return self.data_storage.create(email, is_verified)

    def email_verified_state(self, email: str) -> Optional[bool]:
        result = self.data_storage.read(email)
        return result is not None  
