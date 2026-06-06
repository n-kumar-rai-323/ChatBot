from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load document
loader = TextLoader(
    r"C:\Users\DevOps\Desktop\AI\RAG\document loaders\Untitled document.txt",
    encoding="utf-8"
)

docs = loader.load()

# Prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes the text."),
    ("human", "{text}")
])

# Groq model (FIXED)
model = ChatGroq(model="llama-3.3-70b-versatile")

# Format prompt correctly
prompt = template.invoke({"text": docs[0].page_content})

# Get response
result = model.invoke(prompt)

print(result.content)