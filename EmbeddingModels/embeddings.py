from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()


# 1. GROQ LLM (Chat Model)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=200
)


# 2. FREE EMBEDDING MODEL

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# TEST EMBEDDINGS

text = "Hello, this is a test"
vector = embeddings.embed_query(text)

print("Vector length:", len(vector))
print("First 5 values:", vector[:5])

