import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a professional assistant."},
    {"role": "user", "content": "Explain black holes in 2 sentences."}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print("AI:", response.choices[0].message.content)
