from typing import Annotated

from llama_index.query_engine import BaseQueryEngine

from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, Request, Response

from common.index import get_sub_question_query_engine
from models.chat_data import ChatData
from services.chat_service import ChatService

chat_router = r = APIRouter()


@r.post("")
async def chat(
    request: Request,
    data: ChatData,
    chat_service: Annotated[ChatService, Depends(ChatService)],
    query_engine: BaseQueryEngine = Depends(get_sub_question_query_engine),
):
    response = chat_service.query(request=request, data=data, query_engine=query_engine)

    return Response(str(response))
