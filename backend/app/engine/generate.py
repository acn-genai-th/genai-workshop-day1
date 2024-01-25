import logging

from dotenv import load_dotenv

from app.engine.constants import (
    STORAGE_DIR_FOODS,
    DATA_DIR_FOODS,
    STORAGE_DIR_DRINKS,
    DATA_DIR_DRINKS,
)
from app.engine.context import create_service_context

load_dotenv()

from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(service_context):
    # TODO: 2.1 - Create embeddings from DATA_DIR_FOODS, persist in STORAGE_DIR_FOODS
    # TODO: 2.2 - Create embeddings from DATA_DIR_DRINKS, persist in STORAGE_DIR_DRINKS
    logger.log("Creating embeddings..")


if __name__ == "__main__":
    service_context = create_service_context()
    generate_datasource(service_context)
