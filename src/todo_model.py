from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class TodoTask:
    id: int
    title: str
    description: Optional[str]
    is_completed: bool = False
    created_at: datetime = datetime.now()
