import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

# Fix USER_AGENT warning
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

url = "https://en.wikipedia.org/wiki/Machine_learning"

loader = WebBaseLoader(url)
docs = loader.load()

print("Number of docs:", len(docs))
print("Content preview:")
print(docs[0].page_content[:500])