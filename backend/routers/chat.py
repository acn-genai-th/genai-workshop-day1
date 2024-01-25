from typing import List, Annotated

from fastapi.responses import StreamingResponse
from llama_index.chat_engine.types import BaseChatEngine

from common.index import get_chat_engine
from fastapi import APIRouter, Depends, HTTPException, Request, status
from llama_index.llms.base import ChatMessage
from llama_index.llms.types import MessageRole

from models.chat_data import ChatData
from services.chat_service import ChatService

chat_router = r = APIRouter()


@r.post("")
async def chat(
    request: Request,
    data: ChatData,
    chat_service: Annotated[ChatService, Depends(ChatService)],
    chat_engine: BaseChatEngine = Depends(get_chat_engine),
):
    return chat_service.chat(request=request, data=data, chat_engine=chat_engine)
