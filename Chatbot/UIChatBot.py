from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤖", layout="centered")

# ── Minimal custom style ──────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Hide Streamlit branding */
  #MainMenu, footer { visibility: hidden; }

  /* Chat container spacing */
  .stChatMessage { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Funny AI Chatbot")
st.caption("Powered by LLaMA 3.3 · Groq · LangChain")

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI agent.")
    ]

if "model" not in st.session_state:
    st.session_state.model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )

# ── Render chat history (skip the hidden SystemMessage) ───────────────────────
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ── Chat input ────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Say something…"):
    # Show user message
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get and show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = st.session_state.model.invoke(st.session_state.messages)
        st.write(response.content)
    st.session_state.messages.append(AIMessage(content=response.content))