import os
from dotenv import load_dotenv

load_dotenv()
#configurando una funcion para las variables de entorno
def load_config():
    return {
        "langchain_api_key": os.getenv("LANGCHAIN_API_KEY"),
        "pinecone_api_key": os.getenv("PINECONE_API_KEY"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "tavily_api_key": os.getenv("TAVILY_API_KEY"),
        "langchain_tracing_v2" : os.getenv("LANGCHAIN_TRACING_V2"),
        # Otras configuraciones
    }

#print(load_config())