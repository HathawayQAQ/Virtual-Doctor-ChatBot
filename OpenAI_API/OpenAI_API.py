from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a real doctor, Users will describe their symptoms to you, and give them preliminary diagnoses and sound medication recommendations."},
    {"role": "user", "content": "I am sneezing and have a runny nose and my temperature is 40 degrees."}
  ]
)

print(completion.choices[0].message.content)