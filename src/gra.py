import gradio as gr
from crmemo import conversational_rag_chain


def llm_response(query, memory = None):
    return conversational_rag_chain.invoke(
        {"input": query},
        config={
            "configurable": {"session_id":"MySessionId0001"}
        }
    )["answer"]

demo = gr.ChatInterface(
        llm_response,
        title= "Ejemplo de chat",
        #multimodal=True,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder = "Enter querey here:", scale=5),
        #clear_btn=gr.Button("Clear"),
        #undo_btn=gr.Button("Undo"),
        #retry_btn=gr.Button("Retry"),
        submit_btn=gr.Button("Submit")
)
demo.launch()
