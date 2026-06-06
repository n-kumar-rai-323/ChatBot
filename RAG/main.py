from langchain_community.document_loaders import PyMuPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()

# Load document
data = PyMuPDFLoader(
    r"C:\Users\DevOps\Desktop\AI\RAG\document loaders\document.pdf",
    encoding="utf-8"
)

docs = data.load()

splitter =RecursiveCharacterTextSplitter(
    chunk_size =100,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

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