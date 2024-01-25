This is a [LlamaIndex](https://www.llamaindex.ai/) project using [FastAPI](https://fastapi.tiangolo.com/) bootstrapped with [`create-llama`](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama).

## Getting Started

First, setup the environment:

```
export PATH="$HOME/.local/bin:$PATH"
poetry install
poetry shell
```

By default, the bootstrapped repository use the OpenAI LLM (though you can customize, see `app/context.py`). In this hands on session, we gonna adopt AzureOpenAI, configurations are provided now, and the key will be destroyed after the workshop.


Second, to implement Data Ingestion Service alike behavior, generate the embeddings of the documents in the `./data` directory:

```
python app/engine/generate.py
```

Once the script has been executed, supposedly there should be /storage/food-recipes and /storage/drink-recipes directories and embeddings created

Third, run the development server:

```
python main.py
```

Then call the API endpoint `/api/chat` to see the result:

```
curl --location 'localhost:8000/api/chat' \
--header 'Content-Type: application/json' \
--data '{ "messages": [{ "role": "user", "content": "Hello" }] }'
```

You can start editing the API by modifying `app/api/routers/chat.py`. The endpoint auto-updates as you save the file.

Open [http://localhost:8000/docs](http://localhost:8000/docs) with your browser to see the Swagger UI of the API.

The API allows CORS for all origins to simplify development. You can change this behavior by setting the `ENVIRONMENT` environment variable to `prod`:

```
ENVIRONMENT=prod uvicorn main:app
```

## Challenges

1. As mentioned in the use case, you're provided with two data sets listed in root /datasets folder, you will need to generate embeddings for them too, and create two separate VectorStoreIndex for them
2. Implement SubQuestionQueryEngine so that the application can break down the user query into sub question, and query the respective query engine
