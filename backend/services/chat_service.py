from urllib.request import Request

from fastapi.responses import StreamingResponse
from llama_index.chat_engine.types import BaseChatEngine

from fastapi import HTTPException, status
from llama_index.llms.base import ChatMessage
from llama_index.llms.types import MessageRole

from models.chat_data import ChatData


class ChatService:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # cls.acn_index = get_acn_index()
            # cls.food_index = get_food_index()
            # cls.drink_index = get_drink_index()
        return cls.instance

    async def chat(self, request: Request, data: ChatData, chat_engine: BaseChatEngine):
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
        # convert messages coming from the request to type ChatMessage
        messages = [
            ChatMessage(
                role=m.role,
                content=m.content,
            )
            for m in data.messages
        ]

        # TODO: 4 - Inject and Implement Q&A function, using sub_question_query_engine from get_sub_question_query_engine(),
        # Feel free to comment out or remove existing chat_engine code
        # Recommended to not modify request and response schema, else it has to be reflected on frontend web app too

        # query chat engine
        response = await chat_engine.astream_chat(last_message.content, messages)

        # stream response
        async def event_generator():
            async for token in response.async_response_gen():
                # If client closes connection, stop sending events
                if await request.is_disconnected():
                    break
                yield token

        return StreamingResponse(event_generator(), media_type="text/plain")