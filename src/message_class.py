import datetime
from dataclasses import dataclass

@dataclass
class Message:
    """Class for keeping messages information"""
    id: int
    content: str
    timestamp: datetime.datetime
    user_id = int
    channel_id = int
    response_to = int


    def __init__(self, id: int, content: str, timestamp: str, user_id: int, channel_id: int, response_to: int):
        self.id = id
        self.content = content
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.user_id = user_id
        self.channel_id = channel_id
        self.response_to = response_to

