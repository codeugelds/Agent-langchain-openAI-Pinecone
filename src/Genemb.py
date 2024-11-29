from langchain_openai import OpenAIEmbeddings
from config import load_config

config = load_config()
openai_api_key = config["openai_api_key"]


embeddings = OpenAIEmbeddings(api_key=openai_api_key)
#print(embeddings)




