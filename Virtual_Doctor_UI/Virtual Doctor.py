import gradio as gr

def answer(question):
    return input('Ask Virtual Doctor for any health concerns!')
    

virtual_doctor = gr.Interface(
    fn=answer,
    inputs=["text"],
    outputs=["text"],
)

virtual_doctor.launch()