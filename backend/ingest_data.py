import logging

from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from common.constants import (
    DATA_DIR_DRINKS,
    DATA_DIR_FOODS,
    STORAGE_DIR_DRINKS,
    STORAGE_DIR_FOODS,
)

from common.context_engine import create_service_context

load_dotenv()


def generate_datasource(service_context):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    logger.info(msg="Creating embeddings..")
    # TODO: 2.1 - Create embeddings from DATA_DIR_FOODS, persist in STORAGE_DIR_FOODS
    # TODO: 2.2 - Create embeddings from DATA_DIR_DRINKS, persist in STORAGE_DIR_DRINKS

    logger.info(msg="Created embeddings")


if __name__ == "__main__":
    service_context = create_service_context()
    generate_datasource(service_context)
