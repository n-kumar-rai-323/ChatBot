from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
messages =[
    SystemMessage(content="you are a funny AI agent")
]

while True:
    print("----------- Welcome Type 0 to exit the application --------------")
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ", response.content)