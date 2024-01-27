import openai
import gradio as gr

openai.api_key = "sk-..."  # Replace with your key

def predict(message, history):
    history_openai_format = []
    for human, ai in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "ai", "content":ai})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-4.0-turbo', # need change if applicable
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(predict,
                 title = 'Virtual Doctor',
                 description='you can ask our virtual doctor for any symptoms you have, \
                     with some emergent situation, please contact 911 immediately.').launch()
