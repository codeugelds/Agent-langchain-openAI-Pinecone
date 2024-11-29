from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from pineconeind import retrieved_text_chunk, query, retriever, format_docs
from config import load_config

config = load_config()
openai_api_key = config["openai_api_key"]


template = """Eres un asistente experto especializado en responder preguntas relacionadas con alcaldias o ayuntamientos. Utilice la información proporcionada y sus conocimientos para responder con precisión y claridad a cada pregunta.

Pautas:
1. Proporcione respuestas concisas e informativas.
2. Si la pregunta está más allá del alcance de su conocimiento o de la información proporcionada, diga: "No lo sé".
3. Utilice ejemplos cuando corresponda para ilustrar sus respuestas.
4. Mantenga un tono profesional y servicial.

Contexto: {context}|
Pregunta: {question}

Respuesta:
"""
prompt = template.format(context = format_docs(retrieved_text_chunk), question = query)
#print(prompt) #eliminar o comentar

llm = ChatOpenAI(api_key=openai_api_key)

custom_rag_template = PromptTemplate.from_template(template)

custom_rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | custom_rag_template
    | llm
    | StrOutputParser()
)
custom_rag_chain.invoke(query)
#print(custom_rag_chain.invoke(query))#eliminar o comentar