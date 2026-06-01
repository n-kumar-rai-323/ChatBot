from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from lang

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

response = model.invoke(model)
