from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from promptemplate import llm
from pineconeind import retriever
#from langchain_community.document_loaders import WhatsAppChatLoader


#pruebas aca
contextualised_system_prompt = (
    "Dado un historial de chat y la última pregunta del usuario"
    "que podría hacer referencia al contexto en el historial de chat"
    "formular una pregunta independiente que pueda entenderse"
    "sin el historial de chat. NO respondas la pregunta, "
    "Simplemente reformúlelo si es necesario y, en caso contrario, devuélvalo tal como está"
)

contextualised_template = ChatPromptTemplate.from_messages(
    [
        ("system", contextualised_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualised_template)
#prodias definir el prompt que desees
system_prompt_template ="""Eres un asistente experto especializado en responder preguntas relacionadas con alcaldias o ayuntamientos. Utilice la información proporcionada y sus conocimientos para responder con precisión y claridad a cada pregunta.

Pautas:
1. Proporcione respuestas concisas e informativas.
2. Si la pregunta está más allá del alcance de su conocimiento o de la información proporcionada, diga: "No lo sé".
3. Utilice ejemplos cuando corresponda para ilustrar sus respuestas.
4. Mantenga un tono profesional y servicial.

Contexto: {context}

"""
system_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt_template),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)
