from langchain_text_splitters import RecursiveCharacterTextSplitter
from docloader.pdfcarg import text_chunk

#troseando todo el contenido
text_slitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap =100)
chunk_docs = text_slitter.split_documents(text_chunk)
#esto lo voy a comentar luego
#print(chunk_docs)