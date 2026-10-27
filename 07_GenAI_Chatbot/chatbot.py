import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

token = os.getenv("DATABRICKS_TOKEN")
base_url = os.getenv("DATABRICKS_BASE_URL")
model_name = os.getenv("DATABRICKS_LLM_MODEL")

if not token:
    st.error("Please set DATABRICKS_TOKEN in your .env file.")
    st.stop()
if not base_url:
    st.error("Please set DATABRICKS_BASE_URL in your .env file.")
    st.stop()
if not model_name:
    st.error("Please set DATABRICKS_LLM_MODEL in your .env file.")
    st.stop()

client = OpenAI(api_key=token, base_url=base_url)

import streamlit as st

st.title("Chat Bot Demo")
st.subheader("Powered by Databricks (AI Gateway / OpenAI-compatible)")

with st.chat_message("assistant"):
    st.markdown("Hello there! How can I assist you today?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What's up")

def _content_to_text(content) -> str:
    # Different models/providers can return content in different shapes.
    # This helper normalizes them into plain displayable text.
    if content is None:
        return ""
    if isinstance(content, str):
        # Common case: content is already plain text.
        return content
    if isinstance(content, list):
        # Some responses are a list of parts (e.g., typed blocks).
        parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
                continue
            if not isinstance(item, dict):
                continue
            # Keep only text blocks.
            if item.get("type") == "text" and isinstance(item.get("text"), str):
                parts.append(item["text"])
        if parts:
            return "\n\n".join(parts).strip()
        # Fallback: convert unknown list structures to string.
        return str(content)
    # Final fallback for any unexpected content type.
    return str(content)

def get_response(messages: list[dict]) -> str:
    # Send the conversation history to the model and return assistant text.
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
            max_tokens=1024,
        )
        # Standard OpenAI-style response structure:
        # choices[0].message.content
        content = chat_completion.choices[0].message.content
        return _content_to_text(content)
    except Exception as e:
        # Show the error as assistant text so students can debug quickly.
        return f"Error: {str(e)}"



if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
   
    with st.chat_message("assistant"):
        response = get_response(st.session_state.messages)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content":
        response})
