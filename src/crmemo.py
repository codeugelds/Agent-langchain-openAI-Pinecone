from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from contxprom import system_template, history_aware_retriever
from promptemplate import llm


question_answer_chain = create_stuff_documents_chain(llm, system_template)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain) #runnable


store = {}

def get_session_history(session_id: str) ->BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()

    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)


