
from llama_index.llms.types import MessageRole
from pydantic import BaseModel


class Message(BaseModel):
    role: MessageRole
    content: str
