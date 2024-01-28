import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import os

os.environ["OPENAI_API_KEY"] = "sk-" # Replace with your key

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

initial_message = "Pretending to be a scary scientist doctor, Dr. Chaos, who only feeds his patients the most chaotic ideas, keep it short"

def diagnosis(message, history):
    history = [(initial_message, "Hello, Dr. Chaos is here")]
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content

js = """
function titleAnimation() {
    var container = document.createElement('div');
    container.id = 'animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'left';
    container.style.marginBottom = '20px';

    var text = "🧪 Dr. Chaos's Virtual Clinic";
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""

gr.ChatInterface(
    diagnosis,
    description="Welcome to Dr. Chaos's Virtual Health Consultation Service! <br>Unravel the mysteries of your health with just a few clicks. Whether it's sneezes, wheezes, or nutrition teases, he is here to demystify with wisdom and a sprinkle of fun 😈",
    chatbot=gr.Chatbot(value=[(None, "Greetings, my unfortunate patient 👋 I am Dr. Chaos, the twisted scientist doctor who revels in chaos and mischief. Today, I shall offer you a dose of my peculiar expertise. Brace yourself, for I shall feed your mind with ideas that dwell in the realm of utter chaos. Embrace the madness... if you dare.")], height=500, show_copy_button=True, avatar_images=("/Users/evalin/Downloads/user.jpg", "/Users/evalin/Downloads/doctor.jpg")),
    textbox=gr.Textbox(placeholder="Describe your symptoms", container=False, scale=7),
    examples=[
        "I have a headache and a fever", 
        "Experiencing shortness of breath", 
        "I feel nauseous after eating", 
        "My throat is sore and I'm coughing", 
        "I have a rash on my arm"
    ],
    retry_btn="Ask Dr. Mayhem Again!",
    undo_btn=None,
    clear_btn="Vanish the Chaos!",
    theme="soft",
    js=js
).launch()
