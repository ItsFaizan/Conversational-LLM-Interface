from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv() 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_chat(system_prompt):
    messages = [{"role": "system", "content": system_prompt}]
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        reply = response.choices[0].message.content

        print("AI:", reply)
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    # 3 personas
    personas = {
        "1": "You are a professional assistant. Be concise and formal.",
        "2": "You are a creative companion. Use humor and imagination.",
        "3": "You are a fitness coach. Be motivational and practical."
    }

    print("Choose a persona:")
    for k, v in personas.items():
        print(f"{k}. {v}")

    choice = input("Enter 1/2/3: ")
    run_chat(personas.get(choice, personas["1"]))
