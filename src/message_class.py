from datetime import datetime
from dataclasses import dataclass

@dataclass
class Message:
    """Class for keeping messages information"""
    id: int
    content: str
    timestamp: datetime
    user_id: int
    channel_id: int
    response_to: (int | None)

