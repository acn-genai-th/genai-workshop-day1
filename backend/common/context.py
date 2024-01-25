from llama_index import ServiceContext
from llama_index.llms import AzureOpenAI
from llama_index.embeddings import AzureOpenAIEmbedding

# TODO: 1 - Replace with provided api key
api_key = "TO_BE_REPLACED"
azure_endpoint = "https://southindia.api.cognitive.microsoft.com/"
api_version = "2023-07-01-preview"


def create_base_context():
    return ServiceContext.from_defaults(
        llm=AzureOpenAI(
            temperature=0,
            model="gpt-4",
            deployment_name="gpt-4",
            api_key=api_key,
            azure_endpoint=azure_endpoint,
            api_version=api_version,
        ),
        embed_model=AzureOpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name="text-embedding-ada-002",
            api_key=api_key,
            azure_endpoint=azure_endpoint,
            api_version=api_version,
        ),
    )
