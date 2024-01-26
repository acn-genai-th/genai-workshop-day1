import logging
import os
from llama_index import (
    StorageContext,
    load_index_from_storage,
)
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine

from common.constants import STORAGE_DIR_DRINKS, STORAGE_DIR_FOODS
from common.context_engine import create_service_context


logger = logging.getLogger("uvicorn")


def get_sub_question_query_engine():
    # TODO: 3 - Check if storage already exists, load the existing index that's created from Checkpoint 1
    # Two separate VectorStoreIndex should be created from food-recipes and drink-recipes respectively
    logger.info("Loading multiple indices..")
    return
