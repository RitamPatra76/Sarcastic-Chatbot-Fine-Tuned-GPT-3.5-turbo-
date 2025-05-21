import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import streamlit as st

st.set_page_config(page_title="Sarcastic Chatbot", page_icon="😏", layout="centered")

st.markdown("<h1 style='text-align: center; font-size: 48px;'>🧠 Sarcastic Chatbot</h1>", unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            response = client.chat.completions.create(
                model="ft:gpt-3.5-turbo-your-id",  # change with your original fine tuned model id  
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
