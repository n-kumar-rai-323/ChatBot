from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9,max_tokens=20)


response = model.invoke("write a poem on AI?")
print(response.content)