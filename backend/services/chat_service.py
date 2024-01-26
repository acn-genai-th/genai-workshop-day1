from urllib.request import Request

from llama_index.query_engine import BaseQueryEngine

from fastapi import HTTPException, status
from llama_index.llms.base import ChatMessage
from llama_index.llms.types import MessageRole

from models.chat_data import ChatData


class ChatService:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def query(self, request: Request, data: ChatData, query_engine: BaseQueryEngine):
        # check preconditions and get last message
        if len(data.messages) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No messages provided",
            )
        last_message = data.messages.pop()
        if last_message.role != MessageRole.USER:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Last message must be from user",
            )

        # TODO: 4 - Inject and Implement Q&A function, using sub_question_query_engine from get_sub_question_query_engine()
        # Recommended to not modify request and response schema, else it has to be reflected on frontend web app too

        # query query engine

        return response
