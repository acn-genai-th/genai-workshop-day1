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
    service_context = create_service_context()

    storage_info = [
        {
            "dir": STORAGE_DIR_FOODS,
            "metadata": {
                "name": "food_recipes",
                "description": "Food recipes that contain name, recipe, and ingredients",
            },
        },
        {
            "dir": STORAGE_DIR_DRINKS,
            "metadata": {
                "name": "drink_recipes",
                "description": "Drink recipes that contain name, recipe, and ingredients",
            },
        },
    ]

    query_engine_tools = []

    for info in storage_info:
        storage_context = StorageContext.from_defaults(persist_dir=info["dir"])
        index = load_index_from_storage(
            storage_context, service_context=service_context
        )

        tool = QueryEngineTool(
            query_engine=index.as_query_engine(),
            metadata=ToolMetadata(
                name=info["metadata"]["name"],
                description=info["metadata"]["description"],
            ),
        )

        query_engine_tools.append(tool)

    query_engine = SubQuestionQueryEngine.from_defaults(
        query_engine_tools=query_engine_tools,
        service_context=service_context,
        verbose=True,
        use_async=False,
    )

    return query_engine
