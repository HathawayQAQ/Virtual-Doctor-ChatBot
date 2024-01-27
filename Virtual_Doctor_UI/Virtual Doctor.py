import openai
import gradio as gr

openai.api_key = '123'

def answer(question):
    if not isinstance(question, str):
        raise ValueError("Question must be a string.")

    response = openai.Completion.create(
      engine="text-davinci-003",  
      prompt=question,
      max_tokens=150
    )

    return response.choices[0].text.strip()

question = input('Ask Virtual Doctor for any health concerns!')
print(answer(question))

def check_symptoms(symptoms):
    return f"Received symptoms: {symptoms}"

symptom_checker = gr.Interface(
    fn=check_symptoms,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your symptoms here..."),
    outputs="text",
)

symptom_checker.launch(share=True)

def book_appointment(date, time):
    return f"Appointment booked for {date} at {time}"

appointment_booker = gr.Interface(
    fn=book_appointment,
    inputs=[
        gr.inputs.Textbox(placeholder="Enter date (e.g., 2024-01-27)"),
        gr.inputs.Textbox(placeholder="Enter time (e.g., 13:00)")
    ],
    outputs="text",
)

appointment_booker.launch(share=True)

def chat_with_doctor(message):
    return f"Doctor: {message}"

chat_system = gr.Interface(
    fn=chat_with_doctor,
    inputs=gr.inputs.Textbox(lines=3, placeholder="Type your message here..."),
    outputs="text",
)

chat_system.launch(share=True)

