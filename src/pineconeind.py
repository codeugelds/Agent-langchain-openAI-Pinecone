from pinecone import Pinecone, ServerlessSpec
from config import load_config
from langchain_pinecone import PineconeVectorStore
from chunking import chunk_docs
from Genemb import embeddings
from docloader.pdfcarg import text_chunk

#archivos o librerias deprecada

config = load_config()
pinecone_api_key = config["pinecone_api_key"]

pc = Pinecone(api_key=pinecone_api_key)
index_name = "agent-prototipo"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name = index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print("Indice creado")
else:
    print(f"El Indice {index_name} ya existe")

vector_store = PineconeVectorStore.from_documents(chunk_docs,
                                                  embeddings,
                                                  index_name=index_name)

#query = "como podriamos usar las alcaldias para mejorar la calidad de vida de los ciudadanos"
#query = "que son los ayuntamientos"
#query = "cuantas funciones tiene un alcalde"
#query = "cual es su periodo de duracion"
#query = "ayuntamiento y alcaldia son lo mismo?"
query = "cuantos depaartamentos tiene un ayunatamiento? cuantas alcaldias hay en españa?"


retriever = vector_store.as_retriever(search_kwargs = {"k":3})
retriever.get_relevant_documents(query)

#funcion para dar formato al documento
def format_docs(text_chunk):
    return "\n\n".join(doc.page_content for doc in text_chunk)

retrieved_text_chunk = retriever.invoke(query)
print(format_docs(retrieved_text_chunk))#eliminar o comentar

