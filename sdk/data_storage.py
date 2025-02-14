from typing import List, Optional

class Schema:
    def __init__(self, email: str, is_verified: bool) -> None:
        self.email = email
        self.is_verified = is_verified        

class InMemoryDataStorage:  
    def __init__(self) -> None:  
        self.storage: List[Schema] = []

    def create(self, email: str, is_verified: bool) -> bool:
        if is_verified:
            self.storage.append(Schema(email=email, is_verified=is_verified))
            return True
        return False    

    def read(self, email: str) -> Optional[Schema]:  
        for item in self.storage:
            if item.email == email:
                return item  
        return None  

    def update(self, email: str, is_verified: bool) -> bool: 
        for item in self.storage:
            if item.email == email:
                item.is_verified = is_verified  
                return True
        return False  

    def delete(self, email: str) -> bool:  
        for i, item in enumerate(self.storage):
            if item.email == email:
                del self.storage[i]
                return True
        return False  
