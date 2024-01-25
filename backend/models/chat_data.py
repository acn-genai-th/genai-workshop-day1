from typing import List

from pydantic import BaseModel

from models.message import Message


class ChatData(BaseModel):
    messages: List[Message]
