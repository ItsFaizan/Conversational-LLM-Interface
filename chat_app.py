import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Persona options ---
PERSONAS = {
    "Professional Assistant": "You are a professional assistant. Be concise and formal.",
    "Creative Companion": "You are a creative companion. Use humor and imagination.",
    "Technical Expert": "You are a technical expert. Provide detailed, accurate explanations."
}

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
st.title("💬 Chatbot with Personas")

with st.sidebar:
    st.header("⚙️ Settings")
    persona_choice = st.selectbox("Choose a persona", list(PERSONAS.keys()))
    st.markdown(f"**Current Persona:** {persona_choice}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": PERSONAS[persona_choice]}
    ]

st.subheader("Conversation")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**AI:** {msg['content']}")

user_input = st.text_input("Type your message", key="input")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")

    st.experimental_rerun()
-
if st.button("📄 Export Chat"):
    with open("chat_history.txt", "w", encoding="utf-8") as f:
        for msg in st.session_state.messages:
            f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
    st.success("Chat exported to chat_history.txt")
