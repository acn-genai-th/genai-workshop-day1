import logging

from dotenv import load_dotenv

from context_engine import create_service_context

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(service_context):
    # TODO:: Create embeddings from DATA_DIR_FOODS, persist in STORAGE_DIR_FOODS
    # TODO:: Create embeddings from DATA_DIR_DRINKS, persist in STORAGE_DIR_DRINKS
    logger.log("Create embeddings..")


if __name__ == "__main__":
    service_context = create_service_context()
    generate_datasource(service_context)
