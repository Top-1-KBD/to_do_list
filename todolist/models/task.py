from datetime import datetime
from typing import Optional

class Task:
    def __init__(self, name: str, description: Optional[str] = ""):
        self.id = id(self)  # Unique ID
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_as_complete(self):
        self.completed = True
