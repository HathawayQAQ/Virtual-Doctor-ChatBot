import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import os
import consts

os.environ["OPENAI_API_KEY"] = consts.OPENAI_API_KEY

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

initial_message = "Pretending to be a scary scientist doctor who only feeds his patients the most chaotic ideas, keep it short"

def diagnosis(message, history):
    if not history:
        history = [(initial_message, "")]
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content

gr.ChatInterface(
    diagnosis,
    title="Virtual Doctor",
    description="Ask Virtual Doctor for any health concerns!",
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Describe your symptoms", container=False, scale=7),
    examples=[
        "I have a headache and a fever", 
        "Experiencing shortness of breath", 
        "I feel nauseous after eating", 
        "My throat is sore and I'm coughing", 
        "I have a rash on my arm"
    ],
    retry_btn="Retry",
    undo_btn=None,
    clear_btn="Clear",
    theme="soft"
).launch()