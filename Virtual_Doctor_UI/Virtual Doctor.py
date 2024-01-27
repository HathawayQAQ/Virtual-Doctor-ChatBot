import gradio as gr

def answer(question):
    #we need to pass the user input to the openai here but i don't know how
    #this should return the answer from chatgpt
    return input('Ask Virtual Doctor for any health concerns!')
    

virtual_doctor = gr.Interface(
    fn=answer,
    inputs=["text"],
    outputs=["text"],
)

virtual_doctor.launch()