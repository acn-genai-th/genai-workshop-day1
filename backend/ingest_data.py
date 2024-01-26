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
    # TODO: 2.1 - Create embeddings from DATA_DIR_FOODS, persist in STORAGE_DIR_FOODS
    # TODO: 2.2 - Create embeddings from DATA_DIR_DRINKS, persist in STORAGE_DIR_DRINKS

    directories = [
        {"data_dir": DATA_DIR_FOODS, "storage_dir": STORAGE_DIR_FOODS},
        {"data_dir": DATA_DIR_DRINKS, "storage_dir": STORAGE_DIR_DRINKS},
    ]

    logger.info(msg="Creating embeddings..")
    for directory in directories:
        data_dir = directory.get("data_dir")
        storage_dir = directory.get("storage_dir")

        if data_dir is None or storage_dir is None:
            print(
                "Invalid directory entry. Both 'data_dir' and 'storage_dir' must be specified."
            )
            continue

        # Load data from the specified data directory
        documents = SimpleDirectoryReader(data_dir).load_data()

        # Create embeddings and persist in the specified storage directory
        index = VectorStoreIndex.from_documents(
            documents, service_context=service_context
        )  # replace 'None' with your actual service context
        index.storage_context.persist(storage_dir)
    logger.info(msg="Created embeddings")


if __name__ == "__main__":
    service_context = create_service_context()
    generate_datasource(service_context)
