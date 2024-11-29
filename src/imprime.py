import pprint
from crmemo import conversational_rag_chain


def conversational_chain(query):
    answer = conversational_rag_chain.invoke(
        {"input": query},
        config={
            "configurable": {"session_id":"MySessionId0001"}
        }
    )
    pprint.pprint(answer)
    return answer

#preguntas al sistema
#conversational_chain(" que es un ayuntamiento")

def conversational_chain(query):
    answer = conversational_rag_chain.invoke(
        {"input": query},
        config={
            "configurable": {"session_id":"MySessionId0001"}
        }
    )["answer"]

    return answer
#preguntas al sistema
#conversational_chain("What is the relationship of LLM and carbon emmision?")